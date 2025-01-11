from PyQt6.QtWidgets import QVBoxLayout, QWidget

from windows.left.pannel_widget import Panel


def create_left_widget(parent):
    left_widget = QWidget(parent)
    layout = QVBoxLayout(left_widget)

    lakers_vs_timberwolves = Panel("湖人-森林狼", left_widget, "ws://localhost:6789")
    bucks_vs_pacers = Panel("雄鹿-步行者", left_widget, "ws://localhost:6790")

    layout.addWidget(lakers_vs_timberwolves)
    layout.addWidget(bucks_vs_pacers)

    left_widget.setLayout(layout)
    return left_widget
