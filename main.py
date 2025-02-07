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
        self.setFont(QFont("Bebas Neue", 24))
        self.title_view = TitleView(self)
        self.topic_view = TopicView(self)

        self.title_view.register_buttons(self)
        self.topic_view.register_buttons(self)
        self.setCentralWidget(self.title_view)

    def switch_title_view(self):
        self.centralWidget().setParent(None)
        self.setCentralWidget(self.title_view)

    def switch_topic_view(self):
        self.centralWidget().setParent(None)
        self.setCentralWidget(self.topic_view)

class TitleView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)

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
        self.vbox.addWidget(self.button_group, 0)
        self.vbox.addStretch()

    def register_buttons(self, window):
        self.topic_button.clicked.connect(window.switch_topic_view)
        self.quit_button.clicked.connect(window.close)

class TopicView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.top_bar = TopBar(self)
        self.vbox.addWidget(self.top_bar)

        self.button_layout = QVBoxLayout()
        self.button_layout.setSpacing(0)

        self.topic_buttons = []
        topics = [
            "algorithms",
            "programming",
            "data representation",
            "computer hardware",
            "networks",
            "cyber security",
            "ethics"
        ]
        for topic in topics:
            button = QPushButton(topic, self)
            self.button_layout.addWidget(button)
            self.topic_buttons.append(button)

        self.button_group = QWidget(self)
        self.hbox = QHBoxLayout(self.button_group)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.button_layout, 1)
        self.hbox.addStretch(1)

        self.vbox.addStretch(1)
        self.vbox.addWidget(self.button_group)
        self.vbox.addStretch(1)

    def register_buttons(self, window):
        self.top_bar.register_buttons(window)

class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)

        self.menu_button = QPushButton("MENU")
        self.hbox.addWidget(self.menu_button, 2)
        self.hbox.addStretch(1)
        self.title = QLabel("GCSE COMPUTER SCIENCE\nQUESTION OF THE DAY", self)
        self.hbox.addWidget(self.title)
        self.hbox.addStretch(1)
        self.quit_button = QPushButton("QUIT")
        self.hbox.addWidget(self.quit_button, 2)

    def register_buttons(self, window):
        self.menu_button.clicked.connect(window.switch_title_view)
        self.quit_button.clicked.connect(window.close)

if __name__ == "__main__":
    app = QuizApplication(sys.argv)
    app.window.show()
    sys.exit(app.exec())
