# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtGui import QColor
     
class MyView(QtGui.QGraphicsView):
    def __init__(self,*args):
        QtGui.QGraphicsView.__init__(self,*args)
    def allRotateLeft (self):
        self.rotate(-valueAngle.value())
    def allRotateRight(self):
        self.rotate(valueAngle.value())

    def open_file_dialog(self):
            self.fileName = QtGui.QFileDialog.getOpenFileName(None, 'Open file for add to canvas', '')
            new_img = mscene.addPixmap(QtGui.QPixmap(self.fileName))
            if not (unicode(self.fileName)==''):
                new_img.setFlags(QtGui.QGraphicsItem.ItemIsMovable)            
                objectslist.addItem(self.fileName)         

    def RotateImageLeft(self):
        if not objectslist.currentRow() == -1:
            mscene.items()[objectslist.currentRow()].rotate(-valueAngle.value())
        else: print("Select item in objects list")
    def RotateImageRight(self):
        if not objectslist.currentRow() == -1:
            mscene.items()[objectslist.currentRow()].rotate(valueAngle.value())
        else: print("Select item in objects list")            

    def saveImage(self):    
        img = QtGui.QImage(1024,768,QtGui.QImage.Format_RGB32)
        img.fill(QtGui.QColor(255,255,255).rgb())
        painter = QtGui.QPainter(img)    
        painter.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing|QtGui.QPainter.SmoothPixmapTransform)   
        view.render(painter)
        painter.end()
        img.save("scene1.png")
		
#begin load test data			
def load_test_data():
    six = mscene.addPixmap(QtGui.QPixmap("img/test1.png"))
    six.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test1.png")
	
    pix = mscene.addPixmap(QtGui.QPixmap("img/test2.jpg"))
    pix.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test2.jpg")
#end load test data

def printItemText():    
    print(objectslist.currentItem().text())
	
app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.setWindowTitle('SpEd: Frame Editor')
widget.setWindowIcon(QtGui.QIcon('img/icon.png'))
widget.resize(800, 600)

dialog = QtGui.QFileDialog()
objectslist = QtGui.QListWidget()
#objectslist.setDragDropMode(objectslist.InternalMove)
mscene = QtGui.QGraphicsScene()

view = MyView(mscene)
load_test_data()

buttonLeftAll  = QtGui.QPushButton("Rotate Left All")
buttonRightAll = QtGui.QPushButton("Rotate Right All")
buttonAddFile = QtGui.QPushButton("Add file to canvas")
buttonDelFile = QtGui.QPushButton("Delete image from canvas")
buttonRotateLeftOne = QtGui.QPushButton("Rotate left one image")
buttonRotateRightOne = QtGui.QPushButton("Rotate left one image")
buttonSave = QtGui.QPushButton("Save canvas")

valueAngle = QtGui.QSpinBox()
valueAngle.setValue(10)
valueAngle.setMaximum(359)
valueAngleLabel = QtGui.QLabel("Enter value of angle rotate:")

QtCore.QObject.connect(buttonLeftAll,QtCore.SIGNAL("clicked()"),view.allRotateLeft)
QtCore.QObject.connect(buttonRightAll,QtCore.SIGNAL("clicked()"),view.allRotateRight)
QtCore.QObject.connect(buttonAddFile,QtCore.SIGNAL("clicked()"),view.open_file_dialog)
QtCore.QObject.connect(objectslist,QtCore.SIGNAL("itemSelectionChanged()"),printItemText)
QtCore.QObject.connect(buttonRotateLeftOne,QtCore.SIGNAL("clicked()"),view.RotateImageLeft)
QtCore.QObject.connect(buttonRotateRightOne,QtCore.SIGNAL("clicked()"),view.RotateImageRight)
QtCore.QObject.connect(buttonSave,QtCore.SIGNAL("clicked()"),view.saveImage)

layout=QtGui.QVBoxLayout()
layout.addWidget(view)
layout.addWidget(buttonLeftAll)
layout.addWidget(buttonRightAll)
layout.addWidget(valueAngleLabel)
layout.addWidget(valueAngle)
layout.addWidget(buttonAddFile)
layout.addWidget(buttonDelFile)
layout.addWidget(objectslist)
layout.addWidget(buttonRotateLeftOne)
layout.addWidget(buttonRotateRightOne)
layout.addWidget(buttonSave)

widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())