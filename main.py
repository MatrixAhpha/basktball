import sys
from PyQt6.QtWidgets import QApplication

from pojo.Match import Match
from process_message import process_message
from websocket_manager import WebSocketManager
from windows.MainWindow import MainWindow

match = Match(None, None)

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    websocket_manager = WebSocketManager("ws://localhost:6789")
    websocket_manager.connect()  # 启动 WebSocket 连接
    window = MainWindow()
    window.show()
    websocket_manager.message_received.connect(lambda msg: process_message(msg, match))
    sys.exit(app.exec())
