# -*- coding: utf-8 -*-

#Optomization file
import scipy as sp
from scipy import signal

import PyQt5
import PyQt5.QtWidgets
import sys


def sys_vals(Mp,ts):
    """Returns the damping ratio(zeta) and natural
    fequency(wn) of the desired 2nd order response
    given the user's desired overshoot(Mp) and 
    2% settling time(ts) values."""
    zeta = (-sp.log(Mp/100))/sp.sqrt((sp.pi)**2+(sp.log(Mp/100))**2)
    wn = 4/(zeta*ts)
    return zeta,wn

def place_poles(zeta, wn):
    """Returns the required system poles to achieve
    the desired 2nd order response."""
    s = sp.array([-zeta*wn+1j*wn*sp.sqrt(1-zeta**2),
         -zeta*wn-1j*wn*sp.sqrt(1-zeta**2)])
    return s

def for_the_gui(Mp,ts):
    """Calculates the system gains to place the poles at 
    the desired locations. This is the only function
    that the GUI will need to call and give to the user.
    The matrices are assumed to be for a motor with a 
    transfer function of a/(s(s+b))."""
    a = 1
    b = 2
    
    """The matrices are for state-space form Ax + Bu = x_dot, where A is the"
       state coefficient matrix, and B is the input coefficient matrix. a and b are                       
       arbitrary values for the motor dynamics"""
    A = sp.array([[0, 1],
                    [0, -b]])            
    B = sp.array([[0],             
                   [a]])             
    
    zeta,wn = sys_vals(Mp,ts)
    poles = place_poles(zeta,wn)
    
    """The scipy function that creates
    controller gains for the system"""
    k = signal.place_poles(A,B,poles).gain_matrix
    return k                            

class MainWindow(PyQt5.QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        # Define menus
        #   defintes file menu
        self.menuFile = self.menuBar().addMenu("&Help")
        self.actionHelp = PyQt5.QtWidgets.QAction("&YouCanHelp", self)
        self.actionHelp.triggered.connect(self.Help)
        self.menuFile.addActions([self.actionHelp])
        
        # Define and set main widgets
        widget = PyQt5.QtWidgets.QWidget()
        self.overShoot = PyQt5.QtWidgets.QLineEdit("% Overshoot")
        self.settlingTime = PyQt5.QtWidgets.QLineEdit("Settling Time")
        self.output = PyQt5.QtWidgets.QLineEdit("Output")
        self.optbutton = PyQt5.QtWidgets.QPushButton("Find K",self)
        self.optbutton.clicked.connect(self.buttonEvent)

        widget.setFixedSize(400,225)
        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.overShoot)
        layout.addWidget(self.settlingTime)
        layout.addWidget(self.optbutton)
        layout.addWidget(self.output)
        widget.setLayout(layout)  
        self.setCentralWidget(widget)
    
    #message displayed by Help    
    def Help(self):
        self.output.setText("You can help by giving us 100%")
        
    #When button is pushed call for_the_gui() to get kVals and return to self.output
    def buttonEvent(self):
        #ensures that the inputs are floats or ints
        try:
            os=float(self.overShoot.text())
            ts=float(self.settlingTime.text())
            kVals = for_the_gui(os,ts)
            self.output.setText(str(kVals))
        except (ValueError):
            self.output.setText("Overshoot and Settling Time must be floats or ints")


if __name__ == '__main__':
    #runs the gui
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec_()

