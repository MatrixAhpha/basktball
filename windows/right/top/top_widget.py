from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSplitter
from windows.right.top.court import create_court, CourtEventManager


def create_top_widget(parent):
    top_splitter = QSplitter(Qt.Orientation.Horizontal)

    # 主场事件管理器和场地
    # parent.main_event_manager = CourtEventManager()
    parent.event_managers["main_court"] = CourtEventManager()
    main_court = create_court(parent, parent.event_managers["main_court"], "main_court")
    main_court.setObjectName("main_court")
    top_splitter.addWidget(main_court)

    # 子场事件管理器和场地
    # parent.sub_event_manager = CourtEventManager()
    parent.event_managers["sub_court"] = CourtEventManager()
    sub_court = create_court(parent, parent.event_managers["sub_court"], "sub_court")
    sub_court.setObjectName("sub_court")
    top_splitter.addWidget(sub_court)

    return top_splitter
