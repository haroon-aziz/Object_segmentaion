# Video Segmentation with YOLO26

Real-time instance segmentation on video using the Ultralytics YOLO26 segmentation model — detects and masks objects frame-by-frame and saves the annotated output.

## Features

- Instance segmentation using the pretrained [`yolo26n-seg`] model from Ultralytics
- Live preview window while processing (`show=True`)
- Annotated output automatically saved to disk (`save=True`)
- Minimal setup — no custom training required to get started

## Requirements

- Python 3.9+
- A video file to run inference on

Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Add your video**

   Place your input video in a `videos/` folder (or anywhere you like), then update the `VIDEO_SOURCE` path in `segmentation.py`.

3. **Run**

   ```bash
   python segmentation.py
   ```

   The model weights (`yolo26n-seg.pt`) will be downloaded automatically by Ultralytics on first run if not already present.

## Output

Annotated results are saved under `runs/segment/predict/` by default (Ultralytics' standard output convention), including the processed video with segmentation masks drawn on each frame.

## Configuration

| Setting | Location | Description |
|---|---|---|
| `"yolo26n-seg.pt"` | `YOLO(...)` call | Pretrained model variant — swap for `yolo26s-seg.pt`, `yolo26m-seg.pt`, etc. for higher accuracy at the cost of speed |
| `VIDEO_SOURCE` | Top of script | Path to your input video, or `0` for a live webcam feed |
| `show=True` | `model.predict(...)` | Set to `False` to disable the live preview window (useful for headless/server runs) |
| `save=True` | `model.predict(...)` | Set to `False` if you don't want the annotated output saved to disk |

## Project Structure

```
.
├── segmentation.py       # Main script
├── requirements.txt      # Python dependencies
├── .gitignore
├── videos/               # (not tracked) input videos go here
└── runs/                 # (not tracked) Ultralytics output directory
```

## Known Limitations

- Model weights are auto-downloaded on first run, which requires an internet connection.
- Larger model variants (`s`/`m`/`l`) will be significantly slower without a GPU.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
