from PySide6.QtWidgets import *
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

if __name__ == "__main__":
    app = QuizApplication(sys.argv)
    app.window.show()
    sys.exit(app.exec())
