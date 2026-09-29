try:
    from PySide.QtWidgets import QWizardPage, QVBoxLayout, QLabel
    from PySide.QtGui import QMovie
    from PySide.QtCore import Qt, QSize
except:
    from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel
    from PySide6.QtGui import QMovie
    from PySide6.QtCore import Qt, QSize
from utils.config import INTRO_IMAGES_DIR
import os

class WelcomePage(QWizardPage):
    def __init__(self):
        # Initialize wizard page with title
        super().__init__()

        # Create main layout for vertical centering
        main_layout = QVBoxLayout()
        main_layout.addStretch(1)

        # Setup content layout for title and GIF
        content_layout = QVBoxLayout()
        content_layout.setSpacing(10)

        # Add title label
        title_label = QLabel("Welcome to the Dynamic World Generator Wizard!")
        title_label.setStyleSheet("font-size: 24pt; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(title_label)

        # Load and display GIF or fallback text
        gif_path = os.path.join(INTRO_IMAGES_DIR, "welcome.gif")
        gif_label = QLabel()
        # Keep a reference to the movie: QLabel.setMovie() does not take
        # ownership, and PySide6 would delete the C++ QMovie once the local
        # reference goes out of scope (stopping the animation).
        self.movie = QMovie(gif_path)
        if self.movie.isValid():
            self.movie.setScaledSize(QSize(1200, 750))
            gif_label.setMovie(self.movie)
            self.movie.start()
        else:
            gif_label.setText(f"Preview GIF not found at {gif_path}")
        gif_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(gif_label)

        main_layout.addLayout(content_layout)
        main_layout.addStretch(1)

        # Set page layout
        self.setLayout(main_layout)