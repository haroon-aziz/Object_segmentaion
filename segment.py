from ultralytics import YOLO

# Load a pretrained Ultralytics YOLO26 segmentation model
model = YOLO("yolo26n-seg.pt")

# Run inference on your video file
results = model.predict(
    source="your Vidoe path ",
    show=True,
    save=True
)