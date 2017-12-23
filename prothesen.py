import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import psycopg2
from mainwindow import Ui_MainWindow
from achtung import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):  # Mainwindow-Klasse
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


class achtung(QDialog, Ui_Dialog):  # Dialog-Klasse
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
w = MainWindow()
uwe = achtung()

dic_prothesen = {}  # Dictionary für Formulardaten

status = False  # Datensatzstatus False -> append, True -> update



def init_dictionary():
    global k_list, dic_prothesen
    k_list = ["ID", "Patientennummer", "Prothesenart", "Prothesentyp", "proximal", "distal", "Seite", "Wechseleingriff",
              "Praeop_roentgen", "Postop_roentgen", "Fraktur", "Planung", "Opdatum", "Operateur", "Assistenz",
              "Op_zeiten", "Infektion", "Luxation", "Inklinationswinkel", "Trochanterabriss", "Fissuren",
              "Thrombose/Embolie",
              "Sterblichkeit", "Neurologie", "Dokumentation", "Memo", "knochenverankert", "periprothetisch",
              "Reintervention",
              "Abweichung", "CT", "ab_imp_art", "ab_imp_groesse", "ab_stab", "ab_blutung", "ab_präop", "ab_operation",
              "ab_anaesthesie", "spaet_infekt", "Einweiser"]    # Key-Liste Datenbank
    for it in k_list:
        dic_prothesen.update({it:None})
    print (dic_prothesen)



def open_db():
    # TODO Datenbankfehler abfangen!!!
    global conn
    conn = psycopg2.connect("dbname='prothesen2' user='postgres' password='postgres'")
    global cur
    cur = conn.cursor()


def close_db():
    # TODO Datenbankfehler abfangen!!!
    conn.commit()
    cur.close()
    conn.close()


def change_patientennummer():
    global status
    if status:
        if w.lineEdit_patientennummer.text() != w.label_alt_patnummer.text():
            status = False
    if w.lineEdit_patientennummer.cursorPosition() == 8 or len(w.lineEdit_patientennummer.text()) == 8:
        suche_patientennummer()
    elif w.pushButton_suche.text() == 'Laden...':
        w.label_alt_patnummer.setText('----------')
        w.label_alt_proth_art.setText('----------------')
        w.label_alt_seite.setText('------')
        w.label_alt_op_datum.setText('-----------')
        w.pushButton_suche.setText('Suche...')


def datensatz_laden(patnr):
    global status
    status = True
    global dic_prothesen
    suche = """SELECT "ID", "Patientennummer","Prothesenart","Prothesentyp",proximal,distal,"Seite","Wechseleingriff",\
"Praeop_roentgen","Postop_roentgen","Fraktur","Planung","Opdatum","Operateur","Assistenz","Op_zeiten","Infektion",\
"Luxation","Inklinationswinkel","Trochanterabriss","Fissuren","Thrombose/Embolie","Sterblichkeit","Neurologie",\
"Dokumentation","Memo",knochenverankert,periprothetisch,"Reintervention","Abweichung","CT",ab_imp_art,ab_imp_groesse,\
ab_stab,ab_blutung,"ab_präop",ab_operation,ab_anaesthesie,spaet_infekt,"Einweiser" \
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
    w.pushButton_suche.setText('Ändern')
    w.comboBox_prothesenart.setCurrentText(dic_prothesen['Prothesenart'])
    w.comboBox_seite.setCurrentText(dic_prothesen['Seite'])
    w.comboBox_proximal.setCurrentText(dic_prothesen['proximal'])
    w.comboBox_proximal.setCurrentText(dic_prothesen['distal'])
    w.checkBox_wechseleingriff.setChecked(dic_prothesen['Wechseleingriff'])
    w.checkBox_praeop_roentgen.setChecked(dic_prothesen['Praeop_roentgen'])
    w.checkBox_postop_roentgen.setChecked(dic_prothesen['Postop_roentgen'])
    w.checkBox_fraktur.setChecked(dic_prothesen['Fraktur'])
    w.checkBox_praeop_planung.setChecked(dic_prothesen['Planung'])
    ds = str(dic_prothesen['Opdatum']) # Datums-String
    yy = int(ds[0:4])   # Zerlegung ...
    mm = int(ds[5:7])
    dd = int(ds[8:10])
    w.dateEdit_opdatum.setDate(QDate(yy, mm, dd))


# TODO hier weiter
"""

    ''Operateur'' \
    ''Assistenz',
    "Op_zeiten"" \
    ""Infektion"\
    "Luxation"\
    "Inklinationswinkel"" \
    ""Trochanterabriss"" \
    ""Fissuren"
    "Thrombose/Embolie",
    "Sterblichkeit", "Neurologie", "Dokumentation", "Memo", "knochenverankert", "periprothetisch",
    "Reintervention",
    "Abweichung", "CT", "ab_imp_art", "ab_imp_groesse", "ab_stab", "ab_blutung", "ab_präop", "ab_operation",
    "ab_anaesthesie", "spaet_infekt", "Einweiser"]
