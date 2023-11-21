import sys
from math import sin, cos, pi
from random import randint

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.qp = QPainter()
        self.coor = tuple()
        self.type_figure = None
        self.flag = False

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')

    def mousePressEvent(self, event):
        self.coor = (event.x(), event.y())
        if event.button() == Qt.LeftButton:
            self.type_figure = 'circle'
            self.drawf()
        elif event.button() == Qt.RightButton:
            self.type_figure = 'square'
            self.drawf()

    def mouseMoveEvent(self, event):
        self.coor = (event.x(), event.y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.type_figure = 'triangle'
            self.drawf()

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_figure()
            self.qp.end()

    def draw_figure(self):
        if self.type_figure == 'triangle':
            A = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y = self.coor
            coords = [QPoint(x, y - A),
                      QPoint(int(x + cos(7 * pi / 6) * A),
                             int(y - sin(7 * pi / 6) * A)),
                      QPoint(int(x + cos(11 * pi / 6) * A),
                             int(y - sin(11 * pi / 6) * A))]
            self.qp.drawPolygon(coords)
        elif self.type_figure == 'circle':
            R = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(int(self.coor[0] - R / 2), int(self.coor[1] - R / 2), R, R)
        elif self.type_figure == 'square':
            A = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawRect(int(self.coor[0] - A / 2), int(self.coor[1] - A / 2), A, A)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())