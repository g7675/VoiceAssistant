
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VoiceAssistant")
        self.setMinimumSize(350, 200)

        self.status_label = QLabel("העוזר מוכן")
        self.start_button = QPushButton("הפעל")

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

        self.start_button.clicked.connect(self.on_start)

    def on_start(self):
        self.status_label.setText("העוזר הופעל")