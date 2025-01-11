import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication

from countdown import decrement_time
from match_singleton import MatchSingleton
from process_message import process_message
from websocket_manager import WebSocketManager
from windows.MainWindow import MainWindow


# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    websocket_manager = WebSocketManager("ws://localhost:6789")
    websocket_manager.connect()  # 启动 WebSocket 连接

    window = MainWindow()
    window.show()

    match = MatchSingleton.get_instance()
    match.set_window(window)

    websocket_manager.message_received.connect(lambda msg: process_message(msg))

    # 设置一个定时器，每 1/3 秒更新 Match 的时间
    timer = QTimer()
    timer.timeout.connect(lambda: decrement_time(window))
    timer.start(500)  # 1/3 秒 = 333 毫秒

    sys.exit(app.exec())
