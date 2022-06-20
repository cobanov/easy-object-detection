import torch

# Model Settings
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
image_path = "image/test_image.jpg"

results = model(image_path)
results.save()

# # Results
# results.print()
# results.save()  # or .show()

# results.xyxy[0]  # img1 predictions (tensor)
# results.pandas().xyxy[0]
