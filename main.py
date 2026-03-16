from my_tracking import Tracking, downscale_frame, process_video_in_chunks
from ultralytics import YOLO
from utils import read_video, save_video

def main():
    video_path = "input/car.mp4"
    output_path = "output_video.mp4"
    model_path = "license_plate_detector.pt"  # Path to your YOLO model

    # Initialize the tracking object
    tracker = Tracking(model=YOLO(model_path))

    # Read the video
    frames = read_video(video_path)
    print(len(frames))

    # Process the video in chunks
    chunked_frames = [frames]
    annotated_frames = []

    for chunk in chunked_frames:
        # Get the tracked objects in the chunk
        tracks = tracker.get_object(chunk)

        # Annotate the frames with bounding boxes and IDs
        annotated_chunk = tracker.annotation(chunk, tracks)
        annotated_frames.extend(annotated_chunk)

    # Save the annotated video
    save_video(annotated_frames, output_path)

if __name__ == "__main__":
    main()