from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSplitter

from test import test
from windows.right.top.court import create_court
from windows.right.top.court_event_manager import CourtEventManager


def create_top_widget(parent):
    top_splitter = QSplitter(Qt.Orientation.Horizontal)

    parent.main_event_manager = CourtEventManager()
    main_court = create_court(parent, parent.main_event_manager)
    top_splitter.addWidget(main_court)

    parent.sub_event_manager = CourtEventManager()
    sub_court = create_court(parent, parent.sub_event_manager)
    top_splitter.addWidget(sub_court)


    return top_splitter
