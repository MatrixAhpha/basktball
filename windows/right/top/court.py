from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel


def create_court(parent):
    court = QLabel("court", parent)
    court.setAlignment(Qt.AlignmentFlag.AlignCenter)

    return court
