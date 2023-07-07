import os
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QDesktopServices, QIcon
from main_ui import MainWindow
from conversion import run
# 设置任务栏图标
import ctypes

# 项目基础路径
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
# 图标路径
ICO_PATH = os.path.join(BASE_DIR, "image/transform.ico")

input_path = None
state_str = None
output_path = os.path.join(BASE_DIR, "output")
batch_input_path = os.path.join(BASE_DIR, "videolist.txt")


# 实现打开文件操作
def openfile():
    global input_path
    global state_str
    # 选取文件
    try:
        folder_path = QFileDialog.getExistingDirectory(None, "选择文件夹", "/")
        if folder_path == "":
            return
        state_str = f"打开文件成功，文件所在路径为：{str(folder_path)}"
        input_path = folder_path
    except:
        state_str = "打开文件失败，检查路径是否有中文"
    finally:
        show_state(state_str)
        print(state_str)


# 展示状态
def show_state(state_str):
    ui.status_bar.append(state_str)
    # 刷新
    ui.status_bar.repaint()


def coverse():
    global input_path
    global state_str
    global output_path
    try:
        state_str = run(input_path)
    except:
        if input_path is None:
            state_str = "未选择文件"
        else:
            state_str = "转换失败，请检查文件是否有中文"
    finally:
        show_state(state_str)


def batch_coverse():
    global batch_input_path
    global state_str
    if not os.path.exists(batch_input_path):
        with open(batch_input_path, 'w') as file:
            file.close()
    try:
        file_list = get_data_list(batch_input_path)
        for i in range(len(file_list)):
            folder_path = file_list[i]
            message = run(folder_path)
            show_state(message)
    except:
        state_str = "路径为空，请在“videolist.txt”中填写路径"
        show_state(state_str)


def get_data_list(path):
    with open(path, "r", encoding="UTF-8") as f:
        data = f.readlines()
        path_list = [i.strip("\n") for i in data]
        print(path_list[0])
        f.close()
    return path_list


def open_outputfolder():
    global output_path
    try:
        if not os.path.exists(output_path):
            state_str = "未生成视频缓存文件夹"
            pass
        else:
            QDesktopServices.openUrl(QUrl.fromLocalFile(output_path))
            state_str = "打开输出文件夹成功"
    except:
        state_str = "未选择视频缓存文件夹"
    finally:
        show_state(state_str)


app = QApplication(sys.argv)
# 将按钮点击事件连接到copenfile函数
ui = MainWindow()
ui.button2.clicked.connect(openfile)
ui.button1.clicked.connect(coverse)
ui.button3.clicked.connect(open_outputfolder)
ui.button4.clicked.connect(batch_coverse)
# 设置图标
ui.setWindowIcon(QIcon(ICO_PATH))
ui.show()
sys.exit(app.exec())
