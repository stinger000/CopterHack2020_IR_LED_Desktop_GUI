from Layout.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QObject, QThread
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QProgressBar, QTextEdit, QVBoxLayout, QCheckBox
import sys
import time
import serial
from serial.tools.list_ports import comports


class SerialReceiver(QThread):
    received_data = pyqtSignal(str)

    def __init__(self, mainWindow, parent=None):
        super().__init__()
        self.mainWindow = mainWindow

    def run(self) -> None:
        print("connected")
        while True:
            if not self.mainWindow.connected:
                break
            if self.mainWindow.ser.inWaiting() > 0:
                msg = self.mainWindow.ser.readline().decode("ascii")
                # print(msg)
                self.received_data.emit(msg)
            QThread.msleep(100)


class Counter(QThread):
    update = pyqtSignal(int)

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.millis = 0

    def run(self) -> None:
        self.millis = 0
        startTime = time.time()
        while True:
            if not self.mainWindow.counting:
                break
            delta = int((time.time() - startTime) * 1000)  # delta time in milliseconds
            self.update.emit(delta)
            QThread.msleep(2)


class MainWindow(QMainWindow, Ui_MainWindow):
    laps: int

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.update_comports()
        self.ser = serial.Serial()
        self.connected = False
        self.counting = False
        self.initial_time = None
        self.laps = 0
        self.receiver = SerialReceiver(self)
        self.counter = Counter(self)
        self.receiver.received_data.connect(self.received_data)
        self.counter.update.connect(self.update_counter)
        self.btnConnect.clicked.connect(self.btn_connect_clicked)
        self.btnStart.clicked.connect(self.start_counting)
        self.btnStop.clicked.connect(self.stop_counting)

    def update_comports(self):
        self.comboSerial.clear()
        for port in comports():
            self.comboSerial.addItem(port.description, userData=port.device)
        print("comport list updated")

    @pyqtSlot()
    def start_counting(self):
        if self.connected:
            self.counting = True
            self.initial_time = None
            self.laps = 0
            self.listData.clear()
            self.ser.write("A".encode("ascii"))
            self.counter.start()

    @pyqtSlot()
    def stop_counting(self):
        self.counting = False

    @pyqtSlot(str)
    def received_data(self, string):
        if self.counting:
            current_time = int(string)
            if self.initial_time is None:
                self.initial_time = current_time
            else:
                # print(self.millis_to_string(self, current_time - self.initial_time))
                item = QListWidgetItem()
                item.setText(f"lap {self.laps}: {self.millis_to_string(self, current_time - self.initial_time)}")
                self.laps += 1
                self.listData.addItem(item)

    @pyqtSlot(int)
    def update_counter(self, millis):
        string = self.millis_to_string(self, millis)
        self.labelClock.setText(string)

    @pyqtSlot()
    def btn_connect_clicked(self):
        if not self.connected:
            try:
                self.ser = serial.Serial(self.comboSerial.currentData(), baudrate=115200)
            except (OSError, serial.SerialException):
                QMessageBox.critical(None, "Error", "Can't open serial device!")
                return
            self.connected = True
            self.btnConnect.setText("Disconnect")
            self.comboSerial.setEnabled(False)
            self.receiver.start()
        else:
            self.restore_serial()

    def restore_serial(self):
        if self.ser.isOpen():
            self.ser.close()
        self.btnConnect.setText("Connect")
        self.comboSerial.setEnabled(False)
        self.connected = False
        self.update_comports()

    @staticmethod
    def millis_to_string(self, millis: int) -> str:
        hours = int(millis // (60 * 60 * 1000))
        minutes = int((millis // (60 * 1000)) % 60)
        seconds = int((millis // 1000) % (60))
        millis = int(millis % 1000)
        if hours < 10:
            hours = '0' + str(hours)
        else:
            hours = str(hours)
        if minutes < 10:
            minutes = '0' + str(minutes)
        else:
            minutes = str(minutes)
        if seconds < 10:
            seconds = '0' + str(seconds)
        else:
            seconds = str(seconds)
        if millis < 10:
            millis = '00' + str(millis)
        elif millis < 100:
            millis = '0' + str(millis)
        else:
            millis = str(millis)
        return f"{minutes}:{seconds}:{millis}"

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.ser.isOpen():
            self.ser.close()


if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
