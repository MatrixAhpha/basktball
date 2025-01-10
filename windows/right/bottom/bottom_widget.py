from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from match_singleton import MatchSingleton


def create_bottom_widget(parent):
    # 下部区域
    bottom_widget = QLabel("右下区域", parent)
    bottom_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
    bottom_widget.setStyleSheet("background-color: lightyellow;")

    match = MatchSingleton.get_instance()
    return bottom_widget
