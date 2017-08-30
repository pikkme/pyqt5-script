import sys
from shutil import copyfile
import os
#import vispy.mpl_plot as plt
import subprocess as sp
import vispy.app

vispy.app.use_app(backend_name="PyQt5", call_reuse=True)


#from PyQt5.QtWidgets import (QApplication,QFrame, QCheckBox,QGridLayout, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout, QWidget,
#QGridLayout,QFileDialog,QRadioButton,QMainWindow)
from PyQt5.QtWidgets import *

class Widget(QWidget):
 
    filenames_list = []
    
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.layoutUI()
        

    def layoutUI(self):
        self.setStyleSheet("background-color: white;")

        self.principalLayout = QHBoxLayout(self)

        self.leftFrame = QFrame(self)
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.leftFrame)

        self.principalLayout.addWidget(self.leftFrame)
    

        
        self.verticalLayoutR = QVBoxLayout()
        #self.verticalLayoutR.setSpacing(0)

        self.keyFrame = QFrame(self)
        #self.keyFrame.setStyleSheet("background-color: red;")
        self.keyFrame.setFrameShape(QFrame.StyledPanel)
        self.keyFrame.setFrameShadow(QFrame.Raised)
        
        self.keysverticalLayout = QVBoxLayout(self.keyFrame)
        
        self.AddBtn = QPushButton("Add", self.keyFrame)
        self.SelectBtn = QPushButton("Select", self.keyFrame)
        self.RunBtn = QPushButton("Run", self.keyFrame)
        self.StopBtn = QPushButton("Stop", self.keyFrame)

        ##################################################
        self.keysverticalLayout.addWidget(self.AddBtn)
        self.AddBtn.clicked.connect(self.AddItem)

        ##################################################
        self.keysverticalLayout.addWidget(self.SelectBtn)
        self.SelectBtn.clicked.connect(self.SelectItem)


        #################################################
        self.viewFrame = QFrame(self)
        self.viewFrame.setFrameShape(QFrame.StyledPanel)
        self.viewFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.viewFrame)
        
        #self.verticalLayout.addStretch(1)
        self.cb = QCheckBox(self.viewFrame)
        self.cb.stateChanged.connect(self.checkBox)
        ###################################################
        self.ViewBtn = QPushButton("View", self.viewFrame)
        self.ViewBtn.clicked.connect(self.ViewItem)

        
        self.gridLayout.addWidget(self.cb,0,0)
        self.gridLayout.addWidget(self.ViewBtn,0,1)
        
        #self.ViewBtn.move(0,50)
        
        
        self.keysverticalLayout.addWidget(self.viewFrame)
    
        #self.keysverticalLayout.addWidget(self.ViewBtn)
        #####################################################
        self.keysverticalLayout.addWidget(self.RunBtn)
        self.RunBtn.clicked.connect(self.RunItem)

        ###################################################
        self.keysverticalLayout.addWidget(self.StopBtn)
        self.StopBtn.clicked.connect(self.StopItem)

        
        
        self.verticalLayoutR.addWidget(self.keyFrame)
        self.principalLayout.addLayout(self.verticalLayoutR)

        


        self.rightFrame = QFrame(self)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutRight = QVBoxLayout(self.rightFrame)

        self.principalLayout.addWidget(self.rightFrame)
    
        
    
    def AddItem(self):
        file_name_list = []
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')
        
        file_selected = str(fname[0])
        #print(file_selected)
        file_name_list = file_selected.split('/')
        
        final_file_name = file_name_list[-1]
        Widget.filenames_list.append(final_file_name)
        
        path = str(fname[0])
 
        dst = "/home/raw-at/Desktop/pyqt5/models/"+final_file_name

        
        #print(final_file_name)

        copyfile(path, dst)

            
    def SelectItem(self):
        
        
        for i in range(len(Widget.filenames_list)):
            print(i)
            name = "obj"+str(i)
    
            self.name = QRadioButton(self.filenames_list[i],self.rightFrame) 
            self.verticalLayoutRight.addWidget(self.name)
    
    

        
    def ViewItem(self):
        sp.Popen("python3 run.py debug 1.obj",shell=True)

    def RunItem(self):
        canvas = vispy.app.Canvas()
        w = QMainWindow()
        widget = QWidget()
        w.setCentralWidget(widget)
        widget.setLayout(QVBoxLayout())
        widget.layout().addWidget(canvas.native)
        widget.layout().addWidget(QPushButton())
        w.show()
        vispy.app.run()   

    def StopItem(self):
        print('Stop button')

    def checkBox(self):
        print("Check Box")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())




