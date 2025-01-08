from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel


def create_top_widget(parent):
    # 上部区域
    top_widget = QLabel("右上区域", parent)
    top_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
    top_widget.setStyleSheet("background-color: lightgreen;")

    return top_widget