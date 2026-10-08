from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent
MODEL = ROOT / "runs" / "train" / "SAINet_v11.2" / "weights" / "best.pt"
DATA = ROOT / "dataset" / "data.yaml"


def main():
    if not MODEL.exists():
        raise FileNotFoundError(f"Train the model first. Missing: {MODEL}")

    model = YOLO(str(MODEL))
    metrics = model.val(data=str(DATA), imgsz=640, split="val", plots=True)

    print("\n===== VALIDATION =====")
    print(f"mAP50:    {metrics.box.map50:.4f}")
    print(f"mAP50-95: {metrics.box.map:.4f}")
    print("Per-class mAP50-95:", metrics.box.maps)


if __name__ == "__main__":
    main()
