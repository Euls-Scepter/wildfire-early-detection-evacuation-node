from flask import Flask, request
from ultralytics import YOLO
import os

app = Flask(__name__)
MODEL_PATH = "model/SAINet_v11.2.pt"
model = YOLO(MODEL_PATH)

@app.route("/verify", methods=["POST"])
def verify():
    if "image" not in request.files:
        return "NO_IMAGE", 400

    image = request.files["image"]
    if not image.filename:
        return "NO_IMAGE", 400

    image_path = "received_image.jpg"
    image.save(image_path)

    try:
        results = model.predict(source=image_path, conf=0.25, imgsz=640, verbose=False)

        fire_conf = 0.0
        smoke_conf = 0.0
        screen_fire_conf = 0.0

        for result in results:
            if result.boxes is None:
                continue
            for box in result.boxes:
                class_id = int(box.cls[0])
                conf = float(box.conf[0])
                name = model.names[class_id].lower()
                print(f"Detected: {name.upper()} | Confidence: {conf:.2%}")

                if name == "fire":
                    fire_conf = max(fire_conf, conf)
                elif name == "screen_fire":
                    screen_fire_conf = max(screen_fire_conf, conf)
                elif name == "smoke":
                    smoke_conf = max(smoke_conf, conf)

        # A display containing fire is an intentional hard negative.
        if screen_fire_conf >= fire_conf:
            print("SCREEN FIRE -> NO_FIRE")
            return "NO_FIRE"

        if fire_conf > 0:
            print(f"REAL FIRE -> FIRE ({fire_conf:.2%})")
            return "FIRE"

        if smoke_conf > 0:
            print(f"SMOKE -> NO_FIRE ({smoke_conf:.2%})")
            return "NO_FIRE"

        print("NO FIRE OR SMOKE")
        return "NO_FIRE"
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
