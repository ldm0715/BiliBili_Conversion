import os
import sys
from PyQt5.QtWidgets import QApplication,QSpacerItem,QSizePolicy
from PyQt5.QtWidgets import QLabel, QPushButton, QMainWindow, QTextBrowser, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap

# 项目基础路径
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("bilbili视频转化器")
        self.resize(500, 500)
        self.move(400, 400)

        # 创建Label
        title = QLabel("bilbili缓存视频转化器", self)
        title.setGeometry(150, 50, 300, 30)  # 设置Label的位置和大小

        # 设置字体样式
        font = QFont()
        font.setFamily("Arial")  # 设置字体家族
        font.setPointSize(16)  # 设置字体大小
        font.setBold(True)  # 设置字体粗细
        font.setItalic(False)  # 设置字体为斜体

        title.setFont(font)  # 应用字体样式到Label

        button1 = QPushButton("转换", self)
        button1.resize(100, 100)
        button1.move(100, 150)
        # button1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.button1 = button1

        button2 = QPushButton("选择文件夹", self)
        button2.resize(100, 100)
        button2.move(200, 100)
        self.button2 = button2

        button3 = QPushButton("输出文件夹", self)
        button3.resize(100, 100)
        button3.move(300, 150)
        self.button3 = button3

        button4 = QPushButton("批量转化", self)
        button4.resize(100, 100)
        button4.move(200, 200)
        self.button4 = button4

        tip = QLabel("状态信息:", self)
        tip.setGeometry(100, 240, 300, 30)
        self.tip = tip

        status_bar = QTextBrowser(self)
        status_bar.setGeometry(100, 270, 300, 150)
        self.status_bar = status_bar

        author = QLabel("作者: gcnanmu", self)
        author.setGeometry(300, 380, 500, 100)

        qspace1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        qspace2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        hbox2 = QHBoxLayout()
        hbox2.addItem(qspace1)
        hbox2.addWidget(author)

        hbox3 = QHBoxLayout()
        hbox3.addItem(qspace2)
        hbox3.addWidget(button2)
        hbox3.addWidget(button1)
        hbox3.addItem(qspace2)

        hbox4 = QHBoxLayout()
        hbox4.addItem(qspace2)
        hbox4.addWidget(button3)
        hbox4.addWidget(button4)
        hbox4.addItem(qspace2)

        # 创建 logo对象
        logo = QLabel(self)
        logo.setGeometry(0, 0, 10, 10)  # 设置 Label 的位置和大小
        logo.setFixedSize(50,50)

        # 加载并显示图片
        pixmap = QPixmap(os.path.join(BASE_DIR, "image/bilibili.ico"))  # 通过文件名加载图片
        logo.setPixmap(pixmap)  # 设置 Label 的 pixmap 属性以显示图片
        logo.setScaledContents(True)  # 根据 Label 的大小自动缩放图片内容

        hbox = QHBoxLayout()
        hbox.addWidget(logo)
        hbox.addWidget(title)

        # 创建垂直布局管理器并添加控件

        vbox = QVBoxLayout()
        vbox.setSpacing(20)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        vbox.addWidget(tip)
        vbox.addWidget(status_bar)
        vbox.addLayout(hbox2)

        # 创建主部件并设置布局
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
