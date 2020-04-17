#  Copyright (c) 2017-2020 Steffen Troeger
import datetime
import sys

import psycopg2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from achtung import Ui_Dialog
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Mainwindow-Klasse
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


class achtung(QDialog, Ui_Dialog):  # Dialog-Klasse

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Database:
    """
    Datenbank-Klasse
    """

    def __init__(self, host, dbname, username, password):
        self.host = host
        self.dbname = dbname
        self.username = username
        self.password = password
        self.conn, self.cur = None, None

    def open_db(self):
        try:  # Datenbankfehler abfangen...
            self.conn = psycopg2.connect(
                "host=" + self.host + " dbname=" + self.dbname + " user=" + self.username + " password=" + self.password)
            self.cur = self.conn.cursor()
        except psycopg2.OperationalError as e:
            self.protocol('-- ' + str(e))
            sys.exit(1)

    def close_db(self):
        try:  # Datenbankfehler abfangen...
            self.cur.close()
            self.conn.close()
        except psycopg2.OperationalError as e:
            self.protocol('-- ' + str(e))
            sys.exit(1)

    def fetchall(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def fetchone(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def execute(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def insert(self, sql):
        self.cur.execute(sql)
        self.con.commit()
        return None

    def protocol(self, text: str):
        log = open('protokoll.log', 'a')
        log.write('-- ' + str(datetime.datetime.now()) + '\n')
        log.write(text + '\n')
        log.flush()
        log.close()


class Status:
    """
    Klasse zur Status-Speicherung
    """

    def __init__(self):
        self.__status = False  # Standard

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, stat):
        assert isinstance(stat, bool)
        self.__status = stat


def init_dictionary():
    """
    Dictionaries für Datenspeicherung initialisieren...
    :return: None
    """
    global k_list
    k_list = ["id",
              "patientennummer",
              "prothesenart",
              "prothesentyp",
              "proximal",
              "distal",
              "seite",
              "wechseleingriff",
              "praeop_roentgen",
              "postop_roentgen",
              "fraktur",
              "planung",
              "opdatum",
              "operateur",
              "assistenz",
              "op_zeiten",
              "infektion",
              "luxation",
              "inklinationswinkel",
              "trochanterabriss",
              "fissuren",
              "thrombose_embolie",
              "sterblichkeit",
              "neurologie",
              "dokumentation",
              "memo",
              "knochenverankert",
              "periprothetisch",
              "reintervention",
              "abweichung",
              "ct",
              "ab_imp_art",
              "ab_imp_groesse",
              "ab_stab",
              "ab_blutung",
              "ab_praeop",
              "ab_operation",
              "ab_anaesthesie",
              "spaet_infekt",
              "einweiser",
              "neunzig_tage",
              "kniewinkel_prae",
              "kniewinkel_post",
              "vierundzwanzig_plus",
              "oak"]
    for it in k_list:  # Key-Liste Datenbank
        dic_prothesen.update({it: None})
        dic_typ.update({it: 0})
    dic_typ['prothesenart'] = 1  # in ' setzen?
    dic_typ['prothesentyp'] = 1
    dic_typ['proximal'] = 1
    dic_typ['distal'] = 1
    dic_typ['seite'] = 1
    dic_typ['opdatum'] = 1
    dic_typ['operateur'] = 1
    dic_typ['assistenz'] = 1
    dic_typ['memo'] = 1
    dic_typ['einweiser'] = 1


def hole_statistik():
    """
    statistische Daten aus der PostgreSQL-Datenbank holen...
    :return: None
    """
    mwindow.plainTextEdit_statistik.clear()
    schreibe_statistik('Statistik aus Prothesen-Datenbank...')
    schreibe_statistik('')
    db.open_db()
    # Jahr ?
    sql = """CREATE OR REPLACE VIEW jahr AS SELECT * FROM "public"."prothesen" WHERE \
    "opdatum" >= '2020-01-01' AND "opdatum" <= '2020-12-31' AND "dokumentation" = TRUE;"""
    db.execute(sql)
    sql = """SELECT COUNT(*) FROM jahr;"""
    lesen = db.fetchone(sql)
    schreibe_statistik('Prothesen: ' + str(lesen[0]))
    sql = """SELECT COUNT(*) FROM jahr WHERE "prothesenart" = 'Hüfte'"""
    lesen = db.fetchone(sql)
    schreibe_statistik('Hüft-TEP: ' + str(lesen[0]))
    sql = """SELECT COUNT(*) FROM jahr WHERE "prothesenart" = 'Knie'"""
    lesen = db.fetchone(sql)
    schreibe_statistik('Knie-TEP: ' + str(lesen[0]))
    sql = """SELECT COUNT(*) FROM jahr WHERE "prothesenart" = 'Schulter'"""
    lesen = db.fetchone(sql)
    schreibe_statistik('Schulter-TEP: ' + str(lesen[0]))
    sql = """SELECT COUNT(*) FROM jahr WHERE "prothesenart" = 'Radiusköpfchen'"""
    lesen = db.fetchone(sql)
    schreibe_statistik('Radiusköpfchenprothesen: ' + str(lesen[0]))
    schreibe_statistik('')
    sql = """SELECT operateur, COUNT(id)  FROM jahr GROUP BY operateur;"""
    lesen = db.fetchall(sql)
    for eintrag in lesen:
        schreibe_statistik(eintrag[0] + ': ' + str(eintrag[1]))
    schreibe_statistik('')
    # Jahr ?
    sql = """CREATE OR REPLACE VIEW nicht AS SELECT * FROM  "public"."prothesen" WHERE \
    "opdatum" >= '2020-01-01' AND "opdatum" <= '2020-12-31' AND "dokumentation" = FALSE;"""
    db.execute(sql)
    sql = """SELECT COUNT(*) FROM nicht;"""
    lesen = db.fetchone(sql)
    schreibe_statistik('unvollständige Fälle: ' + str(lesen[0]))
    sql = """SELECT patientennummer from nicht"""
    lesen = db.fetchall(sql)
    for eintrag in lesen:
        schreibe_statistik('Fallnummer: ' + str(eintrag[0]))
    schreibe_statistik('')
    db.close_db()


def schreibe_statistik(text):
    """
    Ausgabe der statistischen Daten...
    :param text: Text
    :return: None
    """
    mwindow.plainTextEdit_statistik.appendPlainText(text)


def change_patientennummer():
    """
    Änderung des Eingabefeldes Patientennummer...
    :return: None
    """
    hole_statistik()  # Statistikfeld zurücksetzen
    if ButtonStatus.status or EPRD_Status.status:  # erster Aufruf nach gefundenem Datensatz?
        EPRD_Status.status = False
        reset_Formular()  # Formular bereinigen
    if mwindow.lineEdit_patientennummer.cursorPosition() == 8 and len(mwindow.lineEdit_patientennummer.text()) == 8:
        suche_patientennummer()
        suche_eprd()
    else:  # Zurücksetzen des Anzeigefeldes...
        mwindow.label_alt_patnummer.setText('----------')
        mwindow.label_alt_proth_art.setText('----------------')
        mwindow.label_alt_seite.setText('------')
        mwindow.label_alt_op_datum.setText('-----------')
        mwindow.pushButton_suche.setText('Suchen...')
        ButtonStatus.status = False  # Suchen...
        DataSetStatus.status = False  # Append


def datensatz_laden(patnr):
    """
    Wird bei Vorhandensein eines Datensatzes und Drücken des
    Laden... -Knopfes aufgerufen / lädt Datensatz in Eingabemaske
    :return: None
    """
    sql = """SELECT "id","patientennummer","prothesenart","prothesentyp","proximal","distal","seite","wechseleingriff",\
"praeop_roentgen","postop_roentgen","fraktur","planung","opdatum","operateur","assistenz",\
"op_zeiten","infektion","luxation","inklinationswinkel","trochanterabriss","fissuren","thrombose_embolie",\
"sterblichkeit","neurologie","dokumentation","memo","knochenverankert","periprothetisch","reintervention",\
"abweichung","ct","ab_imp_art","ab_imp_groesse","ab_stab","ab_blutung","ab_praeop","ab_operation",\
"ab_anaesthesie","spaet_infekt","einweiser","neunzig_tage","kniewinkel_prae","kniewinkel_post",\
"vierundzwanzig_plus","oak"\
 FROM "prothesen" WHERE "patientennummer" = """
    sql += patnr + ';'
    db.open_db()
    lesen = db.fetchone(sql)
    for it in k_list:  # Dictionary Formulardaten mit Datensatz aktualisieren...
        dic_prothesen.update({it: lesen[k_list.index(it)]})
    db.close_db()
    aktualisiere_widgets()


def aktualisiere_widgets():
    """
    Daten aus Dictionary ins Formular laden...
    :return: None
    """
    mwindow.comboBox_prothesenart.setCurrentText(dic_prothesen['prothesenart'])
    mwindow.comboBox_seite.setCurrentText(dic_prothesen['seite'])
    mwindow.comboBox_proximal.setCurrentText(dic_prothesen['proximal'])
    mwindow.comboBox_distal.setCurrentText(dic_prothesen['distal'])
    mwindow.checkBox_wechseleingriff.setChecked(dic_prothesen['wechseleingriff'])
    mwindow.checkBox_praeop_roentgen.setChecked(dic_prothesen['praeop_roentgen'])
    mwindow.checkBox_postop_roentgen.setChecked(dic_prothesen['postop_roentgen'])
    mwindow.checkBox_fraktur.setChecked(dic_prothesen['fraktur'])
    mwindow.checkBox_praeop_planung.setChecked(dic_prothesen['planung'])
    ds = str(dic_prothesen['opdatum'])  # Datums-String
    yy = int(ds[0:4])  # Zerlegung ...
    mm = int(ds[5:7])  # TODO Fehler '' abfangen?
    dd = int(ds[8:10])
    mwindow.dateEdit_opdatum.setDate(QDate(yy, mm, dd))
    mwindow.comboBox_operateur.setCurrentText(dic_prothesen['operateur'])
    mwindow.comboBox_assistenz.setCurrentText(dic_prothesen['assistenz'])
    mwindow.lineEdit_operationszeit.setText(str(dic_prothesen['op_zeiten']))
    mwindow.checkBox_infektion.setChecked(dic_prothesen['infektion'])
    mwindow.checkBox_luxation.setChecked(dic_prothesen['luxation'])
    mwindow.lineEdit_inklinationswinkel.setText(str(dic_prothesen['inklinationswinkel']))
    mwindow.checkBox_trochanterabriss.setChecked(dic_prothesen['trochanterabriss'])
    mwindow.checkBox_fissur.setChecked(dic_prothesen['fissuren'])
    mwindow.checkBox_thromboembolie.setChecked(dic_prothesen['thrombose_embolie'])
    mwindow.checkBox_gestorben.setChecked(dic_prothesen['sterblichkeit'])
    mwindow.checkBox_neurologie.setChecked(dic_prothesen['neurologie'])
    mwindow.checkBox_vollstaendig.setChecked(dic_prothesen['dokumentation'])
    mwindow.plainTextEdit_memo.setPlainText(dic_prothesen['memo'])
    mwindow.checkBox_knochenverankert.setChecked(dic_prothesen['knochenverankert'])
    mwindow.checkBox_periprothetisch.setChecked(dic_prothesen['periprothetisch'])
    mwindow.checkBox_reintervention.setChecked(dic_prothesen['reintervention'])
    mwindow.checkBox_abweichung.setChecked(dic_prothesen['abweichung'])
    mwindow.checkBox_ct.setChecked(dic_prothesen['ct'])
    mwindow.checkBox_implantation.setChecked(dic_prothesen['ab_imp_art'])
    mwindow.checkBox_implantat.setChecked(dic_prothesen['ab_imp_groesse'])
    mwindow.checkBox_stabilisatoren.setChecked(dic_prothesen['ab_stab'])
    mwindow.checkBox_blutung.setChecked(dic_prothesen['ab_blutung'])
    mwindow.checkBox_vorbereitung.setChecked(dic_prothesen['ab_praeop'])
    mwindow.checkBox_operation.setChecked(dic_prothesen['ab_operation'])
    mwindow.checkBox_anaesthesie.setChecked(dic_prothesen['ab_anaesthesie'])
    mwindow.checkBox_spaetinfektion.setChecked(dic_prothesen['spaet_infekt'])
    mwindow.comboBox_einweiser.setCurrentText(dic_prothesen['einweiser'])
    mwindow.checkBox_neunzig.setChecked(
        dic_prothesen['neunzig_tage'] if dic_prothesen['neunzig_tage'] is not None else False)
    mwindow.lineEdit_praeop_winkel.setText(format_winkel(str(dic_prothesen['kniewinkel_prae'])))
    mwindow.lineEdit_postop_winkel.setText(format_winkel(str(dic_prothesen['kniewinkel_post'])))
    mwindow.checkBox_vierundzwanzig.setChecked(
        dic_prothesen['vierundzwanzig_plus'] if dic_prothesen['vierundzwanzig_plus'] is not None else False)
    mwindow.checkBox_oak.setChecked(dic_prothesen['oak'] if dic_prothesen['oak'] is not None else False)
    mwindow.repaint()  # Fenster aktualisieren


def aktualisiere_dictionary():
    """
    Daten aus Formular in das Dictionary laden...
    :return:  None
    """
    dic_prothesen['patientennummer'] = mwindow.lineEdit_patientennummer.text()
    dic_prothesen['prothesenart'] = mwindow.comboBox_prothesenart.currentText()
    dic_prothesen['prothesentyp'] = 'NULL' if str(dic_prothesen['prothesentyp']).strip() != '' else dic_prothesen[
        'prothesentyp']
    dic_prothesen['seite'] = mwindow.comboBox_seite.currentText()
    dic_prothesen['proximal'] = mwindow.comboBox_proximal.currentText()
    dic_prothesen['distal'] = mwindow.comboBox_distal.currentText()
    dic_prothesen[
        'wechseleingriff'] = mwindow.checkBox_wechseleingriff.isChecked()
    dic_prothesen[
        'praeop_roentgen'] = mwindow.checkBox_praeop_roentgen.isChecked()
    dic_prothesen[
        'postop_roentgen'] = mwindow.checkBox_postop_roentgen.isChecked()
    dic_prothesen['fraktur'] = mwindow.checkBox_fraktur.isChecked()
    dic_prothesen['planung'] = mwindow.checkBox_praeop_planung.isChecked()
    dic_prothesen['opdatum'] = mwindow.dateEdit_opdatum.date().toString(
        'yyyy-MM-dd')
    dic_prothesen['operateur'] = mwindow.comboBox_operateur.currentText()
    dic_prothesen['assistenz'] = mwindow.comboBox_assistenz.currentText()
    dic_prothesen[
        'op_zeiten'] = mwindow.lineEdit_operationszeit.text() if mwindow.lineEdit_operationszeit.text() != '' else 'NULL'
    dic_prothesen['infektion'] = mwindow.checkBox_infektion.isChecked()
    dic_prothesen['luxation'] = mwindow.checkBox_luxation.isChecked()
    dic_prothesen[
        'inklinationswinkel'] = mwindow.lineEdit_inklinationswinkel.text() if mwindow.lineEdit_inklinationswinkel.text() != '' else 'NULL'
    dic_prothesen[
        'trochanterabriss'] = mwindow.checkBox_trochanterabriss.isChecked()
    dic_prothesen['fissuren'] = mwindow.checkBox_fissur.isChecked()
    dic_prothesen[
        'thrombose_embolie'] = mwindow.checkBox_thromboembolie.isChecked()
    dic_prothesen['sterblichkeit'] = mwindow.checkBox_gestorben.isChecked()
    dic_prothesen['neurologie'] = mwindow.checkBox_neurologie.isChecked()
    dic_prothesen['dokumentation'] = mwindow.checkBox_vollstaendig.isChecked()
    dic_prothesen[
        'memo'] = mwindow.plainTextEdit_memo.toPlainText() if mwindow.plainTextEdit_memo.toPlainText() != '' else 'NULL'
    dic_prothesen[
        'knochenverankert'] = mwindow.checkBox_knochenverankert.isChecked()
    dic_prothesen[
        'periprothetisch'] = mwindow.checkBox_periprothetisch.isChecked()
    dic_prothesen[
        'reintervention'] = mwindow.checkBox_reintervention.isChecked()
    dic_prothesen['abweichung'] = mwindow.checkBox_abweichung.isChecked()
    dic_prothesen['ct'] = mwindow.checkBox_ct.isChecked()
    dic_prothesen['ab_imp_art'] = mwindow.checkBox_implantation.isChecked()
    dic_prothesen['ab_imp_groesse'] = mwindow.checkBox_implantat.isChecked()
    dic_prothesen['ab_stab'] = mwindow.checkBox_stabilisatoren.isChecked()
    dic_prothesen['ab_blutung'] = mwindow.checkBox_blutung.isChecked()
    dic_prothesen['ab_praeop'] = mwindow.checkBox_vorbereitung.isChecked()
    dic_prothesen['ab_operation'] = mwindow.checkBox_operation.isChecked()
    dic_prothesen['ab_anaesthesie'] = mwindow.checkBox_anaesthesie.isChecked()
    dic_prothesen['spaet_infekt'] = mwindow.checkBox_spaetinfektion.isChecked()
    dic_prothesen[
        'einweiser'] = mwindow.comboBox_einweiser.currentText() if mwindow.comboBox_einweiser.currentText() != '' else 'NULL'
    dic_prothesen['neunzig_tage'] = mwindow.checkBox_neunzig.isChecked()
    dic_prothesen[
        'kniewinkel_prae'] = mwindow.lineEdit_praeop_winkel.text() if mwindow.lineEdit_praeop_winkel.text().strip() not in (
        '.', '+.', '-.') else 'NULL'
    dic_prothesen[
        'kniewinkel_post'] = mwindow.lineEdit_postop_winkel.text() if mwindow.lineEdit_postop_winkel.text().strip() not in (
        '.', '+.', '-.') else 'NULL'
    dic_prothesen[
        'vierundzwanzig_plus'] = mwindow.checkBox_vierundzwanzig.isChecked()
    dic_prothesen['oak'] = mwindow.checkBox_oak.isChecked()


def schalter_suchen_laden():  # Schalter -> Suchen / Laden
    """
    Schalter Suchen/Laden gedrückt
    lädt bei vorhandenem Datensatz diesen
    :return: None
    """
    if ButtonStatus.status:  # Laden...
        patnr = mwindow.lineEdit_patientennummer.text()
        datensatz_laden(patnr)
        DataSetStatus.status = True  # Update...
    else:
        set_start_default()
        suche_patientennummer()  # sonst manuelle Datensatzsuche
        DataSetStatus.status = False  # Append...
        reset_Formular()
        hole_statistik()
        mwindow.repaint()


def suche_eprd():
    """
    Suche in der EPRD-Datenbank und ggf. Eintrag in die Maske
    :return: None
    """
    try:
        patnr = (
            mwindow.lineEdit_patientennummer.text() if mwindow.lineEdit_patientennummer.text() != '' else '0')  # sonst Fehler bei Postgres
        sql = """SELECT id FROM eprd_fall WHERE khintkennz = '"""
        sql += patnr + """';"""
        eprd.open_db()
        lesen = eprd.fetchone(sql)
        if lesen:
            sql = """SELECT opdatum, gelenk_code, seite_code, arteingriff_code, arzt_nachname  FROM eprd_operation WHERE fk_eprd_fall = '"""
            sql += lesen[0] + """';"""
            EPRD_Status.status = True  # Eintrag in der EPRD-Datenbank gefunden
            eprd.open_db()
            eprd_data = eprd.fetchone(sql)
            if eprd_data[1] == '1':
                mwindow.comboBox_prothesenart.setCurrentText('Hüfte')
            else:
                mwindow.comboBox_prothesenart.setCurrentText('Knie')
            if eprd_data[2] == '1':
                mwindow.comboBox_seite.setCurrentText('links')
            else:
                mwindow.comboBox_seite.setCurrentText('rechts')
            if eprd_data[3] != '1':
                mwindow.checkBox_wechseleingriff.setChecked(True)
            else:
                mwindow.checkBox_wechseleingriff.setChecked(False)
            mwindow.dateEdit_opdatum.setDate(eprd_data[0])
            if eprd_data[4] in ['Svacina', 'Neu', 'Suhren', 'Troeger', 'Machner']:
                mwindow.comboBox_operateur.setCurrentText(eprd_data[4])
        eprd.close_db()
    except (psycopg2.OperationalError, psycopg2.ProgrammingError) as e:
        eprd.protocol('-- ' + str(e).split('\n')[0])
    artikel = suche_implantate(patnr)  # Implantate aus EPRD-Datenbank
    if artikel:
        # nach Op-Datum Tupel in Liste sortieren
        artikel.sort(key=lambda x: x[0])
        schreibe_statistik('')
        schreibe_statistik('Implantate aus EPRD-Datenbank...')
        schreibe_statistik('')
        for art_tuple in artikel:
            op_datum, art = art_tuple
            schreibe_statistik(op_datum + ': ' + art)
        schreibe_statistik('')


def suche_implantate(fallnummer):
    """
    Implantatsuche in der EPRD-Datenbank
    :return: List
    """
    artikelliste = []
    eprd.open_db()
    try:
        fall_id_raw = eprd.fetchone(
            "select * from eprd_fall where khintkennz = '" + fallnummer + "'")
        fall_id = fall_id_raw[0]
    except:
        pass
    else:
        try:  # TODO: fetchall?
            op_id_raw_all = eprd.fetchall(
                "select * from eprd_operation where fk_eprd_fall = '" + fall_id + "'")
            op_id_list = []
            for op_item in op_id_raw_all:
                # Liste von Tupeln (Op-Nr., Op-Datum)
                op_id_list.append(
                    (op_item[0], op_item[3].strftime('%d.%m.%Y')))
        except:
            pass
        else:
            try:
                for op_id_item in op_id_list:
                    op_id, op_datum = op_id_item
                artikel_raw = eprd.fetchall(
                    "select * from eprd_op_artikel where fk_eprd_operation = '" + op_id + "'")
                for artikel_zeile in artikel_raw:
                    # Liste von Tupeln (Op-Datum, Artikel)
                    artikelliste.append((op_datum, artikel_zeile[6]))
            except:
                pass
    finally:
        eprd.close_db
    return artikelliste


def suche_patientennummer():
    """
    Suche der Patientennummer...
    wird bei Eingabe der 8. Stelle der Patientennummer automatisch aufgerufen
    :return: None
    """
    patnr = mwindow.lineEdit_patientennummer.text() if mwindow.lineEdit_patientennummer.text() != '' else '0'  # sonst Fehler bei Postgres
    sql = """SELECT "patientennummer","prothesenart","seite","opdatum" FROM "prothesen" WHERE "patientennummer" = """
    sql += patnr + ';'
    db.open_db()
    lesen = db.fetchone(sql)
    if lesen:  # ein Datensatz mit dieser Patientennummer vorhanden...
        mwindow.label_alt_patnummer.setText(str(lesen[0]))  # bigint
        mwindow.label_alt_proth_art.setText(lesen[1])  # varchar
        mwindow.label_alt_seite.setText(lesen[2])  # varchar
        mwindow.label_alt_op_datum.setText(
            lesen[3].strftime('%d.%m.%Y'))  # String aus Datum
        mwindow.pushButton_suche.setText('Laden...')
        ButtonStatus.status = True  # Laden...
    else:
        mwindow.label_alt_patnummer.setText('----------')
        mwindow.label_alt_proth_art.setText('----------------')
        mwindow.label_alt_seite.setText('------')
        mwindow.label_alt_op_datum.setText('-----------')
        mwindow.pushButton_suche.setText('Suchen...')
        ButtonStatus.status = False  # Suchen...
    db.close_db()


def init_comboBox_einweiser():
    """
    Eingabemaske Einweiser initialisieren...
    :return: None
    """
    mwindow.comboBox_einweiser.clear()  # Liste löschen
    db.open_db()
    sql = """SELECT "einweiser" FROM "prothesen";"""
    lesen = set(db.fetchall(sql))  # Satz aller Einweiser (auch None!)
    einweiser = [it[0] for it in lesen if it[0]
                 is not None]  # Einweiserliste bereinigen
    for ew in sorted(einweiser):  # Einweiser laden
        mwindow.comboBox_einweiser.addItem(ew)
    db.close_db()
    mwindow.comboBox_einweiser.setCurrentText('')  # Eingabe leer


def change_prothesenart():
    """
    Eingabemaske an Prothesenart anpassen...
    :return: None
    """
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
        mwindow.checkBox_trochanterabriss.setVisible(
            True)  # Trochanterabriss an
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
    else:  # Schulter- und Radiusköpfchenprothese
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


def change_abweichung():
    """
    Abweichungen an und aus...
    :return: None
    """
    wglist = (  # Elemente der Eingabemaske in Liste laden
        mwindow.checkBox_vorbereitung,
        mwindow.checkBox_blutung,
        mwindow.checkBox_implantation,
        mwindow.checkBox_operation,
        mwindow.checkBox_implantat,
        mwindow.checkBox_stabilisatoren,
        mwindow.checkBox_anaesthesie)
    # Eingabemaske für Abweichungen...
    if mwindow.checkBox_abweichung.isChecked() is True:
        for wg in wglist:  # einschalten
            wg.setVisible(True)
        mwindow.groupBox_abweichung.setVisible(True)
    else:
        for wg in wglist:  # ausschalten
            wg.setVisible(False)
            wg.setCheckState(False)
        mwindow.groupBox_abweichung.setVisible(False)


def change_wechseleingriff():
    """
    Änderung Wechseleingriff -> knochenverankert?
    :return: None
    """
    if mwindow.checkBox_wechseleingriff.isChecked() is True:
        mwindow.checkBox_knochenverankert.setVisible(True)  # Checkbox knochenverankert ein-
    else:
        mwindow.checkBox_knochenverankert.setVisible(False)  # und ausschalten / löschen
        mwindow.checkBox_knochenverankert.setCheckState(False)


def change_fraktur():
    """
    Änderung Fraktur -> periprothetisch?
    :return: None
    """
    if mwindow.checkBox_fraktur.isChecked() is True:
        mwindow.checkBox_periprothetisch.setVisible(True)  # Checkbox periprothetisch ein-
    else:
        mwindow.checkBox_periprothetisch.setVisible(False)  # und ausschalten / löschen
        mwindow.checkBox_periprothetisch.setCheckState(False)


def change_vierundzwanzig():
    """
    Versorgung nach 24h?
    Ursache orale Antikoagulantien?
    :return: None
    """
    if mwindow.checkBox_vierundzwanzig.isChecked() is True:
        mwindow.checkBox_oak.setVisible(True)  # Checkbox periprothetisch ein-
    else:
        mwindow.checkBox_oak.setVisible(False)  # und ausschalten / löschen
        mwindow.checkBox_oak.setCheckState(False)


def change_neunzig():
    """
    Komplikationen < 90 Tage
    :return: None
    """
    regeln = [  # Liste aller Komplikations-Checkboxen
        mwindow.checkBox_infektion.isChecked() is False,
        mwindow.checkBox_luxation.isChecked() is False,
        mwindow.checkBox_trochanterabriss.isChecked() is False,
        mwindow.checkBox_fissur.isChecked() is False,
        mwindow.checkBox_thromboembolie.isChecked() is False,
        mwindow.checkBox_neurologie.isChecked() is False,
        mwindow.checkBox_gestorben.isChecked() is False]
    if all(regeln):
        mwindow.checkBox_neunzig.setCheckState(False)


def init_lineEdit_patientennummer():
    """
    Patientennummer initialisieren...
    :return: None
    """
    mwindow.lineEdit_patientennummer.setText('50000000')  # Maske vorbelegen
    mwindow.lineEdit_patientennummer.setCursorPosition(2)  # Cursor auf 3. Position


def init_comboBox_seite():
    """
    Seitenangabe ...
    :return: None
    """
    mwindow.comboBox_seite.clear()
    mwindow.comboBox_seite.addItem('rechts')
    mwindow.comboBox_seite.addItem('links')


def init_comboBox_prothesenart():
    """
    Prothesenart ...
    :return: None
    """
    mwindow.comboBox_prothesenart.clear()
    mwindow.comboBox_prothesenart.addItem('Hüfte')
    mwindow.comboBox_prothesenart.addItem('Knie')
    mwindow.comboBox_prothesenart.addItem('Schulter')
    mwindow.comboBox_prothesenart.addItem('Radiusköpfchen')


def init_comboBox_proximal():
    """
    Auswahlliste Implantate proximal füllen...
    :return: None
    """
    mwindow.comboBox_proximal.clear()  # Masken löschen und füllen...
    if mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        for it in (
                "Ecofit-Pfanne",
                "Duokopf",
                "Schraubpfanne",
                "McMinn-Pfanne",
                "zementierte Pfanne",
                "Schnapppfanne",
                "sonstiges"):
            mwindow.comboBox_proximal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Knie':
        for it in (
                "3D Knie Femur",
                "ACS-SC Knie Femur",
                "ACS-PS Knie Femur",
                "GenuX Knie Femur",
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
    """
    Auswahlliste Implantate distal füllen...
    :return: None
    """
    mwindow.comboBox_distal.clear()
    if mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        for it in (
                "Ecofit-Schaft",
                "Ecofit-Kurzschaft",
                "Actinia-Schaft",
                "zementierter Ecofit-Schaft",
                "McMinn-Oberflächenersatz",
                "Revisionsschaft zementfrei",
                "sonstiges"):
            mwindow.comboBox_distal.addItem(it)
    elif mwindow.comboBox_prothesenart.currentText() == 'Knie':
        for it in (
                "3D Knie Tibia",
                "ACS-SC Knie Tibia",
                "ACS-PS Knie Tibia",
                "GenuX Knie Tibia",
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
                "Radiusköpfchen Implantcast",
                "Radiusköpfchen Link",
                "sonstiges"):
            mwindow.comboBox_distal.addItem(it)


def init_dateEdit_opdatum():
    """
    Grenzen für Operationsdatum festlegen
    :return: None
    """
    mwindow.dateEdit_opdatum.setMinimumDate(QDate(2014, 1, 1))
    mwindow.dateEdit_opdatum.setMaximumDate(QDate(2021, 12, 31))


def init_lineEdit_dateEdit_opdatum():
    """
    Operationsdatum setzen
    :return: None
    """
    mwindow.dateEdit_opdatum.setDate(QDate(2020, 1, 1))


def init_comboBox_operateur():
    """
    Auswahlmasken für Operateur und Assistent füllen
    :return: None
    """
    ChangeStatus.status = False
    db.open_db()
    sql = """SELECT "operateur" FROM "prothesen";"""
    lesen = list(db.fetchall(sql))  # Liste aller Operateure aus Datenbank (auch None!)
    db.close_db()
    operateur = [it[0]
                 for it in lesen if it[0] != None]  # Operateurliste bereinigen
    operateur = set(['Svacina', 'Neu', 'Suhren', 'Troeger', 'Joker'] + operateur)  # alle zum set() umwandeln
    mwindow.comboBox_operateur.clear()
    mwindow.comboBox_assistenz.clear()
    for op in sorted(operateur):  # Operateure laden
        mwindow.comboBox_operateur.addItem(op)
        mwindow.comboBox_assistenz.addItem(op)


def change_operateur():
    """
    Änderung des Operateurs
    :return: None
    """
    if ChangeStatus.status is True:
        if test_operateur(mwindow.comboBox_operateur.currentText(), mwindow.comboBox_assistenz.currentText()) is False:
            dwindow.exec()  # Fenster Eingabefehler


def change_assistenz():
    """
    Änderung des Assistenten
    :return: None
    """
    if ChangeStatus.status is True:
        if test_operateur(mwindow.comboBox_operateur.currentText(), mwindow.comboBox_assistenz.currentText()) is False:
            dwindow.exec()  # Fenster Eingabefehler


def focus_operateur():
    """
    Eingabefeld erhält Fokus
    :return: None
    """
    ChangeStatus.status = True


def focus_assistenz():
    """
     Eingabefeld erhält Fokus
     :return: None
     """
    ChangeStatus.status = True


def test_operateur(operateur1, operateur2):
    """
    Test der Eingabe von Operateur und Assistent auf Validität
    :param operateur1: Operateur oder Assistent 1
    :param operateur2: Operateur oder Assistent 2
    :return: True wenn richtig
             False wenn falsch
    """
    if operateur1 == 'Joker' and operateur2 == 'Joker':
        return False
    elif operateur1 == operateur2:
        return False
    else:
        return True


def change_opzeit():
    """
    Änderung der Operationszeit
    :return: None
    """
    opzeit = int(
        mwindow.lineEdit_operationszeit.text() if mwindow.lineEdit_operationszeit.text() != '' else '0')  # '' abfangen!
    if opzeit > 100 and mwindow.comboBox_prothesenart.currentText() == 'Hüfte':  # Abweichung Hüfte
        mwindow.label_zeit_achtung.setVisible(True)
    elif opzeit > 120 and mwindow.comboBox_prothesenart.currentText() == 'Knie':  # Abweichung Knie
        mwindow.label_zeit_achtung.setVisible(True)
    else:
        mwindow.label_zeit_achtung.setVisible(False)


def change_inklination():
    """
    Änderung des Inklinationswinkels
    :return: None
    """
    inklination = int(
        mwindow.lineEdit_inklinationswinkel.text() if mwindow.lineEdit_inklinationswinkel.text() != '' else '0')  # '' abfangen!
    if inklination > 50 and mwindow.comboBox_prothesenart.currentText() == 'Hüfte':
        mwindow.label_inklination_achtung.setVisible(True)
    else:
        mwindow.label_inklination_achtung.setVisible(False)


def set_start_default():
    """
    alle Eingabe-Widgets auf Standard stellen...
    :return: None
    """
    for it in lineEditState.keys():
        it.setText(lineEditState[it])
    for it in checkBoxState:
        it.setCheckState(checkBoxState[it])
    mwindow.plainTextEdit_memo.setPlainText('')  # Memo-Feld löschen


def save_state():
    """
    Status der Widgets in Dictionaries speichern
    :return: None
    """
    global lineEditState, checkBoxState
    lineedits = mwindow.findChildren(QLineEdit)
    lineEditState = {}
    for it in lineedits:
        lineEditState.update({it: it.text()})
    checkBoxState = {}
    checkBoxes = mwindow.findChildren(QCheckBox)
    for it in checkBoxes:
        checkBoxState.update({it: it.checkState()})


def datensatz_speichern():
    """
    Schreiben der Daten in die PostgreSQL-Datenbank
    Update oder Insert
    :return: None
    """
    idnr = str(dic_prothesen['id'])
    if DataSetStatus.status:  # SQL Update
        sql = """UPDATE "prothesen" SET ("patientennummer","prothesenart","prothesentyp","proximal","distal","seite","wechseleingriff",\
"praeop_roentgen","postop_roentgen","fraktur","planung","opdatum","operateur","assistenz",\
"op_zeiten","infektion","luxation","inklinationswinkel","trochanterabriss","fissuren","thrombose_embolie",\
"sterblichkeit","neurologie","dokumentation","memo","knochenverankert","periprothetisch","reintervention",\
"abweichung","ct","ab_imp_art","ab_imp_groesse","ab_stab","ab_blutung","ab_praeop","ab_operation",\
"ab_anaesthesie","spaet_infekt","einweiser","neunzig_tage","kniewinkel_prae","kniewinkel_post",\
"vierundzwanzig_plus","oak")\
 = ("""
        for it in k_list:
            if it != 'id':  # Postgres-Update mit 'ID'
                sql += ("'" + str(dic_prothesen[it]) + "'") if dic_typ[it] != 0 and dic_prothesen[
                    it] != 'NULL' else str(dic_prothesen[it])  # '?
                sql += ',' if it != 'oak' else ''  # letztes Feld?
        sql += """) WHERE "id" = """
        sql += str(idnr) + ';'
    else:  # SQL Insert
        sql = """INSERT INTO "prothesen" ("patientennummer","prothesenart","prothesentyp","proximal","distal","seite","wechseleingriff",\
"praeop_roentgen","postop_roentgen","fraktur","planung","opdatum","operateur","assistenz",\
"op_zeiten","infektion","luxation","inklinationswinkel","trochanterabriss","fissuren","thrombose_embolie",\
"sterblichkeit","neurologie","dokumentation","memo","knochenverankert","periprothetisch","reintervention",\
"abweichung","ct","ab_imp_art","ab_imp_groesse","ab_stab","ab_blutung","ab_praeop","ab_operation",\
"ab_anaesthesie","spaet_infekt","einweiser","neunzig_tage","kniewinkel_prae","kniewinkel_post",\
"vierundzwanzig_plus","oak")\
 VALUES ("""
        for it in k_list:
            if it != 'id':  # Postgres-Insert ohne 'ID'
                sql += ("'" + str(dic_prothesen[it]) + "'") if dic_typ[it] != 0 and dic_prothesen[
                    it] != 'NULL' else str(dic_prothesen[it])  # '?
                sql += ',' if it != 'oak' else ''  # letztes Feld?
        sql += """);"""
    db.open_db()
    db.protocol(sql)
    db.execute(sql)
    db.close_db()
    DataSetStatus.status = False


def pruefen():
    """
    Prüfung der Eingaben...
    :return: True wenn Eingaben richtig
             False wenn Eingaben falsch
    """
    korrekt = True
    if test_operateur(mwindow.comboBox_operateur.currentText(),
                      mwindow.comboBox_assistenz.currentText()) is False:  # kein Operateur eingegeben
        korrekt = False
    if mwindow.dateEdit_opdatum.date().toString('yyyy-MM-dd') == '2020-01-01':  # kein Op-Datum eingegeben
        korrekt = False
    if mwindow.lineEdit_operationszeit.text() == '':  # keine Op-Dauer eingegeben
        korrekt = False
    if dic_prothesen['id'] is None and DataSetStatus.status is True:  # Update ohne id
        korrekt = False
    if not korrekt:
        dwindow.exec()
    return korrekt


def speichern():
    """
    Speichern der Daten in der Datenbank
    :return: None
    """
    if pruefen():  # alle Eingaben gemacht?
        aktualisiere_dictionary()
        datensatz_speichern()
        set_start_default()
        init_neuesFormular()


def init_neuesFormular():
    """
    neues Formular initialisieren
    :return: None
    """
    init_dictionary()
    hole_statistik()
    init_lineEdit_patientennummer()
    init_formular_allgemein()


def reset_Formular():
    """
    Formular bei Änderung der Patientennummer zurücksetzen
    :return: None
    """
    line_edit_state_reset = {}
    for key in lineEditState:  # echte Kopie des Dictionary anlegen
        line_edit_state_reset[key] = lineEditState[key]
    # ersten Eintrag des Dictionary löschen
    line_edit_state_reset.pop(next(iter(line_edit_state_reset.keys())))
    for it in line_edit_state_reset.keys():
        it.setText(line_edit_state_reset[it])
    for it in checkBoxState:
        it.setCheckState(checkBoxState[it])
    mwindow.plainTextEdit_memo.setPlainText('')  # Memo-Feld löschen
    init_formular_allgemein()


def init_formular_allgemein():
    """
    gemeinsamer Funktionsrumpf von init_neuesFormular und reset_Formular
    :return: None
    """
    init_comboBox_prothesenart()
    change_prothesenart()
    change_wechseleingriff()
    init_comboBox_seite()
    init_comboBox_proximal()
    init_comboBox_distal()
    change_fraktur()
    change_vierundzwanzig()
    init_dateEdit_opdatum()
    change_abweichung()
    init_comboBox_operateur()
    init_comboBox_einweiser()
    mwindow.label_zeit_achtung.setVisible(False)
    mwindow.label_inklination_achtung.setVisible(False)
    mwindow.lineEdit_operationszeit.setCursorPosition(0)
    mwindow.lineEdit_inklinationswinkel.setCursorPosition(0)
    DataSetStatus.status = False  # Datenbank-Insert als initialer Status
    ButtonStatus.status = False  # Suche...
    EPRD_Status.status = False  # keine positive EPRD-Suche erfolgt
    mwindow.repaint()


def change_praeop():
    """
    Eingabe des präoperativen Knie-Winkels
    :return: None
    """
    if len(mwindow.lineEdit_praeop_winkel.text()) > 4 or mwindow.lineEdit_praeop_winkel.cursorPosition() == 5:
        mwindow.lineEdit_praeop_winkel.setText(
            format_winkel(mwindow.lineEdit_praeop_winkel.text()))
    mwindow.lineEdit_praeop_winkel.repaint()


def change_postop():
    """
    Eingabe des postoperativen Knie-Winkels
    :return: None
    """
    if len(mwindow.lineEdit_postop_winkel.text()) > 4 or mwindow.lineEdit_postop_winkel.cursorPosition() == 5:
        mwindow.lineEdit_postop_winkel.setText(
            format_winkel(mwindow.lineEdit_postop_winkel.text()))
    palette = QPalette()
    try:
        # Winkel auffällig?
        winkel = abs(float(mwindow.lineEdit_postop_winkel.text()))
    except ValueError:
        winkel = 0
    if winkel > 3:
        palette.setColor(QPalette.Text, Qt.red)
        mwindow.lineEdit_postop_winkel.setPalette(palette)
    else:
        palette.setColor(QPalette.Text, Qt.black)
        mwindow.lineEdit_postop_winkel.setPalette(palette)
    mwindow.lineEdit_postop_winkel.repaint()


def format_winkel(text: str) -> 'format_winkel':
    """
    Formatieren der Winkelangaben
    :param text: Text unformatierter Winkel
    :return: Text formatierter Winkel
    """
    text = text.strip()
    if text == 'Null' or text == '.' or text == '':  # leer?
        return ''
    if text[0:1] == '.':  # . an erster Position
        text = '0' + text
        return format_winkel(text)  # Rekursion
    if '.' not in text and text[0:1] not in ('+', '-'):  # nur 3 Ziffern
        text = '+' + text[0:2] + '.' + text[2:3]
        return format_winkel(text)  # Rekursion
    if text[0:1] not in ('+', '-'):  # kein Vorzeichen
        text = '+' + text
        return format_winkel(text)  # Rekursion
    if text[0:1] in ('+', '-') and '.' not in text:  # Vorzeichen, kein Punkt
        text = text[0:3] + '.' + text[3:4]
        return format_winkel(text)  # Rekursion
    if text[2:3] == '.':  # einstellig vor Punkt, Punkt nach hinten
        text = text[0:1] + ' ' + text[1:]
        return format_winkel(text)  # Rekursion
    if len(text) < 5 and '.' in text:  # leer nach Punkt, .0
        text += '0'
        return format_winkel(text)  # Rekursion
    if text[1:2] == '0':  # zwei führende Nullen vor Punkt
        text = text[0:1] + ' ' + text[2:]
        return format_winkel(text)  # Rekursion
    if text[1:2] == ' ' and text[2:3] == ' ':  # 2 Leerstellen vor Punkt
        text = text[0:1] + '0' + text[3:]
        return format_winkel(text)  # Rekursion
    if text[2:3] == ' ':  # Leerstelle vor Punkt
        text = text[0:2] + text[3:]
        return format_winkel(text)  # Rekursion
    return text


if __name__ == "__main__":
    """
    PostgreSQL-Datenbank-Zugang:
    Klinikrechner:
    host='139.64.200.60' dbname='prothesen' user='postgres' password='SuperUser2012'
    eigener Rechner:
    host='localhost' dbname='prothesen' user='postgres' password='postgres'

    """
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    dwindow = achtung()
    db = Database('localhost', 'prothesen', 'postgres', 'postgres')
    eprd = Database('localhost', 'eprd_db2_m1', 'postgres', 'postgres')
    # Datensatzstatus False -> Postgres Append, True -> Postgres Update
    DataSetStatus = Status()
    # Knopfstatus False -> Suche ..., True -> Laden ...
    ButtonStatus = Status()
    # Änderung der Eingabemaske Operateur / Assistenz
    ChangeStatus = Status()
    # Datensatz in EPRD-Datenbank gefunden
    EPRD_Status = Status()
    dic_prothesen = {}  # Dictionary für Formulardaten
    dic_typ = {}  # Dictionary für Typ zur Speicherung in PostgreSQL
    mwindow.checkBox_wechseleingriff.stateChanged.connect(change_wechseleingriff)  # Ereignis Wechseleingriff an / aus
    mwindow.checkBox_abweichung.stateChanged.connect(change_abweichung)  # Ereignis Abweichung an / aus
    # Ereignis Taste Suchen/Laden gedrückt
    mwindow.pushButton_suche.clicked.connect(schalter_suchen_laden)
    mwindow.comboBox_operateur.currentTextChanged.connect(change_operateur)  # Ereignis Wechsel Operateur
    mwindow.comboBox_assistenz.currentTextChanged.connect(change_assistenz)  # Ereignis Wechsel Assistenz
    mwindow.comboBox_operateur.highlighted.connect(focus_operateur)  # Ereignis Focus Operateur
    mwindow.comboBox_assistenz.highlighted.connect(focus_assistenz)  # Ereignis Focus Assistenz
    mwindow.pushButton_speichern.pressed.connect(speichern)  # Ereignis Taste Speichern gedrückt
    mwindow.comboBox_prothesenart.currentTextChanged.connect(change_prothesenart)  # Ereignis Wechsel Prothesenart
    mwindow.lineEdit_patientennummer.textChanged.connect(change_patientennummer)  # Ereignis Änderung Patientennummer
    mwindow.lineEdit_operationszeit.textChanged.connect(change_opzeit)
    mwindow.lineEdit_inklinationswinkel.textChanged.connect(change_inklination)
    mwindow.checkBox_fraktur.stateChanged.connect(change_fraktur)  # Ereignis Änderung Fraktur an / aus
    mwindow.checkBox_vierundzwanzig.stateChanged.connect(
        change_vierundzwanzig)  # Ereignis für alle CheckBoxes in Gruppe setzen
    for cb in mwindow.groupBox_komplikation.findChildren(QCheckBox):
        cb.stateChanged.connect(change_neunzig)
    mwindow.lineEdit_praeop_winkel.textChanged.connect(change_praeop)  # Ereignis Eingabe präop. Winkel
    mwindow.lineEdit_postop_winkel.textChanged.connect(change_postop)  # Ereignis Eingabe postop. Winkel
    init_neuesFormular()  # Formular generieren und anzeigen...
    save_state()  # als Standard speichern
    mwindow.show()  # Fenster anzeigen
    sys.exit(app.exec_())  # Fenster mit Beenden des Programmes schließen
