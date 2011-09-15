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
            self.filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file for add to canvas', '')
            new_img = mscene.addPixmap(QtGui.QPixmap(self.filename))
            if not (unicode(self.filename)==''):
                new_img.setFlags(QtGui.QGraphicsItem.ItemIsMovable)            
                objectslist.addItem(self.filename)
                new_img.rotate(90)            

def RotateImageLeft(self):
    self.rotate(-valueAngle.value())
def RotateImageRight(self):
    self.rotate(valueAngle.value())        

#begin load test data			
def load_test_data():
    six = mscene.addPixmap(QtGui.QPixmap("img/test1.png"))
    six.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test1.png")
	
    #six.setFlags(QtGui.QGraphicsItem.ItemIsFocusable)

    pix = mscene.addPixmap(QtGui.QPixmap("img/test2.jpg"))
    pix.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test2.jpg")
    print(pix)
	
#end load test data

def printItemText():
    #cur = objectslist.currentItem()
    #cur_item_in_mscene = mscene.
    #print(unicode(cur.text()))
    #print(objectslist.currentItem().text())     
    #print(scene_items_list[0])   
    #print(mscene.items())
    #print(dir(objectslist.currentItem().text()))
    #print('- - - - - ')
    currentColor = QColor(1, 0, 0)
    objectslist.currentItem().setTextColor(currentColor)	
    print(objectslist.currentItem().text())
    print(objectslist.currentItem())
    
   # print(dir(scene_items_list[0]))
    #print(scene_items_list[0].rotate(90))
    
	
app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.setWindowTitle('SpEd: Frame Editor')
widget.setWindowIcon(QtGui.QIcon('img/icon.png'))
widget.resize(800, 600)

dialog = QtGui.QFileDialog()
objectslist = QtGui.QListWidget()
objectslist.setDragDropMode(objectslist.InternalMove)
#objectslist.setFocus
mscene = QtGui.QGraphicsScene()

view = MyView(mscene)
load_test_data()

buttonLeftAll  = QtGui.QPushButton("Rotate Left All")
buttonRightAll = QtGui.QPushButton("Rotate Right All")
buttonAddFile = QtGui.QPushButton("Add file to canvas")
buttonDelFile = QtGui.QPushButton("Delete image from canvas")

valueAngle = QtGui.QSpinBox()
valueAngle.setValue(10)
valueAngle.setMaximum(359)
valueAngleLabel = QtGui.QLabel("Enter value of angle rotate:")

QtCore.QObject.connect(buttonLeftAll,QtCore.SIGNAL("clicked()"),view.allRotateLeft)
QtCore.QObject.connect(buttonRightAll,QtCore.SIGNAL("clicked()"),view.allRotateRight)
QtCore.QObject.connect(buttonAddFile,QtCore.SIGNAL("clicked()"),view.open_file_dialog)
QtCore.QObject.connect(objectslist,QtCore.SIGNAL("itemSelectionChanged()"),printItemText)

layout=QtGui.QVBoxLayout()
layout.addWidget(view)
layout.addWidget(buttonLeftAll)
layout.addWidget(buttonRightAll)
layout.addWidget(valueAngleLabel)
layout.addWidget(valueAngle)
layout.addWidget(buttonAddFile)
layout.addWidget(buttonDelFile)
layout.addWidget(objectslist)




widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())