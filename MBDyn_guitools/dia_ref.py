# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dia_ref.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ref_dialog(object):
    def setupUi(self, ref_dialog):
        if ref_dialog.objectName():
            ref_dialog.setObjectName(u"ref_dialog")
        ref_dialog.resize(400, 500)
        self.buttonBox = QDialogButtonBox(ref_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 440, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.parent_ref_box = QComboBox(ref_dialog)
        self.parent_ref_box.setObjectName(u"parent_ref_box")
        self.parent_ref_box.setGeometry(QRect(20, 30, 111, 21))
        self.parent_ref_label = QLabel(ref_dialog)
        self.parent_ref_label.setObjectName(u"parent_ref_label")
        self.parent_ref_label.setGeometry(QRect(30, 0, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.parent_ref_label.setFont(font)
        self.vel_x = QLineEdit(ref_dialog)
        self.vel_x.setObjectName(u"vel_x")
        self.vel_x.setGeometry(QRect(30, 310, 81, 20))
        self.vel_y = QLineEdit(ref_dialog)
        self.vel_y.setObjectName(u"vel_y")
        self.vel_y.setGeometry(QRect(150, 310, 81, 20))
        self.vel_z = QLineEdit(ref_dialog)
        self.vel_z.setObjectName(u"vel_z")
        self.vel_z.setGeometry(QRect(270, 310, 81, 20))
        self.vel_x_label = QLabel(ref_dialog)
        self.vel_x_label.setObjectName(u"vel_x_label")
        self.vel_x_label.setGeometry(QRect(30, 290, 61, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.vel_x_label.setFont(font1)
        self.vel_y_label = QLabel(ref_dialog)
        self.vel_y_label.setObjectName(u"vel_y_label")
        self.vel_y_label.setGeometry(QRect(150, 290, 71, 21))
        self.vel_y_label.setFont(font1)
        self.vel_z_label = QLabel(ref_dialog)
        self.vel_z_label.setObjectName(u"vel_z_label")
        self.vel_z_label.setGeometry(QRect(270, 290, 71, 20))
        self.vel_z_label.setFont(font1)
        self.vect1_x = QLineEdit(ref_dialog)
        self.vect1_x.setObjectName(u"vect1_x")
        self.vect1_x.setGeometry(QRect(30, 190, 81, 20))
        self.vect1_y = QLineEdit(ref_dialog)
        self.vect1_y.setObjectName(u"vect1_y")
        self.vect1_y.setGeometry(QRect(150, 190, 81, 20))
        self.vect1_z = QLineEdit(ref_dialog)
        self.vect1_z.setObjectName(u"vect1_z")
        self.vect1_z.setGeometry(QRect(270, 190, 81, 20))
        self.vect2_z = QLineEdit(ref_dialog)
        self.vect2_z.setObjectName(u"vect2_z")
        self.vect2_z.setGeometry(QRect(270, 220, 81, 20))
        self.vect2_y = QLineEdit(ref_dialog)
        self.vect2_y.setObjectName(u"vect2_y")
        self.vect2_y.setGeometry(QRect(150, 220, 81, 20))
        self.vect2_x = QLineEdit(ref_dialog)
        self.vect2_x.setObjectName(u"vect2_x")
        self.vect2_x.setGeometry(QRect(30, 220, 81, 20))
        self.vect3_x = QLineEdit(ref_dialog)
        self.vect3_x.setObjectName(u"vect3_x")
        self.vect3_x.setGeometry(QRect(30, 250, 81, 20))
        self.vect3_y = QLineEdit(ref_dialog)
        self.vect3_y.setObjectName(u"vect3_y")
        self.vect3_y.setGeometry(QRect(150, 250, 81, 20))
        self.vect3_z = QLineEdit(ref_dialog)
        self.vect3_z.setObjectName(u"vect3_z")
        self.vect3_z.setGeometry(QRect(270, 250, 81, 20))
        self.pos_y = QLineEdit(ref_dialog)
        self.pos_y.setObjectName(u"pos_y")
        self.pos_y.setGeometry(QRect(150, 70, 81, 20))
        self.pos_z = QLineEdit(ref_dialog)
        self.pos_z.setObjectName(u"pos_z")
        self.pos_z.setGeometry(QRect(270, 70, 81, 20))
        self.pos_x_label = QLabel(ref_dialog)
        self.pos_x_label.setObjectName(u"pos_x_label")
        self.pos_x_label.setGeometry(QRect(30, 50, 61, 20))
        self.pos_x_label.setFont(font1)
        self.pos_z_label = QLabel(ref_dialog)
        self.pos_z_label.setObjectName(u"pos_z_label")
        self.pos_z_label.setGeometry(QRect(270, 50, 71, 20))
        self.pos_z_label.setFont(font1)
        self.pos_x = QLineEdit(ref_dialog)
        self.pos_x.setObjectName(u"pos_x")
        self.pos_x.setGeometry(QRect(30, 70, 81, 20))
        self.pos_y_label = QLabel(ref_dialog)
        self.pos_y_label.setObjectName(u"pos_y_label")
        self.pos_y_label.setGeometry(QRect(150, 50, 71, 21))
        self.pos_y_label.setFont(font1)
        self.ang_vel_y = QLineEdit(ref_dialog)
        self.ang_vel_y.setObjectName(u"ang_vel_y")
        self.ang_vel_y.setGeometry(QRect(150, 360, 81, 20))
        self.ang_vel_z = QLineEdit(ref_dialog)
        self.ang_vel_z.setObjectName(u"ang_vel_z")
        self.ang_vel_z.setGeometry(QRect(270, 360, 81, 20))
        self.ang_vel_x_label = QLabel(ref_dialog)
        self.ang_vel_x_label.setObjectName(u"ang_vel_x_label")
        self.ang_vel_x_label.setGeometry(QRect(30, 340, 81, 20))
        self.ang_vel_x_label.setFont(font1)
        self.ang_vel_z_label = QLabel(ref_dialog)
        self.ang_vel_z_label.setObjectName(u"ang_vel_z_label")
        self.ang_vel_z_label.setGeometry(QRect(270, 340, 81, 20))
        self.ang_vel_z_label.setFont(font1)
        self.ang_vel_x = QLineEdit(ref_dialog)
        self.ang_vel_x.setObjectName(u"ang_vel_x")
        self.ang_vel_x.setGeometry(QRect(30, 360, 81, 20))
        self.ang_vel_y_label = QLabel(ref_dialog)
        self.ang_vel_y_label.setObjectName(u"ang_vel_y_label")
        self.ang_vel_y_label.setGeometry(QRect(150, 340, 81, 21))
        self.ang_vel_y_label.setFont(font1)
        self.row_1_label = QLabel(ref_dialog)
        self.row_1_label.setObjectName(u"row_1_label")
        self.row_1_label.setGeometry(QRect(10, 190, 20, 20))
        self.row_1_label.setFont(font1)
        self.row_2_label = QLabel(ref_dialog)
        self.row_2_label.setObjectName(u"row_2_label")
        self.row_2_label.setGeometry(QRect(10, 220, 20, 20))
        self.row_2_label.setFont(font1)
        self.row_3_label = QLabel(ref_dialog)
        self.row_3_label.setObjectName(u"row_3_label")
        self.row_3_label.setGeometry(QRect(10, 250, 20, 20))
        self.row_3_label.setFont(font1)
        self.OM_label = QLabel(ref_dialog)
        self.OM_label.setObjectName(u"OM_label")
        self.OM_label.setGeometry(QRect(120, 160, 161, 20))
        self.OM_label.setFont(font)
        self.col_x = QLabel(ref_dialog)
        self.col_x.setObjectName(u"col_x")
        self.col_x.setGeometry(QRect(64, 170, 21, 20))
        self.col_x.setFont(font1)
        self.col_y = QLabel(ref_dialog)
        self.col_y.setObjectName(u"col_y")
        self.col_y.setGeometry(QRect(190, 170, 21, 20))
        self.col_y.setFont(font1)
        self.col_z = QLabel(ref_dialog)
        self.col_z.setObjectName(u"col_z")
        self.col_z.setGeometry(QRect(310, 170, 21, 20))
        self.col_z.setFont(font1)
        self.frame = QFrame(ref_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(5, 99, 361, 181))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(1)
        self.OM_type_label = QLabel(self.frame)
        self.OM_type_label.setObjectName(u"OM_type_label")
        self.OM_type_label.setGeometry(QRect(120, 0, 121, 31))
        self.OM_type_label.setFont(font)
        self.OM_type = QComboBox(self.frame)
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.OM_type.addItem("")
        self.OM_type.setObjectName(u"OM_type")
        self.OM_type.setGeometry(QRect(130, 30, 111, 21))
        self.frame.raise_()
        self.buttonBox.raise_()
        self.parent_ref_box.raise_()
        self.parent_ref_label.raise_()
        self.vel_x.raise_()
        self.vel_y.raise_()
        self.vel_z.raise_()
        self.vel_x_label.raise_()
        self.vel_y_label.raise_()
        self.vel_z_label.raise_()
        self.vect1_x.raise_()
        self.vect1_y.raise_()
        self.vect1_z.raise_()
        self.vect2_z.raise_()
        self.vect2_y.raise_()
        self.vect2_x.raise_()
        self.vect3_x.raise_()
        self.vect3_y.raise_()
        self.vect3_z.raise_()
        self.pos_y.raise_()
        self.pos_z.raise_()
        self.pos_x_label.raise_()
        self.pos_z_label.raise_()
        self.pos_x.raise_()
        self.pos_y_label.raise_()
        self.ang_vel_y.raise_()
        self.ang_vel_z.raise_()
        self.ang_vel_x_label.raise_()
        self.ang_vel_z_label.raise_()
        self.ang_vel_x.raise_()
        self.ang_vel_y_label.raise_()
        self.row_1_label.raise_()
        self.row_2_label.raise_()
        self.row_3_label.raise_()
        self.OM_label.raise_()
        self.col_x.raise_()
        self.col_y.raise_()
        self.col_z.raise_()

        self.retranslateUi(ref_dialog)
        self.buttonBox.accepted.connect(ref_dialog.accept)
        self.buttonBox.rejected.connect(ref_dialog.reject)

        QMetaObject.connectSlotsByName(ref_dialog)
    # setupUi

    def retranslateUi(self, ref_dialog):
        ref_dialog.setWindowTitle(QCoreApplication.translate("ref_dialog", u"Dialog", None))
        self.parent_ref_label.setText(QCoreApplication.translate("ref_dialog", u"choose reference ", None))
        self.vel_x_label.setText(QCoreApplication.translate("ref_dialog", u"x velocity", None))
        self.vel_y_label.setText(QCoreApplication.translate("ref_dialog", u"y velocity", None))
        self.vel_z_label.setText(QCoreApplication.translate("ref_dialog", u"z velocity", None))
        self.pos_x_label.setText(QCoreApplication.translate("ref_dialog", u"x position", None))
        self.pos_z_label.setText(QCoreApplication.translate("ref_dialog", u"z position", None))
        self.pos_y_label.setText(QCoreApplication.translate("ref_dialog", u"y position", None))
        self.ang_vel_x_label.setText(QCoreApplication.translate("ref_dialog", u"x angular velocity", None))
        self.ang_vel_z_label.setText(QCoreApplication.translate("ref_dialog", u"z  angular velocity", None))
        self.ang_vel_y_label.setText(QCoreApplication.translate("ref_dialog", u"y  angular velocity", None))
        self.row_1_label.setText(QCoreApplication.translate("ref_dialog", u"1", None))
        self.row_2_label.setText(QCoreApplication.translate("ref_dialog", u"2", None))
        self.row_3_label.setText(QCoreApplication.translate("ref_dialog", u"3", None))
        self.OM_label.setText(QCoreApplication.translate("ref_dialog", u"Orientation matrix input", None))
        self.col_x.setText(QCoreApplication.translate("ref_dialog", u"x", None))
        self.col_y.setText(QCoreApplication.translate("ref_dialog", u"y", None))
        self.col_z.setText(QCoreApplication.translate("ref_dialog", u"z", None))
        self.OM_type_label.setText(QCoreApplication.translate("ref_dialog", u"orientation matrix type", None))
        self.OM_type.setItemText(0, QCoreApplication.translate("ref_dialog", u"xy", None))
        self.OM_type.setItemText(1, QCoreApplication.translate("ref_dialog", u"xz", None))
        self.OM_type.setItemText(2, QCoreApplication.translate("ref_dialog", u"yz", None))
        self.OM_type.setItemText(3, QCoreApplication.translate("ref_dialog", u"matr", None))
        self.OM_type.setItemText(4, QCoreApplication.translate("ref_dialog", u"euler123", None))
        self.OM_type.setItemText(5, QCoreApplication.translate("ref_dialog", u"euler313", None))
        self.OM_type.setItemText(6, QCoreApplication.translate("ref_dialog", u"euler321", None))
        self.OM_type.setItemText(7, QCoreApplication.translate("ref_dialog", u"vector", None))

    # retranslateUi

