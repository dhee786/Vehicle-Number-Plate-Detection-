import cv2


def read_video(path):
    cap = cv2.VideoCapture(path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames


def save_video(frames, save_path):
    if len(frames) == 0:
        print("❌ No frames to save")
        return

    height, width = frames[0].shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(save_path, fourcc, 25, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()

    print("✅ Video Saved:", save_path)