import AccountingCycle
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem
from acc_ import *
import os
from sqlalchemy import engine
from extra2 import *
import pandas as pd
import extra
import xlrd
class MyForm(QDialog):
    def __init__(self):

        super().__init__()

        self.Cycle = AccountingCycle.AccountingCycle()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
        self.show()
        self.ui.Submit.clicked.connect(self.initiatedata)

        self.ui.ShowJournal.clicked.connect(self.Journal)
        self.ui.ShowTrial.clicked.connect(self.Trial)
        self.ui.ShowLedger.clicked.connect(self.Ledger)

    def initiatedata(self):


        self.debit = str(self.ui.Debit.currentText())
        print(self.debit)
        self.credit = str(self.ui.Credit.currentText())
        self.value = int(self.ui.Value.text())
        self.Cycle.JournalEntry(self.debit,self.credit,self.value)
        self.Cycle.AddingIntoTrial(self.debit,self.credit,self.value)
        self.Cycle.Balancing(self.debit)
        self.Cycle.Balancing(self.credit)
    def Journal(self):

        self.ui.tabWidget.setCurrentIndex(2)
        book = xlrd.open_workbook(os.path.abspath("./1.xlsx"))
        sheet = book.sheets()[0]

        rows = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        print(rows)
        # row = len(data)

        for row in rows:
            inx = rows.index(row)

            self.ui.tableWidget_2.insertRow(inx)

            # add more if there is more columns in the database.
            self.ui.tableWidget_2.setItem(inx,0,QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_2.setItem(inx, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_2.setItem(inx, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_2.setItem(inx,3,QTableWidgetItem(str(row[3])))


    def Trial(self):


        self.ui.tabWidget.setCurrentIndex(1)
        query = "Select * from Accounts"
        eng = engine.create_engine("sqlite:///" + os.path.abspath("./data1.db"))
        cur = eng.execute(query)

        rows = cur.fetchall()
        #self.ui.tableWidget.InsertRow(0)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Account Number"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Account Name"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("Debit"))
        self.ui.tableWidget.setItem(0,3,QTableWidgetItem("Credit"))

        for row in rows:
            inx = rows.index(row)+1
            print(inx)
            self.ui.tableWidget.insertRow(inx)

            # add more if there is more columns in the database.
            self.ui.tableWidget.setItem(inx,0,QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(inx, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(inx, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(inx,3,QTableWidgetItem(str(row[3])))

        self.ui.tableWidget.insertRow(inx+1)
        credits_ = eng.execute("Select credit from Accounts ")
        credits_= credits_.fetchall()
        credits = []
        for i in range(inx):
            credits.append(credits_[i][0])


        debits_ = eng.execute("Select debit from Accounts")
        debits_= debits_.fetchall()
        debits= []
        for i in range(inx):
            debits.append(debits_[i][0])
        credits = sum(credits)
        debits= sum(debits)
        self.ui.tableWidget.setItem(inx+1, 2, QTableWidgetItem(str(debits)))
        self.ui.tableWidget.setItem(inx+1, 3, QTableWidgetItem(str(credits)))



        # credits_sum = sum(credits)
        # print(credits_sum)
        # cur = eng.execute("Select * From Accounts")
        # allSQLRows = cur.fetchall()
        # print(allSQLRows)
        # self.ui.tableWidget.setRowCount(len(allSQLRows))
        # self.ui.tableWidget.setColumnCount(4)
        #
        # row = 0
        # while True:
        #     sqlRow = cur.fetchone()
        #     if sqlRow == None:
        #         break
        #     for col in range(0, 4):
        #         self.ui.tableWidget.setItem(row, col, QTableWidgetItem(sqlRow[col]))
        #     row += 1

        eng.dispose()
    def Ledger(self):
        self.ui.tabWidget.setCurrentIndex(3)
        book = xlrd.open_workbook(os.path.abspath("./1.xlsx"))
        sheet = book.sheets()[1]

        rows = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        print(rows)
        # row = len(data)

        for row in rows:
            inx = rows.index(row)

            self.ui.tableWidget_3.insertRow(inx)

            # add more if there is more columns in the database.
            self.ui.tableWidget_3.setItem(inx, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_3.setItem(inx, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_3.setItem(inx, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_3.setItem(inx, 3, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_3.setItem(inx, 4, QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_3.setItem(inx, 5, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_3.setItem(inx, 6, QTableWidgetItem(str(row[6])))
            self.ui.tableWidget_3.setItem(inx, 7, QTableWidgetItem(str(row[7])))
            self.ui.tableWidget_3.setItem(inx, 8, QTableWidgetItem(str(row[8])))
            #self.ui.tableWidget_3.setItem(inx, 9, QTableWidgetItem(str(row[9])))


if __name__=="__main__":
    app =QApplication(sys.argv)
    w = MyForm()
    # import threading
    # show_lock = threading.Lock()
    #
    #
    w.show()
    # with show_lock():
    #     w.Journal()
    # for x in range(3):
    #     t = threading.Thread(target=app)
    #     t.daemon = True
    #     t.start()


    sys.exit(app.exec_())





# debit=str(input("Enter the Account you wanna debit: "))
# credit= str(input("Enter the account you wanna Credit: "))
# value= int(input("Enter the value: "))
# company = AccountingCycle.AccountingCycle()
# company.JournalEntry(debit,credit,value)
# # company.AddingIntoTrial(debit,credit,value)
# company.Balancing(debit)
# company.Balancing(credit)
