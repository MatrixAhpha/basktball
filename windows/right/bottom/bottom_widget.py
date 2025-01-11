from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout

from pojo.Match import MatchSingleton
from windows.right.bottom.bottom_event_manager import bottomEventManager


def create_bottom_widget(parent):
    """
    创建底部表格组件，用于展示 Match 信息。
    """
    # 下部区域容器
    bottom_widget = QWidget(parent)
    bottom_widget.setStyleSheet("background-color: lightyellow;")

    # 使用 QGridLayout 布局
    grid_layout = QGridLayout()
    bottom_widget.setLayout(grid_layout)

    # 获取 Match 实例
    match = MatchSingleton.get_instance()

    # 创建 QLabel 并添加到表格
    labels = {
        "quarter": create_label(match.quarter, alignment=Qt.AlignmentFlag.AlignCenter),
        "time": create_label(match.time, alignment=Qt.AlignmentFlag.AlignCenter),
        "score": create_label(f"{match.score[0]} - {match.score[1]}", alignment=Qt.AlignmentFlag.AlignCenter),
        "home_team": create_label(match.home_team, alignment=Qt.AlignmentFlag.AlignCenter),
        "away_team": create_label(match.away_team, alignment=Qt.AlignmentFlag.AlignCenter),
        "home_team_stats": create_label(str(match.home_team_stats), alignment=Qt.AlignmentFlag.AlignCenter),
        "away_team_stats": create_label(str(match.away_team_stats), alignment=Qt.AlignmentFlag.AlignCenter),
        "new_event": create_label(match.new_event, alignment=Qt.AlignmentFlag.AlignCenter),
    }

    # 添加组件到布局
    grid_layout.addWidget(labels["quarter"], 0, 0, 1, 2)  # 第一行，跨2列
    grid_layout.addWidget(labels["time"], 1, 0, 1, 2)  # 第二行，跨2列
    grid_layout.addWidget(labels["score"], 2, 0, 1, 2)  # 第三行，跨2列
    grid_layout.addWidget(labels["home_team"], 3, 0)  # 第四行左侧
    grid_layout.addWidget(labels["away_team"], 3, 1)  # 第四行右侧
    grid_layout.addWidget(labels["home_team_stats"], 4, 0)  # 第五行左侧
    grid_layout.addWidget(labels["away_team_stats"], 4, 1)  # 第五行右侧
    grid_layout.addWidget(labels["new_event"], 5, 0, 1, 2)  # 最后一行，跨2列

    # 创建事件管理器并连接更新信号
    bottom_widget.event_manager = bottomEventManager()
    bottom_widget.event_manager.update.connect(
        lambda: update_bottom_widget(labels)
    )

    return bottom_widget


def create_label(text, alignment=Qt.AlignmentFlag.AlignLeft):
    """
    创建 QLabel 并设置默认样式。
    """
    label = QLabel(text)
    label.setAlignment(alignment)
    label.setStyleSheet("font-size: 14px; padding: 2px;")  # 可根据需求调整样式
    return label


def update_bottom_widget(labels):
    """
    更新表格中 QLabel 的内容。
    """
    match = MatchSingleton.get_instance()
    updated_data = {
        "quarter": match.quarter,
        "time": match.time,
        "score": f"{match.score[0]} - {match.score[1]}",
        "home_team": match.home_team,
        "away_team": match.away_team,
        "home_team_stats": str(match.home_team_stats),
        "away_team_stats": str(match.away_team_stats),
        "new_event": match.new_event,
    }

    for key, new_text in updated_data.items():
        labels[key].setText(new_text)
