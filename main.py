from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

class QuizApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = QuizWindow()

class QuizWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Random GCSE Question of the Day")
        self.resize(800, 500)
        QFontDatabase.addApplicationFont("BebasNeue-Regular.ttf")

        self.widget = QWidget(self)
        self.hbox = QHBoxLayout(self.widget)
        self.setCentralWidget(self.widget)

        self.vbox = QVBoxLayout()
        self.hbox.addLayout(self.vbox, 2)

        self.splash = QWidget(self)
        self.hbox.addWidget(self.splash, 1)
        self.hbox.setStretch(1, 1)

        self.vbox.addStretch()
        self.title = QLabel("GCSE COMPUTER SCIENCE\nQUESTION OF THE DAY", self)
        self.title.setFont(QFont("Bebas Neue", 32))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.title, 0)
        self.vbox.addStretch()

        self.button_group = QWidget(self)
        self.button_layout = QVBoxLayout(self.button_group)
        self.button_layout.addStretch()
        self.topic_button = QPushButton("RANDOM QUESTION BY TOPIC", self)
        self.button_layout.addWidget(self.topic_button)
        self.question_button = QPushButton("RANDOM QUESTION", self)
        self.button_layout.addWidget(self.question_button)
        self.quit_button = QPushButton("QUIT", self)
        self.button_layout.addWidget(self.quit_button)
        self.button_layout.addStretch()
        self.button_layout.setSpacing(0)
        self.button_group.setFont(QFont("Bebas Neue", 24))
        self.vbox.addWidget(self.button_group, 0)
        self.vbox.addStretch()

        self.quit_button.clicked.connect(self.close)

if __name__ == "__main__":
    app = QuizApplication(sys.argv)
    app.window.show()
    sys.exit(app.exec())
