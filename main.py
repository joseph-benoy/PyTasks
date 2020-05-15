from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from ui import *
import pickle

class GUIForm(Ui_MainWindow):
	def __init__(self,window):
		file = open('pytask.dat','rb')
		tasks = Tasks()
		tasks = pickle.load(file)
		self.setupUi(window)
		for i in tasks.unfinished:
			self.UnfinishedList.addItem(i)
		for i in tasks.finished:
			self.FinishedList.addItem(i)
		self.Addtask.clicked.connect(self.addTask)
		self.clearBtn.clicked.connect(self.clearTasks)
	def addTask(self):
		task = self.TaskInput.text()
		self.UnfinishedList.addItem(task)
		self.TaskInput.setText('')
	def clearTasks(self):
		self.FinishedList.clear()

class Tasks:
	def __init__(self,unfinished=None,finished=None):
		self.unfinished=unfinished
		self.finished=finished

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
	def closeEvent(self,event):
		unfinished = [ui.UnfinishedList.item(i).text() for i in range(ui.UnfinishedList.count())]
		finished = [ui.FinishedList.item(i).text() for i in range(ui.FinishedList.count())]
		tasks = Tasks(unfinished,finished)
		file = open('pytask.dat','wb')
		pickle.dump(tasks,file)
		file.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = GUIForm(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

