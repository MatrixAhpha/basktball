from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWebSockets import QWebSocket
from PyQt6.QtCore import QUrl

from match_singleton import MatchSingleton


class WebSocketManager(QObject):
    message_received = pyqtSignal(str)  # 信号：接收到消息
    connected = pyqtSignal()  # 信号：连接成功
    disconnected = pyqtSignal()  # 信号：连接断开

    def __init__(self, urls):
        """
        初始化 WebSocketManager

        :param urls: 一个包含字符串类型 URL 的列表
        """
        super().__init__()
        self.websocket = QWebSocket()
        self.urls = [QUrl(url) for url in urls]  # 将字符串 URL 转换为 QUrl 对象
        self.current_index = 0  # 当前连接的 URL 索引
        self.current_url = self.urls[self.current_index] if self.urls else None

        self.websocket.connected.connect(self.on_connected)
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.textMessageReceived.connect(self.on_message_received)

        if not self.urls:
            raise ValueError("URL 列表不能为空")

    def connect(self):
        match = MatchSingleton.get_instance()
        match.clear()
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
        """
        切换连接到指定的 URL

        :param url: 要切换的目标 URL (字符串)
        """
        new_url = QUrl(url)  # 将字符串类型的 URL 转换为 QUrl 对象
        if new_url != self.current_url and new_url in self.urls:
            self.current_url = new_url
            print(f"切换连接到新的 URL: {self.current_url}")
            self.websocket.close()  # 关闭当前连接
            self.connect()  # 建立新连接
        elif new_url not in self.urls:
            print(f"错误: 指定的 URL 不在初始化时提供的列表中: {url}")
