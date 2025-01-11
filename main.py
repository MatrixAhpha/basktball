import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication

from pojo.Match import MatchSingleton
from process_message import process_message
from websocket_manager import WebSocketManager
from windows.MainWindow import MainWindow


def decrement_time(window):
    """
    每 1/3 秒减少 Match 的倒计时时间。
    """
    match = MatchSingleton.get_instance()
    time_parts = match.time.split(":")
    if len(time_parts) == 2:
        minutes, seconds = map(int, time_parts)
        total_seconds = minutes * 60 + seconds

        if total_seconds > 0:
            total_seconds -= 1

        minutes, seconds = divmod(total_seconds, 60)
        match.time = f"{minutes:02}:{seconds:02}"
        window.event_managers["bottom"].update.emit()


# 主程序入口
if __name__ == "__main__":
    # 检查是否有传入参数
    if len(sys.argv) < 2:
        print("用法: python script.py <url1> <url2> ...")
        sys.exit(1)

    # 从命令行参数创建 URL 集合
    urls = list(set(sys.argv[1:]))  # 去重并转换为列表
    print(f"接收到的 URL 集合: {urls}")

    app = QApplication(sys.argv)

    # 初始化 WebSocketManager，传入第一个和第二个 URL
    websocket_manager = WebSocketManager(urls)
    websocket_manager.connect()  # 启动 WebSocket 连接

    window = MainWindow(urls)
    window.websocket_manager = websocket_manager
    window.show()

    match = MatchSingleton.get_instance()
    match.set_window(window)

    websocket_manager.message_received.connect(lambda msg: process_message(msg))

    # 设置一个定时器，每 1/3 秒更新 Match 的时间
    timer = QTimer()
    timer.timeout.connect(lambda: decrement_time(window))
    timer.start(500)  # 1/3 秒 = 333 毫秒

    sys.exit(app.exec())
