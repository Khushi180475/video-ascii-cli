import cv2

ASCII_CHARS = "@%#*+=-:. "  # characters arranged by darkness → lightness


def resize_frame(frame, max_width=120):
    """Resize frame to fit terminal properly."""
    height, width = frame.shape[:2]
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * max_width * 0.55)  # 0.55 fixes stretched look
    return cv2.resize(frame, (max_width, new_height))


def frame_to_ascii(frame, max_width=120):
    """Convert an image frame (numpy array) into ASCII art."""
    # Step 1: Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 2: Resize
    small_gray = resize_frame(gray, max_width=max_width)

    # Step 3: Map each pixel → ASCII
    ascii_image = []
    for row in small_gray:
        ascii_row = "".join(
            ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]
            for pixel in row
        )
        ascii_image.append(ascii_row)

    return "\n".join(ascii_image)


# Test (optional)
if __name__ == "__main__":
    frame = cv2.imread("sample_frame.jpg")  # temporary test
    print(frame_to_ascii(frame))
