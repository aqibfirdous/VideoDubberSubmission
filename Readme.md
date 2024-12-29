# Video Dubbing with Super-Resolution

This project is a Python-based tool for enhancing video quality using state-of-the-art super-resolution models and synchronizing dubbed audio with the processed video.

---

## Features

### Super-Resolution Models
- **GFPGAN**: High-quality video restoration.
- **CodeFormer**: Advanced video restoration capabilities.

### Audio-Video Synchronization
- Synchronizes input audio with the enhanced video seamlessly.

### Customizable Output
- Define your input video, audio, and desired output filename.

---

## Usage

### Command Syntax
```bash
python x.py --superres [GFPGAN|CodeFormer] -iv <input_video> -ia <input_audio> -o <output_video>
```

### Arguments
- **--superres**: Specifies the super-resolution model to use. Options:
  - GFPGAN
  - CodeFormer
- **-iv**: Path to the input video file.
- **-ia**: Path to the input audio file.
- **-o**: Path to the output video file.

### Example
```bash
python x.py --superres CodeFormer -iv input.mp4 -ia audio.mp3 -o output.mp4
```
This command will:
1. Enhance the quality of `input.mp4` using the **CodeFormer** model.
2. Synchronize the video with the audio from `audio.mp3`.
3. Save the output as `output.mp4`.

---

## Setup

### Prerequisites
- **Python**: Version 3.8+
- **FFmpeg**: Installed and added to your system PATH.
- **Cloned repositories**: Required for the super-resolution models.

### Cloning Required Repositories
- Clone the **GFPGAN** repository:
  ```bash
  git clone https://github.com/TencentARC/GFPGAN.git
  ```
- Clone the **CodeFormer** repository:
  ```bash
  git clone https://github.com/sczhou/CodeFormer.git
  ```

### Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### FFmpeg Installation
1. Download FFmpeg from the [official website](https://ffmpeg.org/).
2. Add FFmpeg to your system PATH.
3. Verify the installation:
   ```bash
   ffmpeg -version
   ```

---

## Project Structure
```
├── x.py                 # Main script for video processing and audio synchronization.
├── requirements.txt     # Python dependencies.
├── README.md            # Project documentation.
├── GFPGAN/              # Cloned repository for GFPGAN.
├── CodeFormer/          # Cloned repository for CodeFormer.
├── input/               # Directory for input video and audio files.
├── output/              # Directory for saving processed videos.
```

---

## Working

### Input Video Processing
- The specified super-resolution model (**GFPGAN** or **CodeFormer**) enhances the input video frame-by-frame.

### Audio Synchronization
- The provided audio file is aligned with the processed video using **FFmpeg**.

### Output Generation
- The final enhanced and synchronized video is saved to the specified output path.

---

