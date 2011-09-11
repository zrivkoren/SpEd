# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
     
class MyView(QtGui.QGraphicsView):
    def __init__(self,*args):
        QtGui.QGraphicsView.__init__(self,*args)
    def slotRotateLeft (self):
        self.rotate(-valueAngle.value())
    def slotRotateRight(self):
        self.rotate(valueAngle.value())

def open_file_dialog():
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file', '/home')
        new_img = scene.addPixmap(QtGui.QPixmap(filename))
        new_img.setFlags(QtGui.QGraphicsItem.ItemIsMovable)


		
		
app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.setWindowTitle('SpEd: Frame Editor')
widget.setWindowIcon(QtGui.QIcon('img/icon.png'))
widget.resize(800, 600)

dialog = QtGui.QFileDialog()

scene = QtGui.QGraphicsScene()
scene.addPixmap(QtGui.QPixmap("img/test1.png"))


six = scene.addPixmap(QtGui.QPixmap("img/test1.png"))
six.setFlags(QtGui.QGraphicsItem.ItemIsMovable)

pix = scene.addPixmap(QtGui.QPixmap("img/test2.jpg"))
pix.setFlags(QtGui.QGraphicsItem.ItemIsMovable)

view = MyView(scene)

buttonLeft  = QtGui.QPushButton("Rotate Left All")
buttonRight = QtGui.QPushButton("Rotate Right All")
buttonAddFile = QtGui.QPushButton("Add file to canvas")

valueAngle = QtGui.QSpinBox()
valueAngle.setValue(10)
valueAngle.setMaximum(359)
valueAngleLabel = QtGui.QLabel("Enter value of angle rotate:")

QtCore.QObject.connect(buttonLeft,QtCore.SIGNAL("clicked()"),view.slotRotateLeft )
QtCore.QObject.connect(buttonRight,QtCore.SIGNAL("clicked()"),view.slotRotateRight)
QtCore.QObject.connect(buttonAddFile,QtCore.SIGNAL("clicked()"),open_file_dialog)

layout=QtGui.QVBoxLayout()
layout.addWidget(view)
layout.addWidget(buttonLeft)
layout.addWidget(buttonRight)
layout.addWidget(valueAngleLabel)
layout.addWidget(valueAngle)
layout.addWidget(buttonAddFile)


widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())