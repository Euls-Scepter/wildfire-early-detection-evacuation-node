from pathlib import Path
from ultralytics import YOLO

try:
    import torch
except ImportError:
    torch = None


ROOT = Path(__file__).resolve().parent

MODEL_PATH = ROOT / "model" / "SAINet_v11.1.pt"
DATA_YAML = ROOT / "dataset" / "data.yaml"


def main():

    # =====================================================
    # CHECK FILES
    # =====================================================

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Missing model: {MODEL_PATH}"
        )

    if not DATA_YAML.exists():
        raise FileNotFoundError(
            f"Missing dataset YAML: {DATA_YAML}"
        )

    # =====================================================
    # LOAD ORIGINAL SAINET
    # =====================================================

    print("==============================================")
    print("WILDFIRE AI - SAINet FINE-TUNING")
    print("==============================================")

    print("\nLoading original SAINet model...")

    model = YOLO(str(MODEL_PATH))

    print("Original classes:")
    print(model.names)

    print("\nTarget classes:")
    print("0 = fire")
    print("1 = screen_fire")
    print("2 = smoke")

    # =====================================================
    # DEVICE
    # =====================================================

    if torch is not None and torch.cuda.is_available():
        device = 0
    else:
        device = "cpu"

    print("\nTraining device:", device)

    # =====================================================
    # TRAIN
    # =====================================================

    print("\nStarting fine-tuning...\n")

    results = model.train(

        # Dataset
        data=str(DATA_YAML),

        # Training
        epochs=100,
        imgsz=640,
        batch=8,

        # Early stopping
        patience=20,

        # Windows
        workers=0,

        # CPU/GPU
        device=device,

        # Output
        project=str(ROOT / "runs" / "train"),
        name="SAINet_fire_screen_v2",
        exist_ok=True,

        # Optimizer
        optimizer="AdamW",

        # Learning rate
        lr0=0.001,
        lrf=0.01,

        # Regularization
        weight_decay=0.0005,

        # Warmup
        warmup_epochs=3,

        # Augmentation
        degrees=8.0,
        translate=0.10,
        scale=0.35,
        shear=2.0,
        perspective=0.0,

        fliplr=0.5,
        flipud=0.0,

        hsv_h=0.015,
        hsv_s=0.50,
        hsv_v=0.40,

        mosaic=0.5,
        mixup=0.0,
        copy_paste=0.0,

        close_mosaic=10,

        # Performance
        cache=False,

        # Save graphs
        plots=True,

        # Save checkpoints
        save=True,
        save_period=10,

        # Reproducibility
        seed=42,
    )

    # =====================================================
    # FINISHED
    # =====================================================

    print("\n==============================================")
    print("TRAINING FINISHED")
    print("==============================================")

    best_model = (
        ROOT
        / "runs"
        / "train"
        / "SAINet_fire_screen_v2"
        / "weights"
        / "best.pt"
    )

    print("\nBest model:")
    print(best_model)

    print("\nTarget classes:")
    print("0 = fire")
    print("1 = screen_fire")
    print("2 = smoke")


if __name__ == "__main__":
    main()