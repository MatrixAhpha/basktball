from PyQt6.QtCore import QObject, pyqtSignal


# 定义事件管理器类
class CourtEventManager(QObject):
    # 定义自定义信号
    possession = pyqtSignal()  # 拥有球权
    foul = pyqtSignal()  # 犯规
    two_points = pyqtSignal()  # 2分进球
    three_points = pyqtSignal()  # 3分进球
    free_throw = pyqtSignal()  # 罚球
    block = pyqtSignal()  # 盖帽
    out_of_bounds = pyqtSignal()  # 球出界

    def __init__(self, parent=None):
        super().__init__(parent)
