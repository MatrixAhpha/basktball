from PyQt6.QtCore import QTimer
from random import choice


def test(event_manager):
    event_manager.foul.emit()
