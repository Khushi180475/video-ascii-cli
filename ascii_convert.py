import cv2

ASCII_CHARS = "@%#*+=-:. " 

def resize_frame(frame, max_width=120):
    """Resize frame to fit terminal properly."""
    height, width = frame.shape[:2]
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * max_width * 0.55) 
    return cv2.resize(frame, (max_width, new_height))

def frame_to_ascii(frame, max_width=120, use_color=False):
    """Convert an image frame into ASCII art (B&W or Color)."""
    
    # Resize the frame first (keep color for now)
    small_frame = resize_frame(frame, max_width=max_width)
    
    # Convert to grayscale for character mapping
    gray_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

    ascii_image = []
    
    for r in range(gray_small.shape[0]):
        ascii_row = []
        for c in range(gray_small.shape[1]):
            # Get character based on grayscale brightness
            pixel_val = gray_small[r, c]
            char = ASCII_CHARS[int(pixel_val) * len(ASCII_CHARS) // 256]

            if use_color:
                # Get BGR from the resized color frame
                b, g, r_val = small_frame[r, c]
                # Wrap char in ANSI RGB code: \033[38;2;R;G;Bm
                colored_char = f"\033[38;2;{r_val};{g};{b}m{char}\033[0m"
                ascii_row.append(colored_char)
            else:
                ascii_row.append(char)
        
        ascii_image.append("".join(ascii_row))

    return "\n".join(ascii_image)