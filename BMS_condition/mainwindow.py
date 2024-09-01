from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget,QButtonGroup
from ui_bms import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BMS状态监测系统")

        group_1 = QButtonGroup(self)
        group_1.setExclusive(True)
        group_1.addButton(self.charge_mos_on)
        group_1.addButton(self.charge_mos_off)
        self.charge_mos_off.setChecked(True)

        group_2 = QButtonGroup(self)
        group_2.setExclusive(True)
        group_2.addButton(self.charge_average_off)
        group_2.addButton(self.charge_average_on)
        self.charge_average_off.setChecked(True)

        group_3 = QButtonGroup(self)
        group_3.addButton(self.tem_pro_on)
        group_3.addButton(self.tem_pro_off)
        self.tem_pro_off.setChecked(True)

        group_4 = QButtonGroup(self)
        group_4.addButton(self.discharge_mos_on)
        group_4.addButton(self.discharge_mos_off)
        self.discharge_mos_off.setChecked(True)

