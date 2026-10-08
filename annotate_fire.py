from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk

ROOT = Path(__file__).resolve().parent

IMAGE_DIR = ROOT / "dataset" / "images" / "train"
LABEL_DIR = ROOT / "dataset" / "labels" / "train"

TEMP_LABEL = "0 0.500000 0.500000 1.000000 1.000000"


def get_images_to_annotate():
    images = []

    for image_path in sorted(IMAGE_DIR.glob("*.jpg")):
        label_path = LABEL_DIR / f"{image_path.stem}.txt"

        if not label_path.exists():
            continue

        try:
            content = label_path.read_text().strip()
        except Exception:
            continue

        if content == TEMP_LABEL:
            images.append(image_path)

    return images


class Annotator:
    def __init__(self, root, images):
        self.root = root
        self.images = images
        self.index = 0

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.root.title("Wildfire AI - Fire Annotation")

        self.info = tk.Label(
            root,
            text="",
            font=("Arial", 12)
        )
        self.info.pack(pady=5)

        self.canvas = tk.Canvas(
            root,
            width=900,
            height=650,
            bg="black"
        )
        self.canvas.pack()

        self.canvas.bind("<ButtonPress-1>", self.start_box)
        self.canvas.bind("<B1-Motion>", self.draw_box)
        self.canvas.bind("<ButtonRelease-1>", self.finish_box)

        self.root.bind("<Return>", self.save_annotation)
        self.root.bind("<Escape>", self.skip_image)

        self.load_image()

    def load_image(self):
        if self.index >= len(self.images):
            self.info.config(
                text="DONE! All temporary fire labels have been annotated."
            )
            self.canvas.delete("all")
            return

        self.image_path = self.images[self.index]
        self.label_path = LABEL_DIR / f"{self.image_path.stem}.txt"

        self.original = Image.open(self.image_path).convert("RGB")

        max_w = 900
        max_h = 650

        scale = min(
            max_w / self.original.width,
            max_h / self.original.height,
            1
        )

        new_w = int(self.original.width * scale)
        new_h = int(self.original.height * scale)

        self.scale = scale

        self.display_image = self.original.resize(
            (new_w, new_h)
        )

        self.tk_image = ImageTk.PhotoImage(self.display_image)

        self.canvas.config(
            width=new_w,
            height=new_h
        )

        self.canvas.delete("all")

        self.canvas.create_image(
            0,
            0,
            anchor="nw",
            image=self.tk_image
        )

        self.info.config(
            text=(
                f"{self.index + 1}/{len(self.images)}  "
                f"{self.image_path.name} | "
                f"Drag box around the FIRE, then press ENTER"
            )
        )

        self.start_x = None
        self.start_y = None
        self.rect = None

    def start_box(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.rect:
            self.canvas.delete(self.rect)

        self.rect = self.canvas.create_rectangle(
            self.start_x,
            self.start_y,
            self.start_x,
            self.start_y,
            outline="red",
            width=3
        )

    def draw_box(self, event):
        if self.start_x is None:
            return

        self.canvas.coords(
            self.rect,
            self.start_x,
            self.start_y,
            event.x,
            event.y
        )

    def finish_box(self, event):
        pass

    def save_annotation(self, event=None):
        if self.start_x is None or self.rect is None:
            return

        coords = self.canvas.coords(self.rect)

        if len(coords) != 4:
            return

        x1, y1, x2, y2 = coords

        left = min(x1, x2)
        right = max(x1, x2)
        top = min(y1, y2)
        bottom = max(y1, y2)

        canvas_w = self.display_image.width
        canvas_h = self.display_image.height

        if right - left < 5 or bottom - top < 5:
            return

        x_center = ((left + right) / 2) / canvas_w
        y_center = ((top + bottom) / 2) / canvas_h

        width = (right - left) / canvas_w
        height = (bottom - top) / canvas_h

        label = (
            f"0 "
            f"{x_center:.6f} "
            f"{y_center:.6f} "
            f"{width:.6f} "
            f"{height:.6f}\n"
        )

        self.label_path.write_text(label)

        self.index += 1
        self.load_image()

    def skip_image(self, event=None):
        self.index += 1
        self.load_image()


images = get_images_to_annotate()

print("==============================================")
print("WILDFIRE AI - FIRE ANNOTATION")
print("==============================================")
print(f"Images needing annotation: {len(images)}")
print()

if not images:
    print("No temporary labels found.")
    print("Nothing to annotate.")
else:
    print("Images:")
    for image in images:
        print(" -", image.name)

    print()
    print("Controls:")
    print("Drag = draw box around fire")
    print("ENTER = save")
    print("ESC = skip")

    root = tk.Tk()
    app = Annotator(root, images)
    root.mainloop()