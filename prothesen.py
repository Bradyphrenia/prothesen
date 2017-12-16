import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

import psycopg2

app = QApplication(sys.argv)

w = loadUi('mainwindow.ui')

dic_prothesen = {}  # Dictionary für Formulardaten


def open_db():
    # Datenbankfehler abfangen!!!
    global conn
    conn = psycopg2.connect("dbname='prothesen2' user='postgres' password='postgres'")
    global cur
    cur = conn.cursor()



def close_db():
    conn.commit()
    cur.close()
    conn.close()



def suche_patientennummer():
    pass


def init_comboBox_einweiser():  # Eingabemaske Einweiser initialisieren
    open_db()
    cur.execute("""SELECT "Einweiser" FROM "Prothesen";""")
    lesen = set(cur.fetchall())  # Satz aller Einweiser (auch None!)
    einweiser = [it[0] for it in lesen if it[0] != None]  # Einweiserliste bereinigen
    for ew in sorted(einweiser):    # Einweiser laden
        w.comboBox_einweiser.addItem(ew)
    close_db()
    w.comboBox_einweiser.setCurrentText('') # Eingabe leer


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

    init_comboBox_proximal()  # beide Auswahlmasken initialisieren
    init_comboBox_distal()



def change_abweichung():  # Abweichung an und aus
    wglist = (  # Elemente der Eingabemaske in Liste laden
        w.checkBox_vorbereitung,
        w.checkBox_blutung,
        w.checkBox_implantation,
        w.checkBox_operation,
        w.checkBox_implantat,
        w.checkBox_stabilisatoren,
        w.checkBox_anaesthesie,
        w.frame)

    if w.checkBox_abweichung.isChecked() == True:  # Eingabemaske für Abweichungen...
        for wg in wglist:  # einschalten
            wg.setVisible(True)
    else:
        for wg in wglist:  # ausschalten
            wg.setVisible(False)
        for wg in wglist[:-1]:  # frame hat kein setCheckState!
            wg.setCheckState(False)



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
    w.comboBox_seite.addItem('rechts')
    w.comboBox_seite.addItem('links')



def init_comboBox_prothesenart():  # Prothesenart ...
    w.comboBox_prothesenart.addItem('Hüfte')
    w.comboBox_prothesenart.addItem('Knie')
    w.comboBox_prothesenart.addItem('Schulter')
    w.comboBox_prothesenart.addItem('Radiusköpfchen')
    w.comboBox_prothesenart.currentTextChanged.connect(change_prothesenart)  # Ereignis Wechsel Prothesenart



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



def init_neuesFormular():  # neues Formular initialisieren
    init_lineEdit_patientennummer()
    init_comboBox_prothesenart()
    change_prothesenart()
    change_wechseleingriff()
    init_comboBox_seite()
    init_comboBox_proximal()
    init_comboBox_distal()
    change_abweichung()
    init_comboBox_einweiser()



# Hauptprogramm
w.checkBox_wechseleingriff.stateChanged.connect(change_wechseleingriff)  # Ereignis Wechseleingriff an / aus
w.checkBox_abweichung.stateChanged.connect(change_abweichung)  # Ereignis Abweichung an / aus
w.pushButton_suche.clicked.connect(suche_patientennummer)  # Ereignis Button Patientensuche gedrückt
init_neuesFormular()  # Aufruf neues Formular
w.show()  # Fenster anzeigen
sys.exit(app.exec_())  # Fenster mit Beenden des Programmes schließen
