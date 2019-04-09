# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys, os
import json,copy
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem,QInputDialog,\
    QLineEdit,QCompleter,QDialog,QPushButton
from PyQt5.QtCore import pyqtSignal,Qt

import translate

path = os.getcwd()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1226, 795)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(470, 10, 331, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(820, 10, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(900, 60, 51, 31))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(970, 60, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1050, 60, 71, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1140, 60, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1020, 740, 91, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(1130, 740, 91, 51))
        self.pushButton_6.setObjectName("pushButton_6")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 1201, 631))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        self.searchList = []

        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setWindowTitle("股票池-炒股小神器V1")

        self.D = []
        if os.path.exists(os.getcwd() + "/Models/data.json"):
            with open(path + "/Models/data.json", "r") as f:
                JsonD = f.read()
            self.D = json.loads(JsonD)
            self.showAllorSearch(self.D)
        self.Form = Form
        self.initsou()

    def generateMenu(self, pos):
        # 计算有多少条数据，默认-1,
        row_num = -1
        column_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
            column_num = i.column()

        if row_num >= 1 and column_num >= 4:
            # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
            menu = QtWidgets.QMenu()
            item1 = menu.addAction(u'修改值')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            # 显示选中行的数据文本
            if action == item1:
                # row_num 行的距离
                # column_num 列的距离
                text_name, okPressed = QInputDialog.getText(self.Form, "请输入备注的值", "请输入备注的值", QLineEdit.Normal,"")
                if okPressed:
                    if text_name:
                        id = self.tableWidget.item(row_num, 1).text()
                        text = self.tableWidget.item(0, column_num).text()
                        self.write_to_beizhu(id, text, text_name)
                    else:
                        QMessageBox.warning(self.Form, "提示", "数据输入为空，导入失败！", QMessageBox.Yes | QMessageBox.No)
                    # print(row_num, column_num)
                # print(self.tableWidget.item(1, 4).text())

    def write_to_beizhu(self, id, text, textname):
        # print(id, text, textname)
        path = os.getcwd() + "/Models/remark.json"
        D = {}
        if os.path.exists(path):
            with open(path, "r") as f:
                D = json.loads(f.read())

        if id not in D:
            D[id] = {}
        D[id][text] = textname

        with open(path, "w") as f:
            f.write(json.dumps(D))

        self.showAllorSearch(self.searchList)

    def get_to_beizhu(self):
        path = os.getcwd() + "/Models/remark.json"
        D = {}
        if os.path.exists(path):
            with open(path, "r") as f:
                D = json.loads(f.read())
        return D

    def initS(self):
        SeD = []
        if os.path.exists(os.getcwd() + "/Models/settings.json"):
            with open(os.getcwd() + "/Models/settings.json", "r") as f:
                if f.read():
                    f.seek(0)
                    SeD = json.loads(f.read())

        SD = {}
        Tem = []
        if os.path.exists(os.getcwd() + "/Tem"):
            for parent, dirnames, filenames in os.walk(os.getcwd() + "/Tem", followlinks=True):
                for filename in filenames:
                    Tem.append(filename[:-5])
        for i in Tem:
            path = os.getcwd() + "/Tem/" + i + '.json'
            with open(path, "r") as f:
                if f.read():
                    f.seek(0)
                    RD = json.loads(f.read())
                    for j in RD:
                        if j[0] not in SD:
                            SD[j[0]] = [i]
                        else:
                            SD[j[0]].append(i)

        return SeD,SD


    def initsou(self):
        StrD = []
        for i in self.D:
            StrD.append(i[0])
            StrD.append(i[1])

        Qcom = QCompleter(StrD)
        self.lineEdit.setCompleter(Qcom)

    def showAllorSearch(self, D):
        SeD, SD = self.initS()
        BD = self.get_to_beizhu()
        self.tableWidget.setColumnCount(len(SeD)+4)  # 控制表格有几列
        self.tableWidget.horizontalHeader().resizeSection(2, 100)  # 调整第一列的大小为100像素
        self.tableWidget.horizontalHeader().resizeSection(3, 300)  # 调整第一列的大小为100像素
        self.tableWidget.clear()
        self.searchList = copy.copy(D)
        lenD = len(D) + 1

        self.tableWidget.setRowCount(lenD)  # 控制表格有几行

        self.tableWidget.setItem(0, 0, QTableWidgetItem("选择框"))  # 设置j行i列的内容为Value
        self.tableWidget.setItem(0, 1, QTableWidgetItem("代码"))  # 设置j行i列的内容为Value
        self.tableWidget.setItem(0, 2, QTableWidgetItem("名称"))  # 设置j行i列的内容为Value
        self.tableWidget.setItem(0, 3, QTableWidgetItem("相关模块"))  # 设置j行i列的内容为Value
        for i in SeD:
            self.tableWidget.setItem(0, SeD.index(i)+4, QTableWidgetItem(i))

        ii = 1
        self.checkBoxS = []
        for i in D:
            check = QtWidgets.QTableWidgetItem()
            check.setCheckState(QtCore.Qt.Unchecked)  # 把checkBox设为未选中状态
            self.checkBoxS.append(check)
            self.tableWidget.setItem(ii, 0, check)  # 在(x,y)添加checkBox
            for j in range(2):
                self.tableWidget.setItem(ii, j+1, QTableWidgetItem(i[j]))  # 设置j行i列的内容为Value
            if i[0] in SD:
                strSD = str(SD[i[0]]).replace("[", "").replace("]", "").replace("'", "")
                self.tableWidget.setItem(ii, 3, QTableWidgetItem(strSD))
            for j in range(len(SeD)):
                if i[0] in BD:
                    if SeD[j] in BD[i[0]]:
                        self.tableWidget.setItem(ii, 4+j, QTableWidgetItem(BD[i[0]][SeD[j]]))
            ii+=1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.pushButton.clicked.connect(lambda: self.search(Form))

        self.checkBox.setText(_translate("Form", "全选"))
        self.checkBox.stateChanged.connect(self.checkAll)
        self.checkBox.setEnabled(False)

        self.pushButton_2.setText(_translate("Form", "删除"))
        self.pushButton_2.clicked.connect(self.deleteD)
        self.pushButton_2.setEnabled(False)

        self.pushButton_3.setText(_translate("Form", "增加"))
        self.pushButton_3.clicked.connect(lambda: self.increase(Form))
        self.pushButton_3.setEnabled(False)

        self.pushButton_4.setText(_translate("Form", "修改"))
        self.pushButton_4.clicked.connect(lambda: self.modify())

        self.pushButton_5.setText(_translate("Form", "导入"))
        self.pushButton_5.clicked.connect(lambda: self.TranslateIN())

        self.pushButton_6.setText(_translate("Form", "导出"))
        self.pushButton_6.clicked.connect(lambda: self.TranslateOUT(Form))

    def increase(self, Form):
        # self.getText(Form, "代码")
        my = MyDialogN(Form)
        # 在主窗口中连接信号和槽
        my.mySignal.connect(self.getDialogSignalN)
        my.exec_()

    def getDialogSignalN(self, JsonD):
        D = json.loads(JsonD)
        if D['id'] == 1:
            path = os.getcwd() + "/Models/settings.json"
            SD = []
            if os.path.exists(path):
                with open(path, "r") as f:
                    SD = json.loads(f.read())
            if D['content'] not in SD:
                SD.append(D['content'])

            with open(path, "w") as f:
                f.write(json.dumps(SD))
            self.showAllorSearch(self.D)
        else:
            self.D.append([D['content1'], D['content2']])
            self.searchList.append([D['content1'], D['content2']])
            self.showAllorSearch(self.D)

    def deleteD(self):
        # print(self.checkBoxS[0].checkState())
        deleteNum = 0
        # print(len(self.searchList))
        if hasattr(self, "checkBoxS"):
            for i in self.checkBoxS:
                    if i.checkState():
                        infoDex = self.checkBoxS.index(i) - deleteNum
                        # print(infoDex)
                        try:
                            self.D.remove(self.searchList[infoDex])
                            del self.searchList[infoDex]
                            deleteNum += 1
                        except:
                            # pass
                            print(infoDex, self.checkBoxS.index(i), deleteNum, len(self.searchList))
        else:
            self.D = []
        # print(self.searchList, self.D)
        with open(os.getcwd() + "/Models/data.json", "w") as f:
            f.write(json.dumps(self.D))
        self.showAllorSearch(self.D)

        self.initsou()

    def search(self, Form):
        text = self.lineEdit.text()
        # print(text)
        if text:
            searchList = []
            for i in self.D:
                if i[0] in text or i[1] in text:
                    searchList.append(i)
            # print(searchList)
            self.showSpecialSearch(searchList)
        else:
            QMessageBox.warning(Form, "消息提示框", "未输入搜索数据状态下默认返回目前的所有股票！", QMessageBox.Yes | QMessageBox.No)
            self.showAllorSearch(self.D)

    def showSpecialSearch(self, XD):
        self.checkBoxS = []
        self.searchList = []
        SeD, SD = self.initS()

        LSD = []
        for i in XD:
            if i[0] in SD:
                for j in SD[i[0]]:
                    if j not in LSD:
                        LSD.append(j)
        LD = {}
        for i in LSD:
            for j in XD:
                if j[0] in SD and i in SD[j[0]]:
                    if i not in LD:
                        LD[i] = [j[1]]
                    else:
                        LD[i].append(j[1])

        self.tableWidget.clear()
        lenD = len(LSD)+1
        self.tableWidget.setRowCount(lenD)  # 控制表格有几行
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("模板"))  # 设置j行i列的内容为Value
        self.tableWidget.setItem(0, 1, QTableWidgetItem("数量"))  # 设置j行i列的内容为Value
        self.tableWidget.setItem(0, 2, QTableWidgetItem("股票"))  # 设置j行i列的内容为Value

        self.tableWidget.horizontalHeader().resizeSection(2, 300)  # 调整第一列的大小为100像素

        ii = 1
        # print(SeD) # 这个是备注
        # print(SD['601398']) # 这个是对应模板
        # print(LD)
        # print(LSD)
        LD = sorted(LD.items(), key=lambda d:len(d[1]), reverse=True)

        for i in LD:
            self.tableWidget.setItem(ii, 0, QTableWidgetItem(i[0]))
            self.tableWidget.setItem(ii, 1, QTableWidgetItem(str(len(i[1]))))
            strD = str(i[1]).replace("[", "").replace("]", "").replace("'","")
            self.tableWidget.setItem(ii, 2, QTableWidgetItem(strD))
            ii+=1


    def checkAll(self):
        if self.checkBox.isChecked():
            if hasattr(self, "checkBoxS"):
                for i in self.checkBoxS:
                    i.setCheckState(QtCore.Qt.Checked)
        else:
            if hasattr(self, "checkBoxS"):
                for i in self.checkBoxS:
                    i.setCheckState(QtCore.Qt.Unchecked)

    def modify(self):
        # print(self.pushButton_4.text())
        if self.pushButton_4.text() == "修改":
            self.pushButton_4.setText("完成")
            self.pushButton_3.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.checkBox.setEnabled(True)
        else:
            self.pushButton_4.setText("修改")
            self.pushButton_3.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.checkBox.setEnabled(False)

    def TranslateIN(self):
        directory1 = QFileDialog.getOpenFileName()
        if directory1[0] and directory1[0][-4:] == 'xlsx':
            translate.input(directory1[0])
        if os.path.exists(os.getcwd() + "/Models/settings.json"):
            os.remove(os.getcwd() + "/Models/settings.json")
        if os.path.exists(os.getcwd() + "/Models/remark.json"):
            os.remove(os.getcwd() + "/Models/remark.json")
        if os.path.exists(os.getcwd()+"/Models/data.json"):
            with open(path+"/Models/data.json", "r") as f:
                JsonD = f.read()
            # print(222222)
            D = json.loads(JsonD)
            # print(len(D))
            self.D = D
            self.showAllorSearch(self.D)

            self.initsou()


    def TranslateOUT(self, Form):
        if self.searchList:
            try:
                directory1 = QFileDialog.getExistingDirectory(Form, "选取导出文件夹")
                translate.output(directory1, self.D)
            except:
                QMessageBox.warning(Form, "消息提示框", "导出出错，请关闭当前目录下打开的exl文件！", QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.warning(Form, "消息提示框", "本地没有数据可以导出！", QMessageBox.Yes | QMessageBox.No)

class MyDialogN(QDialog):
    # 自定义信号
    mySignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyDialogN, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('请输入需要导入的字段：')
        self.setFixedSize(400, 180)

        self.cb1 = QtWidgets.QCheckBox('选择新增列', self)
        self.cb1.move(10, 10)
        self.cb1.stateChanged.connect(self.changecb1)

        self.Qlinedit = QtWidgets.QLineEdit(self)
        self.Qlinedit.setGeometry(QtCore.QRect(150, 30, 180, 30))
        self.Qlinedit.setEnabled(False)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 30, 120, 30))
        self.label.setText("请输入新增列的名称：")

        self.cb2 = QtWidgets.QCheckBox('选择新增行', self)
        self.cb2.move(10, 70)
        self.cb2.stateChanged.connect(self.changecb2)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(10, 100, 60, 30))
        self.label2.setText("股票代码：")

        self.Qlinedit2 = QtWidgets.QLineEdit(self)
        self.Qlinedit2.setGeometry(QtCore.QRect(80, 100, 100, 30))
        self.Qlinedit2.setEnabled(False)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(220, 100, 60, 30))
        self.label3.setText("股票名称：")

        self.Qlinedit3 = QtWidgets.QLineEdit(self)
        self.Qlinedit3.setGeometry(QtCore.QRect(280, 100, 100, 30))
        self.Qlinedit3.setEnabled(False)

        button = QPushButton('确定', self)
        button.setGeometry(QtCore.QRect(150, 140, 100, 40))
        button.clicked.connect(self.sendEditContent)

    def sendEditContent(self):
        if self.cb1.checkState() == Qt.Checked:
            line1 = self.Qlinedit.text()
            if line1:
                D = []
                path = os.getcwd() + "/Models/settings.json"
                if os.path.exists(path):
                    with open(path, "r") as f:
                        if f.read():
                            f.seek(0)
                            D = json.loads(f.read())
                if line1 not in D:
                    self.mySignal.emit(json.dumps({'id': 1, 'content':line1}))  # 发射信号
                    self.hide()
                else:
                    QMessageBox.warning(self, "警告", "其他项命名重复！", QMessageBox.Yes | QMessageBox.No)
            else:
                QMessageBox.warning(self, "警告", "命名不能为空！", QMessageBox.Yes | QMessageBox.No)
        elif self.cb2.checkState() == Qt.Checked:
            line2 = self.Qlinedit2.text()
            line3 = self.Qlinedit3.text()
            if line2 and  line3:
                self.mySignal.emit(json.dumps({'id': 2, 'content1':line2, 'content2':line2}))  # 发射信号
                self.hide()
            else:
                QMessageBox.warning(self, "警告", "命名不能为空！", QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.warning(self, "消息提示框", "导入失败！", QMessageBox.Yes | QMessageBox.No)

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.Qlinedit.setEnabled(True)
            self.Qlinedit2.setEnabled(False)
            self.Qlinedit3.setEnabled(False)
            self.cb2.setChecked(False)

    def changecb2(self):
        if self.cb2.checkState() == Qt.Checked:
            self.Qlinedit.setEnabled(False)
            self.Qlinedit2.setEnabled(True)
            self.Qlinedit3.setEnabled(True)
            self.cb1.setChecked(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())