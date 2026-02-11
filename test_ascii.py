import cv2
from ascii_convert import frame_to_ascii

# Load video
video = cv2.VideoCapture("sample.mp4")

# Read first frame
success, frame = video.read()

if not success:
    print("❌ Error: Could not read video.")
else:
    print("✅ First frame loaded!")
    ascii_art = frame_to_ascii(frame)
    print("\n--- ASCII OUTPUT START ---\n")
    print(ascii_art)
    print("\n--- ASCII OUTPUT END ---")
