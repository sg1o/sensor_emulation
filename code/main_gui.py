import sys

try:
        zone = sys.argv[1]
except:
        zone = 1

from global_var import * #type: ignore
from aux_code import * #type: ignore
from ui import * #type: ignore
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

def iconFromBase64(base64):
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    icon = QtGui.QIcon(pixmap)
    return icon

def clicked_presence(button):
    if button.isChecked():
        send(3, 1)
    else:
        send(3, 0)

def scroll(scroll, inter):
    value = int((scroll.value() / 100) * max_lum)
    inter.scroll_value.setText(str(value))
    send(4, str(value) + lum_unit)

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
        self.presen_switch.toggled.connect(lambda: clicked_presence(self.presen_switch))
        self.scroll_lum.valueChanged.connect(lambda: scroll(self.scroll_lum, self))
    

def main():
    global object_gui, zone, temp_interval, hum_interval
    print("[+]Running...")
    app = QApplication(sys.argv)
    object_gui = GUI()
    object_gui.principal_text.setText("Control panel -> zone " + str(zone))
    object_gui.show()
    object_gui.temp_cancel.setEnabled(False)
    object_gui.hum_cancel.setEnabled(False)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()