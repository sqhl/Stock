# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'three.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import os,sys,json,copy
from itertools import groupby
from PyQt5 import QtCore,QtWidgets
from openpyxl import load_workbook
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem,QInputDialog,QLineEdit,\
    QFileDialog,QDialog,QPushButton

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1045, 739)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(880, 40, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 110, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 180, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 380, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(880, 440, 121, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(880, 500, 121, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(880, 560, 121, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(880, 620, 121, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 340, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 121, 21))
        self.label_2.setObjectName("label_2")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 841, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(9)
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏竖表头
        self.tableWidget.itemSelectionChanged.connect(self.tableSelect)

        for i in range(9):
            self.tableWidget.verticalHeader().resizeSection(i, 25)  # 调整第一列的大小为100像素
        self.tableWidget.setShowGrid(False)

        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 370, 841, 351))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.tableWidget_2.verticalHeader().setVisible(False)  # 隐藏竖表头
        for i in range(5):
            self.tableWidget_2.horizontalHeader().resizeSection(i, 150)  # 调整第一列的大小为100像素
        self.tableWidget_2.setShowGrid(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setWindowTitle("自创建模板库-炒股小神器V1")
        self.init()

        self.flag = 1
        if os.path.exists(os.getcwd()+"/Models/data.json"):
            with open(os.getcwd() + "/Models/data.json", "r") as f:
                JsonD = f.read()
            self.D = json.loads(JsonD)
        else:
            QMessageBox.warning(Form, "警告", "股票池文件不存在！请导入", QMessageBox.Yes)

    def init(self):
        self.Tem = []
        if os.path.exists(os.getcwd() + "/Tem"):
            for parent, dirnames, filenames in os.walk(os.getcwd()+"/Tem", followlinks=True):
                for filename in filenames:
                    self.Tem.append(filename[:-5])
        else:
            os.mkdir(os.getcwd()+"/Tem")
        self.insertUP()

    def insertUP(self):
        self.tableWidget.clear()
        self.Tem.sort()
        lenT = len(self.Tem)
        horizon = lenT // 9
        if lenT % 9 !=0:
            horizon+=1
        self.tableWidget.setColumnCount(horizon)
        for i in range(horizon):
                self.tableWidget.horizontalHeader().resizeSection(i, 150)  # 调整第一列的大小为100像素

        for i in range(horizon):
            x = (lenT-9*i) // 9
            if x > 0:
                for j in range(9):
                    lab1 = QTableWidgetItem(QIcon(os.getcwd() + '/img/dic.jpg'), self.Tem[i * 9 + j])
                    self.tableWidget.setItem(j, i, lab1)
            else:
                y = lenT - 9*i
                for j in range(y):
                    # lab1 = QLabel()
                    # lab1.setPixmap(QPixmap(os.getcwd() + '/img/dic.jpg').scaled(18, 18))
                    # self.tableWidget.setCellWidget(j, i*2, lab1)
                    lab1 = QTableWidgetItem(QIcon(os.getcwd() + '/img/dic.jpg'), self.Tem[i * 9 + j])
                    self.tableWidget.setItem(j, i, lab1)

    def insertDOWN(self, XD):
        self.tableWidget_2.clear()
        self.XD = XD
        lenT = len(XD)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "股票名称 ["+str(lenT)+"]"))
        horizon = lenT // 5
        if lenT % 5 != 0:
            horizon += 1
        # print(lenT, horizon)
        self.tableWidget_2.setRowCount(horizon)
        for i in range(horizon):
                self.tableWidget_2.verticalHeader().resizeSection(i, 25)  # 调整第一列的大小为100像素

        for i in range(horizon):
            x = (lenT - 5 * i) // 5
            if x > 0:
                for j in range(5):
                    # lab1 = QTableWidgetItem(QIcon(os.getcwd() + '/img/dor.jpg'), XD[i * 5 + j][1])
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(XD[i * 5 + j][1]))
            else:
                y = lenT - 5 * i
                for j in range(y):
                    # lab1 = QTableWidgetItem(QIcon(os.getcwd() + '/img/dor.jpg'), XD[i * 5 + j][1])
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(XD[i * 5 + j][1]))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "新建模板"))
        self.pushButton.clicked.connect(lambda: self.Filemkdir(Form))

        self.pushButton_2.setText(_translate("Form", "删除模板"))
        self.pushButton_2.clicked.connect(lambda: self.Filedel(Form))

        self.pushButton_3.setText(_translate("Form", "模板改名"))
        self.pushButton_3.clicked.connect(lambda: self.rename(Form))

        self.pushButton_4.setText(_translate("Form", "添加品种"))
        self.pushButton_4.clicked.connect(lambda: self.inFile(Form))

        self.pushButton_5.setText(_translate("Form", "移出品种"))
        self.pushButton_5.clicked.connect(lambda: self.removeD(Form))

        self.pushButton_6.setText(_translate("Form", "清空品种"))
        self.pushButton_6.clicked.connect(lambda: self.removeA(Form))

        self.pushButton_7.setText(_translate("Form", "导入模板"))
        self.pushButton_7.clicked.connect(lambda: self.openMyDialog(Form))

        self.pushButton_8.setText(_translate("Form", "导出模板"))
        self.pushButton_8.clicked.connect(lambda: self.outFile(Form))

        self.label.setText(_translate("Form", "股票名称"))
        self.label_2.setText(_translate("Form", "自创建模板概念库"))

    def openMyDialog(self, Form):
        clickList_1 = self.tableWidget.selectedItems()
        if clickList_1:
            directory1 = QFileDialog.getOpenFileName()
            if directory1[0] and directory1[0][-4:] == 'xlsx':
                wb = load_workbook(directory1[0])
                ws = wb.active
                i = 1
                fields = []
                data = []
                for row in ws.rows:
                    list = []
                    for cell in row:
                        aa = str(cell.value)
                        if (aa == ""):
                            aa = "1"
                        list.append(aa)
                    if (i < 1):
                        pass
                    elif (i == 1):
                        fields = list
                    else:
                        data.append(list[:2])
                    i = i + 1
                path = os.getcwd() + '/Tem/' + clickList_1[-1].text() +".json"
                D = []
                with open(path, "r") as f:
                    if f.read():
                        f.seek(0)
                        D = json.loads(f.read())
                with open(path, "w") as f:
                    newD = data
                    for i in D:
                        if i not in newD:
                            newD += i
                    f.write(json.dumps(newD))
                    self.insertDOWN(newD)
        else:
            QMessageBox.warning(Form, "警告", "你需要选择一个模板进行导入！", QMessageBox.Yes)

    def Filemkdir(self, Form):
        text, okPressed = QInputDialog.getText(Form, "新建概念库", "请输入这个概念库的名称：", QLineEdit.Normal, "")
        try:
            if okPressed and text != '':
                if os.path.exists(os.getcwd() + "/Tem/" + text + ".json"):
                    QMessageBox.warning(Form, "警告", "要建立的目录已存在，先删除才能够创建！", QMessageBox.Yes)
                else:
                    with open(os.getcwd()+"/Tem/"+text+".json", "w+") as f:
                        f.write("")
                    self.Tem.append(text)
        except:
            QMessageBox.warning(Form, "警告", "请输入正确文件名称！", QMessageBox.Yes)

        self.insertUP()

    def Filedel(self, Form):
        items = self.tableWidget.selectedItems()
        if len(items) != 0:
            flag = QMessageBox.question(Form, "警告", "确认删除这些概念库吗？", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if flag == QMessageBox.Yes:
                try:
                    for i in items:
                        # print(i.text())
                        if os.path.exists(os.getcwd()+"/Tem/"+i.text()+".json"):
                            os.remove(os.getcwd()+"/Tem/"+i.text()+".json")
                            self.Tem.remove(i.text())
                except:
                    pass
            self.insertUP()
        else:
            QMessageBox.warning(Form, "提示", "你可以单击选中，也可以多个选中删除！",  QMessageBox.Yes | QMessageBox.No,QMessageBox.No)

    def rename(self, Form):
        items = self.tableWidget.selectedItems()
        if len(items) == 1:
            text, okPressed = QInputDialog.getText(Form, "概念库改名", "将这个概念库的名称更改为：", QLineEdit.Normal, "")
            if text and not os.path.exists(os.getcwd()+"/Tem/"+text+".json"):
                os.rename(os.getcwd()+"/Tem/"+items[0].text()+".json",
                          os.getcwd() + "/Tem/" + text + ".json")
                self.Tem.remove(items[0].text())
                self.Tem.append(text)
                self.insertUP()
            else:
                QMessageBox.warning(Form, "警告", "修改失败！文件不存在或内容不允许为空...", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        else:
            QMessageBox.warning(Form, "警告", "更改文件名不允许多选或者不选！",  QMessageBox.Yes | QMessageBox.No,QMessageBox.No)

    def tableSelect(self):
        clickList = self.tableWidget.selectedItems()
        if clickList:
            path = os.getcwd() + "/Tem/" + clickList[-1].text() + ".json"
            if os.path.exists(path):
                with open(path, "r") as f:
                    JsonG = f.read()
                try:
                    G = json.loads(JsonG)
                    # print(1)
                    self.insertDOWN(G)
                except:
                    self.insertDOWN([])

    def removeD(self, Form):
        clickList_1 = self.tableWidget.selectedItems()
        clickList_2 = self.tableWidget_2.selectedItems()
        if clickList_1 and clickList_2:
            path = os.getcwd() + "/Tem/" + clickList_1[-1].text() + ".json"
            if os.path.exists(path):
                flag = QMessageBox.warning(Form, "提示", "确定移除改股票么！",  QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
                if flag == QMessageBox.Yes:
                    XD = copy.copy(self.XD)
                    for i in XD:
                        for j in clickList_2:
                            if i[1] == j.text():
                                self.XD.remove(i)
                    with open(path, "w") as f:
                        f.write(json.dumps(self.XD))
                    self.insertDOWN(self.XD)
        else:
            QMessageBox.warning(Form, "警告", "操作错误,请选中需要操作的模块，然后选中需要操作的股票！", QMessageBox.Yes)

    def removeA(self, Form):
        clickList_1 = self.tableWidget.selectedItems()
        if clickList_1:
            path = os.getcwd() + "/Tem/" + clickList_1[-1].text() + ".json"
            flag = QMessageBox.warning(Form, "提示", "确定移除改股票么！",  QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            if flag == QMessageBox.Yes:
                with open(path, "w") as f:
                    f.write("")
                self.XD = []
                self.insertDOWN(self.XD)
        else:
            QMessageBox.warning(Form, "警告", "操作错误！", QMessageBox.Yes)

    def outFile(self, Form):
        clickList_1 = self.tableWidget.selectedItems()
        if clickList_1:
            path = os.getcwd() + "/Tem/" + clickList_1[-1].text() + ".json"
            directory1 = QFileDialog.getExistingDirectory(Form, "选取导出文件夹")
            import shutil
            shutil.copyfile(path, directory1 + "/" + clickList_1[-1].text() + ".json")
        else:
            QMessageBox.warning(Form, "警告", "操作错误，需选中导出模块！", QMessageBox.Yes)

    def inFile(self, Form):
        clickList_1 = self.tableWidget.selectedItems()
        if clickList_1:
            my = MyDialogN(Form)
            # 在主窗口中连接信号和槽
            my.mySignal.connect(self.getDialogSignalN)
            my.exec_()
        else:
            QMessageBox.warning(Form, "提示", "导入失败,请选择导入模块，可以新建之后再进行导入！", QMessageBox.Yes)

    def getDialogSignalN(self, TextPD):
        NumPD = [''.join(g) for _, g in groupby(TextPD, key=lambda x: x.isdigit()*'d' or x.isalpha()*'a' )]
        # print("处理数字和其他文字的分词",NumPD)
        Num = [i for i in NumPD if i.isdigit()]
        # print("得到所有数字的list",Num)
        # print(Num)
        if TextPD:
            clickList_1 = self.tableWidget.selectedItems()
            path = os.getcwd()
            if os.path.exists(path + "/Models/data.json"):
                with open(path + "/Models/data.json", "r") as f:
                    if f.read():
                        f.seek(0)
                        D = json.loads(f.read())
                    oldD= []
                    flag = 0
                    with open(path + "/Tem/" + clickList_1[-1].text() + ".json", "r") as f:
                        if f.read():
                            f.seek(0)
                            oldD = json.loads(f.read())
                        for j in D:
                            if (j[0] in Num or j[1] in TextPD) and j not in oldD:
                                if not flag:
                                    flag = 1
                                oldD.append(j)
                    if flag:
                        with open(path + "/Tem/" + clickList_1[-1].text() + ".json", "w") as f:
                            f.write(json.dumps(oldD))
                        self.insertDOWN(oldD)

class MyDialogN(QDialog):
    # 自定义信号
    mySignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyDialogN, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('请输入需要导入的字段：')
        self.setFixedSize(740, 600)

        self.Qtextedit = QtWidgets.QTextEdit(self)
        self.Qtextedit.setGeometry(QtCore.QRect(20, 10, 703, 500))

        button = QPushButton('确定', self)
        button.setGeometry(QtCore.QRect(600, 530, 120, 50))
        button.clicked.connect(self.sendEditContent)

    def sendEditContent(self):
        textALl = self.Qtextedit.toPlainText()
        # print(textALl)
        if textALl:
            self.mySignal.emit(textALl)  # 发射信号
        self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
