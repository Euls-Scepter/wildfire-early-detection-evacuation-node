# Annotation Guide for Sir's Requirement

## 1. Real lighter flame

Image: a real lighter burning in front of the camera.

Label: `fire` (class 0)

Bounding box: around the visible flame. Do not include the whole hand unless necessary to contain the flame.

## 2. Real candle/match/burning material

Label the actual flame as `fire`.

## 3. Wildfire

Label visible real flame regions as `fire`. If substantial real smoke is visible and you want smoke detection, label the smoke region separately as `smoke`.

## 4. Phone showing wildfire/flame

Label the whole phone/screen as `screen_fire` (class 1).

Do NOT label the fire pixels inside the screen as class 0. The point is to teach the detector that this visual fire is coming from a display.

## 5. TV/laptop/monitor showing fire

Same rule: label the display/device as `screen_fire`.

## 6. Normal no-fire images

No bounding boxes. No `.txt` file is required.

## 7. Critical split rule

Do not put near-duplicate frames of the same video or same scene into train and validation/test. Otherwise the metrics can look artificially high.
