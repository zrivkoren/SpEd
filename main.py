﻿# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
     
class MyView(QtGui.QGraphicsView):
    def __init__(self,*args):
        QtGui.QGraphicsView.__init__(self,*args)
    def allRotateLeft (self):
        self.rotate(-valueAngle.value())
    def allRotateRight(self):
        self.rotate(valueAngle.value())

    def open_file_dialog(self):
            self.filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file for add to canvas', '')
            new_img = scene.addPixmap(QtGui.QPixmap(self.filename))
            new_img.setFlags(QtGui.QGraphicsItem.ItemIsMovable)            
            objectslist.addItem(self.filename)
            new_img.rotate(90)
    #def RotateLeft(self):
        

#begin load test data			
def load_test_data():
    six = scene.addPixmap(QtGui.QPixmap("img/test1.png"))
    six.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test1.png")

    pix = scene.addPixmap(QtGui.QPixmap("img/test2.jpg"))
    pix.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test2.jpg")    
#end load test data
def printItemText():
    cur = objectslist.currentItem()
    #cur_item_in_scene = scene.
    print(cur.text())
    #print(objectslist.currentItem().text())    
    #print(MyView.)	
	
app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.setWindowTitle('SpEd: Frame Editor')
widget.setWindowIcon(QtGui.QIcon('img/icon.png'))
widget.resize(800, 600)

dialog = QtGui.QFileDialog()
objectslist = QtGui.QListWidget()
scene = QtGui.QGraphicsScene()

view = MyView(scene)

load_test_data()

buttonLeft  = QtGui.QPushButton("Rotate Left All")
buttonRight = QtGui.QPushButton("Rotate Right All")
buttonAddFile = QtGui.QPushButton("Add file to canvas")
buttonDelFile = QtGui.QPushButton("Delete image from canvas")

valueAngle = QtGui.QSpinBox()
valueAngle.setValue(10)
valueAngle.setMaximum(359)
valueAngleLabel = QtGui.QLabel("Enter value of angle rotate:")

QtCore.QObject.connect(buttonLeft,QtCore.SIGNAL("clicked()"),view.allRotateLeft)
QtCore.QObject.connect(buttonRight,QtCore.SIGNAL("clicked()"),view.allRotateRight)
QtCore.QObject.connect(buttonAddFile,QtCore.SIGNAL("clicked()"),view.open_file_dialog)
QtCore.QObject.connect(objectslist,QtCore.SIGNAL("itemSelectionChanged()"),printItemText)

layout=QtGui.QVBoxLayout()
layout.addWidget(view)
layout.addWidget(buttonLeft)
layout.addWidget(buttonRight)
layout.addWidget(valueAngleLabel)
layout.addWidget(valueAngle)
layout.addWidget(buttonAddFile)
layout.addWidget(buttonDelFile)
layout.addWidget(objectslist)


widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())