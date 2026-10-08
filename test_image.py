import sys
from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

# =====================================================
# V2 TRAINED MODEL
# =====================================================

MODEL = (
    ROOT
    / "runs"
    / "train"
    / "SAINet_fire_screen_v2"
    / "weights"
    / "best.pt"
)

# =====================================================
# CHECK ARGUMENT
# =====================================================

if len(sys.argv) != 2:
    print("Usage:")
    print("python test_image.py path/to/image.jpg")
    raise SystemExit(1)

image = Path(sys.argv[1]).resolve()

# =====================================================
# CHECK FILES
# =====================================================

if not MODEL.exists():
    raise FileNotFoundError(
        f"Missing trained model:\n{MODEL}"
    )

if not image.exists():
    raise FileNotFoundError(
        f"Missing image:\n{image}"
    )

# =====================================================
# LOAD MODEL
# =====================================================

print("\nLoading V2 trained model...")
print(MODEL)

model = YOLO(str(MODEL))

print("\nModel classes:")
print(model.names)

# =====================================================
# PREDICT
# =====================================================

results = model.predict(
    source=str(image),
    conf=0.25,
    imgsz=640,
    verbose=False
)

# =====================================================
# DISPLAY RESULTS
# =====================================================

print("\n======================================")
print("SAINet V2 FIRE / SCREEN TEST")
print("======================================")
print(f"Image: {image.name}")
print()

found = False

for result in results:

    if result.boxes is None:
        continue

    for box in result.boxes:

        found = True

        class_id = int(box.cls[0])
        conf = float(box.conf[0])

        name = model.names[class_id]

        print(
            f"Detected: {name.upper():12s} "
            f"| Confidence: {conf:.2%}"
        )

if not found:
    print("NO DETECTION")

print("======================================")