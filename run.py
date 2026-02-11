import argparse
from ascii_player import play_ascii_video

def main():
    parser = argparse.ArgumentParser(description="Play any video as ASCII art in terminal.")

    parser.add_argument("video", help="Path to the video file")
    parser.add_argument("--width", type=int, default=120, help="ASCII width (default: 120)")
    parser.add_argument("--speed", type=float, default=1.0, help="Playback speed multiplier")
    
    # ADD THIS LINE: This creates the --color flag
    parser.add_argument("--color", action="store_true", help="Enable 24-bit TrueColor mode")

    args = parser.parse_args()

    print(f"🎬 Playing: {args.video}")
    print(f"➡ Width: {args.width}")
    print(f"➡ Speed: {args.speed}x")
    # Helpful to show if color is on or off
    print(f"➡ Color Mode: {'Enabled' if args.color else 'Disabled'}")

    # Pass the color flag to your play_ascii_video function
    play_ascii_video(args.video, max_width=args.width, speed=args.speed, use_color=args.color)

if __name__ == "__main__":
    main()