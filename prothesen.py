import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import psycopg2
from mainwindow import Ui_MainWindow
from achtung import Ui_Dialog
import datetime


class MainWindow(QMainWindow, Ui_MainWindow):  # Mainwindow-Klasse
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


class achtung(QDialog, Ui_Dialog):  # Dialog-Klasse
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
mwindow = MainWindow()
dwindow = achtung()

dic_prothesen = {}  # Dictionary für Formulardaten
dic_typ = {}  # Dictionary für Typ zur Speicherung in PostgreSQL

status = False  # Datensatzstatus False -> Postgres Append, True -> Postgres Update


def init_dictionary():
    global k_list, dic_prothesen, dic_typ
    k_list = ["ID", "Patientennummer", "Prothesenart", "Prothesentyp", "proximal", "distal", "Seite", "Wechseleingriff",
              "Praeop_roentgen", "Postop_roentgen", "Fraktur", "Planung", "Opdatum", "Operateur", "Assistenz",
              "Op_zeiten", "Infektion", "Luxation", "Inklinationswinkel", "Trochanterabriss", "Fissuren",
              "Thrombose/Embolie",
              "Sterblichkeit", "Neurologie", "Dokumentation", "Memo", "knochenverankert", "periprothetisch",
              "Reintervention",
              "Abweichung", "CT", "ab_imp_art", "ab_imp_groesse", "ab_stab", "ab_blutung", "ab_präop", "ab_operation",
              "ab_anaesthesie", "spaet_infekt", "Einweiser"]  # Key-Liste Datenbank
    for it in k_list:
        dic_prothesen.update({it: None})
        dic_typ.update({it: 0})
    dic_typ['Prothesenart'] = 1  # in ' setzen?
    dic_typ['Prothesentyp'] = 1
    dic_typ['proximal'] = 1
    dic_typ['distal'] = 1
    dic_typ['Seite'] = 1
    dic_typ['Opdatum'] = 1
    dic_typ['Operateur'] = 1
    dic_typ['Assistenz'] = 1
    dic_typ['Memo'] = 1
    dic_typ['Einweiser'] = 1


def open_db():
    global conn, cur
    try:  # Datenbankfehler abfangen...
        conn = psycopg2.connect("dbname='prothesen2' user='postgres' password='postgres'")
        cur = conn.cursor()
    except psycopg2.OperationalError as e:
        print(e)
        sys.exit(1)
    else:
        pass


def close_db():
    try:  # Datenbankfehler abfangen...
        conn.commit()
        cur.close()
        conn.close()
    except  psycopg2.OperationalError as e:
        print(e)
        sys.exit(1)
    else:
        pass


def change_patientennummer():
    global status
    if status:
        if mwindow.lineEdit_patientennummer.text() != mwindow.label_alt_patnummer.text():
            status = False
    if mwindow.lineEdit_patientennummer.cursorPosition() == 8 or len(mwindow.lineEdit_patientennummer.text()) == 8:
        suche_patientennummer()
    elif mwindow.pushButton_suche.text() == 'Laden...':
        mwindow.label_alt_patnummer.setText('----------')
        mwindow.label_alt_proth_art.setText('----------------')
        mwindow.label_alt_seite.setText('------')
        mwindow.label_alt_op_datum.setText('-----------')
        mwindow.pushButton_suche.setText('Suchen...')


def datensatz_laden(patnr):
    global status
    status = True
    global dic_prothesen
    suche = """SELECT "ID", "Patientennummer","Prothesenart","Prothesentyp",proximal,distal,"Seite","Wechseleingriff",\
"Praeop_roentgen","Postop_roentgen","Fraktur","Planung","Opdatum","Operateur","Assistenz","Op_zeiten","Infektion",\
"Luxation","Inklinationswinkel","Trochanterabriss","Fissuren","Thrombose/Embolie","Sterblichkeit","Neurologie",\
"Dokumentation","Memo",knochenverankert,periprothetisch,"Reintervention","Abweichung","CT",ab_imp_art,ab_imp_groesse,\
ab_stab,ab_blutung,"ab_präop",ab_operation,ab_anaesthesie,spaet_infekt,"Einweiser"\
 FROM "Prothesen" WHERE "Patientennummer" = """
    suche += patnr + ';'
    open_db()
    cur.execute(suche)
    lesen = cur.fetchone()
    pos = 0
    for it in k_list:
        dic_prothesen.update({it: lesen[pos]})  # Dictionary Formulardaten mit Datensatz aktualisieren...
        pos += 1
    close_db()
    aktualisiere_widgets()


