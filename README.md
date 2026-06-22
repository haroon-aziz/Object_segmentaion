YOLO26n-Seg: Real-Time Instance Segmentation

"Python" (https://img.shields.io/badge/Python-3.9+-blue.svg)
"PyTorch" (https://img.shields.io/badge/PyTorch-2.x-red.svg)
"License" (https://img.shields.io/badge/License-MIT-green.svg)

Overview

YOLO26n-Seg is a lightweight and efficient instance segmentation model designed for real-time computer vision applications. It combines object detection and pixel-level segmentation, enabling precise identification and localization of objects within images and video streams.

The model is optimized for edge devices, embedded systems, and resource-constrained environments while maintaining competitive segmentation accuracy and fast inference speeds.

Typical applications include:

- Medical image segmentation
- Industrial inspection
- Autonomous robotics
- Smart surveillance
- Agriculture monitoring
- Traffic analysis
- Retail analytics
- Sports analytics

---

Features

- Real-time instance segmentation
- Lightweight nano architecture
- High-speed inference
- GPU and CPU support
- Video stream processing
- Image batch inference
- Easy integration with Python applications
- Compatible with OpenCV workflows
- ONNX export support
- Edge deployment ready

---

Model Information

Property| Value
Model| YOLO26n-Seg
Task| Instance Segmentation
Framework| PyTorch
Input Size| 640×640 (default)
Output| Bounding Boxes + Segmentation Masks
Deployment| CPU, GPU, Edge Devices
Format| ".pt"

---

Installation

Clone Repository

git clone https://github.com/yourusername/yolo26n-seg.git
cd yolo26n-seg

Create Virtual Environment

python -m venv venv

Linux/macOS:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

---

Requirements

ultralytics
torch
torchvision
opencv-python
numpy
supervision

Install manually:

pip install ultralytics torch torchvision opencv-python numpy supervision

---

Quick Start

Image Segmentation

from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

results = model("image.jpg")

results[0].show()

---

Save Results

from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

results = model("image.jpg", save=True)

Output will be stored in:

runs/segment/predict/

---

Video Inference

from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

results = model.predict(
    source="video.mp4",
    save=True
)

---

Webcam Segmentation

from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

model.predict(
    source=0,
    show=True
)

---

Access Segmentation Masks

from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

results = model("image.jpg")

masks = results[0].masks

if masks is not None:
    print(masks.data.shape)

---

Access Bounding Boxes

from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

results = model("image.jpg")

boxes = results[0].boxes

for box in boxes:
    print(box.xyxy)

---

Real-Time OpenCV Integration

import cv2
from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("YOLO26n-Seg", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

---

Training

Train on a custom dataset:

yolo segment train \
    model=yolo26n-seg.pt \
    data=data.yaml \
    epochs=100 \
    imgsz=640

Validation

yolo segment val \
    model=runs/segment/train/weights/best.pt \
    data=data.yaml

---

Export Model

ONNX

yolo export \
    model=yolo26n-seg.pt \
    format=onnx

TensorRT

yolo export \
    model=yolo26n-seg.pt \
    format=engine

OpenVINO

yolo export \
    model=yolo26n-seg.pt \
    format=openvino

---

Performance Considerations

For maximum performance:

- Use CUDA-enabled GPUs.
- Increase batch size when memory allows.
- Use TensorRT for deployment.
- Use FP16 inference.
- Resize inputs to match training resolution.
- Avoid unnecessary image conversions.

---

Example Applications

Medical Imaging

- Organ segmentation
- Tumor localization
- Surgical assistance

Agriculture

- Crop segmentation
- Fruit counting
- Disease monitoring

Industrial Inspection

- Defect detection
- Product quality assessment
- Assembly verification

Smart Cities

- Vehicle segmentation
- Traffic monitoring
- Pedestrian analysis


License

This project is distributed under the MIT License.

See the LICENSE file for details.

---

Acknowledgements

Special thanks to:

- Ultralytics
- PyTorch Team
- OpenCV Community
- Open Source Contributors

Their tools and frameworks make modern computer vision development accessible and efficient.

--