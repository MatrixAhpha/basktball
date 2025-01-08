from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QDialog, QVBoxLayout, QPushButton, QMainWindow, QApplication, QSplitter
import sys


def create_top_widget(parent):
    top_splitter = QSplitter(Qt.Orientation.Horizontal)

    top_widget = QLabel(parent)
    top_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

    return top_widget