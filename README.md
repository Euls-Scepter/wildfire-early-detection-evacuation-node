# Wildfire AI Training Package — SAINet v11.2

This package prepares a custom Ultralytics YOLO dataset for the wildfire node.

## Goal

The model must distinguish:

- `fire` — real flames/fire (lighter, candle, match, burning paper, campfire, wildfire, etc.)
- `screen_fire` — fire visible on a phone/TV/monitor/printed display; treat as NO_FIRE in the application
- `smoke` — real smoke

Negative images with no target object are allowed to have no `.txt` label file.

## IMPORTANT: Seed dataset is NOT production-ready

Only a few seed images are included so the training pipeline is immediately usable. Do not claim high accuracy from these images. Add a large, diverse set of annotated images before final training.

Recommended minimum starting target:

- 150–300 real-fire images, including 30–50 lighter/candle/match close-ups
- 100–200 screen-fire images (phone, TV, laptop, monitor, printed photo/video)
- 100–200 smoke images
- 200+ negative images (forest, roads, people, buildings, sunset, orange lights, reflections, etc.)

Keep validation/test images from scenes not used in training.

## Dataset layout

```
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
└── data.yaml
```

For YOLO detection labels, each object is one line:

```
class_id x_center y_center width height
```

All coordinates are normalized from 0 to 1. Class IDs are:

```
0 = fire
1 = screen_fire
2 = smoke
```

## Annotation rule

For a real lighter photo, draw a box around the visible flame and label it `fire`.

For a phone showing a wildfire, draw a box around the phone/screen and label it `screen_fire`. Do NOT label the fire pixels inside the screen as `fire`.

For real smoke, draw a box around the smoke region and label it `smoke`.

For a normal no-fire image, create no label file.

## Training

From the `wildfire_ai_training` folder:

```
pip install -U ultralytics
python train_sainet.py
```

The script starts from `model/SAINet_v11.1.pt` and writes a new model under:

```
runs/train/SAINet_v11.2/weights/best.pt
```

## Validation and testing

After training:

```
python validate_sainet.py
python test_image.py path/to/image.jpg
```

Do not use the same images for both training and final demonstration testing.
