from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWebSockets import QWebSocket
from PyQt6.QtCore import QUrl


class WebSocketManager(QObject):
    message_received = pyqtSignal(str)  # 信号：接收到消息
    connected = pyqtSignal()           # 信号：连接成功
    disconnected = pyqtSignal()        # 信号：连接断开

    def __init__(self, url1, url2):
        super().__init__()
        self.websocket = QWebSocket()
        self.url1 = QUrl(url1)
        self.url2 = QUrl(url2)
        self.current_url = self.url1

        self.websocket.connected.connect(self.on_connected)
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.textMessageReceived.connect(self.on_message_received)


    def connect(self):
        """建立 WebSocket 连接"""
        print(f"正在连接到 {self.current_url}...")
        self.websocket.open(self.current_url)

    def on_connected(self):
        """连接成功"""
        print(f"WebSocket 连接已建立: {self.current_url}")
        self.connected.emit()

    def on_disconnected(self):
        """连接断开"""
        print(f"WebSocket 连接已断开: {self.current_url}")
        self.disconnected.emit()

    def on_message_received(self, message):
        """处理接收到的消息"""
        self.message_received.emit(message)

    def on_change(self, url):
        new_url = QUrl(url)  # 将字符串类型的 URL 转换为 QUrl 对象
        if new_url != self.current_url:
            self.current_url = new_url
            print("切换连接中...")
            self.websocket.close()  # 关闭当前连接
            self.connect()  # 建立新连接