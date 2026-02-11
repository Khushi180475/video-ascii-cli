import cv2
import os
import time
from ascii_convert import frame_to_ascii

# Added use_color=False as a default parameter
def play_ascii_video(video_path, max_width=120, speed=1.0, use_color=False):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Error: Could not open video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1 / fps if fps > 0 else 0.04 

    print(f"🎬 Playing video at {fps:.2f} FPS\n")

    while True:
        success, frame = cap.read()
        if not success:
            break 

        ascii_frame = frame_to_ascii(frame, max_width, use_color=use_color)

        # THE FIX: This sequence clears the screen AND the scrollback buffer
        # \033[2J clears screen, \033[3J clears scrollback, \033[H moves to top
        print("\033[2J\033[3J\033[H", end="") 

        print(ascii_frame)

        time.sleep(frame_delay / speed)

    cap.release()
    print("\n🎉 Video finished!")

if __name__ == "__main__":
    # If running this file directly, you can manually set color to True to test
    play_ascii_video("sample.mp4", use_color=True)