import argparse
import os
import cv2
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(description="Enhance video with super-resolution.")
    parser.add_argument('--superres', choices=['GFPGAN', 'CodeFormer'], required=True,
                        help='Super-resolution method to use.')
    parser.add_argument('-iv', '--input_video', required=True, help='Path to input video.')
    parser.add_argument('-ia', '--input_audio', required=True, help='Path to input audio.')
    parser.add_argument('-o', '--output', required=True, help='Path to output video.')
    return parser.parse_args()


def extract_frames(video_path):
    # Extract frames from the video using OpenCV
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Error opening video file: {video_path}")

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames


def identify_generated_region(frame):
    # Identify generated region (simplified for this example)
    height, width, _ = frame.shape
    return frame[int(height / 2):, int(width / 2):]  # Assume the generated region is bottom-right corner


def apply_super_resolution(region, method):
    # Apply super-resolution based on the selected method
    if method == "GFPGAN":
        # Implement GFPGAN processing here (placeholder for now)
        pass
    elif method == "CodeFormer":
        # Implement CodeFormer processing here (placeholder for now)
        pass
    return region  # Return the region without changes for now


def reconstruct_frame(original_frame, enhanced_region):
    # Reconstruct frame by inserting the enhanced region back into the original frame
    height, width, _ = original_frame.shape
    original_frame[int(height / 2):, int(width / 2):] = enhanced_region
    return original_frame


def merge_audio_video(video_path, audio_path, output_path):
    # Check if the output file already exists and delete it
    if os.path.exists(output_path):
        os.remove(output_path)

    # Merge audio and video using ffmpeg
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'bin', 'ffmpeg.exe')  # Adjust if needed

    # Check if ffmpeg exists at the specified path
    if not os.path.exists(ffmpeg_path):
        raise FileNotFoundError(f"FFmpeg not found at {ffmpeg_path}")

    command = [
        ffmpeg_path,
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-y',  # Auto-overwrite output file if it exists
        output_path
    ]
    subprocess.run(command, check=True)


def main():
    args = parse_args()

    # Get the current working directory
    current_dir = os.getcwd()

    # Construct paths for video and audio in the same directory
    video_path = os.path.join(current_dir, args.input_video)
    audio_path = os.path.join(current_dir, args.input_audio)
    output_path = os.path.join(current_dir, args.output)

    # Extract frames from the video
    frames = extract_frames(video_path)

    # Check if frames were successfully extracted
    if not frames:
        raise ValueError("No frames extracted from the video. Please check the input video.")

    # Process each frame
    for idx, frame in enumerate(frames):
        region = identify_generated_region(frame)
        if region is not None:
            enhanced_region = apply_super_resolution(region, args.superres)
            frame = reconstruct_frame(frame, enhanced_region)

    # Save the processed video
    temp_video_path = os.path.join(current_dir, "demo_video.mp4")
    height, width, _ = frames[0].shape  # Get dimensions from the first frame
    temp_video = cv2.VideoWriter(temp_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    for frame in frames:
        temp_video.write(frame)

    temp_video.release()

    # Merge audio with the video
    merge_audio_video(temp_video_path, audio_path, output_path)

    # Optionally delete the temporary video file after merging
    if os.path.exists(temp_video_path):
        os.remove(temp_video_path)


if __name__ == "__main__":
    main()
