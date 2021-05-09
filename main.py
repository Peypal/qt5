import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TableView(QWidget):
    def __init__(self, arg=None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle("QTableView表格视图控件演示")
        self.resize(500, 300)
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])
        self.tableview = QTableView()
        self.tableview.setModel(self.model)
        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)
        item11 = QStandardItem('10')
        item12 = QStandardItem('listen')
        item13 = QStandardItem('200')
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = TableView()
    gui.show()
    sys.exit(app.exec_())
