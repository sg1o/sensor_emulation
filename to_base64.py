from PyQt5 import QtCore, QtGui

def Base64ToBytes(filename):
    image = QtGui.QImage(filename)
    ba = QtCore.QByteArray()
    buff = QtCore.QBuffer(ba)
    image.save(buff, "PNG")
    return ba.toBase64().data()

if __name__ == '__main__':
    val = Base64ToBytes("settings-icon.png")
    print(val)