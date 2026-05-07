from PySide6.QtWidgets import QDialog, QAbstractButton, QDialogButtonBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Signal, Qt
from modules import Enums

from .Windows import ShowOption_ui


class ShowOptionsUi(QDialog):
    optionChange = Signal(Enums.ShowDetaleOption)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("选择显示选项")
        self.ui = ShowOption_ui.Ui_Dialog()
        self.ui.setupUi(self)  # type: ignore
        self._model = QStandardItemModel(self.ui.optionsView)
        self._orignOptions = Enums.ShowDetaleOption.NONE
        self.initUi()

    def initUi(self):
        self.ui.optionsView.setModel(self._model)
        self.ui.optionsView.clicked.connect(self.optionClicked)
        self.ui.buttonBox.clicked.connect(self.buttonBoxClicked)
        self._setItems()

    def optionClicked(self, item: QStandardItem):
        self.optionChange.emit(self._getSelectedItems())

    def buttonBoxClicked(self, button: QAbstractButton):
        if button == self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok):
            self.optionChange.emit(self._getSelectedItems())
            self.close()
        elif button == self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel):
            self.optionChange.emit(self._orignOptions)
            self.close()

    def setOrignOption(self, options: Enums.ShowDetaleOption):
        self._orignOptions = options

    def _addItem(self, name: str):
        item = QStandardItem(name)
        item.setFlags(
            item.flags() | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled
        )
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        self._model.appendRow(item)

    def _setItems(self):
        for option in Enums.ShowDetaleOption:
            self._addItem(Enums.optionNames[option])

    def _getSelectedItems(self):
        selectedItems: list[Enums.ShowDetaleOption] = []
        for i in range(self._model.rowCount()):
            item = self._model.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selectedItems.append(
                    Enums.oppositeOptionNames.get(
                        item.text(), Enums.ShowDetaleOption.NONE
                    )
                )

        options = Enums.ShowDetaleOption.NONE
        for item in selectedItems:
            options |= item
        return options
