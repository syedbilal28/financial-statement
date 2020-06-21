import AccountingCycle
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMessageBox,QHeaderView

from acc_2 import *
import sys
import error
import newaccount
import xlrd
import ledger
import wrapper
class MyForm(QDialog):
    def __init__(self):

        super().__init__()

        self.Cycle = AccountingCycle.AccountingCycle()
        self.ui = Ui_Dialog()
        self.debit = []
        self.credit = []
        self.ui.setupUi(self)
        self.show()
        self.ui.Submit.clicked.connect(self.initiatedata)

        self.ui.ShowJournal.clicked.connect(self.Journal)
        self.ui.ShowTrial.clicked.connect(self.Trial)
        self.ui.ShowLedger.clicked.connect(self.Ledger)
        self.ui.AnotherDebit.clicked.connect(self.DebitList)
        self.ui.AnotherCredit.clicked.connect(self.CreditList)
        self.ui.Income.clicked.connect(self.Income_Statement)
        self.ui.Balance.clicked.connect(self.Balance_Sheet)
        self.ui.Close_pre.clicked.connect(self.Closing_Wrapper)

    def Error(self):
        widget = QDialog(self)
        widget.ui = error.Ui_Error()
        widget.ui.setupUi(widget)
        widget.exec_()
        widget.show()



    def Balanced(self):
        deb = 0
        for i in range(len(self.debit)):
            deb += self.debit[i][1]
        cred = 0
        for i in range(len(self.credit)):
            cred += self.credit[i][1]
        if deb != cred:
            return True
        return False

    def initiatedata(self):
        self.DebitList()
        self.CreditList()
        self.ui.PreviousEntry.clear()
        for i in range(len(self.debit)):
            if self.debit[i][0] not in self.Cycle.accountnumbers:
                widget = NewAccount()
                widget.nameinput.setText(self.debit[i][0])
                widget.exec_()

                self.Cycle.accountnumbers.update(widget.Account_)
                x=open("accounts.txt","w")
                x.write(str(self.Cycle.accountnumbers))
                x.close()
                widget.Account_=dict()
        for i in range(len(self.credit)):
            if self.credit[i][0] not in self.Cycle.accountnumbers:
                widget = NewAccount()
                widget.nameinput.setText(self.credit[i][0])
                widget.exec_()

                self.Cycle.accountnumbers.update(widget.Account_)
                x=open("accounts.txt","w")
                x.write(str(self.Cycle.accountnumbers))
                x.close()
                widget.Account_=dict()

        #self.Cycle.accountnumbers.
        if self.Balanced() == True:
            self.Error()
            self.debit = []
            self.credit=[]
            self.ui.DebitValue.clear()
            self.ui.CreditValue.clear()
            self.ui.Debit.setCurrentIndex(0)
            self.ui.Credit.setCurrentIndex(0)
        else:
            x = self.ui.dateEdit.date()
            Date=(x.toPyDate())
            print(Date)
            self.Cycle.JournalEntry(self.debit,self.credit,Date)
            print("hello")
            self.Cycle.AddingIntoTrial(self.debit,self.credit)


        for i in range(len(self.debit)):
            self.Cycle.Balancing(self.debit[i][0])
        for i in range(len(self.credit)):
            self.Cycle.Balancing(self.credit[i][0])
        print("balanced")
        self.Cycle.Ledger(self.debit,self.credit)
        print("Ledger")
        self.debit= []
        self.credit=[]

    def DebitList(self):
        debit = str(self.ui.Debit.currentText()).title()


        try:
            debit_value = int(self.ui.DebitValue.text())
            self.ui.Debit.setCurrentIndex(0)
            self.ui.DebitValue.clear()
            Debit = [debit, debit_value]
            self.debit.append(Debit)


            prev = ("Debit   Account :  {}    Value :  {} ".format(debit, debit_value))
            self.ui.PreviousEntry.setText(prev)

        except:
            widget = QDialog(self)
            widget.ui = error.Ui_Error()
            widget.ui.setupUi(widget)

            widget.ui.label.setText("Please Enter a number")
            widget.exec_()
            widget.show()
            self.debit = []
            debit_value=0
            self.ui.DebitValue.clear()

            self.ui.Debit.setCurrentIndex(0)



    def CreditList(self):
        credit = str(self.ui.Credit.currentText())
        try :
            credit_value = int(self.ui.CreditValue.text())
            self.ui.Credit.setCurrentIndex(0)
            self.ui.CreditValue.clear()
            Credit = [credit, credit_value]
            self.credit.append(Credit)
            prev = ("Credit   Account :  {}    Value :  {} ".format(credit, credit_value))
            self.ui.PreviousEntry.setText(prev)

        except:
            widget = QDialog(self)
            widget.ui = error.Ui_Error()
            widget.ui.setupUi(widget)

            widget.ui.label.setText("Please Enter a number")
            widget.exec_()
            widget.show()
            self.credit = []
            credit_value = 0
            self.ui.CreditValue.clear()

            self.ui.Credit.setCurrentIndex(0)
    def Journal(self):
        self.ui.tableWidget_2.setRowCount(0)

        self.ui.tabWidget.setCurrentIndex(2)
        book = xlrd.open_workbook(self.Cycle.xlpath)
        sheet = book.sheets()[0]

        rows = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]



        for i in range(len(rows)):


            self.ui.tableWidget_2.insertRow(i)
            for j in range(len(rows[0])):
                self.ui.tableWidget_2.setItem(i,j,QTableWidgetItem(str((rows[i][j]))))
        header = self.ui.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    def Trial(self):

        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(13)
        self.ui.tableWidget.setColumnCount(13)
        self.ui.tabWidget.setCurrentIndex(1)
        query = "Select * from Accounts"
        eng = engine.create_engine("sqlite:///" + os.path.abspath("./data1.db"))
        cur = eng.execute(query)

        rows = cur.fetchall()
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
        eng.dispose()
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    def Ledger(self):
        widget= LedgerShower()
        widget.exec_()
    def Income_Statement(self):
        self.ui.tableWidget_4.setRowCount(0)

        self.ui.tabWidget.setCurrentIndex(4)
        book = xlrd.open_workbook(self.Cycle.xlpath)
        sheet = book.sheets()[1]
        print("here")
        rows = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

        for i in range(len(rows)):

            self.ui.tableWidget_4.insertRow(i)
            for j in range(len(rows[0])):
                self.ui.tableWidget_4.setItem(i, j, QTableWidgetItem(str((rows[i][j]))))
        header = self.ui.tableWidget_4.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
    def Balance_Sheet(self):
        self.ui.tableWidget_5.setRowCount(0)

        self.ui.tabWidget.setCurrentIndex(5)
        book = xlrd.open_workbook(self.Cycle.xlpath)
        sheet = book.sheets()[2]

        rows = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

        for i in range(len(rows)):

            self.ui.tableWidget_5.insertRow(i)
            for j in range(len(rows[0])):
                self.ui.tableWidget_5.setItem(i, j, QTableWidgetItem(str((rows[i][j]))))
        header = self.ui.tableWidget_5.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
    def Closing_Wrapper(self):
        widget = Wrap()
        widget.exec_()


class LedgerShower(QDialog,ledger.Ui_Ledger):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.LedgerOK.clicked.connect(self.Ledgertable)
from sqlalchemy import engine,Table, Column, Integer, String, MetaData
import os
class NewAccount(QDialog,newaccount.Ui_Account):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.AccountInput.clicked.connect(self.new_account)

    def new_account(self):
        Account = str(self.nameinput.text())
        AccountNumber = int(self.numberinput.text())
        self.Account_ = {Account: AccountNumber}
        eng = engine.create_engine("sqlite:///"+os.path.abspath("./data1.db"))
        meta = MetaData()
        x= Table(str(AccountNumber),meta,Column("Debit",Integer),Column("Credit",Integer))
        meta.create_all(eng)
        self.close()
class Wrap(QDialog,wrapper.Ui_Dialog):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Closed)
    def Closed(self):
        self.cycle = AccountingCycle.AccountingCycle()
        self.cycle.Closing()








if __name__=="__main__":
    app =QApplication(sys.argv)
    w = MyForm()

    w.show()

    sys.exit(app.exec_())




