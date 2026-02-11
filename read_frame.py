import cv2

# Path of your video file
video_path = "sample.mp4"

# Load the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Cannot open video")
    exit()

# Read first frame
success, frame = cap.read()

if success:
    print("✅ Frame read successfully!")
    print("Frame size:", frame.shape)  # (height, width, 3)
else:
    print("❌ Could not read frame")

cap.release()
