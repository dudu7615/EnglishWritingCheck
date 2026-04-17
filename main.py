from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from qt_material import apply_stylesheet  # type: ignore
from ui import Main

if __name__ == "__main__":
    app = QApplication([])
    font = QFont("MapleMono NF CN")
    apply_stylesheet(app, theme="dark_cyan.xml")
    font.setPointSize(14)
    app.setFont(font)
    ui = Main.MainUi()
    ui.show()
    app.exec()
