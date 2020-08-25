# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resolution_3.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
import cv2
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QMainWindow, QGraphicsPixmapItem, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import os
import sys
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_2.addWidget(self.graphicsView_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.pic_display)
        self.pushButton_2.clicked.connect(self.rec_display)
        self.pushButton_6.clicked.connect(self.pic_sharpen)
        self.pushButton_7.clicked.connect(self.pic_zoom_in)
        self.pushButton_8.clicked.connect(self.pic_zoom_out)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEM"))
        self.pushButton_3.setText(_translate("MainWindow", "读入"))
        self.pushButton_2.setText(_translate("MainWindow", "截取"))
        self.pushButton_6.setText(_translate("MainWindow", "边缘"))
        self.pushButton_5.setText(_translate("MainWindow", "圆拟合"))
        self.pushButton_7.setText(_translate("MainWindow", "放大"))
        self.pushButton_8.setText(_translate("MainWindow", "缩小"))
        self.pushButton_4.setText(_translate("MainWindow", "复位"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))

class PicShow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(PicShow, self).__init__(parent)
        self.setupUi(self)
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        self.pixel_data = []
        self.data_2 = []
        self.dst = []
        self.scale = 1


    def pic_display(self):

        # self.name1.append(float(self.lineEdit_2.text()))
        # text_0 = str(self.lineEdit.text())
        # text_2 = str(self.lineEdit_2.text())
        # text_3 = str(self.lineEdit_3.text())
        # path = text_0 + "/" + text_2 + "." + text_3
        file_name = QFileDialog.getOpenFileName(self, "Open File", "./", "All Files (*) ;;bmp (*.bmp)")
        path = file_name[0]
        (filepath, tempfilename) = os.path.split(path)
        (filename, extension) = os.path.splitext(tempfilename)

        if filename:
            # print(file_name)

            pic = cv2.imread(path)
            # size = pic.shape
            # img_s = cv2.resize(pic, (int(size[1] / 2), int(size[0] / 2)), interpolation=cv2.INTER_AREA)

            self.img_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)  # 转为灰度图
            w, h = self.img_gray.shape[0:2]
            pic1 = cv2.cvtColor(self.img_gray, cv2.COLOR_BGR2RGB)  # 转换通道
            frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView.setScene(self.scene)
            # self.scene.mousePressEvent = self.myMousePressEvent
            # print(self.name1)
            self.scene.mousePressEvent = self.myMousePressEvent
        else:
            self.textBrowser.append("please select the file")  # 在指定的区域显示提示信息
            self.cursot = self.textBrowser.textCursor()
            self.textBrowser.moveCursor(self.cursot.End)

    def myMousePressEvent(self, mouseEvent):
        # print(len(self.a), len(self.b))
        # if len(self.a) < 2 & len(self.b) < 2:
        point = str(mouseEvent.scenePos())
        x = mouseEvent.scenePos().x()
        y = mouseEvent.scenePos().y()
        self.a.append(int(x))
        self.b.append(int(y))
        self.textBrowser.append(point)
        # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)
        # print(len(self.a), len(self.b))
        if len(self.a) >= 2:
            self.rec_draw()

    def rec_draw(self):

        if self.a[-2] >= self.a[-1]:
            self.a[-2], self.a[-1] = self.a[-1], self.a[-2]
        # if self.b[0] >= self.b[1]:
        #     self.b[0], self.b[1] = self.b[1], self.b[0]
        if self.b[-2] >= self.b[-1]:
            self.b[-2], self.b[-1] = self.b[-1], self.b[-2]
        draw_rec = cv2.rectangle(self.img_gray, (self.a[-2], self.b[-2]), (self.a[-1], self.b[-1]), (0, 255, 0), 2)
        # self.img_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)  # 转为灰度图
        w, h = draw_rec.shape[0:2]
        pic1 = cv2.cvtColor(draw_rec, cv2.COLOR_BGR2RGB)  # 转换通道
        frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)

    def rec_display(self):
        if len(self.a) >= 2 and len(self.b) >= 2:
            self.pixel_data = np.array(self.img_gray)
            self.data_2 = self.pixel_data[self.b[-2]:self.b[-1], self.a[-2]:self.a[-1]]
            # print(data_2)
            # im = Image.fromarray(data_2)
            # im = im.convert('L')
            # cv2.imshow('a', data_2)
            # cv2.waitKey(0)
            w, h = self.data_2.shape[0:2]
            # w = len(data_2)
            # h = len(data_2[0])
            pic1 = cv2.cvtColor(self.data_2, cv2.COLOR_BGR2RGB)  # 转换通道
            frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView_2.setScene(self.scene)
            # self.scene.mousePressEvent = self.myMousePressEvent_2

    def pic_sharpen(self):

        self.data_2 = cv2.medianBlur(self.data_2, 5)
        # 中值滤波
        # 拉普拉斯算子
        # kernel = np.array(([0, 1, 0],
        #                    [1, -4, 1],
        #                    [0, 1, 0]), dtype="float32")
        # self.dst = cv2.filter2D(self.data_2, -1, kernel)
        # cv2.imshow('a', self.data_2)
        # cv2.waitKey(0)
        self.data_2 = cv2.GaussianBlur(self.data_2, (7, 7), 0)
        # 高斯滤波
        self.dst = cv2.Canny(self.data_2, 30, 100)
        # Canny 边缘检测
        w, h = self.dst.shape[0:2]

        pic1 = cv2.cvtColor(self.dst, cv2.COLOR_BGR2RGB)  # 转换通道
        frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView_2.setScene(self.scene)
        self.scene.mousePressEvent = self.myMousePressEvent_2

    def pic_zoom_in(self):
        if not (self.dst == []) and self.scale < 2:
            self.scale = 1.2
            h, w = self.dst.shape[0:2]
            size = (int(w * self.scale), int(h * self.scale))
            self.dst = cv2.resize(self.dst, size, interpolation=cv2.INTER_AREA)
            w, h = self.dst.shape[0:2]

            pic1 = cv2.cvtColor(self.dst, cv2.COLOR_BGR2RGB)  # 转换通道
            frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView_2.setScene(self.scene)
            self.scene.mousePressEvent = self.myMousePressEvent_2

    def pic_zoom_out(self):
        if not (self.dst == []) and self.scale > 0.4:
            self.scale = 0.8
            h, w = self.dst.shape[0:2]
            size = (int(w * self.scale), int(h * self.scale))
            self.dst = cv2.resize(self.dst, size, interpolation=cv2.INTER_AREA)
            w, h = self.dst.shape[0:2]

            pic1 = cv2.cvtColor(self.dst, cv2.COLOR_BGR2RGB)  # 转换通道
            frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView_2.setScene(self.scene)
            self.scene.mousePressEvent = self.myMousePressEvent_2

    def myMousePressEvent_2(self, mouseEvent):

        point = str(mouseEvent.scenePos())
        x = mouseEvent.scenePos().x()
        y = mouseEvent.scenePos().y()
        self.c.append(int(x))
        self.d.append(int(y))
        self.textBrowser.append(point)
        # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)
        # print(self.dst.shape[:])
        # self.dst = cv2.merge((self.dst, self.dst, self.dst))
        # print(self.dst.shape[:])
        # self.dst = cv2.cvtColor(self.dst, cv2.COLOR_GRAY2BGR)

        if len(self.c) == 2 and len(self.d) == 2:
            self.dst = cv2.cvtColor(self.dst, cv2.COLOR_GRAY2BGR)
            self.dst = cv2.line(self.dst, (self.c[0], self.d[0]), (self.c[1], self.d[1]), (0, 0, 255), 3)
            # cv2.imshow('a', self.dst)
            # cv2.waitKey(0)
            w, h = self.dst.shape[0:2]

            pic1 = cv2.cvtColor(self.dst, cv2.COLOR_BGR2RGB)  # 转换通道
            frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView_2.setScene(self.scene)
            self.scene.mousePressEvent = self.myMousePressEvent_2

        if len(self.c) == 4 and len(self.d) == 4:
            # self.dst = cv2.cvtColor(self.dst, cv2.COLOR_GRAY2BGR)
            self.dst = cv2.line(self.dst, (self.c[2], self.d[2]), (self.c[3], self.d[3]), (0, 0, 255), 3)
            # cv2.imshow('a', self.dst)
            # cv2.waitKey(0)
            w, h = self.dst.shape[0:2]

            pic1 = cv2.cvtColor(self.dst, cv2.COLOR_BGR2RGB)  # 转换通道
            frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView_2.setScene(self.scene)
            # self.scene.mousePressEvent = self.myMousePressEvent_2


def main():

    app = QApplication(sys.argv)
    pic = PicShow()
    pic.show()
    app.exec_()


if __name__ == '__main__':

    main()
