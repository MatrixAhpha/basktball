from PyQt6.QtWidgets import QSplitter
from PyQt6.QtCore import Qt
from windows.right.bottom.bottom_widget import create_bottom_widget
from windows.right.top.top_widget import create_top_widget


def create_right_splitter(parent):
    right_splitter = QSplitter(Qt.Orientation.Vertical)

    top_widget = create_top_widget(parent)
    right_splitter.addWidget(top_widget)

    bottom_widget = create_bottom_widget(parent)
    right_splitter.addWidget(bottom_widget)

    right_splitter.setStretchFactor(0, 20)  # 上部分控件比例 3
    right_splitter.setStretchFactor(1, 1)  # 下部分控件比例 2

    parent.event_managers["bottom"] = bottom_widget.event_manager
    return right_splitter
