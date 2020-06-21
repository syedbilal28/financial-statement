import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication,QTableView
from PyQt5.QtCore import QAbstractTableModel,Qt
import numpy as np



class pandasModel(QAbstractTableModel):
    def __init__(self,data):
        super().__init__()
        self.data=data

    def rowCount(self, parent=None):
        return self.data.shape[0]

    def columnCount(self, parent=None):
        return self.data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.data.columns[col]
        return None
# if __name__ =="__main__":
#     app =QApplication(sys.argv)
#     model = pandasModel()
#     view = QTableView()
#     view.setModel(model)
#     view.resize(600,800)
#     view.show()
#     sys.exit(app.exec_())