def aktualisiere_widgets():  # Daten aus Dictionary ins Formular laden...
    mwindow.comboBox_prothesenart.setCurrentText(dic_prothesen['Prothesenart'])
    mwindow.comboBox_seite.setCurrentText(dic_prothesen['Seite'])
    mwindow.comboBox_proximal.setCurrentText(dic_prothesen['proximal'])
    mwindow.comboBox_proximal.setCurrentText(dic_prothesen['distal'])
    mwindow.checkBox_wechseleingriff.setChecked(dic_prothesen['Wechseleingriff'])
    mwindow.checkBox_praeop_roentgen.setChecked(dic_prothesen['Praeop_roentgen'])
    mwindow.checkBox_postop_roentgen.setChecked(dic_prothesen['Postop_roentgen'])
    mwindow.checkBox_fraktur.setChecked(dic_prothesen['Fraktur'])
    mwindow.checkBox_praeop_planung.setChecked(dic_prothesen['Planung'])
    ds = str(dic_prothesen['Opdatum'])  # Datums-String
    yy = int(ds[0:4])  # Zerlegung ...
    mm = int(ds[5:7])  # TODO Fehler '' abfangen?
    dd = int(ds[8:10])
    mwindow.dateEdit_opdatum.setDate(QDate(yy, mm, dd))
    mwindow.comboBox_operateur.setCurrentText(dic_prothesen['Operateur'])
    mwindow.comboBox_assistenz.setCurrentText(dic_prothesen['Assistenz'])
    mwindow.lineEdit_operationszeit.setText(str(dic_prothesen['Op_zeiten']))
    mwindow.checkBox_infektion.setChecked(dic_prothesen['Infektion'])
    mwindow.checkBox_luxation.setChecked(dic_prothesen['Luxation'])
    mwindow.lineEdit_inklinationswinkel.setText(str(dic_prothesen['Inklinationswinkel']))
    mwindow.checkBox_trochanterabriss.setChecked(dic_prothesen['Trochanterabriss'])
    mwindow.checkBox_fissur.setChecked(dic_prothesen['Fissuren'])
    mwindow.checkBox_thromboembolie.setChecked(dic_prothesen['Thrombose/Embolie'])
    mwindow.checkBox_gestorben.setChecked(dic_prothesen['Sterblichkeit'])
    mwindow.checkBox_neurologie.setChecked(dic_prothesen['Neurologie'])
    mwindow.checkBox_vollstaendig.setChecked(dic_prothesen['Dokumentation'])
    mwindow.plainTextEdit_memo.setPlainText(dic_prothesen['Memo'])
    mwindow.checkBox_knochenverankert.setChecked(dic_prothesen['knochenverankert'])
    mwindow.checkBox_periprothetisch.setChecked(dic_prothesen['periprothetisch'])
    mwindow.checkBox_reintervention.setChecked(dic_prothesen['Reintervention'])
    mwindow.checkBox_abweichung.setChecked(dic_prothesen['Abweichung'])
    mwindow.checkBox_ct.setChecked(dic_prothesen['CT'])
    mwindow.checkBox_implantation.setChecked(dic_prothesen['ab_imp_art'])
    mwindow.checkBox_implantat.setChecked(dic_prothesen['ab_imp_groesse'])
    mwindow.checkBox_stabilisatoren.setChecked(dic_prothesen['ab_stab'])
    mwindow.checkBox_blutung.setChecked(dic_prothesen['ab_blutung'])
    mwindow.checkBox_vorbereitung.setChecked(dic_prothesen['ab_präop'])
    mwindow.checkBox_operation.setChecked(dic_prothesen['ab_operation'])
    mwindow.checkBox_anaesthesie.setChecked(dic_prothesen['ab_anaesthesie'])
    mwindow.checkBox_spaetinfektion.setChecked(dic_prothesen['spaet_infekt'])
    mwindow.comboBox_einweiser.setCurrentText(dic_prothesen['Einweiser'])


