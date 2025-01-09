import json

from PyQt6.QtWidgets import QMainWindow, QSplitter
from PyQt6.QtCore import Qt
from windows.left.left_widget import create_left_widget
from windows.right.right_widget import create_right_splitter


def process_message(message, window):
    """
    处理接收到的 JSON 消息，将其解析为键值对变量
    """
    try:
        # 将 JSON 字符串转换为字典
        message_dict = json.loads(message)

        # 提取前四个键值对
        keys = list(message_dict.keys())
        key1, key2, key3, key4 = (keys + [None] * 4)[:4]  # 确保始终有 4 个键
        time = message_dict.get(key1, None)
        msg1 = message_dict.get(key2, None)
        score = message_dict.get(key3, None)
        msg2 = message_dict.get(key4, None)

        window.main_event_manager.foul.emit()
        print(time, msg1, score, msg2)

    except json.JSONDecodeError:
        print("接收到的消息不是有效的 JSON 格式:", message)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt 示例")
        self.setGeometry(100, 100, 1200, 700)

        # 创建主窗口布局
        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # 左边区域
        left_widget = create_left_widget(self)
        main_splitter.addWidget(left_widget)
        main_splitter.setStretchFactor(0, 1)  # 调窄左边部分

        # 右边区域分为上下两部分
        right_splitter = create_right_splitter(self)
        main_splitter.addWidget(right_splitter)
        left_widget.setStyleSheet("background-color: lightblue;")
        main_splitter.setStretchFactor(1, 3)  # 扩大右边部分

        # 设置主窗口的中心控件
        self.setCentralWidget(main_splitter)
