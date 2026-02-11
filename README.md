CLI Video to ASCII Animation Tool 🎬
A powerful and optimized Command Line Interface (CLI) tool built with Python and OpenCV that transforms standard .mp4 videos into stunning ASCII art animations. This tool supports both classic Grayscale and vibrant 24-bit TrueColor rendering directly in your terminal.

✨ Features
Real-time Conversion: Processes and plays video frames as ASCII characters in the terminal.

TrueColor Support: Uses ANSI escape codes to render ASCII in 24-bit color.

Customizable Resolution: Adjust the width of the output to fit your terminal size.

Playback Control: Built-in speed multiplier to speed up or slow down animations.

Optimized Rendering: Uses advanced ANSI sequences (\033[2J\033[3J\033[H) to prevent flickering and ghosting.

🛠️ Tech Stack
Language: Python

Libraries: opencv-python, numpy, argparse

Environment: CLI (Compatible with Windows Terminal, VS Code, and Linux/Mac)

🚀 Getting Started
Prerequisites
Ensure you have Python installed. You can install the required dependencies using:

Bash
Publish with Tiiny Host
pip install opencv-python numpy
Installation
Clone the repository to your local machine:

Bash
Publish with Tiiny Host
git clone https://github.com/Khushi180475/video-ascii-cli.git
cd video-ascii-cli
📖 Usage
Run the tool using the run.py entry point.

Classic Black & White
Bash
Publish with Tiiny Host
python run.py path/to/your_video.mp4
24-bit TrueColor (Recommended)
Bash
Publish with Tiiny Host
python run.py path/to/your_video.mp4 --color
Custom Width and Speed
Bash
Publish with Tiiny Host
python run.py path/to/your_video.mp4 --width 150 --speed 1.5 --color
⚙️ Project Structure
run.py: The main entry point handling CLI arguments.

ascii_player.py: Manages the video stream, timing, and terminal rendering.

ascii_convert.py: Contains the core logic for frame resizing and ASCII mapping.

read_frame.py: A helper utility to verify video file integrity.

Developed by Khushi Aggarwal