def aktualisiere_dictionary():  # Daten aus Formular in das Dictionary laden...
    dic_prothesen['Patientennummer'] = mwindow.lineEdit_patientennummer.text()
    dic_prothesen['Prothesenart'] = mwindow.comboBox_prothesenart.currentText()
    dic_prothesen['Seite'] = mwindow.comboBox_seite.currentText()
    dic_prothesen['proximal'] = mwindow.comboBox_proximal.currentText()
    dic_prothesen['distal'] = mwindow.comboBox_distal.currentText()
    dic_prothesen['Wechseleingriff'] = mwindow.checkBox_wechseleingriff.isChecked()
    dic_prothesen['Praeop_roentgen'] = mwindow.checkBox_praeop_roentgen.isChecked()
    dic_prothesen['Postop_roentgen'] = mwindow.checkBox_postop_roentgen.isChecked()
    dic_prothesen['Fraktur'] = mwindow.checkBox_fraktur.isChecked()
    dic_prothesen['Planung'] = mwindow.checkBox_praeop_planung.isChecked()
    dic_prothesen['Opdatum'] = mwindow.dateEdit_opdatum.date().toString('yyyy-MM-dd')
    dic_prothesen['Operateur'] = mwindow.comboBox_operateur.currentText()
    dic_prothesen['Assistenz'] = mwindow.comboBox_assistenz.currentText()
    dic_prothesen['Op_zeiten'] = int(
        mwindow.lineEdit_operationszeit.text() if mwindow.lineEdit_operationszeit.text() != '' else '0')
    dic_prothesen['Infektion'] = mwindow.checkBox_infektion.isChecked()
    dic_prothesen['Luxation'] = mwindow.checkBox_luxation.isChecked()
    dic_prothesen['Inklinationswinkel'] = int(
        mwindow.lineEdit_inklinationswinkel.text() if mwindow.lineEdit_inklinationswinkel.text() != '' else '0')
    dic_prothesen['Trochanterabriss'] = mwindow.checkBox_trochanterabriss.isChecked()
    dic_prothesen['Fissuren'] = mwindow.checkBox_fissur.isChecked()
    dic_prothesen['Thrombose/Embolie'] = mwindow.checkBox_thromboembolie.isChecked()
    dic_prothesen['Sterblichkeit'] = mwindow.checkBox_gestorben.isChecked()
    dic_prothesen['Neurologie'] = mwindow.checkBox_neurologie.isChecked()
    dic_prothesen['Dokumentation'] = mwindow.checkBox_vollstaendig.isChecked()
    dic_prothesen['Memo'] = mwindow.plainTextEdit_memo.toPlainText()
    dic_prothesen['knochenverankert'] = mwindow.checkBox_knochenverankert.isChecked()
    dic_prothesen['periprothetisch'] = mwindow.checkBox_periprothetisch.isChecked()
    dic_prothesen['Reintervention'] = mwindow.checkBox_reintervention.isChecked()
    dic_prothesen['Abweichung'] = mwindow.checkBox_abweichung.isChecked()
    dic_prothesen['CT'] = mwindow.checkBox_ct.isChecked()
    dic_prothesen['ab_imp_art'] = mwindow.checkBox_implantation.isChecked()
    dic_prothesen['ab_imp_groesse'] = mwindow.checkBox_implantat.isChecked()
    dic_prothesen['ab_stab'] = mwindow.checkBox_stabilisatoren.isChecked()
    dic_prothesen['ab_blutung'] = mwindow.checkBox_blutung.isChecked()
    dic_prothesen['ab_präop'] = mwindow.checkBox_vorbereitung.isChecked()
    dic_prothesen['ab_operation'] = mwindow.checkBox_operation.isChecked()
    dic_prothesen['ab_anaesthesie'] = mwindow.checkBox_anaesthesie.isChecked()
    dic_prothesen['spaet_infekt'] = mwindow.checkBox_spaetinfektion.isChecked()
    dic_prothesen['Einweiser'] = mwindow.comboBox_einweiser.currentText()


def schalter_suchen_laden():  # Schalter mit 2 Funktionen Suchen / Laden
    if mwindow.pushButton_suche.text() == 'Laden...':
        patnr = mwindow.lineEdit_patientennummer.text()
        datensatz_laden(patnr)


