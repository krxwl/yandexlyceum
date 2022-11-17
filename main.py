import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5 import uic


class Krug(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.label = QLabel()
        kartina = QPixmap('kartinka.jpg')
        self.label.setPixmap(kartina)
        self.label.setMaximumSize(500, 500)
        setka = QGridLayout(self.centralwidget)
        setka.addWidget(self.pushButton)
        setka.addWidget(self.label)
        self.pushButton.clicked.connect(self.krug)

    def krug(self):
        x = randint(10, 500)
        y = randint(10, 500)
        width = randint(10, 200)
        height = randint(10, 200)
        qp = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor('yellow'))
        qp.setPen(pen)
        qp.drawEllipse(x, y, width, height)
        qp.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Krug()
    a.show()
    sys.exit(app.exec())
