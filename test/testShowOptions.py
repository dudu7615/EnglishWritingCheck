from PySide6.QtWidgets import QApplication
from modules import Enums
from ui import ShowOptions

def testShowOptions(options: Enums.ShowDetaleOption):
    print(options)

app = QApplication()
ui = ShowOptions.ShowOptionsUi()
ui.setOrignOption(
    Enums.ShowDetaleOption.advanced_expression_pattern
    | Enums.ShowDetaleOption.advanced_vocabulary
)
ui.optionChange.connect(testShowOptions)
ui.show()
app.exec()
