## -*- coding: utf-8 -*-
#
##Optomization file
#import scipy as sp
#from scipy.optomize import optomize
#
#print(dabo)
#
#

import PyQt5
import PyQt5.QtWidgets
import sys

class MainWindow(PyQt5.QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        # Define menus (e.g., File and Help)
        #   defintes file menu
        self.menuFile = self.menuBar().addMenu("&Help")
        self.actionHelp = PyQt5.QtWidgets.QAction("&EasterEgg", self)
        self.actionHelp.triggered.connect(self.Help)
        self.menuFile.addActions([self.actionHelp])
        
        # Define and set main widgets
        widget = PyQt5.QtWidgets.QWidget()
        self.value = PyQt5.QtWidgets.QLineEdit("Enter Number")
        items=["% Overshoot","Settling Time"]
        self.drop = PyQt5.QtWidgets.QComboBox()
        self.drop.addItems(items)
        self.output = PyQt5.QtWidgets.QLineEdit("Output")
        self.optbutton = PyQt5.QtWidgets.QPushButton("Optimize",self)
        self.optbutton.clicked.connect(self.optEvent)

        widget.setFixedSize(400,225)
        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.value)
        layout.addWidget(self.drop)  
        layout.addWidget(self.output)
        layout.addWidget(self.optbutton)
        widget.setLayout(layout)  
        self.setCentralWidget(widget)
        
    def Help(self):
        self.output.setText("Michelle Le says Gabe sucks")
        
    def optEvent(self):
        self.output.setText(str("It works"))
        item = str(self.drop.itemText(self.drop.currentIndex()))
        if item=="% Overshoot":
            #Ts = OS(float(self.value.text()))
            Ts = "Ts optimized" #to be removed once OS is callable
            self.output.setText(str(Ts))
        else:
            #Os = TS(float(self.value.text()))
            Os = "Os optimized" # to be removed once TS is callable
            self.output.setText(str(Os))
        
app = PyQt5.QtWidgets.QApplication(sys.argv)
widget = MainWindow()
widget.show()
app.exec_()