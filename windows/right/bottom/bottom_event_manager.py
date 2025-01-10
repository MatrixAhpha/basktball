from PyQt6.QtCore import QObject, pyqtSignal


# 定义事件管理器类
class bottomEventManager(QObject):
    # 定义自定义信号
    update = pyqtSignal()  # 拥有球权

    def __init__(self, parent=None):
        super().__init__(parent)
