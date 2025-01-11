from PyQt6.QtWidgets import QVBoxLayout, QWidget

from windows.left.pannel_widget import Panel


def create_left_widget(parent):
    """
    动态创建左边的 Panel 组件

    :param parent: 父组件，必须包含 `urls` 属性
    """
    if not hasattr(parent, 'urls') or not isinstance(parent.urls, list):
        raise ValueError("父组件需要包含一个有效的 'urls' 列表属性")

    left_widget = QWidget(parent)
    layout = QVBoxLayout(left_widget)

    for index, url in enumerate(parent.urls):
        title = f"频道{index + 1}"  # 生成标题，例如 "频道1", "频道2"
        panel = Panel(title, left_widget, url)
        layout.addWidget(panel)

    left_widget.setLayout(layout)
    return left_widget
