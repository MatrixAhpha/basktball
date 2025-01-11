from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent

from pojo.Match import MatchSingleton


class Panel(QFrame):
    def __init__(self, title, parent=None, url=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)

        self.layout = QVBoxLayout()
        self.label = QLabel(title)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.setStyleSheet("background-color: lightblue; border-radius: 5px;")

        self.url = url

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            match = MatchSingleton.get_instance()
            match.window.websocket_manager.on_change(self.url)
