import sys
from PyQt6.QtWidgets import QApplication

from websocket_manager import WebSocketManager
from windows.MainWindow import MainWindow

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    websocket_manager = WebSocketManager("ws://localhost:6789")
    websocket_manager.connect()  # 启动 WebSocket 连接
    window = MainWindow()
    window.show()
    websocket_manager.message_received.connect(lambda msg: print(f"主窗口收到消息: {msg}"))
    sys.exit(app.exec())
