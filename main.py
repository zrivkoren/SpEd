# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

#fromUtf8 = QtCore.QString.fromUtf8

class FrameEditor(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)                       
        self.statusBar()		        
        lableVisibility = QtGui.QLabel()
        lableVisibility.setText('Hi All!')
        		
        exit = QtGui.QAction(QtGui.QIcon('img/exit.png'), 'Exit', self)        
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
		
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)        		
      
class MyView(QtGui.QGraphicsView):
    def __init__(self,*args):
        QtGui.QGraphicsView.__init__(self,*args)
    def slotRotateLeft (self):
        self.rotate(-valueAngle.value())
    def slotRotateRight(self):
        self.rotate(valueAngle.value())
		
app = QtGui.QApplication(sys.argv)
frameeditor = FrameEditor()
widget = QtGui.QWidget()
widget.setWindowTitle('SpEd: Frame Editor')
widget.setWindowIcon(QtGui.QIcon('img/icon.png'))
widget.resize(800, 600)  		


scene = QtGui.QGraphicsScene()

scene.addPixmap(QtGui.QPixmap("img/test1.png"))

six = scene.addPixmap(QtGui.QPixmap("img/test1.png"))
six.setFlags(QtGui.QGraphicsItem.ItemIsMovable)


pix = scene.addPixmap(QtGui.QPixmap("img/test2.jpg"))
pix.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
view = MyView(scene)

buttonLeft  = QtGui.QPushButton("Rotate Left All")
buttonRight = QtGui.QPushButton("Rotate Right All")

valueAngle = QtGui.QSpinBox()
valueAngle.setValue(10)
valueAngle.setMaximum(359)
valueAngleLabel = QtGui.QLabel("Enter value of angle rotate:")

#  Qt.QObject.connect(spinbox, Qt.SIGNAL("valueChanged(int)"), slider.setValue)

# связываем нажатие кнопки с поворотом против/по часовой стрелке
QtCore.QObject.connect(buttonLeft ,QtCore.SIGNAL("clicked()"),view.slotRotateLeft )
QtCore.QObject.connect(buttonRight,QtCore.SIGNAL("clicked()"),view.slotRotateRight)
# размещаем виджеты
layout=QtGui.QVBoxLayout()
layout.addWidget(view)
layout.addWidget(buttonLeft)
layout.addWidget(buttonRight)
layout.addWidget(valueAngleLabel)
layout.addWidget(valueAngle)
widget.setLayout(layout)
frameeditor.setLayout(layout)
widget.show()

frameeditor.show()
sys.exit(app.exec_())