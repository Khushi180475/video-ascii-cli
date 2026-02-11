import cv2
import os
import time
from ascii_convert import frame_to_ascii

def play_ascii_video(video_path, max_width=120):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Error: Could not open video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1 / fps if fps > 0 else 0.04  # safe fallback

    print(f"🎬 Playing video at {fps:.2f} FPS\n")

    while True:
        success, frame = cap.read()
        if not success:
            break  # End of video

        ascii_frame = frame_to_ascii(frame, max_width)


        # Clear terminal (Windows + Mac/Linux support)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(ascii_frame)

        time.sleep(frame_delay)

    cap.release()
    print("\n🎉 Video finished!")

if __name__ == "__main__":
    play_ascii_video("sample.mp4")