def suche_patientennummer():
    patnr = (
        mwindow.lineEdit_patientennummer.text() if mwindow.lineEdit_patientennummer.text() != '' else '0')  # sonst Fehler bei Postgres
    suche = """SELECT "Patientennummer","Prothesenart","Seite","Opdatum" FROM "Prothesen" WHERE "Patientennummer" = """
    suche += patnr + ';'
    open_db()
    cur.execute(suche)
    lesen = cur.fetchone()
    if lesen:
        mwindow.label_alt_patnummer.setText(str(lesen[0]))
        mwindow.label_alt_proth_art.setText(str(lesen[1]))
        mwindow.label_alt_seite.setText(str(lesen[2]))
        mwindow.label_alt_op_datum.setText(str(lesen[3]))
        mwindow.pushButton_suche.setText('Laden...')
    else:
        mwindow.label_alt_patnummer.setText('----------')
        mwindow.label_alt_proth_art.setText('----------------')
        mwindow.label_alt_seite.setText('------')
        mwindow.label_alt_op_datum.setText('-----------')
        mwindow.pushButton_suche.setText('Suchen...')
    close_db()


def init_comboBox_einweiser():  # Eingabemaske Einweiser initialisieren
    mwindow.comboBox_einweiser.clear()
    open_db()
    cur.execute("""SELECT "Einweiser" FROM "Prothesen";""")
    lesen = set(cur.fetchall())  # Satz aller Einweiser (auch None!)
    einweiser = [it[0] for it in lesen if it[0] != None]  # Einweiserliste bereinigen
    for ew in sorted(einweiser):  # Einweiser laden
        mwindow.comboBox_einweiser.addItem(ew)
    close_db()
    mwindow.comboBox_einweiser.setCurrentText('')  # Eingabe leer


def change_prothesenart():  # Eingabemaske anpassen...
    if mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        mwindow.label_praeop_winkel.setVisible(False)  # präop. Winkel aus
        mwindow.lineEdit_praeop_winkel.setText('')
        mwindow.lineEdit_praeop_winkel.setVisible(False)
        mwindow.label_postop_winkel.setVisible(False)  # postop. Winkel aus
        mwindow.lineEdit_postop_winkel.setText('')
        mwindow.lineEdit_postop_winkel.setVisible(False)
        mwindow.checkBox_luxation.setVisible(True)  # Luxation an
        mwindow.checkBox_luxation.setCheckState(False)
        mwindow.label_inklinationswinkel.setVisible(True)  # Inklination an
        mwindow.lineEdit_inklinationswinkel.setVisible(True)
        mwindow.checkBox_trochanterabriss.setVisible(True)  # Trochanterabriss an
    elif mwindow.comboBox_prothesenart.currentText() == 'Knie':
        mwindow.label_praeop_winkel.setVisible(True)  # präop. Winkel an
        mwindow.lineEdit_praeop_winkel.setVisible(True)
        mwindow.label_postop_winkel.setVisible(True)  # postop. Winkel an
        mwindow.lineEdit_postop_winkel.setVisible(True)
        mwindow.lineEdit_inklinationswinkel.setText('')  # Inklination aus
        mwindow.lineEdit_inklinationswinkel.setVisible(False)
        mwindow.label_inklinationswinkel.setVisible(False)
        mwindow.checkBox_luxation.setVisible(False)  # Luxation aus
        mwindow.checkBox_luxation.setCheckState(False)
        mwindow.checkBox_trochanterabriss.setVisible(False)  # Trochanterabriss aus
        mwindow.checkBox_trochanterabriss.setCheckState(False)
    else:  # Schulter- und Radiusköpchenprothese
        mwindow.label_praeop_winkel.setVisible(False)  # präop. Winkel aus
        mwindow.lineEdit_praeop_winkel.setText('')
        mwindow.lineEdit_praeop_winkel.setVisible(False)
        mwindow.label_postop_winkel.setVisible(False)  # postop. Winkel aus
        mwindow.lineEdit_postop_winkel.setText('')
        mwindow.lineEdit_postop_winkel.setVisible(False)
        mwindow.label_inklinationswinkel.setVisible(False)  # Inklination aus
        mwindow.lineEdit_inklinationswinkel.setText('')
        mwindow.lineEdit_inklinationswinkel.setVisible(False)
        mwindow.checkBox_luxation.setVisible(True)  # Luxation an
        mwindow.checkBox_trochanterabriss.setVisible(False)  # Trochanterabriss aus
        mwindow.checkBox_trochanterabriss.setCheckState(False)
    init_comboBox_proximal()
    init_comboBox_distal()


