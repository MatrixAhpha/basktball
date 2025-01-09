from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QLabel


# 创建篮球场控件
def create_court(parent, event_manager):
    court = QLabel("court", parent)
    court.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # 设置默认背景颜色
    court.setStyleSheet("background-color: lightgray;")

    # 绑定事件信号到响应函数
    event_manager.possession.connect(lambda: change_background(court, "white", persistent=True))
    event_manager.foul.connect(lambda: change_background(court, "red", 1000))
    event_manager.two_points.connect(lambda: change_background(court, "lightgreen", 1000))
    event_manager.three_points.connect(lambda: change_background(court, "darkgreen", 1000))
    event_manager.free_throw.connect(lambda: change_background(court, "lightblue", 1000))
    event_manager.block.connect(lambda: change_background(court, "blue", 1000))
    event_manager.out_of_bounds.connect(lambda: change_background(court, "yellow", 1000))

    return court


# 修改背景颜色的函数
def change_background(court, color, duration=0, persistent=False):
    """
    改变 court 的背景颜色。
    :param court: QLabel 实例。
    :param color: 背景颜色。
    :param duration: 颜色持续时间（毫秒）。
    :param persistent: 是否保持该颜色。
    """
    court.setStyleSheet(f"background-color: {color};")

    # 如果需要恢复背景颜色，设置计时器
    if not persistent and duration > 0:
        QTimer.singleShot(duration, lambda: court.setStyleSheet("background-color: lightgray;"))
