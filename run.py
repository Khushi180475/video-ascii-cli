import argparse
from ascii_player import play_ascii_video

def main():
    parser = argparse.ArgumentParser(description="Play any video as ASCII art in terminal.")

    parser.add_argument("video", help="Path to the video file")
    parser.add_argument("--width", type=int, default=120, help="ASCII width (default: 120)")
    parser.add_argument("--speed", type=float, default=1.0, help="Playback speed multiplier")

    args = parser.parse_args()

    print(f"🎬 Playing: {args.video}")
    print(f"➡ Width: {args.width}")
    print(f"➡ Speed: {args.speed}x")

    play_ascii_video(args.video, max_width=args.width, speed=args.speed)

if __name__ == "__main__":
    main()
