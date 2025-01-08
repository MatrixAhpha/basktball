from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel


def create_top_widget(parent):
    # 上部区域
    top_widget = QLabel(parent)
    top_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
    top_widget.setStyleSheet("""
            QLabel {
                background-image: url('assets/background.jpg');
                background-repeat: no-repeat;
                background-position: center;
                background-size: 100% 100%;
            }
            color: white;  /* 设置文字颜色，确保与背景对比清晰 */
        """)

    return top_widget