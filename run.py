from ECCrawl import ECCrawl
import Ali, JD
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import time
import source
import Verify

url_lock = QMutex()
wid_lock = QMutex()
download_list = []


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # self.MainWindow = QMainWindow()
        self.setupUi()
        self.td1 = Dthread()
        self.td2 = Dthread()
        self.td3 = Dthread()
        self.item_items = []
        self.statue = False
        self.mem = MemerySetting()
        self.load_setting()
        self.write_setting()
        self.my_ui()
        self.my_action()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setEnabled(True)
        self.setFixedSize(960, 700)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(0)
        self.top_widget = QtWidgets.QWidget(self.centralwidget)
        self.top_widget.setMinimumSize(QtCore.QSize(0, 80))
        self.top_widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_lb = QtWidgets.QLabel(self.top_widget)
        self.logo_lb.setMinimumSize(QtCore.QSize(120, 0))
        self.logo_lb.setMaximumSize(QtCore.QSize(120, 16777215))
        self.logo_lb.setObjectName("logo_lb")
        self.horizontalLayout.addWidget(self.logo_lb)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.top_setting = QtWidgets.QPushButton(self.top_widget)
        self.top_setting.setMinimumSize(QtCore.QSize(150, 65))
        self.top_setting.setMaximumSize(QtCore.QSize(150, 16777215))
        self.top_setting.setObjectName("top_setting")
        self.gridLayout_4.addWidget(self.top_setting, 0, 2, 1, 1, Qt.AlignBottom)
        self.top_list = QtWidgets.QPushButton(self.top_widget)
        self.top_list.setMinimumSize(QtCore.QSize(150, 65))
        self.top_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.top_list.setObjectName("top_list")
        self.gridLayout_4.addWidget(self.top_list, 0, 1, 1, 1, Qt.AlignBottom)
        self.top_dnld = QtWidgets.QPushButton(self.top_widget)
        self.top_dnld.setMinimumSize(QtCore.QSize(150, 65))
        self.top_dnld.setMaximumSize(QtCore.QSize(150, 16777215))
        self.top_dnld.setObjectName("top_dnld")
        self.gridLayout_4.addWidget(self.top_dnld, 0, 0, 1, 1, Qt.AlignBottom)
        self.top_vip = QtWidgets.QPushButton(self.top_widget)
        self.top_vip.setMinimumSize(QtCore.QSize(150, 65))
        self.top_vip.setMaximumSize(QtCore.QSize(150, 16777215))
        self.top_vip.setObjectName("top_vip")
        self.gridLayout_4.addWidget(self.top_vip, 0, 3, 1, 1, Qt.AlignBottom)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.label_3 = QtWidgets.QLabel(self.top_widget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 7, 7, -1)
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.top_min = QtWidgets.QPushButton(self.top_widget)
        self.top_min.setMinimumSize(QtCore.QSize(30, 30))
        self.top_min.setMaximumSize(QtCore.QSize(30, 30))
        self.top_min.setText("")
        self.top_min.setObjectName("top_min")
        self.gridLayout_3.addWidget(self.top_min, 0, 0, 1, 1, Qt.AlignTop)
        self.top_close = QtWidgets.QPushButton(self.top_widget)
        self.top_close.setMinimumSize(QtCore.QSize(30, 30))
        self.top_close.setMaximumSize(QtCore.QSize(30, 30))
        self.top_close.setText("")
        self.top_close.setObjectName("top_close")
        self.gridLayout_3.addWidget(self.top_close, 0, 2, 1, 1, Qt.AlignTop)
        self.top_max = QtWidgets.QPushButton(self.top_widget)
        self.top_max.setMinimumSize(QtCore.QSize(30, 30))
        self.top_max.setMaximumSize(QtCore.QSize(30, 30))
        self.top_max.setText("")
        self.top_max.setObjectName("top_max")
        self.gridLayout_3.addWidget(self.top_max, 0, 1, 1, 1, Qt.AlignTop)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.top_widget)
        self.button_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.button_widget.setMinimumSize(QtCore.QSize(0, 540))
        self.button_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.button_widget.setObjectName("button_widget")
        self.button_dnld = QtWidgets.QWidget()
        self.button_dnld.setObjectName("button_dnld")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.button_dnld)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QPlainTextEdit(self.button_dnld)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.button_dnld)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.dnld_bt = QtWidgets.QPushButton(self.button_dnld)
        self.dnld_bt.setMinimumSize(QtCore.QSize(100, 50))
        self.dnld_bt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dnld_bt.setObjectName("dnld_bt")
        self.gridLayout_2.addWidget(self.dnld_bt, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 5)
        self.gridLayout_2.setColumnStretch(1, 5)
        self.gridLayout_2.setRowStretch(0, 5)
        self.gridLayout_2.setRowStretch(1, 5)
        self.button_widget.addTab(self.button_dnld, "")
        self.button_list = QtWidgets.QWidget()
        self.button_list.setObjectName("button_list")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.button_list)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.button_list)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.button_widget.addTab(self.button_list, "")
        self.button_setting = QtWidgets.QWidget()
        self.button_setting.setObjectName("button_setting")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.button_setting)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.button_setting)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.button_setting)
        self.groupBox_8.setMinimumSize(QtCore.QSize(640, 240))
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 240))
        self.groupBox_8.setObjectName("groupBox_8")
        self.mb_ck = QtWidgets.QCheckBox(self.groupBox_8)
        self.mb_ck.setGeometry(QtCore.QRect(60, 40, 101, 19))
        self.mb_ck.setObjectName("mb_ck")
        self.pc_ck = QtWidgets.QCheckBox(self.groupBox_8)
        self.pc_ck.setGeometry(QtCore.QRect(60, 80, 101, 19))
        self.pc_ck.setObjectName("pc_ck")
        self.vd_ck = QtWidgets.QCheckBox(self.groupBox_8)
        self.vd_ck.setGeometry(QtCore.QRect(310, 80, 91, 19))
        self.vd_ck.setObjectName("vd_ck")
        self.label_13 = QtWidgets.QLabel(self.groupBox_8)
        self.label_13.setGeometry(QtCore.QRect(40, 152, 72, 15))
        self.label_13.setObjectName("label_13")
        self.file_edit = QtWidgets.QLineEdit(self.groupBox_8)
        self.file_edit.setGeometry(QtCore.QRect(120, 150, 300, 20))
        self.file_edit.setObjectName("file_edit")
        self.file_edit.setReadOnly(True)
        self.file_bt = QtWidgets.QPushButton(self.groupBox_8)
        self.file_bt.setGeometry(QtCore.QRect(440, 148, 50, 24))
        self.file_bt.setObjectName("file_bt")
        self.file_open = QtWidgets.QPushButton(self.groupBox_8)
        self.file_open.setGeometry(QtCore.QRect(500, 148, 50, 24))
        self.file_open.setObjectName("file_open")

        self.cl_ck = QtWidgets.QCheckBox(self.groupBox_8)
        self.cl_ck.setGeometry(QtCore.QRect(310, 40, 121, 19))
        self.cl_ck.setObjectName("cl_ck")
        self.verticalLayout_2.addWidget(self.groupBox_8)
        self.groupBox_7 = QtWidgets.QGroupBox(self.button_setting)
        self.groupBox_7.setMinimumSize(QtCore.QSize(600, 150))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_7)
        self.label_11.setGeometry(QtCore.QRect(60, 70, 72, 15))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        self.label_12.setGeometry(QtCore.QRect(310, 70, 72, 15))
        self.label_12.setObjectName("label_12")
        self.ip_edit = QtWidgets.QLineEdit(self.groupBox_7)
        self.ip_edit.setGeometry(QtCore.QRect(120, 70, 150, 21))
        self.ip_edit.setObjectName("ip_edit")
        self.ip_edit.setEnabled(False)
        self.port_edit = QtWidgets.QLineEdit(self.groupBox_7)
        self.port_edit.setGeometry(QtCore.QRect(360, 70, 113, 21))
        self.port_edit.setObjectName("port_edit")
        self.port_edit.setEnabled(False)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.groupBox_9 = QtWidgets.QGroupBox(self.button_setting)
        self.groupBox_9.setMinimumSize(QtCore.QSize(150, 150))
        self.groupBox_9.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_9.setObjectName("groupBox_9")
        self.update_bt = QtWidgets.QPushButton(self.groupBox_9)
        self.update_bt.setGeometry(QtCore.QRect(60, 40, 93, 28))
        self.update_bt.setObjectName("update_bt")
        self.verticalLayout_2.addWidget(self.groupBox_9)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label_6 = QtWidgets.QLabel(self.button_setting)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.button_widget.addTab(self.button_setting, "")
        self.button_vip = QtWidgets.QWidget()
        self.button_vip.setObjectName("button_vip")
        self.button_widget.addTab(self.button_vip, "")
        self.verticalLayout.addWidget(self.button_widget)
        self.verticalLayout.setStretch(0, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 0, 0)
        self.setCentralWidget(self.centralwidget)
        self.set_vip_widget()
        self.retranslateUi(self)
        self.button_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.style_sheet()

    def set_vip_widget(self):
        self.button_vip.setStyleSheet(
            "QPushButton{background-color:rgb(255, 255, 255);border:1px solid #B7B7B7;font-size:35px;color:#F5AE14;cursor:Pointing Hand}QPushButton:hover{background-color:rgb(0, 255, 0)}QPushButton:pressed{background-color:rgb(0, 0, 255)}\n")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.button_vip)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.vip_tabWidget = QtWidgets.QTabWidget(self.button_vip)
        self.vip_tabWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.vip_tabWidget.setMaximumSize(QtCore.QSize(900, 450))
        self.vip_tabWidget.setStyleSheet(
            "QTabBar::tab{width:120px;height:50px;font-size:20px;color:#515151;background-color:white}QTabBar::tab:selected{color:balck;border-bottom:2px solid #F5AE14;font-size:25px}\n"
            "QTabWidget{border:1px solid #B7B7B7;background-color:rgb(200,200,200)}\n"
            "QPushButton{background-color:rgb(255, 255, 255);border:1px solid #B7B7B7;font-size:20px;color:black}\n"
            "QPushButton:hover{background-color:rgb(200, 200, 200)}\n"
            "QPushButton:pressed{background-color:rgb(100, 100, 100)}\n"
            "QWidget{background:white}")
        self.vip_tabWidget.setObjectName("vip_tabWidget")
        self.vip_tab1 = QtWidgets.QWidget()
        self.vip_tab1.setStyleSheet(
            "QLineEdit{border:1px solid #B7B7B7;border-radius:2px;background-color:rgb(255,255,255)}")
        self.vip_tab1.setObjectName("vip_tab1")
        self.act_code = QtWidgets.QLineEdit(self.vip_tab1)
        self.act_code.setGeometry(QtCore.QRect(320, 140, 280, 31))
        self.act_code.setObjectName("act_code")
        self.label_2 = QtWidgets.QLabel(self.vip_tab1)
        self.label_2.setGeometry(QtCore.QRect(240, 150, 72, 15))
        self.label_2.setObjectName("label_2")
        self.code_copy = QtWidgets.QPushButton(self.vip_tab1)
        self.code_copy.setGeometry(QtCore.QRect(640, 80, 93, 28))
        self.code_copy.setObjectName("code_copy")
        self.mec_code = QtWidgets.QLineEdit(self.vip_tab1)
        self.mec_code.setGeometry(QtCore.QRect(320, 80, 280, 31))
        self.mec_code.setObjectName("mec_code")
        self.mec_code.setReadOnly(True)
        self.mec_code.setText(Verify.machine_code())
        self.label = QtWidgets.QLabel(self.vip_tab1)
        self.label.setGeometry(QtCore.QRect(240, 90, 72, 15))
        self.label.setObjectName("label")
        self.act = QtWidgets.QPushButton(self.vip_tab1)
        self.act.setGeometry(QtCore.QRect(370, 210, 151, 51))
        self.act.setObjectName("act")
        self.buy = QtWidgets.QPushButton(self.vip_tab1)
        self.buy.setGeometry(QtCore.QRect(640, 140, 93, 28))
        self.buy.setObjectName("buy")
        self.vip_tabWidget.addTab(self.vip_tab1, "")
        self.vip_tab2 = QtWidgets.QWidget()
        self.vip_tab2.setObjectName("vip_tab2")
        self.QR_code = QtWidgets.QWidget(self.vip_tab2)
        self.QR_code.setGeometry(QtCore.QRect(80, 50, 231, 201))
        self.QR_code.setObjectName("QR_code")
        self.pay_count = QtWidgets.QLabel(self.vip_tab2)
        self.pay_count.setGeometry(QtCore.QRect(370, 70, 101, 16))
        self.pay_count.setObjectName("pay_count")
        self.label_8 = QtWidgets.QLabel(self.vip_tab2)
        self.label_8.setGeometry(QtCore.QRect(370, 110, 171, 16))
        self.label_8.setObjectName("label_8")
        self.vip_tabWidget.addTab(self.vip_tab2, "")
        self.gridLayout_5.addWidget(self.vip_tabWidget, 1, 0, 1, 1)
        self.vip_groupBox = QtWidgets.QGroupBox(self.button_vip)
        self.vip_groupBox.setMaximumSize(QtCore.QSize(960, 300))
        self.vip_groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.vip_groupBox.setStyleSheet("QRadioButton::indicator{width:0px;height:0px}\n"
                                        "QRadioButton:checked{background-color:#FFF7E6}\n"
                                        "QRadioButton{width:150px;height:150px;background-color:rgb(255, 255, 255);border:1px solid #B7B7B7;border-radius:8px;font-size:35px;color:#F5AE14;}")
        self.vip_groupBox.setTitle("")
        self.vip_groupBox.setObjectName("vip_groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.vip_groupBox)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vip_month = QtWidgets.QRadioButton(self.vip_groupBox)
        self.vip_month.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vip_month.setToolTipDuration(-1)
        self.vip_month.setStyleSheet("")
        self.vip_month.setChecked(True)
        self.vip_month.setObjectName("vip_month")
        self.horizontalLayout_3.addWidget(self.vip_month)
        self.vip_season = QtWidgets.QRadioButton(self.vip_groupBox)
        self.vip_season.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vip_season.setObjectName("vip_season")
        self.horizontalLayout_3.addWidget(self.vip_season)
        self.vip_half = QtWidgets.QRadioButton(self.vip_groupBox)
        self.vip_half.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vip_half.setObjectName("vip_half")
        self.horizontalLayout_3.addWidget(self.vip_half)
        self.vip_year = QtWidgets.QRadioButton(self.vip_groupBox)
        self.vip_year.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vip_year.setObjectName("vip_year")
        self.horizontalLayout_3.addWidget(self.vip_year)
        self.gridLayout_5.addWidget(self.vip_groupBox, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

    def style_sheet(self):
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.top_widget.setStyleSheet(
            "QWidget{background:#71c5ea;;border-top-left-radius:10px;border-top-right-radius:10px;}"
            "QPushButton{border:none;color:white;backgrond:red;font-size:30px;}"
            "QPushButton:hover{font-weight:1200;font-size:32px}"
            "QLabel{border-top-right-radius:0px}")
        self.logo_lb.setStyleSheet("")
        self.top_min.setStyleSheet(
            "QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green}")
        self.top_close.setStyleSheet(
            "QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red}")
        self.top_max.setStyleSheet(
            "QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}")
        self.textEdit.setStyleSheet("background:#FFF7E6")
        self.listWidget.setStyleSheet('QListWidget{border:none;border-image:url(:newPrefix/Images/download_back.png)}')

        self.button_widget.setStyleSheet(
            'QTabWidget::pane{border:0px}QWidget{background:#F5F5F5;border-bottom-right-radius:10px;border-bottom-left-radius:10px}'
            'QPushButton{border:1px solid #9db5b9;background-color:white}QPushButton:hover{background:#BDBDBD}QPushButton:pressed{background:rgb(100,100,100)}')
        # self.centralwidget.setStyleSheet('background:green;border-bottom-right-radius:10px')
        # self.setStyleSheet('background:green;border-bottom-right-radius:10px;border-bottom-left-radius:10px')
        self.button_setting.setStyleSheet(
            'QGroupBox{border:1px solid #9db5b9}QLineEdit{border:1px solid #9db5b9;border-radius:2px}QPushButton{border:1px solid #9db5b9;border-radius:2px}')
        self.top_vip.setStyleSheet('color:#FFEB3B;border-radius:0px;')
        self.dnld_bt.setStyleSheet('border-radius:10px;')
        self.top_min.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/min.png')))
        self.top_max.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/max.png')))
        self.top_close.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/close.png')))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_lb.setText(_translate("MainWindow", "Logo"))
        self.top_setting.setText(_translate("MainWindow", "设置"))
        self.top_list.setText(_translate("MainWindow", "下载列表"))
        self.top_dnld.setText(_translate("MainWindow", "下载"))
        self.top_vip.setText(_translate("MainWindow", "会员中心"))
        self.dnld_bt.setText(_translate("MainWindow", "下载"))
        self.button_widget.setTabText(self.button_widget.indexOf(self.button_dnld), _translate("MainWindow", "Tab 1"))
        self.button_widget.setTabText(self.button_widget.indexOf(self.button_list), _translate("MainWindow", "Tab 2"))
        self.groupBox_8.setTitle(_translate("MainWindow", "下载设置"))
        self.mb_ck.setText(_translate("MainWindow", "手机详情图"))
        self.pc_ck.setText(_translate("MainWindow", "电脑详情图"))
        self.vd_ck.setText(_translate("MainWindow", "视频"))
        self.label_13.setText(_translate("MainWindow", "保存位置"))
        self.file_bt.setText(_translate("MainWindow", "选择"))
        self.file_open.setText(_translate("MainWindow", "打开"))
        self.cl_ck.setText(_translate("MainWindow", "颜色及分类图"))
        self.groupBox_7.setTitle(_translate("MainWindow", "代理设置"))
        self.label_11.setText(_translate("MainWindow", "地址"))
        self.label_12.setText(_translate("MainWindow", "端口"))
        self.groupBox_9.setTitle(_translate("MainWindow", "下载更新"))
        self.update_bt.setText(_translate("MainWindow", "下载更新"))
        # self.mb_ck.setChecked(True)
        # self.cl_ck.setChecked(True)
        # self.pc_ck.setChecked(True)
        # self.vd_ck.setChecked(True)
        self.button_widget.setTabText(self.button_widget.indexOf(self.button_setting), _translate("MainWindow", "tab3"))
        self.vip_month.setText(_translate("MainWindow", "  一个月\n"
                                                        "   10元"))
        self.vip_half.setText(_translate("MainWindow", "   半年\n"
                                                       "   50元"))
        self.vip_season.setText(_translate("MainWindow", "  一季度\n"
                                                         "   28元"))
        self.vip_year.setText(_translate("MainWindow", "   一年\n"
                                                       "   96元"))
        self.label_2.setText(_translate("MainWindow", "激活码"))
        self.code_copy.setText(_translate("MainWindow", "复制"))
        self.label.setText(_translate("MainWindow", "机器码"))
        self.act.setText(_translate("MainWindow", "激活"))
        self.buy.setText(_translate("MainWindow", "购买"))
        self.vip_tabWidget.setTabText(self.vip_tabWidget.indexOf(self.vip_tab1), _translate("MainWindow", "激活码"))
        self.pay_count.setText(_translate("MainWindow", "应付金额10元"))
        self.label_8.setText(_translate("MainWindow", "请使用支付宝或微信支付"))
        self.vip_tabWidget.setTabText(self.vip_tabWidget.indexOf(self.vip_tab2), _translate("MainWindow", "扫码支付"))
        self.button_widget.setTabText(self.button_widget.indexOf(self.button_vip), _translate("MainWindow", "tab4"))

    def my_ui(self):
        self.button_widget.tabBar().hide()
        self.textEdit.setPlaceholderText('添加多个链接时，请确保每行只有一个链接')
        # self.setStyleSheet('background')
        self.button_widget.setCurrentIndex(0)
        self.top_dnld.setStyleSheet('font-weight:1200;border-bottom:6px solid #7196b1;')
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 去除窗体状态栏

    def my_action(self):
        self.top_dnld.clicked.connect(lambda: self.top_list_action(0))
        self.top_list.clicked.connect(lambda: self.top_list_action(1))
        self.top_setting.clicked.connect(lambda: self.top_list_action(2))
        self.top_vip.clicked.connect(lambda: self.top_list_action(3))
        self.top_close.clicked.connect(lambda: self.close())
        self.top_min.clicked.connect(lambda: self.showMinimized())
        self.top_max.clicked.connect(self.max_action)
        self.file_bt.clicked.connect(self.select_dir_action)
        self.file_open.clicked.connect(self.open_dir_action)
        self.dnld_bt.clicked.connect(self.dnld_bt_action)
        self.code_copy.clicked.connect(self.copy_code_action)
        self.act.clicked.connect(self.activation_action)
        self.thread_action()
        self.member_statue()

    def activation_action(self):
        activation = self.act_code.text()
        try:
            cur_time = Verify.current_time()
            text = Verify.my_decrypt(activation)
            data = text.split('-')
            mac_addr = data[0]
            end_time = int(data[1])
            date = time.localtime(end_time + 8 * 60 * 60)
            date_str = '\n至尊会员\n' + str(date.tm_year) + '-' + str(date.tm_mon) + '-' + str(date.tm_mday)
            if end_time > cur_time and mac_addr == Verify.get_mac().replace('-', ''):
                self.member_control(True, date_str)
                self.mem.writeInit('activation', activation)
                QMessageBox.information(self, '激活提示', '激活成功\n' + date_str + '到期', QMessageBox.Yes)
            else:
                QMessageBox.information(self, '激活提示', '激活失败\n1.检查激活码是否过期\n2.检查激活码是否匹配计算机', QMessageBox.Yes)
            self.act_code.clear()
        except:
            QMessageBox.information(self, '激活提示', '激活失败\n1.请检查网络是否连接\n2.请检查激活码是否完整', QMessageBox.Yes)
            self.act_code.clear()

    def member_statue(self):
        self.vip_check = VipThread(self.mem.readInit('activation'), self.mem.readInit('free'))
        self.vip_check.sign.connect(self.member_control)
        self.vip_check.start()

    def member_control(self, statue, date):
        self.label_3.setText(date)
        self.statue = statue

    def copy_code_action(self):
        QApplication.clipboard().setText(self.mec_code.text())

    def select_dir_action(self):
        dir = QFileDialog.getExistingDirectory()
        if len(dir) > 0:
            self.file_edit.setText(dir)

    def open_dir_action(self):
        dir = self.file_edit.text().replace('/','\\')
        try:
            os.system('start explorer '+dir)
        except:
            print('无该文件夹')

    def max_action(self):
        if self.isMaximized():
            self.showNormal()
            self.top_max.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/max.png')))
        else:
            self.showMaximized()
            self.top_max.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/mmax.png')))

    def top_list_action(self, msg):
        self.button_widget.setCurrentIndex(msg)
        self.top_dnld.setStyleSheet('color:white')
        self.top_list.setStyleSheet('color:white')
        self.top_setting.setStyleSheet('color:white')
        self.top_vip.setStyleSheet('color:#FFEB3B;border-radius:0px')
        if msg == 0:
            self.top_dnld.setStyleSheet('font-weight:1200;border-bottom:6px solid #7196b1')
        if msg == 1:
            self.top_list.setStyleSheet('font-weight:1200;border-bottom:6px solid #7196b1')
        if msg == 2:
            self.top_setting.setStyleSheet('font-weight:1200;border-bottom:6px solid #7196b1')
        if msg == 3:
            self.top_vip.setStyleSheet(
                'color:#FFEB3B;font-weight:1200;border-radius:0px;border-bottom:6px solid #7196b1')

    def dnld_bt_action(self):
        if not os.path.exists(self.file_edit.text()):
            QMessageBox.warning(self, '警告','请选择正确的保存路径',QMessageBox.Yes)
            return
        # free = int(Verify.my_decrypt(self.mem.readInit('free')))
        free=100
        if self.statue:
            self.dl()

        elif free > 0:
            # free = free - 1
            is_run = self.dl()
            if is_run:
                self.mem.writeInit('free', Verify.my_encryption(str(free)))
                self.label_3.setText('')

        # else:
        #     re_code = QMessageBox.information(self, '会员提示', '您暂时不是会员\n现在开通', QMessageBox.Yes)
        #     if re_code == 16384:
        #         self.top_list_action(3)

    def dl(self):
        content = self.textEdit.toPlainText()
        spls = content.split('\n')
        urls = []
        setting = {}
        setting['mb'] = self.mb_ck.isChecked()
        setting['pc'] = self.pc_ck.isChecked()
        setting['vd'] = self.vd_ck.isChecked()
        setting['cl'] = self.cl_ck.isChecked()
        setting['path'] = self.file_edit.text()
        # setting['ip'] = self.ip_edit.text()
        # setting['port'] = self.port_edit.text()
        for sp in spls:
            sp = sp.strip()
            if len(sp) > 5:
                urls.append(sp)
        for url in urls:
            self.item_items.append(self.add_item())
            download_list.append((url, setting))
        if len(download_list) > 0:
            self.listWidget.setStyleSheet('border:none;border-image:none')
            self.td1.start()
            self.td2.start()
            self.td3.start()
            # QMessageBox.information(self, '下载提示','正在下载',QMessageBox.Yes)
            self.textEdit.clear()
            infoBox = QMessageBox()  ##Message Box that doesn't run
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("正在下载")
            infoBox.setWindowTitle("Information")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.button(QMessageBox.Ok).animateClick(1 * 500)  # 3秒自动关闭
            infoBox.exec_()
            return True
        return False

    m_flag = False  # 窗口拖动管理初始化

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.y() < self.top_widget.height():
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if self.m_flag:
            if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
                return
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def write_setting(self):
        # self.mb_ck.stateChanged.connect(lambda: mem.writeInit('config.ini', 'mb_img', self.mb_ck.checkState()))
        # self.pc_ck.stateChanged.connect(lambda: mem.writeInit('config.ini', 'pc_img', self.pc_ck.checkState()))
        # self.cl_ck.stateChanged.connect(lambda: mem.writeInit('config.ini', 'cl_img', self.cl_ck.checkState()))
        # self.vd_ck.stateChanged.connect(lambda: mem.writeInit('config.ini', 'vd_img', self.vd_ck.checkState()))
        # self.file_edit.textChanged.connect(lambda: mem.writeInit('config.ini', 'file', self.file_edit.text()))
        # self.ip_edit.textChanged.connect(lambda: mem.writeInit('config.ini', 'ip', self.ip_edit.text()))
        # self.port_edit.textChanged.connect(lambda: mem.writeInit('config.ini', 'port', self.port_edit.text()))
        self.mb_ck.stateChanged.connect(lambda: self.mem.writeInit('mb_img', self.mb_ck.checkState()))
        self.pc_ck.stateChanged.connect(lambda: self.mem.writeInit('pc_img', self.pc_ck.checkState()))
        self.cl_ck.stateChanged.connect(lambda: self.mem.writeInit('cl_img', self.cl_ck.checkState()))
        self.vd_ck.stateChanged.connect(lambda: self.mem.writeInit('vd_img', self.vd_ck.checkState()))
        self.file_edit.textChanged.connect(lambda: self.mem.writeInit('file', self.file_edit.text()))
        self.ip_edit.textChanged.connect(lambda: self.mem.writeInit('ip', self.ip_edit.text()))
        self.port_edit.textChanged.connect(lambda: self.mem.writeInit('port', self.port_edit.text()))

    def load_setting(self):
        try:
            # self.mb_ck.setCheckState(int(mem.readInit('config.ini', 'mb_img')))
            # self.pc_ck.setCheckState(int(mem.readInit('config.ini', 'pc_img')))
            # self.cl_ck.setCheckState(int(mem.readInit('config.ini', 'cl_img')))
            # self.vd_ck.setCheckState(int(mem.readInit('config.ini', 'vd_img')))
            # self.file_edit.setText(mem.readInit('config.ini', 'file'))
            # self.ip_edit.setText(mem.readInit('config.ini', 'ip'))
            # self.port_edit.setText(mem.readInit('config.ini', 'port'))
            self.mb_ck.setCheckState(int(self.mem.readInit('mb_img')))
            self.pc_ck.setCheckState(int(self.mem.readInit('pc_img')))
            self.cl_ck.setCheckState(int(self.mem.readInit('cl_img')))
            self.vd_ck.setCheckState(int(self.mem.readInit('vd_img')))
            self.file_edit.setText(self.mem.readInit('file'))
            self.ip_edit.setText(self.mem.readInit('ip'))
            self.port_edit.setText(self.mem.readInit('port'))
        except:
            print('配置异常')

    def add_item(self):
        item = QtWidgets.QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QtCore.QSize(200, 50))  # 设置QListWidgetItem大小
        widget = self.widget_list()  # 调用上面的函数获取对应
        self.listWidget.addItem(item)  # 添加item
        self.listWidget.setItemWidget(item, widget)  # 为item设置widget
        return item

    def widget_list(self):
        widget = QtWidgets.QWidget()
        widget.setMaximumSize(QtCore.QSize(1677215, 120))
        widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        widget.setObjectName("widget")
        horizontalLayout_3 = QtWidgets.QHBoxLayout(widget)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        # horizontalLayout_3.setContentsMargins(10,3,3,3)
        title_lb = QtWidgets.QLabel(widget)
        title_lb.setText('等待下载')
        title_lb.setMaximumSize(QtCore.QSize(300, 16777215))
        title_lb.setObjectName("title_lb")
        horizontalLayout_3.addWidget(title_lb)
        progressBar = QtWidgets.QProgressBar(widget)
        progressBar.setMaximumSize(QtCore.QSize(300, 16))
        progressBar.setMinimumSize(QtCore.QSize(300, 16))
        progressBar.setProperty("value", 0)
        progressBar.setObjectName("progressBar")
        horizontalLayout_3.addWidget(progressBar)
        lb = QtWidgets.QLabel(widget)
        lb.setText('已下载--项/共--项')
        lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        lb.setObjectName("lb")
        horizontalLayout_3.addWidget(lb)
        start_bt = QtWidgets.QPushButton(widget)
        start_bt.setMaximumSize(QtCore.QSize(20, 16777215))
        start_bt.setObjectName("start_bt")
        horizontalLayout_3.addWidget(start_bt)
        delete_bt = QtWidgets.QPushButton(widget)
        delete_bt.setMaximumSize(QtCore.QSize(20, 16777215))
        delete_bt.setObjectName("delete_bt")
        horizontalLayout_3.addWidget(delete_bt)
        open_bt = QtWidgets.QPushButton(widget)
        open_bt.setMaximumSize(QtCore.QSize(20, 16777215))
        open_bt.setObjectName("open_bt")
        horizontalLayout_3.addWidget(open_bt)
        start_bt.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/stop.png')))
        delete_bt.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/close.png')))
        open_bt.setIcon(QIcon(QtGui.QPixmap(':newPrefix/Images/file.png')))
        progressBar.setStyleSheet(
            'QProgressBar::chunk{background:#71c5ea;border-radius:6px}QProgressBar{text-align: center;border:1px solid #9db5b9;border-radius:8px}')
        widget.setStyleSheet('QWidget{border-radius:0px}QPushButton:hover{background:#BDBDBD}')
        return widget

    def thread_action(self):
        self.td1.start_sign.connect(self.td1_init)
        self.td2.start_sign.connect(self.td2_init)
        self.td3.start_sign.connect(self.td3_init)

        self.td1.len_title.connect(self.td1_load)
        self.td1.pgb_value.connect(self.td1_work)
        self.td1.end_sign.connect(self.td1_end)

        self.td2.len_title.connect(self.td2_load)
        self.td2.pgb_value.connect(self.td2_work)
        self.td2.end_sign.connect(self.td2_end)

        self.td3.len_title.connect(self.td3_load)
        self.td3.pgb_value.connect(self.td3_work)
        self.td3.end_sign.connect(self.td3_end)

    def td1_init(self):
        wid_lock.lock()
        self.item1 = self.item_items[0]
        wid = self.listWidget.itemWidget(self.item1)
        del self.item_items[0]
        wid_lock.unlock()
        self.pgb1 = wid.findChild(QProgressBar, "progressBar")
        self.title_lb1 = wid.findChild(QLabel, "title_lb")
        self.lb1 = wid.findChild(QLabel, "lb")

    def td2_init(self):
        wid_lock.lock()
        self.item2 = self.item_items[0]
        wid = self.listWidget.itemWidget(self.item2)
        del self.item_items[0]
        wid_lock.unlock()
        self.pgb2 = wid.findChild(QProgressBar, "progressBar")
        self.title_lb2 = wid.findChild(QLabel, "title_lb")
        self.lb2 = wid.findChild(QLabel, "lb")

    def td3_init(self):
        wid_lock.lock()
        self.item3 = self.item_items[0]
        wid = self.listWidget.itemWidget(self.item3)
        del self.item_items[0]
        wid_lock.unlock()
        self.pgb3 = wid.findChild(QProgressBar, "progressBar")
        self.title_lb3 = wid.findChild(QLabel, "title_lb")
        self.lb3 = wid.findChild(QLabel, "lb")

    def td1_load(self, length, title):
        self.pgb1.setMaximum(length)
        self.title_lb1.setText(title)
        self.lb1.setText('已下载--项/共' + str(length) + '项')

    def td2_load(self, length, title):
        self.pgb2.setMaximum(length)
        self.title_lb2.setText(title)
        self.lb2.setText('已下载--项/共' + str(length) + '项')

    def td3_load(self, length, title):
        self.pgb3.setMaximum(length)
        self.title_lb3.setText(title)
        self.lb3.setText('已下载--项/共' + str(length) + '项')

    def td1_work(self):
        self.pgb1.setValue(self.pgb1.value() + 1)
        self.lb1.setText('已下载' + str(self.pgb1.value()) + '项/共' + str(self.pgb1.maximum()) + '项')

    def td2_work(self):
        self.pgb2.setValue(self.pgb2.value() + 1)
        self.lb2.setText('已下载' + str(self.pgb2.value()) + '项/共' + str(self.pgb2.maximum()) + '项')

    def td3_work(self):
        self.pgb3.setValue(self.pgb3.value() + 1)
        self.lb3.setText('已下载' + str(self.pgb3.value()) + '项/共' + str(self.pgb3.maximum()) + '项')

    def td1_end(self):
        self.listWidget.takeItem(self.listWidget.row(self.item1))
        if self.listWidget.count() == 0:
            self.no_work()

    def td2_end(self):
        self.listWidget.takeItem(self.listWidget.row(self.item2))
        if self.listWidget.count() == 0:
            self.no_work()

    def td3_end(self):
        self.listWidget.takeItem(self.listWidget.row(self.item3))
        if self.listWidget.count() == 0:
            self.no_work()

    def no_work(self):
        self.listWidget.setStyleSheet('QListWidget{border:none;border-image:url(:newPrefix/Images/download_back.png)}')


# class MemerySetting():
#     def __init__(self, parent=None):
#         pass
#
#     def writeInit(self, path, user_key, user_value):
#         # if path.isEmpty() or user_key.isEmpty():
#         #     return False
#         # else:
#         # 创建配置文件操作对象
#         self.config = QSettings(path, QSettings.IniFormat)
#
#         # 将信息写入配置文件
#         self.config.beginGroup("config")
#         self.config.setValue(user_key, user_value)
#         self.config.endGroup()
#         return True
#
#     def readInit(self, path, user_key):
#         user_value = ""
#         # 创建配置文件操作对象
#         self.config = QSettings(path, QSettings.IniFormat)
#         # 读取用户配置信息
#         user_value = self.config.value("config/" + user_key)
#         return user_value

class MemerySetting():
    def __init__(self, parent=None):
        self.config = QSettings('Control', 'Base')
        if self.config.contains('mb_img') is False:
            self.writeInit('mb_img', 2)
            self.writeInit('pc_img', 2)
            self.writeInit('cl_img', 2)
            self.writeInit('vd_img', 2)
            self.writeInit('vd_img', 2)
            self.writeInit('activation', '')
            self.writeInit('free', Verify.my_encryption('3'))
            try:
                path = r'D:\电商图片'
                if not os.path.exists(path):
                    os.makedirs(path)
                self.writeInit('file', path)
            except:
                pass

    def writeInit(self, user_key, user_value):
        self.config = QSettings('Control', 'Base')
        # 将信息写入配置文件
        self.config.setValue(user_key, user_value)
        return True

    def readInit(self, user_key):
        user_value = ""
        # 创建配置文件操作对象
        self.config = QSettings('Control', 'Base')
        # 读取用户配置信息
        user_value = self.config.value(user_key)
        return user_value


class Dthread(QThread):
    start_sign = QtCore.pyqtSignal()
    len_title = QtCore.pyqtSignal(int, str)
    pgb_value = QtCore.pyqtSignal()
    end_sign = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            url = ''
            try:
                url_lock.lock()
                if len(download_list) > 0:
                    self.start_sign.emit()
                    url = download_list[0][0]
                    setting = download_list[0][1]
                    del download_list[0]
                    url_lock.unlock()
                    #  去分链接是哪个平台的
                    c = ECCrawl()
                    split_url = url.split('.')
                    if split_url[1] == 'taobao' or split_url[1] == 'tmall':
                        c = Ali.TB(url)
                    elif split_url[1] == 'jd':
                        c = JD.JD(url)
                    elif split_url[1] == '1688':
                        c = Ali.Ali(url)
                    else:
                        print('链接错误')
                        return

                    path = setting['path'] + '/' + c.title + c.id
                    mbs = []
                    pcs = []
                    cls = {}
                    vds = []
                    length = 0
                    main_imgs = c.main_img()
                    length = length + len(main_imgs)
                    if setting['mb']:
                        mbs = c.mb_img()
                        length = length + len(mbs)
                    if setting['pc']:
                        pcs = c.pc_img()
                        length = length + len(pcs)
                    if setting['vd']:
                        vds = c.video()
                        length = length + len(vds)
                    if setting['cl']:
                        cls = c.color_img()
                        length = length + len(cls)
                    self.len_title.emit(length, c.title)

                    self.download(c.session, c.headers, path=path + '/主图', urls=main_imgs)

                    if setting['mb']:
                        self.download(c.session, c.headers, path=path + '/手机详情图', urls=mbs)

                    if setting['pc']:
                        self.download(c.session, c.headers, path=path + '/电脑详情图', urls=pcs)

                    if setting['vd']:
                        self.download(c.session, c.headers, path=path + '/视频', urls=vds)

                    if setting['cl']:
                        self.download(c.session, c.headers, path=path + '/颜色及分类图', urls=list(cls.values()),
                                      names=list(cls.keys()))
                    self.end_sign.emit()

                else:
                    url_lock.unlock()
                    break
            except:
                self.end_sign.emit()
                print(url+'不合法')
                if len(download_list) <= 0:
                    break

    def download(self, session, header, path='D:\你好', urls=[], names=[]):
        if len(urls) == 0:
            return
        if not os.path.exists(path):
            os.makedirs(path)
        if len(names) == 0:
            names = [str(i) for i in range(1, len(urls) + 1)]
        i = 0
        for url in urls:
            suffix = os.path.splitext(url)[1][0:4]
            name = names[i]
            img = session.get(url, headers=header)
            if int(img.headers['Content-Length']) > 1024:
                with open(path + '/' + name + suffix, 'wb') as file:
                    file.write(img.content)
                i += 1
            self.pgb_value.emit()
            time.sleep(0.1)


class VipThread(QThread):
    sign = QtCore.pyqtSignal(bool, str)

    def __init__(self, activation, free):
        super().__init__()
        self.activation = activation
        self.free = Verify.my_decrypt(free)

    def run(self):
        while True:
            try:
                pass
                # cur_time = Verify.current_time()
                # text = Verify.my_decrypt(self.activation)
                # data = text.split('-')
                # mac_addr = data[0]
                # end_time = int(data[1])
                # date = time.localtime(end_time + 8 * 60 * 60)
                # date_str = '\n至尊会员\n' + str(date.tm_year) + '-' + str(date.tm_mon) + '-' + str(date.tm_mday) + ' 到期'
                # if end_time > cur_time and mac_addr == Verify.get_mac().replace('-', ''):
                #     self.sign.emit(True, date_str)
                # else:
                #     self.sign.emit(False, '\n您暂时不是会员\n剩余体验次数:' + str(self.free))
            except:
                pass
                # self.sign.emit(False, '\n您暂时不是会员\n剩余体验次数:' + str(self.free))
            time.sleep(300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        tran=QtCore.QTranslator()
        tran.load('qt_zh_CN.qm')
        app.installTranslator(tran)
        wid=QtCore.QTranslator()
        wid.load('widgets_zh_CN.qm')
        app.installTranslator(wid)
    except:
        print('汉化文件缺失')
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
