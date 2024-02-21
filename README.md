
# Python Screen Recorder

This Python script captures the screen and optionally the webcam feed, allowing you to record your desktop activity. It utilizes OpenCV, PIL (Python Imaging Library), and `win32api` to grab the screen and webcam frames, and `cv2.VideoWriter` to save the recording as an MP4 video file.

## Features

- **Screen Recording**: Captures the screen with customizable frame rate.
- **Webcam Integration**: Optionally includes the webcam feed in the recording.
- **User Interaction**: Prompts the user to include webcam and terminates recording when 'q' is pressed.
- **Timestamped Output**: Saves the recorded video with a timestamped filename.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- PIL (`pillow`)
- `win32api` (Windows-only)

## Usage

1. Run the script.
2. Choose whether to include the webcam in the recording.
3. Press 'q' to stop the recording.

## Note

- Ensure proper permissions for accessing the screen and webcam.
- Customize frame rate and file name generation according to your preferences.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute, report issues, or suggest improvements via GitHub. Contributions are welcome!
```
