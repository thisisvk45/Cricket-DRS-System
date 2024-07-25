# Cricket-DRS-System

# Third Umpire Decision Review System

A GUI application that simulates a third umpire decision review system using video playback controls, decision-making features, and an enhanced user interface.

## Features

- **Play/Pause Toggle**: Toggle the video playback between play and pause.
- **Playback Speed Control**: Adjust playback speed using predefined buttons and a slider.
- **Frame Display**: Display the current frame number.
- **Jump to Start/End**: Quickly jump to the beginning or end of the video.
- **Decision Buttons**: Simulate 'Out' or 'Not Out' decisions with a pending animation.
- **Enhanced UI**: Organized and user-friendly interface.

## Requirements

- Python 3.x
- Tkinter
- OpenCV
- Pillow
- Imutils

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/third-umpire-decision-review-system.git
   cd third-umpire-decision-review-system
   ```

2. Install the required packages:
   ```bash
   pip install opencv-python pillow imutils
   ```

## Usage

1. Ensure you have the required video and image files in the same directory as the script:
   - `clip5.mp4`: The video clip to be analyzed.
   - `welcome.png`: The welcome image displayed on startup.
   - `pending.png`: The image displayed when the decision is pending.
   - `sponsor.png`: The sponsor image displayed during the decision process.
   - `out.png`: The image displayed for an 'Out' decision.
   - `not out.png`: The image displayed for a 'Not Out' decision.

2. Run the script:
   ```bash
   python third_umpire_decision_review_system.py
   ```

3. Use the GUI to control video playback and make decisions.

## How It Works

The application creates a GUI using Tkinter and displays video frames using OpenCV and Pillow. It provides buttons to control playback speed, toggle play/pause, jump to specific points in the video, and simulate third umpire decisions with animations.

### Key Components

- **Video Playback Control**: Functions to play the video at different speeds and jump to specific frames.
- **Decision Simulation**: Functions to display 'Out' and 'Not Out' decisions with intermediate animations.
- **GUI**: A user-friendly interface built with Tkinter, including buttons, sliders, and labels for various controls.

## Example

![screenshot](screenshot.png)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Author: Vikas Kumar
email : Vikas.kumar1@plaksha.edu.in

---

Feel free to customize this README file further to match your project's specifics and any additional details you may want to include.
