from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget

from pojo.Match import MatchSingleton


class PopupWindow(QDialog):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Player Statistics")
        self.setFixedSize(600, 600)  # 调整宽度为 600

        # 获取统计数据
        match = MatchSingleton.get_instance()
        if name == "main_court":
            statistics = match.home_team_stats.player_statistics
        else:
            statistics = match.away_team_stats.player_statistics

        # 设置主布局
        layout = QVBoxLayout(self)

        # 添加滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用横向滚动条
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)    # 启用竖向滚动条
        layout.addWidget(scroll_area)

        # 创建滚动区域的内容部件
        content_widget = QWidget()
        scroll_layout = QVBoxLayout(content_widget)

        for player_name, player_stat in statistics.items():  # 如果 statistics 是字典
            stat_label = QLabel(f"{player_name}: {player_stat}", self)  # 展示球员名称和统计
            stat_label.setStyleSheet("font-size: 14px; margin-bottom: 10px;")
            scroll_layout.addWidget(stat_label)

        content_widget.setLayout(scroll_layout)
        scroll_area.setWidget(content_widget)
