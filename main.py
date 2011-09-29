# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
import copy
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
                tempItemList = objectslist.item(objectslist.count()-1).clone()
                objectslist.insertItem(0, tempItemList)          
                objectslist.takeItem(objectslist.count()-1)
                
                mainList.append([objectslist.count()-1, 0, mainList[len(mainList)-1][2]+1, 0])
                for i in range(objectslist.count()-1):
                    for j in range(4):
                        if j == 1:
                            mainList[i][j] = mainList[i][j] +1
                        if j == 3:
                            mainList[i][j] = mainList[i][j] +1
				
                for i in range(len(mainList)):
                    for k in range(len(mainList)):
                        if i == mainList[k][0]:                              				
                            mscene.items()[mainList[k][0]].setZValue(mainList[k][2]) #accordance current row in objectsList and record in mainList

    def RotateImageLeft(self):
        if not objectslist.currentRow() == -1:
            for i in range(len(mainList)):
                if objectslist.currentRow() == mainList[i][3]:                        
                    mscene.items()[mainList[i][0]].rotate(-valueAngle.value())
        else: print("Select item in objects list")
    def RotateImageRight(self):
        if not objectslist.currentRow() == -1:
            for i in range(len(mainList)):
                if objectslist.currentRow() == mainList[i][3]:                        
                    mscene.items()[mainList[i][0]].rotate(valueAngle.value())            
        else: print("Select item in objects list")            

    def saveImage(self):
        img = QtGui.QImage(self.size().width(),self.size().height(),QtGui.QImage.Format_RGB32)
        img.fill(QtGui.QColor(255,255,255).rgb())
        painter = QtGui.QPainter(img)    
        painter.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing|QtGui.QPainter.SmoothPixmapTransform)   
        view.render(painter)
        painter.end()
        fileName = QtGui.QFileDialog.getSaveFileName(self, "Save canvas to image", QtCore.QDir.currentPath(),self.trUtf8("*.png"), None)
        img.save(fileName)
		
    def imageUp(self):
        if not objectslist.currentRow() == -1:
            if not objectslist.currentRow() == 0:
                cR = objectslist.currentRow()
                #print(mainList)				
                for i in range(len(mainList)):
                    if cR == mainList[i][3]:                        
                        tempList0 = copy.deepcopy(mainList[i][0])
                        tempList1 = copy.deepcopy(mainList[i][1])
                        mainList[i][0] = mainList[i+1][0]
                        mainList[i][1] = mainList[i+1][1]
                        mainList[i+1][0] = tempList0
                        mainList[i+1][1] = tempList1

                for i in range(len(mainList)):
                    for k in range(len(mainList)):
                        if i == mainList[k][0]:                              				
                            mscene.items()[mainList[k][0]].setZValue(mainList[k][2]) #accordance current row in objectsList and record in mainList
				
                tempItemList = objectslist.item(cR).clone()
                objectslist.insertItem(cR-1,tempItemList)
                objectslist.setCurrentItem(objectslist.item(cR-1))
                objectslist.takeItem(cR+1)				
            print("- - -")
        else: print("Select item in objects list")
	
    def imageDown(self):
        if not objectslist.currentRow() == -1:
            if not objectslist.currentRow() == objectslist.count()-1:
                for i in range(len(mainList)):
                    if objectslist.currentRow() == mainList[i][3]:                        
                        tempList0 = copy.deepcopy(mainList[i][0])
                        tempList1 = copy.deepcopy(mainList[i][1])
                        mainList[i][0] = mainList[i-1][0]
                        mainList[i][1] = mainList[i-1][1]
                        mainList[i-1][0] = tempList0
                        mainList[i-1][1] = tempList1

                for i in range(len(mainList)):
                    for k in range(len(mainList)):
                        if i == mainList[k][0]:                              				
                            mscene.items()[mainList[k][0]].setZValue(mainList[k][2]) #accordance current row in objectsList and record in mainList
						
                tempItemList = objectslist.item(objectslist.currentRow()).clone()
                objectslist.insertItem(objectslist.currentRow()+2,tempItemList)
                objectslist.takeItem(objectslist.currentRow())
                objectslist.setCurrentItem(objectslist.item(objectslist.currentRow()+1))                
			
            print("- - -")			
        else: print("Select item in objects list")
		
#self.centerOn(1.0, 1.0)
		
#begin load test data			
def load_test_data():    
    pix = mscene.addPixmap(QtGui.QPixmap("img/test2.jpg"))
    pix.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test2.jpg")
    #print(objectslist.count())	
    mainList.append([0, 0, 99, 0])    

    six = mscene.addPixmap(QtGui.QPixmap("img/test1.png"))
    six.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
    objectslist.addItem("img/test1.png")
    mainList.append([1, 0, 100, 0])
    mainList[0] = [0, 1, 99, 1]
    #print(mainList)
	
    #tempItemList = objectslist.item(objectslist.count()-1).clone()
    #objectslist.insertItem(0, tempItemList)                
    #objectslist.takeItem(objectslist.count()-1)
	
    tempItemList = objectslist.item(objectslist.count()-1).clone()
    objectslist.insertItem(0, tempItemList)          
    objectslist.takeItem(objectslist.count()-1)
	
    mscene.items()[0].setZValue(99)
    mscene.items()[1].setZValue(100)
    
#end load test data

def printItemText():
    print("objectslist.currentRow: ", objectslist.currentRow())
	
app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.setWindowTitle('SpEd: Frame Editor')
widget.setWindowIcon(QtGui.QIcon('img/icon.png'))
widget.resize(800, 600)

mainList = []
dialog = QtGui.QFileDialog()
objectslist = QtGui.QListWidget()
#objectslist.setDragDropMode(objectslist.InternalMove)
mscene = QtGui.QGraphicsScene()
mscene.setItemIndexMethod(-1)

view = MyView(mscene)
load_test_data()


buttonLeftAll  = QtGui.QPushButton("Rotate Left All")
buttonRightAll = QtGui.QPushButton("Rotate Right All")
buttonAddFile = QtGui.QPushButton("Add file to canvas")
buttonDelFile = QtGui.QPushButton("Delete image from canvas")
buttonRotateLeftOne = QtGui.QPushButton("Rotate left one image")
buttonRotateRightOne = QtGui.QPushButton("Rotate right one image")
buttonSave = QtGui.QPushButton("Save canvas")
buttonUp = QtGui.QPushButton("Image up")
buttonDown = QtGui.QPushButton("Image down")

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
QtCore.QObject.connect(buttonUp,QtCore.SIGNAL("clicked()"),view.imageUp)
QtCore.QObject.connect(buttonDown,QtCore.SIGNAL("clicked()"),view.imageDown)

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
layout.addWidget(buttonUp)
layout.addWidget(buttonDown)
layout.addWidget(buttonSave)

widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())