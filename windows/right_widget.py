from PyQt6.QtWidgets import QSplitter, QLabel
from PyQt6.QtCore import Qt
from windows.bottom_widget import create_bottom_widget
from windows.top_widget import create_top_widget


def create_right_splitter(parent):
    right_splitter = QSplitter(Qt.Orientation.Vertical)

    top_widget = create_top_widget(parent)
    right_splitter.addWidget(top_widget)

    bottom_widget = create_bottom_widget(parent)
    right_splitter.addWidget(bottom_widget)

    right_splitter.setStretchFactor(0, 3)  # 上部分控件比例 3
    right_splitter.setStretchFactor(1, 2)  # 下部分控件比例 2
    return right_splitter
