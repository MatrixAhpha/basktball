from PyQt6.QtWidgets import QMainWindow, QSplitter
from PyQt6.QtCore import Qt
from windows.left.left_widget import create_left_widget
from windows.right.right_widget import create_right_splitter


class MainWindow(QMainWindow):
    def __init__(self, urls):
        super().__init__()
        self.setWindowTitle("体育赛事直播可视化系统")
        self.setGeometry(100, 100, 1200, 700)
        self.event_managers = {}
        self.websocket_manager = None
        self.urls = urls

        # 创建主窗口布局
        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # 左边区域
        left_widget = create_left_widget(self)
        main_splitter.addWidget(left_widget)
        main_splitter.setStretchFactor(0, 1)  # 调窄左边部分

        # 右边区域分为上下两部分
        right_splitter = create_right_splitter(self)
        main_splitter.addWidget(right_splitter)
        # left_widget.setStyleSheet("background-color: lightblue;")
        main_splitter.setStretchFactor(1, 3)  # 扩大右边部分

        # 设置主窗口的中心控件
        self.setCentralWidget(main_splitter)
