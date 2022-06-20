## easy-object-detection

Very fast and incredibly simple plug and play object detection script

## Examples
<img src="/image/test_image.jpg" alt="test1 image" style="height: 500px"/>  <img src="/runs/detect/exp/test_image.jpg" alt="test1 image" style="height: 500px"/>

## Requirements

```
pip install -r requirements.txt
```

## Usage
```python
import torch

# Model Settings
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
image_path = "image/test_image.jpg"

results = model(image_path)
results.save()
```