def change_abweichung():  # Abweichung an und aus
    wglist = (  # Elemente der Eingabemaske in Liste laden
        mwindow.checkBox_vorbereitung,
        mwindow.checkBox_blutung,
        mwindow.checkBox_implantation,
        mwindow.checkBox_operation,
        mwindow.checkBox_implantat,
        mwindow.checkBox_stabilisatoren,
        mwindow.checkBox_anaesthesie)
    if mwindow.checkBox_abweichung.isChecked() == True:  # Eingabemaske für Abweichungen...
        for wg in wglist:  # einschalten
            wg.setVisible(True)
        mwindow.groupBox_abweichung.setVisible(True)
    else:
        for wg in wglist:  # ausschalten
            wg.setVisible(False)
            wg.setCheckState(False)
        mwindow.groupBox_abweichung.setVisible(False)


def change_wechseleingriff():  # Änderung Wechseleingriff -> knochenverankert?
    if mwindow.checkBox_wechseleingriff.isChecked() == True:
        mwindow.checkBox_knochenverankert.setVisible(True)  # Checkbox knochenverankert ein-
    else:
        mwindow.checkBox_knochenverankert.setVisible(False)  # und ausschalten / löschen
        mwindow.checkBox_knochenverankert.setCheckState(False)


def init_lineEdit_patientennummer():  # Patientennummer initialisieren
    mwindow.lineEdit_patientennummer.setText('48000000')  # Maske vorbelegen
    mwindow.lineEdit_patientennummer.setCursorPosition(2)  # Cursor auf 3. Position


def init_comboBox_seite():  # Seitenangabe ...
    mwindow.comboBox_seite.clear()
    mwindow.comboBox_seite.addItem('rechts')
    mwindow.comboBox_seite.addItem('links')


def init_comboBox_prothesenart():  # Prothesenart ...
    mwindow.comboBox_prothesenart.clear()
    mwindow.comboBox_prothesenart.addItem('Hüfte')
    mwindow.comboBox_prothesenart.addItem('Knie')
    mwindow.comboBox_prothesenart.addItem('Schulter')
    mwindow.comboBox_prothesenart.addItem('Radiusköpfchen')


def init_comboBox_proximal():  # Eingabemasken Implantate proximal und distal
    mwindow.comboBox_proximal.clear()  # Masken löschen und füllen...
    if mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        for it in (
                "Ecofit-Pfanne",
                "Pyramid-Pfanne",
                "Link-Pfanne",
                "Duokopf",
                "Schraubpfanne",
                "zementierte Pfanne",
                "sonstiges"):
            mwindow.comboBox_proximal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Knie':
        for it in (
                "3D Knie Femur",
                "PS Knie Femur",
                "Scharnierknie Femur",
                "Rotationsknie Femur",
                "Allergie-Knie Femur",
                "sonstiges"):
            mwindow.comboBox_proximal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Schulter':
        for it in (
                "inverse Schulter Glenoidkomponente",
                "Glenoidkomponente",
                "sonstiges"):
            mwindow.comboBox_proximal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Radiusköpfchen':
        for it in ("",
                   "sonstiges"):
            mwindow.comboBox_proximal.addItem(it)


def init_comboBox_distal():
    mwindow.comboBox_distal.clear()
    if mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        for it in (
                "Ecofit-Schaft",
                "Pyramid-Schaft",
                "Actinia-Schaft",
                "CFP-Schaft",
                "zementierter Link-Schaft",
                "Icon-Oberflächenersatz",
                "Icon-Schaft zementfrei",
                "sonstiges"):
            mwindow.comboBox_distal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Knie':
        for it in (
                "3D Knie Tibia",
                "3D Knie Tibia mit Stem",
                "Scharnierknie Tibia",
                "Rotationsknie Tibia",
                "Allergie-Knie Tibia",
                "sonstiges"):
            mwindow.comboBox_distal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Schulter':
        for it in (
                "inverse Schulter Schaftkomponente",
                "Oberflächenersatz Humeruskopf",
                "sonstiges"):
            mwindow.comboBox_distal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Radiusköpfchen':
        for it in (
                "Radiusköpfchen Link",
                "sonstiges"):
            mwindow.comboBox_distal.addItem(it)


