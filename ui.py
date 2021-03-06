from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 530)
        MainWindow.setMinimumSize(QtCore.QSize(800, 530))
        MainWindow.setMaximumSize(QtCore.QSize(800, 530))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons8-task-planning-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UnfinishedList = QtWidgets.QListWidget(self.centralwidget)
        self.UnfinishedList.setGeometry(QtCore.QRect(20, 50, 461, 381))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.UnfinishedList.setFont(font)
        self.UnfinishedList.setDragEnabled(True)
        self.UnfinishedList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.UnfinishedList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.UnfinishedList.setObjectName("UnfinishedList")
        self.UnLabel = QtWidgets.QLabel(self.centralwidget)
        self.UnLabel.setGeometry(QtCore.QRect(20, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.UnLabel.setFont(font)
        self.UnLabel.setObjectName("UnLabel")
        self.FinishedList = QtWidgets.QListWidget(self.centralwidget)
        self.FinishedList.setGeometry(QtCore.QRect(500, 50, 291, 331))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.FinishedList.setFont(font)
        self.FinishedList.setDragEnabled(True)
        self.FinishedList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.FinishedList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.FinishedList.setObjectName("FinishedList")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(500, 390, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clearBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons8-erase-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearBtn.setIcon(icon1)
        self.clearBtn.setObjectName("clearBtn")
        self.FLabel = QtWidgets.QLabel(self.centralwidget)
        self.FLabel.setGeometry(QtCore.QRect(500, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FLabel.setFont(font)
        self.FLabel.setObjectName("FLabel")
        self.TaskInput = QtWidgets.QLineEdit(self.centralwidget)
        self.TaskInput.setGeometry(QtCore.QRect(20, 460, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TaskInput.setFont(font)
        self.TaskInput.setObjectName("TaskInput")
        self.Addtask = QtWidgets.QPushButton(self.centralwidget)
        self.Addtask.setGeometry(QtCore.QRect(630, 460, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Addtask.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons8-plus-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Addtask.setIcon(icon2)
        self.Addtask.setObjectName("Addtask")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyTasks"))
        self.UnLabel.setText(_translate("MainWindow", "Unfinished tasks"))
        self.clearBtn.setText(_translate("MainWindow", "Clear Finished"))
        self.FLabel.setText(_translate("MainWindow", "Finished tasks"))
        self.TaskInput.setPlaceholderText(_translate("MainWindow", "Enter a new task "))
        self.Addtask.setText(_translate("MainWindow", "Add Task"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
