from global_var import * #type: ignore
from aux_code import * #type: ignore
from ui import * #type: ignore
import sys
import io
import base64
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

def set_interval_temp_aux(text):
    global temp_interval
    if text.isnumeric():
        temp_interval = set_interval_temp(int(text))
        object_gui.set_temp.setEnabled(False)
        object_gui.temp_cancel.setEnabled(True)
    else:
        print("[!]Need a number...")

def cancel_temp():
    temp_interval.cancel()
    object_gui.set_temp.setEnabled(True)
    object_gui.temp_cancel.setEnabled(False)

def set_interval_hum_aux(text):
    global hum_interval
    if text.isnumeric():
        hum_interval = set_interval_hum(int(text))
        object_gui.set_hum.setEnabled(False)
        object_gui.hum_cancel.setEnabled(True)
    else:
        print("[!]Need a number...")

def cancel_hum():
    hum_interval.cancel()
    object_gui.set_hum.setEnabled(True)
    object_gui.hum_cancel.setEnabled(False)

def send_power(text):
    if text.isnumeric():
            send(2, text + ' ' + power_unit)
    else:
        print("[!]Need a number...")

def plus_people():
    global people
    people += 1
    send(3, str(people) + ' ' + people_unit)
    object_gui.less_one.setEnabled(True)
    object_gui.counter.display(people)

def less_people():
    global people
    if people == 0:
        print("[!] Seriously, negative people is imposible...")
        return
    people -= 1
    send(3, str(people) + ' ' + people_unit)
    object_gui.counter.display(people)

def iconFromBase64(base64):
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    icon = QtGui.QIcon(pixmap)
    return icon

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        icon = iconFromBase64(b64_icon)
        self.setWindowIcon(QtGui.QIcon(icon))
        gui_loader = io.StringIO(gui_str)
        uic.loadUi(gui_loader, self)
        self.set_temp.clicked.connect(lambda: set_interval_temp_aux(self.temp_text.text()))
        self.temp_cancel.clicked.connect(lambda: cancel_temp())
        self.set_hum.clicked.connect(lambda: set_interval_hum_aux(self.hum_text.text()))
        self.hum_cancel.clicked.connect(lambda: cancel_hum())
        self.send_cons.clicked.connect(lambda: send_power(self.cons_text.text()))
        self.plus_one.clicked.connect(lambda: plus_people())
        self.less_one.clicked.connect(lambda: less_people())

    

def main():
    global object_gui, zone, temp_interval, hum_interval
    print("[+]Running...")
    app = QApplication(sys.argv)
    object_gui = GUI()
    try:
        zone = sys.argv[1]
    except:
        zone = 1
    object_gui.principal_text.setText("Control panel -> zone " + str(zone))
    object_gui.show()
    object_gui.temp_cancel.setEnabled(False)
    object_gui.hum_cancel.setEnabled(False)
    object_gui.less_one.setEnabled(False)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()