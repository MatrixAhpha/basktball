from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWebSockets import QWebSocket
from PyQt6.QtCore import QUrl


class WebSocketManager(QObject):
    message_received = pyqtSignal(str)  # 信号：接收到消息
    connected = pyqtSignal()           # 信号：连接成功
    disconnected = pyqtSignal()        # 信号：连接断开

    def __init__(self, url):
        super().__init__()
        self.websocket = QWebSocket()
        self.url = QUrl(url)

        self.websocket.connected.connect(self.on_connected)
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.textMessageReceived.connect(self.on_message_received)

    def connect(self):
        """建立 WebSocket 连接"""
        print(f"正在连接到 {self.url}...")
        self.websocket.open(self.url)

    def on_connected(self):
        """连接成功"""
        print("WebSocket 连接已建立")
        self.connected.emit()

    def on_disconnected(self):
        """连接断开"""
        print("WebSocket 连接已断开")
        self.disconnected.emit()

    def on_message_received(self, message):
        """处理接收到的消息"""
        print(f"收到消息: {message}")
        self.message_received.emit(message)