def init_dateEdit_opdatum():
    mwindow.dateEdit_opdatum.setMinimumDate(QDate(2018, 1, 1))
    mwindow.dateEdit_opdatum.setMaximumDate(QDate(2020, 12, 31))


def init_comboBox_operateur():  # Eingabemaske Operateur initialisieren
    mwindow.comboBox_operateur.clear()
    mwindow.comboBox_assistenz.clear()
    open_db()
    cur.execute("""SELECT "Operateur" FROM "Prothesen";""")
    lesen = set(cur.fetchall())  # Satz aller Operateure (auch None!)
    operateur = [it[0] for it in lesen if it[0] != None]  # Operateurliste bereinigen
    for op in sorted(operateur):  # Einweiser laden
        mwindow.comboBox_operateur.addItem(op)
        mwindow.comboBox_assistenz.addItem(op)
    close_db()
    mwindow.comboBox_operateur.setCurrentText('Joker')  # Eingabe vorbelegen
    mwindow.comboBox_assistenz.setCurrentText('Joker')


def change_operateur():
    if test_operateur(mwindow.comboBox_operateur.currentText(), mwindow.comboBox_assistenz.currentText()) == False:
        dwindow.exec()  # Fenster Eingabefehler
        mwindow.comboBox_operateur.setCurrentText('Joker')


def change_assistenz():
    if test_operateur(mwindow.comboBox_operateur.currentText(), mwindow.comboBox_assistenz.currentText()) == False:
        dwindow.exec()  # Fenster Eingabefehler
        mwindow.comboBox_assistenz.setCurrentText('Joker')


def test_operateur(operateur1, operateur2):  # Test der Eingabe Operateur & Assistenz
    if operateur1 == 'Joker' and operateur2 == 'Joker':
        return True
    elif operateur1 == '' and operateur2 == '':
        return True
    elif operateur1 == operateur2:
        return False
    else:
        return True


def change_opzeit():
    opzeit = int(
        mwindow.lineEdit_operationszeit.text() if mwindow.lineEdit_operationszeit.text() != '' else '0')  # '' abfangen!
    if opzeit > 100 and mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        mwindow.label_zeit_achtung.setVisible(True)
    elif opzeit > 120 and mwindow.comboBox_prothesenart.currentText() == 'Knie':
        mwindow.label_zeit_achtung.setVisible(True)
    else:
        mwindow.label_zeit_achtung.setVisible(False)


def change_inklination():
    inklination = int(
        mwindow.lineEdit_inklinationswinkel.text() if mwindow.lineEdit_inklinationswinkel.text() != '' else '0')  # '' abfangen!
    if inklination > 50 and mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        mwindow.label_inklination_achtung.setVisible(True)
    else:
        mwindow.label_inklination_achtung.setVisible(False)


def set_start_default():  # alle Eingaben auf Standard stellen...
    mwindow.pushButton_suche.setText('Suchen...')  # Schalter zurückstellen, sonst Datensatzsuche!
    global status
    status = False  # Datensatzstatus zurücksetzen
    for it in lineEditState.keys():
        it.setText(lineEditState[it])
    for it in checkBoxState:
        it.setCheckState(checkBoxState[it])


def save_state():  # Status der Widgets in Dictionaries speichern
    lineEdits = mwindow.findChildren(QLineEdit)
    global lineEditState
    lineEditState = {}
    for it in lineEdits:
        lineEditState.update({it: it.text()})
    global checkBoxState
    checkBoxState = {}
    checkBoxes = mwindow.findChildren(QCheckBox)
    for it in checkBoxes:
        checkBoxState.update({it: it.checkState()})


