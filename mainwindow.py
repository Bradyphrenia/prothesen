# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1225, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1225, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1225, 800))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_suche = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_suche.setGeometry(QtCore.QRect(316, 73, 101, 40))
        self.pushButton_suche.setObjectName("pushButton_suche")
        self.label_patientennummer = QtWidgets.QLabel(self.centralwidget)
        self.label_patientennummer.setGeometry(QtCore.QRect(60, 80, 111, 16))
        self.label_patientennummer.setObjectName("label_patientennummer")
        self.lineEdit_patientennummer = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_patientennummer.setGeometry(QtCore.QRect(180, 80, 81, 21))
        self.lineEdit_patientennummer.setText("")
        self.lineEdit_patientennummer.setCursorPosition(3)
        self.lineEdit_patientennummer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_patientennummer.setPlaceholderText("")
        self.lineEdit_patientennummer.setClearButtonEnabled(False)
        self.lineEdit_patientennummer.setObjectName("lineEdit_patientennummer")
        self.checkBox_wechseleingriff = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_wechseleingriff.setGeometry(QtCore.QRect(60, 160, 141, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_wechseleingriff.sizePolicy().hasHeightForWidth())
        self.checkBox_wechseleingriff.setSizePolicy(sizePolicy)
        self.checkBox_wechseleingriff.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_wechseleingriff.setAccessibleName("")
        self.checkBox_wechseleingriff.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_wechseleingriff.setObjectName("checkBox_wechseleingriff")
        self.label_art_der_prothese = QtWidgets.QLabel(self.centralwidget)
        self.label_art_der_prothese.setGeometry(QtCore.QRect(70, 120, 111, 16))
        self.label_art_der_prothese.setObjectName("label_art_der_prothese")
        self.label_seite = QtWidgets.QLabel(self.centralwidget)
        self.label_seite.setGeometry(QtCore.QRect(130, 190, 41, 16))
        self.label_seite.setObjectName("label_seite")
        self.label_proximal = QtWidgets.QLabel(self.centralwidget)
        self.label_proximal.setGeometry(QtCore.QRect(110, 220, 60, 16))
        self.label_proximal.setObjectName("label_proximal")
        self.label_distal = QtWidgets.QLabel(self.centralwidget)
        self.label_distal.setGeometry(QtCore.QRect(130, 250, 41, 16))
        self.label_distal.setObjectName("label_distal")
        self.checkBox_praeop_planung = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_praeop_planung.setGeometry(QtCore.QRect(76, 280, 121, 20))
        self.checkBox_praeop_planung.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_praeop_planung.setChecked(True)
        self.checkBox_praeop_planung.setObjectName("checkBox_praeop_planung")
        self.checkBox_fraktur = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_fraktur.setGeometry(QtCore.QRect(110, 310, 87, 20))
        self.checkBox_fraktur.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_fraktur.setObjectName("checkBox_fraktur")
        self.checkBox_praeop_roentgen = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_praeop_roentgen.setGeometry(QtCore.QRect(76, 340, 121, 20))
        self.checkBox_praeop_roentgen.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_praeop_roentgen.setChecked(True)
        self.checkBox_praeop_roentgen.setObjectName("checkBox_praeop_roentgen")
        self.checkBox_ct = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ct.setGeometry(QtCore.QRect(110, 370, 87, 20))
        self.checkBox_ct.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_ct.setObjectName("checkBox_ct")
        self.checkBox_postop_roentgen = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_postop_roentgen.setGeometry(QtCore.QRect(66, 400, 131, 20))
        self.checkBox_postop_roentgen.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_postop_roentgen.setChecked(True)
        self.checkBox_postop_roentgen.setObjectName("checkBox_postop_roentgen")
        self.label_opdatum = QtWidgets.QLabel(self.centralwidget)
        self.label_opdatum.setGeometry(QtCore.QRect(70, 430, 111, 20))
        self.label_opdatum.setObjectName("label_opdatum")
        self.label_operateur = QtWidgets.QLabel(self.centralwidget)
        self.label_operateur.setGeometry(QtCore.QRect(110, 460, 71, 20))
        self.label_operateur.setObjectName("label_operateur")
        self.label_assistenz = QtWidgets.QLabel(self.centralwidget)
        self.label_assistenz.setGeometry(QtCore.QRect(110, 490, 71, 20))
        self.label_assistenz.setObjectName("label_assistenz")
        self.label_opzeit = QtWidgets.QLabel(self.centralwidget)
        self.label_opzeit.setGeometry(QtCore.QRect(86, 520, 91, 20))
        self.label_opzeit.setObjectName("label_opzeit")
        self.lineEdit_operationszeit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_operationszeit.setGeometry(QtCore.QRect(194, 520, 31, 21))
        self.lineEdit_operationszeit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_operationszeit.setObjectName("lineEdit_operationszeit")
        self.label_inklinationswinkel = QtWidgets.QLabel(self.centralwidget)
        self.label_inklinationswinkel.setGeometry(QtCore.QRect(266, 370, 111, 20))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_inklinationswinkel.setFont(font)
        self.label_inklinationswinkel.setObjectName("label_inklinationswinkel")
        self.lineEdit_inklinationswinkel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inklinationswinkel.setGeometry(QtCore.QRect(386, 370, 31, 21))
        self.lineEdit_inklinationswinkel.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_inklinationswinkel.setPlaceholderText("")
        self.lineEdit_inklinationswinkel.setObjectName("lineEdit_inklinationswinkel")
        self.checkBox_vollstaendig = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_vollstaendig.setGeometry(QtCore.QRect(40, 731, 161, 20))
        self.checkBox_vollstaendig.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_vollstaendig.setObjectName("checkBox_vollstaendig")
        self.checkBox_reintervention = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_reintervention.setGeometry(QtCore.QRect(430, 80, 341, 20))
        self.checkBox_reintervention.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_reintervention.setObjectName("checkBox_reintervention")
        self.checkBox_abweichung = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_abweichung.setGeometry(QtCore.QRect(660, 120, 111, 20))
        self.checkBox_abweichung.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_abweichung.setObjectName("checkBox_abweichung")
        self.plainTextEdit_memo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_memo.setGeometry(QtCore.QRect(438, 340, 341, 151))
        self.plainTextEdit_memo.setObjectName("plainTextEdit_memo")
        self.comboBox_seite = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_seite.setGeometry(QtCore.QRect(176, 190, 111, 26))
        self.comboBox_seite.setEditable(False)
        self.comboBox_seite.setMaxVisibleItems(2)
        self.comboBox_seite.setMaxCount(2)
        self.comboBox_seite.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_seite.setObjectName("comboBox_seite")
        self.comboBox_proximal = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_proximal.setGeometry(QtCore.QRect(179, 220, 241, 26))
        self.comboBox_proximal.setObjectName("comboBox_proximal")
        self.comboBox_distal = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_distal.setGeometry(QtCore.QRect(179, 250, 241, 26))
        self.comboBox_distal.setObjectName("comboBox_distal")
        self.comboBox_prothesenart = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_prothesenart.setGeometry(QtCore.QRect(179, 120, 241, 26))
        self.comboBox_prothesenart.setObjectName("comboBox_prothesenart")
        self.comboBox_operateur = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_operateur.setGeometry(QtCore.QRect(189, 460, 231, 26))
        self.comboBox_operateur.setObjectName("comboBox_operateur")
        self.comboBox_assistenz = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_assistenz.setGeometry(QtCore.QRect(189, 490, 231, 26))
        self.comboBox_assistenz.setObjectName("comboBox_assistenz")
        self.label_copyright = QtWidgets.QLabel(self.centralwidget)
        self.label_copyright.setGeometry(QtCore.QRect(1080, 710, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_copyright.setFont(font)
        self.label_copyright.setObjectName("label_copyright")
        self.comboBox_einweiser = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_einweiser.setGeometry(QtCore.QRect(544, 310, 231, 26))
        self.comboBox_einweiser.setEditable(True)
        self.comboBox_einweiser.setObjectName("comboBox_einweiser")
        self.label_einweiser = QtWidgets.QLabel(self.centralwidget)
        self.label_einweiser.setGeometry(QtCore.QRect(436, 311, 71, 16))
        self.label_einweiser.setObjectName("label_einweiser")
        self.checkBox_vierundzwanzig = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_vierundzwanzig.setGeometry(QtCore.QRect(300, 430, 61, 20))
        self.checkBox_vierundzwanzig.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_vierundzwanzig.setObjectName("checkBox_vierundzwanzig")
        self.lineEdit_postop_winkel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_postop_winkel.setGeometry(QtCore.QRect(376, 400, 41, 21))
        self.lineEdit_postop_winkel.setFrame(True)
        self.lineEdit_postop_winkel.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_postop_winkel.setObjectName("lineEdit_postop_winkel")
        self.label_postop_winkel = QtWidgets.QLabel(self.centralwidget)
        self.label_postop_winkel.setGeometry(QtCore.QRect(266, 400, 101, 20))
        self.label_postop_winkel.setObjectName("label_postop_winkel")
        self.label_praeop_winkel = QtWidgets.QLabel(self.centralwidget)
        self.label_praeop_winkel.setGeometry(QtCore.QRect(266, 340, 91, 20))
        self.label_praeop_winkel.setObjectName("label_praeop_winkel")
        self.lineEdit_praeop_winkel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_praeop_winkel.setGeometry(QtCore.QRect(376, 340, 41, 21))
        self.lineEdit_praeop_winkel.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_praeop_winkel.setObjectName("lineEdit_praeop_winkel")
        self.checkBox_knochenverankert = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_knochenverankert.setGeometry(QtCore.QRect(272, 160, 141, 20))
        self.checkBox_knochenverankert.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_knochenverankert.setObjectName("checkBox_knochenverankert")
        self.pushButton_speichern = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_speichern.setGeometry(QtCore.QRect(588, 720, 190, 40))
        self.pushButton_speichern.setObjectName("pushButton_speichern")
        self.label_boddenkliniken = QtWidgets.QLabel(self.centralwidget)
        self.label_boddenkliniken.setGeometry(QtCore.QRect(1078, 717, 131, 51))
        self.label_boddenkliniken.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_boddenkliniken.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_boddenkliniken.setLineWidth(2)
        self.label_boddenkliniken.setText("")
        self.label_boddenkliniken.setPixmap(QtGui.QPixmap("Logomit Haus.jpg"))
        self.label_boddenkliniken.setScaledContents(True)
        self.label_boddenkliniken.setObjectName("label_boddenkliniken")
        self.label_endocert = QtWidgets.QLabel(self.centralwidget)
        self.label_endocert.setGeometry(QtCore.QRect(1023, 717, 51, 51))
        self.label_endocert.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_endocert.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_endocert.setLineWidth(2)
        self.label_endocert.setText("")
        self.label_endocert.setPixmap(QtGui.QPixmap("endocert_logozertifikat_RZ_cmyk.jpg"))
        self.label_endocert.setScaledContents(True)
        self.label_endocert.setObjectName("label_endocert")
        self.dateEdit_opdatum = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_opdatum.setGeometry(QtCore.QRect(190, 430, 110, 24))
        self.dateEdit_opdatum.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_opdatum.setCalendarPopup(True)
        self.dateEdit_opdatum.setDate(QtCore.QDate(2017, 1, 1))
        self.dateEdit_opdatum.setObjectName("dateEdit_opdatum")
        self.label_copyright_year = QtWidgets.QLabel(self.centralwidget)
        self.label_copyright_year.setGeometry(QtCore.QRect(1080, 720, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_copyright_year.setFont(font)
        self.label_copyright_year.setObjectName("label_copyright_year")
        self.groupBox_vorhanden = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_vorhanden.setGeometry(QtCore.QRect(790, 70, 421, 61))
        self.groupBox_vorhanden.setTitle("")
        self.groupBox_vorhanden.setObjectName("groupBox_vorhanden")
        self.label_patientennummer_2 = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_patientennummer_2.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label_patientennummer_2.setObjectName("label_patientennummer_2")
        self.label_art_der_prothese_2 = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_art_der_prothese_2.setGeometry(QtCore.QRect(130, 10, 104, 16))
        self.label_art_der_prothese_2.setObjectName("label_art_der_prothese_2")
        self.label_seite_2 = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_seite_2.setGeometry(QtCore.QRect(250, 10, 35, 16))
        self.label_seite_2.setObjectName("label_seite_2")
        self.label_opdatum_2 = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_opdatum_2.setGeometry(QtCore.QRect(300, 10, 109, 16))
        self.label_opdatum_2.setObjectName("label_opdatum_2")
        self.label_alt_patnummer = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_alt_patnummer.setGeometry(QtCore.QRect(10, 32, 81, 16))
        self.label_alt_patnummer.setObjectName("label_alt_patnummer")
        self.label_alt_proth_art = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_alt_proth_art.setGeometry(QtCore.QRect(130, 32, 98, 16))
        self.label_alt_proth_art.setObjectName("label_alt_proth_art")
        self.label_alt_seite = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_alt_seite.setGeometry(QtCore.QRect(250, 32, 39, 16))
        self.label_alt_seite.setObjectName("label_alt_seite")
        self.label_alt_op_datum = QtWidgets.QLabel(self.groupBox_vorhanden)
        self.label_alt_op_datum.setGeometry(QtCore.QRect(300, 32, 71, 16))
        self.label_alt_op_datum.setObjectName("label_alt_op_datum")
        self.groupBox_abweichung = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_abweichung.setGeometry(QtCore.QRect(430, 148, 351, 161))
        self.groupBox_abweichung.setTitle("")
        self.groupBox_abweichung.setObjectName("groupBox_abweichung")
        self.checkBox_implantation = QtWidgets.QCheckBox(self.groupBox_abweichung)
        self.checkBox_implantation.setGeometry(QtCore.QRect(80, 10, 261, 20))
        self.checkBox_implantation.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_implantation.setObjectName("checkBox_implantation")
        self.checkBox_implantat = QtWidgets.QCheckBox(self.groupBox_abweichung)
        self.checkBox_implantat.setGeometry(QtCore.QRect(170, 30, 171, 20))
        self.checkBox_implantat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_implantat.setObjectName("checkBox_implantat")
        self.checkBox_stabilisatoren = QtWidgets.QCheckBox(self.groupBox_abweichung)
        self.checkBox_stabilisatoren.setGeometry(QtCore.QRect(0, 50, 341, 20))
        self.checkBox_stabilisatoren.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_stabilisatoren.setObjectName("checkBox_stabilisatoren")
        self.checkBox_blutung = QtWidgets.QCheckBox(self.groupBox_abweichung)
        self.checkBox_blutung.setGeometry(QtCore.QRect(200, 70, 141, 20))
        self.checkBox_blutung.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_blutung.setObjectName("checkBox_blutung")
        self.checkBox_vorbereitung = QtWidgets.QCheckBox(self.groupBox_abweichung)
        self.checkBox_vorbereitung.setGeometry(QtCore.QRect(150, 90, 191, 20))
        self.checkBox_vorbereitung.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_vorbereitung.setObjectName("checkBox_vorbereitung")
        self.checkBox_operation = QtWidgets.QCheckBox(self.groupBox_abweichung)
        self.checkBox_operation.setGeometry(QtCore.QRect(110, 110, 231, 20))
        self.checkBox_operation.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_operation.setObjectName("checkBox_operation")
        self.checkBox_anaesthesie = QtWidgets.QCheckBox(self.groupBox_abweichung)
        self.checkBox_anaesthesie.setGeometry(QtCore.QRect(100, 130, 241, 20))
        self.checkBox_anaesthesie.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_anaesthesie.setObjectName("checkBox_anaesthesie")
        self.groupBox_komplikation = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_komplikation.setGeometry(QtCore.QRect(10, 550, 411, 181))
        self.groupBox_komplikation.setTitle("")
        self.groupBox_komplikation.setCheckable(False)
        self.groupBox_komplikation.setObjectName("groupBox_komplikation")
        self.checkBox_neunzig = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_neunzig.setGeometry(QtCore.QRect(310, 10, 91, 20))
        self.checkBox_neunzig.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_neunzig.setObjectName("checkBox_neunzig")
        self.checkBox_infektion = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_infektion.setGeometry(QtCore.QRect(103, 10, 87, 20))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.checkBox_infektion.setFont(font)
        self.checkBox_infektion.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_infektion.setObjectName("checkBox_infektion")
        self.checkBox_spaetinfektion = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_spaetinfektion.setGeometry(QtCore.QRect(79, 30, 111, 20))
        self.checkBox_spaetinfektion.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_spaetinfektion.setObjectName("checkBox_spaetinfektion")
        self.checkBox_luxation = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_luxation.setGeometry(QtCore.QRect(103, 50, 87, 20))
        self.checkBox_luxation.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_luxation.setTristate(False)
        self.checkBox_luxation.setObjectName("checkBox_luxation")
        self.checkBox_trochanterabriss = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_trochanterabriss.setGeometry(QtCore.QRect(59, 70, 131, 20))
        self.checkBox_trochanterabriss.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_trochanterabriss.setObjectName("checkBox_trochanterabriss")
        self.checkBox_fissur = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_fissur.setGeometry(QtCore.QRect(103, 90, 87, 20))
        self.checkBox_fissur.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_fissur.setObjectName("checkBox_fissur")
        self.checkBox_thromboembolie = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_thromboembolie.setGeometry(QtCore.QRect(29, 110, 161, 20))
        self.checkBox_thromboembolie.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_thromboembolie.setObjectName("checkBox_thromboembolie")
        self.checkBox_neurologie = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_neurologie.setGeometry(QtCore.QRect(0, 130, 191, 20))
        self.checkBox_neurologie.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_neurologie.setObjectName("checkBox_neurologie")
        self.checkBox_gestorben = QtWidgets.QCheckBox(self.groupBox_komplikation)
        self.checkBox_gestorben.setGeometry(QtCore.QRect(104, 150, 87, 20))
        self.checkBox_gestorben.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_gestorben.setObjectName("checkBox_gestorben")
        self.checkBox_periprothetisch = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_periprothetisch.setGeometry(QtCore.QRect(294, 308, 121, 20))
        self.checkBox_periprothetisch.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_periprothetisch.setObjectName("checkBox_periprothetisch")
        self.label_zeit_achtung = QtWidgets.QLabel(self.centralwidget)
        self.label_zeit_achtung.setGeometry(QtCore.QRect(230, 520, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_zeit_achtung.setFont(font)
        self.label_zeit_achtung.setObjectName("label_zeit_achtung")
        self.label_inklination_achtung = QtWidgets.QLabel(self.centralwidget)
        self.label_inklination_achtung.setGeometry(QtCore.QRect(420, 370, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_inklination_achtung.setFont(font)
        self.label_inklination_achtung.setObjectName("label_inklination_achtung")
        self.checkBox_oak = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_oak.setGeometry(QtCore.QRect(360, 430, 51, 20))
        self.checkBox_oak.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_oak.setObjectName("checkBox_oak")
        self.plainTextEdit_statistik = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_statistik.setGeometry(QtCore.QRect(795, 150, 413, 561))
        self.plainTextEdit_statistik.setObjectName("plainTextEdit_statistik")
        self.label_boddenkliniken.raise_()
        self.pushButton_suche.raise_()
        self.label_patientennummer.raise_()
        self.lineEdit_patientennummer.raise_()
        self.checkBox_wechseleingriff.raise_()
        self.label_art_der_prothese.raise_()
        self.label_seite.raise_()
        self.label_proximal.raise_()
        self.label_distal.raise_()
        self.checkBox_praeop_planung.raise_()
        self.checkBox_fraktur.raise_()
        self.checkBox_praeop_roentgen.raise_()
        self.checkBox_ct.raise_()
        self.checkBox_postop_roentgen.raise_()
        self.label_opdatum.raise_()
        self.label_operateur.raise_()
        self.label_assistenz.raise_()
        self.label_opzeit.raise_()
        self.lineEdit_operationszeit.raise_()
        self.label_inklinationswinkel.raise_()
        self.lineEdit_inklinationswinkel.raise_()
        self.checkBox_vollstaendig.raise_()
        self.checkBox_reintervention.raise_()
        self.checkBox_abweichung.raise_()
        self.plainTextEdit_memo.raise_()
        self.comboBox_seite.raise_()
        self.comboBox_proximal.raise_()
        self.comboBox_distal.raise_()
        self.comboBox_prothesenart.raise_()
        self.comboBox_operateur.raise_()
        self.comboBox_assistenz.raise_()
        self.label_copyright.raise_()
        self.comboBox_einweiser.raise_()
        self.label_einweiser.raise_()
        self.checkBox_vierundzwanzig.raise_()
        self.lineEdit_postop_winkel.raise_()
        self.label_postop_winkel.raise_()
        self.label_praeop_winkel.raise_()
        self.lineEdit_praeop_winkel.raise_()
        self.checkBox_knochenverankert.raise_()
        self.pushButton_speichern.raise_()
        self.label_endocert.raise_()
        self.dateEdit_opdatum.raise_()
        self.label_copyright_year.raise_()
        self.groupBox_vorhanden.raise_()
        self.groupBox_abweichung.raise_()
        self.groupBox_komplikation.raise_()
        self.checkBox_periprothetisch.raise_()
        self.label_zeit_achtung.raise_()
        self.label_inklination_achtung.raise_()
        self.checkBox_oak.raise_()
        self.plainTextEdit_statistik.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_patientennummer, self.pushButton_suche)
        MainWindow.setTabOrder(self.pushButton_suche, self.comboBox_prothesenart)
        MainWindow.setTabOrder(self.comboBox_prothesenart, self.checkBox_wechseleingriff)
        MainWindow.setTabOrder(self.checkBox_wechseleingriff, self.checkBox_knochenverankert)
        MainWindow.setTabOrder(self.checkBox_knochenverankert, self.comboBox_seite)
        MainWindow.setTabOrder(self.comboBox_seite, self.comboBox_proximal)
        MainWindow.setTabOrder(self.comboBox_proximal, self.comboBox_distal)
        MainWindow.setTabOrder(self.comboBox_distal, self.checkBox_praeop_planung)
        MainWindow.setTabOrder(self.checkBox_praeop_planung, self.checkBox_fraktur)
        MainWindow.setTabOrder(self.checkBox_fraktur, self.checkBox_praeop_roentgen)
        MainWindow.setTabOrder(self.checkBox_praeop_roentgen, self.lineEdit_praeop_winkel)
        MainWindow.setTabOrder(self.lineEdit_praeop_winkel, self.checkBox_ct)
        MainWindow.setTabOrder(self.checkBox_ct, self.checkBox_postop_roentgen)
        MainWindow.setTabOrder(self.checkBox_postop_roentgen, self.dateEdit_opdatum)
        MainWindow.setTabOrder(self.dateEdit_opdatum, self.checkBox_vierundzwanzig)
        MainWindow.setTabOrder(self.checkBox_vierundzwanzig, self.comboBox_operateur)
        MainWindow.setTabOrder(self.comboBox_operateur, self.comboBox_assistenz)
        MainWindow.setTabOrder(self.comboBox_assistenz, self.lineEdit_operationszeit)
        MainWindow.setTabOrder(self.lineEdit_operationszeit, self.checkBox_infektion)
        MainWindow.setTabOrder(self.checkBox_infektion, self.checkBox_neunzig)
        MainWindow.setTabOrder(self.checkBox_neunzig, self.checkBox_spaetinfektion)
        MainWindow.setTabOrder(self.checkBox_spaetinfektion, self.checkBox_luxation)
        MainWindow.setTabOrder(self.checkBox_luxation, self.lineEdit_inklinationswinkel)
        MainWindow.setTabOrder(self.lineEdit_inklinationswinkel, self.lineEdit_postop_winkel)
        MainWindow.setTabOrder(self.lineEdit_postop_winkel, self.checkBox_trochanterabriss)
        MainWindow.setTabOrder(self.checkBox_trochanterabriss, self.checkBox_fissur)
        MainWindow.setTabOrder(self.checkBox_fissur, self.checkBox_thromboembolie)
        MainWindow.setTabOrder(self.checkBox_thromboembolie, self.checkBox_gestorben)
        MainWindow.setTabOrder(self.checkBox_gestorben, self.checkBox_neurologie)
        MainWindow.setTabOrder(self.checkBox_neurologie, self.checkBox_vollstaendig)
        MainWindow.setTabOrder(self.checkBox_vollstaendig, self.checkBox_reintervention)
        MainWindow.setTabOrder(self.checkBox_reintervention, self.checkBox_abweichung)
        MainWindow.setTabOrder(self.checkBox_abweichung, self.checkBox_implantation)
        MainWindow.setTabOrder(self.checkBox_implantation, self.checkBox_implantat)
        MainWindow.setTabOrder(self.checkBox_implantat, self.checkBox_stabilisatoren)
        MainWindow.setTabOrder(self.checkBox_stabilisatoren, self.checkBox_blutung)
        MainWindow.setTabOrder(self.checkBox_blutung, self.checkBox_vorbereitung)
        MainWindow.setTabOrder(self.checkBox_vorbereitung, self.checkBox_operation)
        MainWindow.setTabOrder(self.checkBox_operation, self.checkBox_anaesthesie)
        MainWindow.setTabOrder(self.checkBox_anaesthesie, self.comboBox_einweiser)
        MainWindow.setTabOrder(self.comboBox_einweiser, self.plainTextEdit_memo)
        MainWindow.setTabOrder(self.plainTextEdit_memo, self.pushButton_speichern)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prothesendatenbank EPZ"))
        self.pushButton_suche.setText(_translate("MainWindow", "Suchen..."))
        self.label_patientennummer.setText(_translate("MainWindow", "Patientennummer:"))
        self.lineEdit_patientennummer.setInputMask(_translate("MainWindow", "D9999999"))
        self.checkBox_wechseleingriff.setText(_translate("MainWindow", "Wechseleingriff:"))
        self.label_art_der_prothese.setText(_translate("MainWindow", "Art der Prothese:"))
        self.label_seite.setText(_translate("MainWindow", "Seite:"))
        self.label_proximal.setText(_translate("MainWindow", "proximal:"))
        self.label_distal.setText(_translate("MainWindow", "distal:"))
        self.checkBox_praeop_planung.setText(_translate("MainWindow", "präop. Planung:"))
        self.checkBox_fraktur.setText(_translate("MainWindow", "Fraktur:"))
        self.checkBox_praeop_roentgen.setText(_translate("MainWindow", "präop. Röntgen:"))
        self.checkBox_ct.setText(_translate("MainWindow", "CT:"))
        self.checkBox_postop_roentgen.setText(_translate("MainWindow", "postop. Röntgen:"))
        self.label_opdatum.setText(_translate("MainWindow", "Operationsdatum:"))
        self.label_operateur.setText(_translate("MainWindow", "Operateur:"))
        self.label_assistenz.setText(_translate("MainWindow", "Assistenz:"))
        self.label_opzeit.setText(_translate("MainWindow", "Operationszeit:"))
        self.lineEdit_operationszeit.setInputMask(_translate("MainWindow", "999"))
        self.label_inklinationswinkel.setText(_translate("MainWindow", "Inklinationswinkel:"))
        self.lineEdit_inklinationswinkel.setInputMask(_translate("MainWindow", "99"))
        self.checkBox_vollstaendig.setText(_translate("MainWindow", "Dokumentation vollst.:"))
        self.checkBox_reintervention.setText(_translate("MainWindow", "Änderung des Behandlungspfades / Reintervention:"))
        self.checkBox_abweichung.setText(_translate("MainWindow", "Abweichung:"))
        self.label_copyright.setText(_translate("MainWindow", "© Steffen Troeger"))
        self.label_einweiser.setText(_translate("MainWindow", "Einweiser:"))
        self.checkBox_vierundzwanzig.setText(_translate("MainWindow", ">24 h:"))
        self.lineEdit_postop_winkel.setInputMask(_translate("MainWindow", "#d9.9"))
        self.label_postop_winkel.setText(_translate("MainWindow", "postop. Winkel:"))
        self.label_praeop_winkel.setText(_translate("MainWindow", "präop. Winkel:"))
        self.lineEdit_praeop_winkel.setInputMask(_translate("MainWindow", "#d9.9"))
        self.checkBox_knochenverankert.setText(_translate("MainWindow", "knochenverankert:"))
        self.pushButton_speichern.setText(_translate("MainWindow", "Prüfen und Speichern..."))
        self.dateEdit_opdatum.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_copyright_year.setText(_translate("MainWindow", "2017"))
        self.label_patientennummer_2.setText(_translate("MainWindow", "Patientennummer:"))
        self.label_art_der_prothese_2.setText(_translate("MainWindow", "Art der Prothese:"))
        self.label_seite_2.setText(_translate("MainWindow", "Seite:"))
        self.label_opdatum_2.setText(_translate("MainWindow", "Operationsdatum:"))
        self.label_alt_patnummer.setText(_translate("MainWindow", "----------"))
        self.label_alt_proth_art.setText(_translate("MainWindow", "----------------"))
        self.label_alt_seite.setText(_translate("MainWindow", "------"))
        self.label_alt_op_datum.setText(_translate("MainWindow", "-----------"))
        self.checkBox_implantation.setText(_translate("MainWindow", "Implantation zementiert / zementfrei:"))
        self.checkBox_implantat.setText(_translate("MainWindow", "Implantat +/- 2 Größen:"))
        self.checkBox_stabilisatoren.setText(_translate("MainWindow", "Stabilisatoren (Stem, Inlay mit Kragen o.ä.):"))
        self.checkBox_blutung.setText(_translate("MainWindow", "vermehrte Blutung:"))
        self.checkBox_vorbereitung.setText(_translate("MainWindow", "präoperative Vorbereitung:"))
        self.checkBox_operation.setText(_translate("MainWindow", "Vorkommnisse bei der Operation:"))
        self.checkBox_anaesthesie.setText(_translate("MainWindow", "Vorkommnisse bei der Anästhesie:"))
        self.checkBox_neunzig.setText(_translate("MainWindow", "< 90 Tage:"))
        self.checkBox_infektion.setText(_translate("MainWindow", "Infektion:"))
        self.checkBox_spaetinfektion.setText(_translate("MainWindow", "Spätinfektion:"))
        self.checkBox_luxation.setText(_translate("MainWindow", "Luxation:"))
        self.checkBox_trochanterabriss.setText(_translate("MainWindow", "Trochanterabriss:"))
        self.checkBox_fissur.setText(_translate("MainWindow", "Fissur:"))
        self.checkBox_thromboembolie.setText(_translate("MainWindow", "Thrombose / Embolie:"))
        self.checkBox_neurologie.setText(_translate("MainWindow", "neurolog. Komplikationen:"))
        self.checkBox_gestorben.setText(_translate("MainWindow", "gestorben:"))
        self.checkBox_periprothetisch.setText(_translate("MainWindow", "periprothetisch"))
        self.label_zeit_achtung.setText(_translate("MainWindow", "!"))
        self.label_inklination_achtung.setText(_translate("MainWindow", "!"))
        self.checkBox_oak.setText(_translate("MainWindow", "OAK:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

