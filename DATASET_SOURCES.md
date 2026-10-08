# Recommended source datasets

## D-Fire

D-Fire contains more than 21,000 fire/smoke images, including 1,164 fire-only images, 5,867 smoke-only images, 4,658 images containing both, and 9,838 negatives. Its annotations use YOLO normalized bounding boxes.

Use D-Fire as a **base fire/smoke dataset**, not as the complete solution to Sir's requirement. It does not by itself teach the model that a fire displayed on a phone is a false alarm.

Official repository:
https://github.com/gaia-solutions-on-demand/DFireDataset

## Custom screen-fire dataset

You must add your own images of:

- phone showing a fire video
- phone showing a fire image
- laptop showing wildfire
- monitor/TV showing flame
- printed fire photograph

Annotate the **device/display** as `screen_fire`.

Do not annotate the fire pixels inside the display as `fire`.

## Custom real-small-fire dataset

Add real photos/videos converted to frames of:

- lighter flame
- candle
- match
- burning paper
- small controlled flame

These are especially important because your current failure is a small lighter flame.

Keep the original lighter image you provided as a final test image rather than putting it into the training split.
