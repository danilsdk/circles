import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPen
from UI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.b)
        self.ok = False

    def paintEvent(self, event):
        if self.ok:
            qp = QPainter()
            qp.begin(self)
            for i in range(4):
                self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        a = randint(10, min([self.width(), self.height()]) // 4)
        qp.drawEllipse(randint(self.width() // 4, self.width() * 3 // 4),
                       randint(self.height() // 4, self.height() * 3 // 4), a, a)

    def b(self):
        self.ok = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