def datensatz_speichern():
    global status, dic_prothesen, k_list
    idnr = str(dic_prothesen['ID'])
    if status:  # Update
        schreiben = """UPDATE "Prothesen" SET ("Patientennummer","Prothesenart","Prothesentyp",proximal,distal,"Seite","Wechseleingriff",\
"Praeop_roentgen","Postop_roentgen","Fraktur","Planung","Opdatum","Operateur","Assistenz","Op_zeiten","Infektion",\
"Luxation","Inklinationswinkel","Trochanterabriss","Fissuren","Thrombose/Embolie","Sterblichkeit","Neurologie",\
"Dokumentation","Memo",knochenverankert,periprothetisch,"Reintervention","Abweichung","CT",ab_imp_art,ab_imp_groesse,\
ab_stab,ab_blutung,"ab_präop",ab_operation,ab_anaesthesie,spaet_infekt,"Einweiser")\
 = ("""
        pos = 0
        for it in k_list:
            if it != 'ID':  # Postgres-Update ohne 'ID'
                schreiben += ("'" + str(dic_prothesen[it]) + "'") if dic_typ[it] != 0 else str(dic_prothesen[it])  # '?
                schreiben += ',' if it != 'Einweiser' else ''  # letztes Feld?
        schreiben += """) WHERE "ID" = """
        schreiben += str(idnr) + ';'
        print(schreiben)
        open_db()
        cur.execute(schreiben)
        close_db()
    else:  # Insert
        schreiben = """INSERT INTO "Prothesen" ("Patientennummer","Prothesenart","Prothesentyp",proximal,distal,"Seite","Wechseleingriff",\
"Praeop_roentgen","Postop_roentgen","Fraktur","Planung","Opdatum","Operateur","Assistenz","Op_zeiten","Infektion",\
"Luxation","Inklinationswinkel","Trochanterabriss","Fissuren","Thrombose/Embolie","Sterblichkeit","Neurologie",\
"Dokumentation","Memo",knochenverankert,periprothetisch,"Reintervention","Abweichung","CT",ab_imp_art,ab_imp_groesse,\
ab_stab,ab_blutung,"ab_präop",ab_operation,ab_anaesthesie,spaet_infekt,"Einweiser")\
 VALUES ("""
        pos = 0
        for it in k_list:
            if it != 'ID':  # Postgres-Insert ohne 'ID'
                schreiben += ("'" + str(dic_prothesen[it]) + "'") if dic_typ[it] != 0 else str(dic_prothesen[it])  # '?
                schreiben += ',' if it != 'Einweiser' else ''  # letztes Feld?
        schreiben += """);"""
        print(schreiben)
        open_db()
        cur.execute(schreiben)
        close_db()
    status = False


def speichern():
    # TODO prüfen...
    aktualisiere_dictionary()
    datensatz_speichern()
    set_start_default()
    init_neuesFormular()


def init_neuesFormular():  # neues Formular initialisieren
    init_dictionary()
    init_lineEdit_patientennummer()
    init_comboBox_prothesenart()
    change_prothesenart()
    change_wechseleingriff()
    init_comboBox_seite()
    init_comboBox_proximal()
    init_comboBox_distal()
    init_dateEdit_opdatum()
    change_abweichung()
    init_comboBox_operateur()
    init_comboBox_einweiser()
    mwindow.label_zeit_achtung.setVisible(False)
    mwindow.label_inklination_achtung.setVisible(False)


# Ereignisse mit Funktionen verbinden...
mwindow.checkBox_wechseleingriff.stateChanged.connect(change_wechseleingriff)  # Ereignis Wechseleingriff an / aus
mwindow.checkBox_abweichung.stateChanged.connect(change_abweichung)  # Ereignis Abweichung an / aus
mwindow.pushButton_suche.clicked.connect(schalter_suchen_laden)  # Ereignis Taste Suchen/Laden gedrückt
mwindow.comboBox_operateur.currentTextChanged.connect(change_operateur)  # Ereignis Wechsel Operateur
mwindow.comboBox_assistenz.currentTextChanged.connect(change_assistenz)  # Ereignis Wechsel Assistenz
mwindow.pushButton_speichern.pressed.connect(speichern)  # Ereignis Taste Speichern gedrückt
mwindow.comboBox_prothesenart.currentTextChanged.connect(change_prothesenart)  # Ereignis Wechsel Prothesenart
mwindow.lineEdit_patientennummer.textChanged.connect(change_patientennummer)  # Ereignis Änderung Patientennummer
mwindow.lineEdit_operationszeit.textChanged.connect(change_opzeit)
mwindow.lineEdit_inklinationswinkel.textChanged.connect(change_inklination)
init_neuesFormular()  # Aufruf neues Formular
save_state()  # als Standard speichern
mwindow.show()  # Fenster anzeigen
sys.exit(app.exec_())  # Fenster mit Beenden des Programmes schließen
