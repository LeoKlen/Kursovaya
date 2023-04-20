import sys
import random
import os
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PySide6.QtGui import QBrush, QPen, QFont, QColor, QPainter, QPointList, QPolygonF, QPolygon, QMouseEvent, QWheelEvent
from PySide6.QtCore import Qt, QRect, QPoint, QPointF, QEvent
from PySide6 import QtGui
# from ui_mainWin4 import Ui_MainWindow
from mainWin6_ui import Ui_MainWindow
# from PySide6.QtGui import *
# from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # вызовем конструктор базовго класса
        super(MainWindow, self).__init__(parent)
        # создаем переменную экземпляра класса графического интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # очистка блока вывода сообщения об ошибки
        self.ui.label_err.clear()
        # подключаем кнопку расчитать
        self.ui.btn_work.clicked.connect(self.calculate)
        self.ui.btn_rotate_minus.clicked.connect(self.rotate_minus)
        self.ui.btn_rotate_plus.clicked.connect(self.rotate_plus)
        self.ui.btn_zoom_minus.clicked.connect(self.zoom_minus)
        self.ui.btn_zoom_plus.clicked.connect(self.zoom_plus)
        
        # данное подключение работает
        # self.ui.lineEdit_V.textChanged.connect(self.calculate)
        # self.ui.lineEdit_H.textChanged.connect(self.calculate)

        # # создаем сцену
        # self.scene = QGraphicsScene(self)
        # # подключаем сцену в окно
        # self.view = self.ui.graphicsView.setScene(self.scene)
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QColor("#563d7c"))

        # self.view = QGraphicsView(self.scene, self.ui.frame_2)
        self.view = QGraphicsView(self.scene)
        # self.view.scrollBarWidgets(False)
        self.ui.verticalLayout.addWidget(self.view)
        
        self.view.setRenderHint(QPainter.Antialiasing)
        self.data = dict()

    def calculate(self):
        self.ui.label_err.clear()
        g = 9.8
        if (self.ui.lineEdit_V.text() == '' 
            or self.ui.lineEdit_H.text() == ''
            or self.ui.lineEdit_V.text() == ''
            or self.ui.lineEdit_L.text() == ''
            or self.ui.lineEdit_D.text() == ''
            or self.ui.lineEdit_gamma.text() == ''):
            self.ui.label_err.setText("Ошибка ввода данных:\n Заполните все поля.")
            return
        if (float(self.ui.lineEdit_V.text()) <= 0 
            or float(self.ui.lineEdit_H.text()) <= 0
            or float(self.ui.lineEdit_V.text())  <= 0
            or float(self.ui.lineEdit_L.text())  <= 0
            or float(self.ui.lineEdit_D.text())  <= 0
            or float(self.ui.lineEdit_gamma.text())  <= 0):
            self.ui.label_err.setText("Ошибка ввода данных:\n Все вводимые данные, должны быть числа больше нуля.")
            return
        if (float(self.ui.lineEdit_gamma.text()) >= 90):
            self.ui.label_err.setText("Ошибка ввода данных:\n Угол крена должен быть меньше 90 град.")
            return
        V = float(self.ui.lineEdit_V.text())
        H = float(self.ui.lineEdit_H.text())
        self.A = V*math.sqrt(2*H/g)
        self.distance_A=self.A
        self.ui.label_A.setText(f"{round(  self.A , 0)}")
        angle_G = math.radians(float(self.ui.lineEdit_gamma.text()))
        # Перегрузка
        Ny = 1/math.cos(angle_G)
        self.ui.label_Ny.setText(f"{round(  Ny , 1)}")
        # print("Перегрузка=", Ny)
        # R1
        self.R1 = V*V/(g*math.sqrt(Ny*Ny-1))
        self.ui.label_Rv.setText(f"{round(  self.R1 , 0)}")
        # загрузка LK
        self.L = float(self.ui.lineEdit_L.text())
        
        self.LK=0
        # загрузка D
        self.D = float(self.ui.lineEdit_D.text())
        self.R2 = math.sqrt((self.A-self.L)*(self.A-self.L)+self.R1*self.R1)
        self.R3 = math.sqrt(self.A*self.A+self.R1*self.R1)
        print("R1=",self.R1, "  R2=",self.R2, "  R3=",self.R3, "  D=",self.D)
        

        if self.D>=(self.R2+self.R3):
            # расчет координат схемы в классическом случае
            self.cacl_LongDistance()
        elif self.D<self.R2+self.R3 and self.D>=self.L:
            # расчет координат схемы в классическом случае
            self.cacl_gen()
        else: 
            self.ui.label_err.setText("Ошибка ввода данных:\n Расстояние между целями меньше длина серии.\n Показан предельный возможный случай когда D=L.")
            self.D=self.L
            self.cacl_gen()

        # расчеты контура самолета
        self.createPointsFly()

        # отрисовать чертеж
        self.drawing()


    def cacl_gen(self):
        # расчет углов конуса
        print("cos(W1)=", (self.R2*self.R2+self.D*self.D-self.R3*self.R3)/(2*self.D*self.R2), "  cos(W2)=", (self.R2*self.R2+(self.A-self.L)*(self.A-self.L)-self.R1*self.R1)/(2*(self.A-self.L)*self.R2))
        self.angle_W1 = math.acos((self.R2*self.R2+self.D*self.D-self.R3*self.R3)/(2*self.D*self.R2))
        self.angle_W2 = math.acos((self.R2*self.R2+(self.A-self.L)*(self.A-self.L)-self.R1*self.R1)/(2*(self.A-self.L)*self.R2))
        
        
        # расчет половины угла конуса
        self.angle_K = math.pi-self.angle_W1-self.angle_W2
        self.ui.label_K.setText(f"{round(  2*math.degrees(self.angle_K) , 1)}")

        # расчет точек
        self.C1_x = 0
        self.C1_y = 0

        self.C2_x = 0
        self.C2_y = self.D
        # координаты самолета в 1 точке
        self.S1_x = -1*(self.A-self.L)*math.sin(self.angle_K)
        self.S1_y = -1*(self.A-self.L)*math.cos(self.angle_K)
        # симметричная точка S1 относительно прямой С1С2
        self.S3_x=-self.S1_x
        self.S3_y=self.S1_y
        # координаты центра окружностей с радиусами R1 R2 R3
        self.O_x = -1*self.R2*math.sin(self.angle_W1)
        self.O_y = self.R2*math.cos(self.angle_W1)

        # расчет конечной точки серии выстрелов у цели 1
        self.LC1_x, self.LC1_y, err =self.getpointInLine(self.C1_x,self.C1_y, self.S1_x, self.S1_y, self.L, -1)

        # расчет координат самолета в точке 2
        # угол alfa1 между С2-O-горизонталь  
        alfa1=math.atan((self.C2_y-self.O_y)/(self.C2_x-self.O_x))
        # угол между С2-О-S2
        alfa=math.atan((self.A+self.L*self.LK)/self.R1)
        # угол между S2-O_горизонталь
        alfa2= alfa-alfa1
        # координаты самолета в точке 2
        self.S2_x=self.O_x + self.R1*math.cos(alfa2)
        self.S2_y=self.O_y - self.R1*math.sin(alfa2)

       


    def cacl_LongDistance(self): 
        # расчет точек
        self.C1_x = 0
        self.C1_y = 0

        self.C2_x = 0
        self.C2_y = self.D

        # расчет половины угла конуса
        self.angle_K = math.pi-math.asin(self.R1/self.R2)
        self.ui.label_K.setText(f"{round(  2*math.degrees(self.angle_K) , 1)}")

       
        # координаты самолета в 1 точке
        self.S1_x = -1*(self.A-self.L)*math.sin(math.pi-self.angle_K)
        self.S1_y = 1*(self.A-self.L)*math.cos(math.pi-self.angle_K)
        # симметричная точка S1 относительно прямой С1С2
        self.S3_x=-self.S1_x
        self.S3_y=self.S1_y




        # координаты центра окружностей с радиусами R1 R2 R3
        self.O_x = 0
        self.O_y = self.R2

        OC2=self.C2_y-self.O_y
        self.S2_x=self.R1*math.sqrt(1-(self.R1/OC2)**2)
        self.S2_y=self.R2+(self.R1**2)/OC2
        # расчет конечной точки серии выстрелов у цели 1
        self.LC1_x, self.LC1_y, err =self.getpointInLine(self.C1_x,self.C1_y, self.S1_x, self.S1_y, self.L, -1)

    
    def getpointInLine(self,x1,y1,x2,y2,Ra,b):
        R12=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
        if R12==0:
            return 0,0,1
        k = Ra / R12
        x3 = x1 + (x2-x1) * k
        y3 = y1 + (y2-y1) * k
        if b<0:
            x3=2*x1-x3
            y3=2*y1-y3
        return x3,y3,0
    
    def createPointsFly(self):
        # расчеты контура самолета
        self.flagFly=True
        lenFly=200
        self.f1_x, self.f1_y, err =self.getpointInLine(self.S1_x,self.S1_y, self.C1_x,self.C1_y,lenFly, 1)
        if err==1:
            self.flagFly=False
        self.f2_x, self.f2_y, err =self.getpointInLine(self.S1_x,self.S1_y, self.C1_x,self.C1_y,lenFly, -1)
        if err==1:
            self.flagFly=False
        self.f5_x, self.f5_y, err =self.getpointInLine(self.S1_x,self.S1_y, self.C1_x,self.C1_y,1.5*lenFly, -1)
        if err==1:
            self.flagFly=False
        f31_x, f31_y, err =self.getpointInLine(self.S1_x,self.S1_y, self.O_x,self.O_y,lenFly, -1)
        if err==1:
            self.flagFly=False
        f41_x, f41_y, err =self.getpointInLine(self.S1_x,self.S1_y, self.O_x,self.O_y,lenFly, 1)
        if err==1:
            self.flagFly=False

        self.f3_x = self.f2_x - self.S1_x + f31_x
        self.f3_y = self.f2_y - self.S1_y + f31_y

        self.f4_x = self.f2_x - self.S1_x + f41_x
        self.f4_y = self.f2_y - self.S1_y + f41_y

    def drawing(self):
        # очищаем сцену
        self.scene.clear()
        # обновляем view
        self.view.update()
        # устанавливаем фон
        self.scene.setBackgroundBrush(QColor("#000103"))
        # рисуем сетку
        self.drawGrid()
        # задаем перья - цвет и толщину
        whitePen = QPen(Qt.white)
        whitePen.setWidth(15) 

        whitePen2 = QPen(Qt.white)
        whitePen2.setWidth(50) 

        whitePenDL = QPen(Qt.white)
        whitePenDL.setWidth(15)
        whitePenDL.setStyle(Qt.DashLine)

        whitePenDDL = QPen(Qt.white)
        whitePenDDL.setWidth(15)
        whitePenDDL.setStyle(Qt.DashDotLine)

        redPen = QPen(Qt.red)
        redPen.setWidth(15)
        bluePen = QPen(Qt.blue)
        bluePen.setWidth(30)
        bluePen2 = QPen(Qt.blue)
        bluePen2.setWidth(50)
        brushRed=QBrush(Qt.red, Qt.SolidPattern)
        brushBlue=QBrush(Qt.blue, Qt.SolidPattern)
        redPen2 = QPen(Qt.red)
        redPen2.setWidth(30)

        # рисуем круги
        c1=self.scene.addEllipse(self.O_x-self.R1,-self.O_y-self.R1, 2*self.R1, 2*self.R1, whitePen)
        self.scene.addEllipse(self.O_x-self.R2,-self.O_y-self.R2, 2*self.R2, 2*self.R2, whitePenDDL)
        self.scene.addEllipse(self.O_x-self.R3,-self.O_y-self.R3, 2*self.R3, 2*self.R3, whitePenDL)
        # отрезок от самолета в новой точке до цели 2
        self.scene.addLine(self.S2_x,-self.S2_y,self.C2_x,-self.C2_y,whitePen)
        # self.scene.addLine(self.S2_x,-self.S2_y,self.LC2b_x,-self.LC2b_y,whitePen)
        # self.scene.addLine(self.LC2b_x,-self.LC2b_y,self.LC2e_x,-self.LC2e_y,redPen2)
        # отрезок между целью 1 и целью 2
        self.scene.addLine(self.C1_x,-self.C1_y,self.C2_x,-self.C2_y,whitePen2)
        # отрезок между целью 1 и концом длины серии
        self.scene.addLine(self.C1_x,-self.C1_y,self.LC1_x,-self.LC1_y,redPen2)
        # отрезок от самолета в начальной позиции и целью 1
        self.scene.addLine(self.C1_x,-self.C1_y,self.S1_x,-self.S1_y,whitePen)
        #  отрезок зеркальный от самолета в начально позиции до цели  1 
        #  чтобы показать угол конуса захода на цель 2
        self.scene.addLine(self.C1_x,-self.C1_y,self.S3_x,-self.S3_y,whitePen)
        # самолет
        flyPen = QPen(Qt.white)
        flyPen.setWidth(75)  
        if self.flagFly:
            self.scene.addLine(self.f1_x,-self.f1_y,self.S1_x,-self.S1_y,flyPen)
            self.scene.addLine(self.f3_x,-self.f3_y,self.f4_x,-self.f4_y,flyPen)
            self.scene.addLine(self.S1_x,-self.S1_y,self.f3_x,-self.f3_y,flyPen)
            self.scene.addLine(self.S1_x,-self.S1_y,self.f4_x,-self.f4_y,flyPen)
            self.scene.addLine(self.f2_x,-self.f2_y,self.f5_x,-self.f5_y,flyPen)
        
        rr=100
        # выделяем самолет 1        
        self.scene.addEllipse(self.S1_x-rr, -self.S1_y-rr, 2*rr,2*rr, bluePen2)
        # подписываем - ставим 1
        txt1=self.scene.addText("1", QFont("Sanserif", 300))
        txt1.setPos(self.S1_x-600,-self.S1_y-200)
        txt1.setDefaultTextColor(Qt.white)
        # выделяем самолет 2
        self.scene.addEllipse(self.S2_x-rr, -self.S2_y-rr, 2*rr,2*rr, whitePen, brushBlue)
        # подписываем - ставим 2
        txt2=self.scene.addText("2", QFont("Sanserif", 300))
        txt2.setPos(self.S2_x+200,-self.S2_y-200)
        txt2.setDefaultTextColor(Qt.white)
        # выделяем цель 1
        self.scene.addEllipse(self.C1_x-rr, -self.C1_y-rr, 2*rr,2*rr, whitePen)
        # подписываем цель 1
        txt1=self.scene.addText("1", QFont("Sanserif", 350))
        txt1.setPos(self.C1_x+200,-self.C1_y-200)
        txt1.setDefaultTextColor(Qt.white)
        # выделяем цель 2
        self.scene.addEllipse(self.C2_x-rr, -self.C2_y-rr, 2*rr,2*rr, redPen2)
        # подписываем цель 2
        txt2=self.scene.addText("2", QFont("Sanserif", 350))
        txt2.setPos(self.C2_x+200,-self.C2_y-200)
        txt2.setDefaultTextColor(Qt.white)        
        
        rrr=1
        kr=2.5
        self.scene.addEllipse(kr*self.S3_x-rrr, -kr*self.S3_y-rrr, 2*rrr,2*rrr, bluePen)
        self.scene.addEllipse(kr*self.S3_x-rrr, -kr*self.S3_y-rrr, 2*rrr,2*rrr, bluePen)
        
        #  ------------------------------------------
        # выделение угла конуса захода на цель 2
        # colorKonus = QColor.fromString("#753535")
        # colorKonus.setAlpha(100) 
        colorKonus = QColor.fromString("#47fd21")
        colorKonus.setAlpha(100)

        start_angle = (-math.degrees(self.angle_K)-90)*16
        arc_length = math.degrees(self.angle_K)*2*16

        ellipseItem = QGraphicsEllipseItem(-self.distance_A/2, -self.distance_A/2, self.distance_A,self.distance_A)
        ellipseItem.setStartAngle(start_angle)
        ellipseItem.setSpanAngle(arc_length)
        ellipseItem.setBrush(colorKonus)
        self.scene.addItem(ellipseItem)
        # ---------------------------------------------

    def drawGrid(self):
        # color = QColor.fromString("#293c52")
        # color.setAlpha(100)
        # penGrid= QPen(color)
        # penGrid.setWidth(20)

        color = QColor.fromString("#21b5fd")
        color.setAlpha(150)
        penGrid= QPen(color)
        penGrid.setWidth(10)

        L_left=self.O_x-10*self.R1
        st=10*int(self.R1)
        step_l=1000
        xs=0
        while xs>L_left:
            self.scene.addLine(xs,-3*st,xs,3*st,penGrid)
            self.scene.addLine(-xs,-3*st,-xs,3*st,penGrid)
            self.scene.addLine(-3*st,xs,3*st,xs,penGrid)
            self.scene.addLine(-3*st,-xs,3*st,-xs,penGrid)
            xs=xs-step_l  
    
    # def mousePressEvent(self,  event: QWheelEvent):
    #         if(event.angleDelta().y()>0):
    #             self.view.scale(1.2, 1.2)
    #         else:
    #             self.view.scale(0.8, 0.8)

    # def mousePressEvent(self, QMouseEvent):
    #     #print mouse position
    #     print (QMouseEvent.pos(), " ", QMouseEvent.source(), " ", QMouseEvent.screenPos())

    # def wheelEvent(self, event: QWheelEvent):
    #     if event.angleDelta().y() > 0:
    #         print("+")
    #     else:
    #         print("-")

    def wheelEvent(self, event: QWheelEvent):
        if(event.angleDelta().y()>0):
            self.view.scale(1.2, 1.2)
        else:
            self.view.scale(0.8, 0.8)
            # adj = (event.angleDelta().y() / 120) * 0.1
            # # self.scale(1 + adj, 1 + adj) 
            # self.view.scale(1.2, 1.2)
    # def mouseMoveEvent (self, event: QMouseEvent):
    def mouseMoveEvent (self, event: QMouseEvent):
        # print(QMouseEvent(QEvent.MouseMove, Qt.NoButton, Qt.NoButton, Qt.NoModifier).pos())
        print(event.pos())
    # def mouseReleaseEvent(self, QMouseEvent):
    #     # self.label.setText("mouseReleaseEvent")
    #     # print ("mouseReleaseEvent")
    #     print (QMouseEvent.pos())




    def rotate_minus(self):
        self.view.rotate(-14)


    def rotate_plus(self):
        self.view.rotate(14)
    
    def zoom_plus(self):
        self.view.scale(1.2, 1.2)
    
    def zoom_minus(self):
        self.view.scale(0.8, 0.8)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.setWindowTitle("Расчет выхода на две цели")
    window.show()
    sys.exit(app.exec())
