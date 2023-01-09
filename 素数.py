import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon


from style import *
from other import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('生成素数')
        self.setWindowIcon(QIcon('.././icon/Qt.png'))
        self.resize(500, 600)
        self.init_ui()

    def init_ui(self):
        contain = QVBoxLayout()


        h1 = QHBoxLayout()
        label = QLabel('请输入n的值')
        self.n = QLineEdit('100')
        label.setStyleSheet(style_input1)
        self.n.setStyleSheet(style_input2)
        h1.addWidget(label)
        h1.addWidget(self.n)


        self.text = QTextEdit()
        self.text.setStyleSheet(style_output)

        h2 = QHBoxLayout()
        btn1 = QPushButton('生成')
        btn2 = QPushButton('复制')
        btn1.setStyleSheet(style_btn)
        btn2.setStyleSheet(style_btn)
        btn1.clicked.connect(self.btn1Clicked)
        btn2.clicked.connect(self.btn2Clicked)
        h2.addStretch(3)
        h2.addWidget(btn1)
        h2.addStretch(1)
        h2.addWidget(btn2)
        h2.addStretch(3)

        contain.addLayout(h1)
        contain.addWidget(self.text)
        contain.addLayout(h2)


        self.setLayout(contain)
    def btn1Clicked(self):
        self.text.clear()
        for i in range(2, int(self.n.text())+1):
            if isPrime(i):
                self.text.append(str(i))
        #设置输出内容只读
        self.text.setReadOnly(True)

    def btn2Clicked(self):
        clipboard = QApplication.clipboard()
        # 设置剪贴板内容
        clipboard.setText(self.text.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    app.exec_()