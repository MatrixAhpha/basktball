from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWebSockets import QWebSocket
from PyQt6.QtCore import QUrl


class WebSocketManager(QObject):
    message_received = pyqtSignal(str)  # 信号：接收到消息
    connected = pyqtSignal()           # 信号：连接成功
    disconnected = pyqtSignal()        # 信号：连接断开
    change = pyqtSignal()              # 信号：切换连接

    def __init__(self, url1, url2):
        super().__init__()
        self.websocket = QWebSocket()
        self.url1 = QUrl(url1)
        self.url2 = QUrl(url2)
        self.current_url = self.url1

        self.websocket.connected.connect(self.on_connected)
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.textMessageReceived.connect(self.on_message_received)

        self.change.connect(self.on_change)

    def connect(self):
        """建立 WebSocket 连接"""
        print(f"正在连接到 {self.current_url}...")
        self.websocket.open(self.current_url)

    def on_connected(self):
        """连接成功"""
        print(f"WebSocket 连接已建立: {self.current_url.toString()}")
        self.connected.emit()

    def on_disconnected(self):
        """连接断开"""
        print(f"WebSocket 连接已断开: {self.current_url.toString()}")
        self.disconnected.emit()

    def on_message_received(self, message):
        """处理接收到的消息"""
        self.message_received.emit(message)

    def on_change(self):
        """切换连接"""
        print("切换连接中...")
        self.websocket.close()
        self.current_url = self.url2 if self.current_url == self.url1 else self.url1
        self.connect()
