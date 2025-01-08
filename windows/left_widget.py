from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt


def create_left_widget(parent):
    left_widget = QLabel("左边区域", parent)
    left_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 使用正确的对齐标志
    return left_widget
