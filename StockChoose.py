# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys,os,json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem,QDialog,QPushButton

sys.path.append(os.getcwd())

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.setFixedSize(682, 567)

        self.label = QtWidgets.QLabel(form)
        self.label.setGeometry(QtCore.QRect(20, 20, 86, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(form)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 59, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 50, 331, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(form)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 59, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(form)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 90, 331, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.tableWidget = QtWidgets.QTableWidget(form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 621, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏竖表头

        self.tableWidget.horizontalHeader().resizeSection(0, 60)  # 调整第一列的大小为100像素
        self.tableWidget.horizontalHeader().resizeSection(1, 330)  # 调整第一列的大小为100像素
        self.tableWidget.horizontalHeader().resizeSection(2, 210)  # 调整第一列的大小为100像素

        self.pushButton = QtWidgets.QPushButton(form)
        self.pushButton.setGeometry(QtCore.QRect(420, 510, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(form)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 510, 81, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QtWidgets.QToolButton(form)
        self.toolButton.setGeometry(QtCore.QRect(450, 10, 31, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(form)
        self.toolButton_2.setGeometry(QtCore.QRect(450, 50, 31, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(form)
        self.toolButton_3.setGeometry(QtCore.QRect(450, 90, 31, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        self.pushButton_3 = QtWidgets.QPushButton(form)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 52, 80, 60))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

        if not os.path.exists(os.getcwd() + "/Models/"):
            os.mkdir(os.getcwd() + "/Models/")

        form.setWindowTitle('多板块叠加选股-炒股小神器V1')

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.label.setText(_translate("form", "自由匹配模块："))
        self.label_2.setText(_translate("form", "必加模块："))
        self.label_3.setText(_translate("form", "必减模块："))

        self.pushButton.setText(_translate("form", "股票池"))
        self.pushButton.clicked.connect(lambda: self.jumpPool())
        self.pushButton_2.setText(_translate("form", "模板库"))
        self.pushButton_2.clicked.connect(lambda: self.jumpTem())

        self.toolButton.setText(_translate("form", "+"))
        self.toolButton.clicked.connect(lambda: self.openMyDialog(form))
        self.toolButton_2.setText(_translate("form", "+"))
        self.toolButton_2.clicked.connect(lambda: self.openMyDialog_2(form))
        self.toolButton_3.setText(_translate("form", "+"))
        self.toolButton_3.clicked.connect(lambda: self.openMyDialog_3(form))

        self.pushButton_3.setText(_translate("form", "搜索"))
        self.pushButton_3.clicked.connect(lambda: self.search())

    def search(self):
        L1 = list(set(self.lineEdit.text().split(";")))
        L2 = list(set(self.lineEdit_2.text().split(";")))
        L3 = list(set(self.lineEdit_3.text().split(";")))

        # 去重 将L1中的必加板块去掉 将L1中的比减板块去掉
        for i in L3:
            if i in L1:
                L1.remove(i)
        for i in L2:
            if i in L1:
                L1.remove(i)

        path = os.getcwd() + "/Tem/"
        # 得到必加板块中的股票名称
        D2 = []
        for i in L2:
            rL2 = path + i + ".json"
            if os.path.exists(rL2):
                with open(rL2, "r") as f:
                    if f.read():
                        f.seek(0)
                        D = json.loads(f.read())
                        for j in D:
                            if j not in D2:
                                D2.append(j[1])

        # 得到必减板块中的股票名称
        D3 = []
        for i in L3:
            rL3 = path + i + ".json"
            if os.path.exists(rL3):
                with open(rL3, "r") as f:
                    if f.read():
                        f.seek(0)
                        D = json.loads(f.read())
                        for j in D:
                            if j not in D3:
                                D3.append(j[1])

        finalResult = {}
        if D2:
            for i in L1:
                rL1 = path + i + ".json"
                if os.path.exists(rL1):
                    with open(rL1, "r") as f:
                        if f.read():
                            f.seek(0)
                            PD = json.loads(f.read())
                            XD = [i[1] for i in PD]
                            result = list(set(XD).intersection(set(D2)))
                            for j in result:
                                if j not in D3:
                                    if j not in finalResult:
                                        finalResult[j] = [i]
                                    else:
                                        finalResult[j].append(i)
        else:
            for i in L1:
                rL1 = path + i + ".json"
                if os.path.exists(rL1):
                    with open(rL1, "r") as f:
                        if f.read():
                            f.seek(0)
                            PD = json.loads(f.read())
                            result = [i[1] for i in PD]
                            for j in result:
                                if j not in D3:
                                    if j not in finalResult:
                                        finalResult[j] = [i]
                                    else:
                                        finalResult[j].append(i)

        finalResult = sorted(finalResult.items(), key=lambda x: len(x[1]), reverse=True)
        self.insertDOWN(finalResult)

    def insertDOWN(self, PD):
        self.tableWidget.clear()

        XD= {}
        for i in PD:
            if i[0] not in XD:
                # print(i[0], i[1], len(i[1]))
                Ji = str(i[1])
                if Ji not in XD:
                    XD[Ji] = {"list": [i[0]], "mount":len(i[1])}
                else:
                    XD[Ji]["list"].append(i[0])

        lenT = len(XD)
        self.tableWidget.setRowCount(lenT+1)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("叠加次数"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("板块名称"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("股票"))

        # print(XD)
        ii = 1
        for i in XD.keys():
            # print(str(len(XD[i][1])), XD[i], str(XD[i][1]), ii, i)
            iname = i.replace("[", "").replace("]", "").replace("'", "")
            ilist = str(XD[i]['list']).replace("[", "").replace("]", "").replace("'", "")
            self.tableWidget.setItem(ii, 2, QTableWidgetItem(ilist))
            self.tableWidget.setItem(ii, 1, QTableWidgetItem(iname))
            self.tableWidget.setItem(ii, 0, QTableWidgetItem(str(XD[i]['mount'])))
            ii += 1

    def takeSecond(self, elem):
        return  len(elem.values()[1])

    def openMyDialog(self, form):
        my = MyDialog(form)
        # 在主窗口中连接信号和槽
        my.mySignal.connect(self.getDialogSignal)
        my.exec_()

    def getDialogSignal(self, JsonPD):
        PD = json.loads(JsonPD)
        if PD:
            oldText = self.lineEdit.text()
            for i in PD:
                oldText += str(i)+";"
            self.lineEdit.setText(oldText)

    def openMyDialog_2(self, form):
        my = MyDialog(form)
        # 在主窗口中连接信号和槽
        my.mySignal.connect(self.getDialogSignal_2)
        my.exec_()

    def getDialogSignal_2(self, JsonPD):
        PD = json.loads(JsonPD)
        if PD:
            oldText = self.lineEdit_2.text()
            for i in PD:
                oldText += str(i) + ";"
            self.lineEdit_2.setText(oldText)

    def openMyDialog_3(self, form):
        my = MyDialog(form)
        # 在主窗口中连接信号和槽
        my.mySignal.connect(self.getDialogSignal_3)
        my.exec_()

    def getDialogSignal_3(self, JsonPD):
        PD = json.loads(JsonPD)
        if PD:
            oldText = self.lineEdit_3.text()
            for i in PD:
                oldText += str(i) + ";"
            self.lineEdit_3.setText(oldText)

    def jumpPool(self):
        pass

    def jumpTem(self):
        pass

class MyDialog(QDialog):

    # 自定义信号
    mySignal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(MyDialog, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.setWindowTitle('选择股票池的股票')
        self.setFixedSize(1245, 900)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 1205, 800))
        self.tableWidget.setObjectName("tableWidget_2")
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏竖表头
        self.tableWidget.setColumnCount(9)

        button = QPushButton('确定', self)
        button.setGeometry(QtCore.QRect(600, 820, 120, 50))
        button.clicked.connect(self.sendEditContent)

        self.init()

    def init(self):
        self.Tem = []
        if os.path.exists(os.getcwd() + "/Tem"):
            for parent, dirnames, filenames in os.walk(os.getcwd() + "/Tem", followlinks=True):
                for filename in filenames:
                    self.Tem.append(filename[:-5])
            self.insertUP()
        else:
            os.mkdir(os.getcwd() + "/Tem")

    def insertUP(self):
        self.tableWidget.clear()
        self.Tem.sort()
        lenT = len(self.Tem)
        horizon = lenT // 9
        if lenT % 9 !=0:
            horizon+=1
        self.tableWidget.setRowCount(horizon)

        for i in range(horizon):
            x = (lenT-12*i) //9
            if x > 0:
                for j in range(9):
                    lab1 = QTableWidgetItem(QIcon(os.getcwd() + '/img/dic.jpg'), self.Tem[i * 9 + j])
                    self.tableWidget.setItem(i, j, lab1)
            else:
                y = lenT - 9*i
                for j in range(y):
                    # lab1 = QLabel()
                    # lab1.setPixmap(QPixmap(os.getcwd() + '/img/dic.jpg').scaled(18, 18))
                    # self.tableWidget.setCellWidget(j, i*2, lab1)
                    lab1 = QTableWidgetItem(QIcon(os.getcwd() + '/img/dic.jpg'), self.Tem[i * 9 + j])
                    self.tableWidget.setItem(i, j, lab1)

    def sendEditContent(self):
        clickList_1 = self.tableWidget.selectedItems()
        if clickList_1:
            PD = []
            for i in clickList_1:
                if i.text() not in PD:
                    PD.append(i.text())
            if PD:
                self.mySignal.emit(json.dumps(PD)) # 发射信号
            self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())