# author: swM
# version: 炒股小神器V1
# time: 2019/03/26
from PyQt5 import QtWidgets
import sys,os

sys.path.append(os.getcwd())

from StockPool import Ui_Form as Ui_pool

from StockChoose import Ui_form as Ui_choose

from StockTem import Ui_Form as Ui_tem

class Ui_Pool(QtWidgets.QWidget,Ui_pool): # 股票池弹出
    def __init__(self):
        super(Ui_Pool, self).__init__()
        self.setupUi(self)

class Ui_Tem(QtWidgets.QWidget,Ui_tem): # 自创建概念库弹出
    def __init__(self):
        super(Ui_Tem, self).__init__()
        self.setupUi(self)

class Choose(QtWidgets.QMainWindow,Ui_choose): # 选择器弹出
    def __init__(self):
        super(Choose, self).__init__()
        self.setupUi(self)

    def jumpPool(self):
        # self.hide()  # 可以隐藏本地款
        self.dia1 = Ui_Pool()
        self.dia1.show()

    def jumpTem(self):
        self.dia2 = Ui_Tem()
        self.dia2.show()

    def closeEvent(self, QCloseEvent):
        flag = QtWidgets.QMessageBox .warning(self, "消息提示框", "确定要关闭当前窗口吗？", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.No)
        if flag == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



        #运行窗口Login
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    login_show=Choose()
    login_show.show()
    sys.exit(app.exec_())
