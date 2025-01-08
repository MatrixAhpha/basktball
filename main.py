import sys
from PyQt6.QtWidgets import QApplication

from windows.MainWindow import MainWindow

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