"""


def aktualisiere_dictionary():
    pass


# TODO Daten aus Formular in das Dictionary laden...


def suche_patientennummer():  # Schalter mit 2 Funktionen Suchen / Laden
    patnr = w.lineEdit_patientennummer.text()
    if w.pushButton_suche.text() == 'Laden...':
        datensatz_laden(patnr)
    if w.lineEdit_patientennummer.text() == '':
        patnr = '0'  # sonst Fehler bei Postgres
    suche = """SELECT "Patientennummer","Prothesenart","Seite","Opdatum" FROM "Prothesen" WHERE "Patientennummer" = """
    suche += patnr + ';'
    open_db()
    cur.execute(suche)
    lesen = cur.fetchone()
    if lesen:
        w.label_alt_patnummer.setText(str(lesen[0]))
        w.label_alt_proth_art.setText(str(lesen[1]))
        w.label_alt_seite.setText(str(lesen[2]))
        w.label_alt_op_datum.setText(str(lesen[3]))
        w.pushButton_suche.setText('Laden...')
    else:
        w.label_alt_patnummer.setText('----------')
        w.label_alt_proth_art.setText('----------------')
        w.label_alt_seite.setText('------')
        w.label_alt_op_datum.setText('-----------')
        w.pushButton_suche.setText('Suche...')
    close_db()


def init_comboBox_einweiser():  # Eingabemaske Einweiser initialisieren
    w.comboBox_einweiser.clear()
    open_db()
    cur.execute("""SELECT "Einweiser" FROM "Prothesen";""")
    lesen = set(cur.fetchall())  # Satz aller Einweiser (auch None!)
    einweiser = [it[0] for it in lesen if it[0] != None]  # Einweiserliste bereinigen
    for ew in sorted(einweiser):  # Einweiser laden
        w.comboBox_einweiser.addItem(ew)
    close_db()
    w.comboBox_einweiser.setCurrentText('')  # Eingabe leer


def change_prothesenart():  # Eingabemaske anpassen...
    if w.comboBox_prothesenart.currentText() == 'Hüfte':
        w.label_praeop_winkel.setVisible(False)  # präop. Winkel aus
        w.lineEdit_praeop_winkel.setText('')
        w.lineEdit_praeop_winkel.setVisible(False)

        w.label_postop_winkel.setVisible(False)  # postop. Winkel aus
        w.lineEdit_postop_winkel.setText('')
        w.lineEdit_postop_winkel.setVisible(False)

        w.checkBox_luxation.setVisible(True)  # Luxation an
        w.checkBox_luxation.setCheckState(False)

        w.label_inklinationswinkel.setVisible(True)  # Inklination an
        w.lineEdit_inklinationswinkel.setVisible(True)

        w.checkBox_trochanterabriss.setVisible(True)  # Trochanterabriss an


    elif w.comboBox_prothesenart.currentText() == 'Knie':
        w.label_praeop_winkel.setVisible(True)  # präop. Winkel an
        w.lineEdit_praeop_winkel.setVisible(True)

        w.label_postop_winkel.setVisible(True)  # postop. Winkel an
        w.lineEdit_postop_winkel.setVisible(True)

        w.lineEdit_inklinationswinkel.setText('')  # Inklination aus
        w.lineEdit_inklinationswinkel.setVisible(False)
        w.label_inklinationswinkel.setVisible(False)

        w.checkBox_luxation.setVisible(False)  # Luxation aus
        w.checkBox_luxation.setCheckState(False)

        w.checkBox_trochanterabriss.setVisible(False)  # Trochanterabriss aus
        w.checkBox_trochanterabriss.setCheckState(False)

    else:  # Schulter- und Radiusköpchenprothese
        w.label_praeop_winkel.setVisible(False)  # präop. Winkel aus
        w.lineEdit_praeop_winkel.setText('')
        w.lineEdit_praeop_winkel.setVisible(False)

        w.label_postop_winkel.setVisible(False)  # postop. Winkel aus
        w.lineEdit_postop_winkel.setText('')
        w.lineEdit_postop_winkel.setVisible(False)

        w.label_inklinationswinkel.setVisible(False)  # Inklination aus
        w.lineEdit_inklinationswinkel.setText('')
        w.lineEdit_inklinationswinkel.setVisible(False)

        w.checkBox_luxation.setVisible(True)  # Luxation an

        w.checkBox_trochanterabriss.setVisible(False)  # Trochanterabriss aus
        w.checkBox_trochanterabriss.setCheckState(False)
    init_comboBox_proximal()
    init_comboBox_distal()

def change_abweichung():  # Abweichung an und aus
    wglist = (  # Elemente der Eingabemaske in Liste laden
        w.checkBox_vorbereitung,
        w.checkBox_blutung,
        w.checkBox_implantation,
        w.checkBox_operation,
        w.checkBox_implantat,
        w.checkBox_stabilisatoren,
        w.checkBox_anaesthesie)

    if w.checkBox_abweichung.isChecked() == True:  # Eingabemaske für Abweichungen...
        for wg in wglist:  # einschalten
            wg.setVisible(True)
        w.groupBox_abweichung.setVisible(True)
    else:
        for wg in wglist:  # ausschalten
            wg.setVisible(False)
            wg.setCheckState(False)
        w.groupBox_abweichung.setVisible(False)


def change_wechseleingriff():  # Änderung Wechseleingriff -> knochenverankert?
    if w.checkBox_wechseleingriff.isChecked() == True:
        w.checkBox_knochenverankert.setVisible(True)  # Checkbox knochenverankert ein-
    else:
        w.checkBox_knochenverankert.setVisible(False)  # und ausschalten / löschen
        w.checkBox_knochenverankert.setCheckState(False)


def init_lineEdit_patientennummer():  # Patientennummer initialisieren
    w.lineEdit_patientennummer.setText('48000000')  # Maske vorbelegen
    w.lineEdit_patientennummer.setCursorPosition(2)  # Cursor auf 3. Position


def init_comboBox_seite():  # Seitenangabe ...
    w.comboBox_seite.clear()
    w.comboBox_seite.addItem('rechts')
    w.comboBox_seite.addItem('links')


def init_comboBox_prothesenart():  # Prothesenart ...
    w.comboBox_prothesenart.clear()
    w.comboBox_prothesenart.addItem('Hüfte')
    w.comboBox_prothesenart.addItem('Knie')
    w.comboBox_prothesenart.addItem('Schulter')
    w.comboBox_prothesenart.addItem('Radiusköpfchen')


def init_comboBox_proximal():  # Eingabemasken Implantate proximal und distal
    w.comboBox_proximal.clear()  # Masken löschen und füllen...
    if w.comboBox_prothesenart.currentText() == 'Hüfte':
        for it in (
                "Ecofit-Pfanne",
                "Pyramid-Pfanne",
                "Link-Pfanne",
                "Duokopf",
                "Schraubpfanne",
                "zementierte Pfanne",
                "sonstiges"):
            w.comboBox_proximal.addItem(it)
    elif w.comboBox_prothesenart.currentText() == 'Knie':
        for it in (
                "3D Knie Femur",
                "PS Knie Femur",
                "Scharnierknie Femur",
                "Rotationsknie Femur",
                "Allergie-Knie Femur",
                "sonstiges"):
            w.comboBox_proximal.addItem(it)
    elif w.comboBox_prothesenart.currentText() == 'Schulter':
        for it in (
                "inverse Schulter Glenoidkomponente",
                "Glenoidkomponente",
                "sonstiges"):
            w.comboBox_proximal.addItem(it)
    elif w.comboBox_prothesenart.currentText() == 'Radiusköpfchen':
        for it in ("",
                   "sonstiges"):
            w.comboBox_proximal.addItem(it)


def init_comboBox_distal():
    w.comboBox_distal.clear()
    if w.comboBox_prothesenart.currentText() == 'Hüfte':
        for it in (
                "Ecofit-Schaft",
                "Pyramid-Schaft",
                "Actinia-Schaft",
                "CFP-Schaft",
                "zementierter Link-Schaft",
                "Icon-Oberflächenersatz",
                "Icon-Schaft zementfrei",
                "sonstiges"):
            w.comboBox_distal.addItem(it)
    elif w.comboBox_prothesenart.currentText() == 'Knie':
        for it in (
                "3D Knie Tibia",
                "3D Knie Tibia mit Stem",
                "Scharnierknie Tibia",
                "Rotationsknie Tibia",
                "Allergie-Knie Tibia",
                "sonstiges"):
            w.comboBox_distal.addItem(it)
    elif w.comboBox_prothesenart.currentText() == 'Schulter':
        for it in (
                "inverse Schulter Schaftkomponente",
                "Oberflächenersatz Humeruskopf",
                "sonstiges"):
            w.comboBox_distal.addItem(it)
    elif w.comboBox_prothesenart.currentText() == 'Radiusköpfchen':
        for it in (
                "Radiusköpfchen Link",
                "sonstiges"):
            w.comboBox_distal.addItem(it)


def init_dateEdit_opdatum():
    # w.dateEdit_opdatum.setMinimumDate(QDate(2018, 1, 1))
    w.dateEdit_opdatum.setMaximumDate(QDate(2020, 12, 31))


def init_comboBox_operateur():  # Eingabemaske Operateur initialisieren
    w.comboBox_operateur.clear()
    w.comboBox_assistenz.clear()
    open_db()
    cur.execute("""SELECT "Operateur" FROM "Prothesen";""")
    lesen = set(cur.fetchall())  # Satz aller Operateure (auch None!)
    operateur = [it[0] for it in lesen if it[0] != None]  # Operateurliste bereinigen
    for op in sorted(operateur):  # Einweiser laden
        w.comboBox_operateur.addItem(op)
        w.comboBox_assistenz.addItem(op)
    close_db()
    w.comboBox_operateur.setCurrentText('Joker')  # Eingabe vorbelegen
    w.comboBox_assistenz.setCurrentText('Joker')


def change_operateur():
    if test_operateur(w.comboBox_operateur.currentText(), w.comboBox_assistenz.currentText()) == False:
        uwe.exec()  # Fenster Eingabefehler
        w.comboBox_operateur.setCurrentText('Joker')


def change_assistenz():
    if test_operateur(w.comboBox_operateur.currentText(), w.comboBox_assistenz.currentText()) == False:
        uwe.exec()  # Fenster Eingabefehler
        w.comboBox_assistenz.setCurrentText('Joker')


def test_operateur(op1, op2):  # Test der Eingabe Operateur & Assistenz
    if op1 == 'Joker' and op2 == 'Joker':
        return True
    elif op1 == '' and op2 == '':
        return True
    elif op1 == op2:
        return False
    else:
        return True


def set_start_default():  # alle Eingaben auf Standard stellen...
    w.pushButton_suche.setText('Suche...')  # Schalter zurückstellen, sonst Datensatzsuche!
    global status
    status = False  # Datensatzstatus zurücksetzen
    for it in lineEditState.keys():
        it.setText(lineEditState[it])
    for it in checkBoxState:
        it.setCheckState(checkBoxState[it])


def save_state():  # Status der Widgets in Dictionaries speichern
    lineEdits = w.findChildren(QLineEdit)
    global lineEditState
    lineEditState = {}
    for it in lineEdits:
        lineEditState.update({it: it.text()})
    global checkBoxState
    checkBoxState = {}
    checkBoxes = w.findChildren(QCheckBox)
    for it in checkBoxes:
        checkBoxState.update({it: it.checkState()})


def speichern():
    # TODO prüfen und speichern
    print (dic_prothesen)
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


# Ereignisse mit Funktionen verbinden...
w.checkBox_wechseleingriff.stateChanged.connect(change_wechseleingriff)  # Ereignis Wechseleingriff an / aus
w.checkBox_abweichung.stateChanged.connect(change_abweichung)  # Ereignis Abweichung an / aus
w.pushButton_suche.clicked.connect(suche_patientennummer)  # Ereignis Taste Suchen/Laden gedrückt
w.comboBox_operateur.currentTextChanged.connect(change_operateur)  # Ereignis Wechsel Operateur
w.comboBox_assistenz.currentTextChanged.connect(change_assistenz)  # Ereignis Wechsel Assistenz
w.pushButton_speichern.pressed.connect(speichern)  # Ereignis Taste Speichern gedrückt
w.comboBox_prothesenart.currentTextChanged.connect(change_prothesenart)  # Ereignis Wechsel Prothesenart
w.lineEdit_patientennummer.textChanged.connect(change_patientennummer)  # Ereignis Änderung Patientennummer

init_neuesFormular()  # Aufruf neues Formular
save_state()  # als Standard speichern

w.show()  # Fenster anzeigen
sys.exit(app.exec_())  # Fenster mit Beenden des Programmes schließen
