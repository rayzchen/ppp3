from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import random
import functools
import os
import sys

questions = {}
answers = {}
topics = [
    "algorithms",
    "programming",
    "data representation",
    "computer hardware",
    "networks",
    "cyber security",
    "ethics"
]

def load_questions():
    for topic in topics:
        questions[topic] = []
        answers[topic] = []
        files = os.listdir(os.path.join("questions", topic))
        question_nums = [file[:-5] for file in files if file.endswith("q.png")]
        for number in question_nums:
            path = os.path.join("questions", topic, number + "q.png")
            questions[topic].append(QPixmap(path))
            path = os.path.join("questions", topic, number + "a.png")
            answers[topic].append(QPixmap(path))

class QuizWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Random GCSE Question of the Day")
        self.resize(800, 500)
        QFontDatabase.addApplicationFont("BebasNeue-Regular.ttf")
        self.setFont(QFont("Bebas Neue", 24))
        self.title_view = TitleView(self)
        self.topic_view = TopicView(self)
        self.question_view = QuestionView(self)

        self.title_view.register_buttons(self)
        self.topic_view.register_buttons(self)
        self.question_view.register_buttons(self)
        self.setCentralWidget(self.title_view)

    def switch_title_view(self):
        self.centralWidget().setParent(None)
        self.setCentralWidget(self.title_view)

    def switch_topic_view(self):
        self.centralWidget().setParent(None)
        self.setCentralWidget(self.topic_view)

    def switch_question_view(self):
        self.centralWidget().setParent(None)
        self.question_view.reset()
        self.setCentralWidget(self.question_view)

    def show_random_question(self):
        topic = random.choice(topics)
        self.show_topic_question(topic)

    def show_topic_question(self, topic):
        self.question_view.topic = topic
        self.question_view.question = random.randrange(len(questions[topic]))
        self.switch_question_view()

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
        self.question_button.clicked.connect(window.show_random_question)
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
        for button in self.topic_buttons:
            button.clicked.connect(functools.partial(
                window.show_topic_question,
                button.text()
            ))

class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)

        self.menu_button = QPushButton("MENU")
        self.hbox.addWidget(self.menu_button, 2)
        self.hbox.addStretch(1)
        self.title = QLabel("GCSE COMPUTER SCIENCE\nQUESTION OF THE DAY", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hbox.addWidget(self.title)
        self.hbox.addStretch(1)
        self.quit_button = QPushButton("QUIT")
        self.hbox.addWidget(self.quit_button, 2)

    def register_buttons(self, window):
        self.menu_button.clicked.connect(window.switch_title_view)
        self.quit_button.clicked.connect(window.close)

class QuestionView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.top_bar = TopBar(self)
        self.vbox.addWidget(self.top_bar, 0)

        self.question_container = QWidget(self)
        self.vbox.addWidget(self.question_container, 1)

        self.question_layout = QHBoxLayout(self.question_container)
        self.question_widget = QLabel("filler text", self)
        self.question_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_widget.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Ignored
        )
        self.question_layout.addWidget(self.question_widget, 1)

        self.answer_button = QPushButton("CLICK TO SHOW\nMARK SCHEME")
        self.answer_button.setFont(QFont("Bebas Neue", 48))
        self.answer_button.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Ignored
        )
        self.answer_button.clicked.connect(self.show_mark_scheme)
        self.question_layout.addWidget(self.answer_button, 1)

        self.mark_scheme_widget = QLabel("mark scheme")
        self.mark_scheme_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mark_scheme_widget.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Ignored
        )

        self.topic = "algorithms"
        self.question = 0

    def show_mark_scheme(self):
        widget = self.question_layout.itemAt(1).widget()
        self.question_layout.removeWidget(widget)
        widget.setParent(None)
        self.question_layout.addWidget(self.mark_scheme_widget, 1)

    def reset(self):
        widget = self.question_layout.itemAt(1).widget()
        self.question_layout.removeWidget(widget)
        widget.setParent(None)
        self.question_layout.addWidget(self.answer_button, 1)

    def paintEvent(self, event):
        super().paintEvent(event)
        self.resize_images()

    def resize_images(self):
        scaled = questions[self.topic][self.question].scaled(
            self.question_widget.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.question_widget.setPixmap(scaled)

        scaled = answers[self.topic][self.question].scaled(
            self.mark_scheme_widget.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.mark_scheme_widget.setPixmap(scaled)

    def register_buttons(self, window):
        self.top_bar.register_buttons(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_questions()
    window = QuizWindow()
    window.show()
    sys.exit(app.exec())
