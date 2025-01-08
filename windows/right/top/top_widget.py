from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QDialog, QVBoxLayout, QPushButton, QMainWindow, QApplication, QSplitter
import sys

from windows.right.top.court import create_court


def create_top_widget(parent):
    top_splitter = QSplitter(Qt.Orientation.Horizontal)

    main_court = create_court(parent)
    top_splitter.addWidget(main_court)

    sub_court = create_court(parent)
    top_splitter.addWidget(sub_court)

    return top_splitter
