import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Sbnetter(QWidget):

    def __init__(self):
        super(Sbnetter, self).__init__()

        self.holder_frame = QFrame(self)
        self.output_browser = QTextBrowser(self.holder_frame)
        self.generate_button = QPushButton(self.holder_frame)
        self.subnet_input = QLineEdit(self.holder_frame)
        self.subnet_label = QLabel(self.holder_frame)
        self.subnet_layout = QHBoxLayout()
        self.ip_input = QLineEdit(self.holder_frame)
        self.ip_label = QLabel(self.holder_frame)
        self.ip_layout = QHBoxLayout()
        self.main_layout = QHBoxLayout()
        self.holder_frame_grid = QGridLayout(self.holder_frame)
        self.self_grid = QGridLayout(self)
        self.set_actions()
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        self.resize(782, 576)
        self.setStyleSheet(u"QLabel{\n"
                           "font:  \"Roboto\";\n"
                           "color: rgb(52, 52, 52);\n"
                           "font-size:14px;\n"
                           "background-color: none;\n"
                           "\n"
                           "}\n"
                           "QPushButton{\n"
                           "border:1px solid  rgb(171, 173, 179);\n"
                           "border-radius:6px;\n"
                           "background-color:rgba(171, 173, 179, 0.4);\n"
                           "width:80px;\n"
                           "height:23px;\n"
                           "}\n"
                           "QPushButton:hover {\n"
                           "border:1px solid  rgb(170, 0, 0);\n"
                           "background-color:rgba(171, 173, 179, 0.2);\n"
                           "\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed {\n"
                           "border:1px solid  rgb(170, 0, 0);\n"
                           "background-color:rgba(171, 173, 179, 0.4);\n"
                           "\n"
                           "}\n"
                           "\n"
                           "QLineEdit{\n"
                           "border:1px solid  rgb(171, 173, 179);\n"
                           "font-family: Segoe ui;\n"
                           "font-size: 15px;\n"
                           "border-radius:6px;\n"
                           "width:80px;\n"
                           "height:23px;\n"
                           "} \n"
                           "\n"
                           "QLineEdit:hover{\n"
                           "background-color:rgba(171, 173, 179, 0.5);\n"
                           "}\n"
                           "QTextBrowser{\n"
                           "font-size:20px;\n"
                           "	color: rgb(170, 0, 0);\n"
                           "}")

        self.self_grid.setObjectName(u"self_grid")

        self.holder_frame.setObjectName(u"holder_frame")
        self.holder_frame.setFrameShape(QFrame.StyledPanel)
        self.holder_frame.setFrameShadow(QFrame.Raised)

        self.holder_frame_grid.setObjectName(u"holder_frame_grid")

        self.main_layout.setSpacing(6)
        self.main_layout.setObjectName(u"main_layout")

        self.ip_layout.setObjectName(u"ip_layout")

        self.ip_label.setObjectName(u"ip_label")

        self.ip_layout.addWidget(self.ip_label)

        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setAlignment(Qt.AlignCenter)

        self.ip_layout.addWidget(self.ip_input)

        self.main_layout.addLayout(self.ip_layout)

        self.subnet_layout.setObjectName(u"subnet_layout")

        self.subnet_label.setObjectName(u"subnet_label")

        self.subnet_layout.addWidget(self.subnet_label)

        self.subnet_input.setObjectName(u"subnet_input")
        self.subnet_input.setAlignment(Qt.AlignCenter)

        self.subnet_layout.addWidget(self.subnet_input)

        self.main_layout.addLayout(self.subnet_layout)

        self.generate_button.setObjectName(u"generate_button")

        self.main_layout.addWidget(self.generate_button)

        self.main_layout.setStretch(0, 2)
        self.main_layout.setStretch(1, 2)
        self.main_layout.setStretch(2, 1)

        self.holder_frame_grid.addLayout(self.main_layout, 0, 0, 1, 1)

        self.output_browser.setObjectName(u"output_browser")

        self.holder_frame_grid.addWidget(self.output_browser, 1, 0, 1, 1)

        self.self_grid.addWidget(self.holder_frame, 0, 0, 1, 1)

        QMetaObject.connectSlotsByName(self)

    def set_actions(self):
        self.generate_button.clicked.connect(lambda: self.get_data())

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"subnetting-tool", None))
        self.ip_label.setText(QCoreApplication.translate("self", u"IP", None))
        self.ip_input.setPlaceholderText(QCoreApplication.translate("self", u"Enter network IP", None))
        self.subnet_label.setText(QCoreApplication.translate("self", u"subnet-mask", None))
        self.subnet_input.setPlaceholderText(QCoreApplication.translate("self", u"Enter subnet-mask", None))
        self.generate_button.setText(QCoreApplication.translate("self", u"Generate", None))

    def get_data(self):
        try:
            IP = self.ip_input.text()
            Subnet = self.subnet_input.text()
            IP_binary = self.Int2Bin(IP)
            Subnet_binary = self.Int2Bin(Subnet)

            self.output_browser.append(f"[GETTING DATA] IP: {IP}  IP binary: {IP_binary} \n")
            self.output_browser.append(f"[GETTING DATA] Subnet: {Subnet}  Subnet binary: {Subnet_binary} \n")

            wildcard_binary = self.find_wildcard(self.Int2Bin(Subnet))
            WildCard = self.convert_decimal(wildcard_binary)

            self.output_browser.append(f"[CALCULATED DATA] Wildcard: {WildCard}  wildcard binary: {wildcard_binary} \n")

            networkID = self.andOP(IP, Subnet)
            network_Binary = self.Int2Bin(networkID)

            self.output_browser.append(f"[CALCULATED DATA] networkID: {networkID}  network Binary: {network_Binary} \n")

            broadcastIP = self.orOP(networkID, WildCard)
            broadcastIP_binary = self.Int2Bin(broadcastIP)

            self.output_browser.append(f"[CALCULATED DATA] broadcastIP: {broadcastIP}  broadcastIP binary: {broadcastIP_binary} \n")

            maxIP = self.maxiIP(broadcastIP)
            maxIP_binary = self.Int2Bin(maxIP)

            self.output_browser.append(f"[CALCULATED DATA] maxIP: {maxIP}  maxIP binary: {maxIP_binary} \n")

            minIP = self.miniIP(networkID)
            minIP_binary = self.Int2Bin(networkID)

            self.output_browser.append(f"[CALCULATED DATA] minIP: {minIP}  minIP binary: {minIP_binary} \n")

        except:
            self.output_browser.append(f"ERROR")

    def Int2Bin(self, integer):
        binary = '.'.join([bin(int(x) + 256)[3:] for x in integer.split('.')])
        return binary

    # Wild Card
    def complement(self, number):
        if number == '0':
            number = '1'
        elif number == '.':
            pass
        else:
            number = '0'
        return number

    def find_wildcard(self, binary_subnet):
        binary_list = list(binary_subnet)
        wildcard = ''.join(self.complement(binary_list[y]) for y in range(len(binary_list)))
        return wildcard

    def convert_decimal(self, wildcard_Binary):
        binary = {}
        for x in range(4):
            binary[x] = int(wildcard_Binary.split(".")[x], 2)
        dec = ".".join(str(binary[x]) for x in range(4))
        return dec

    # Network ID
    def andOP(self, IP1, IP2):
        ID_list = {}
        for y in range(4):
            ID_list[y] = int(IP1.split(".")[y]) & int(IP2.split(".")[y])
        ID = ".".join(str(ID_list[z]) for z in range(4))
        return ID

    # Broadcast IP
    def orOP(self, IP1, IP2):
        Broadcast_list = {}
        for z in range(4):
            Broadcast_list[z] = int(IP1.split(".")[z]) | int(IP2.split(".")[z])
        broadcast = ".".join(str(Broadcast_list[c]) for c in range(4))
        return broadcast

    # Max IP
    def maxiIP(self, brdcstIP):
        maxIPs = brdcstIP.split(".")
        if int(brdcstIP.split(".")[3]) - 1 == 0:
            if int(brdcstIP.split(".")[2]) - 1 == 0:
                if int(brdcstIP.split(".")[1]) - 1 == 0:
                    maxIPs[0] = int(brdcstIP.split(".")[0]) - 1
                else:
                    maxIPs[1] = int(brdcstIP.split(".")[1]) - 1
            else:
                maxIPs[2] = int(brdcstIP.split(".")[2]) - 1
        else:
            maxIPs[3] = int(brdcstIP.split(".")[3]) - 1
        return ".".join(str(maxIPs[x]) for x in range(4))

    # Min IP
    def miniIP(self, ntwrkID):
        miniIPs = ntwrkID.split(".")
        if int(ntwrkID.split(".")[3]) + 1 == 256:
            if int(ntwrkID.split(".")[2]) + 1 == 256:
                if int(ntwrkID.split(".")[1]) + 1 == 256:
                    miniIPs[0] = int(ntwrkID.split(".")[0]) + 1
                    miniIPs[1] = 0
                    miniIPs[2] = 0
                    miniIPs[3] = 0
                else:
                    miniIPs[1] = int(ntwrkID.split(".")[1]) + 1
                    miniIPs[2] = 0
                    miniIPs[3] = 0
            else:
                miniIPs[2] = int(ntwrkID.split(".")[2]) + 1
                miniIPs[3] = 0
        else:
            miniIPs[3] = int(ntwrkID.split(".")[3]) + 1
        return ".".join(str(miniIPs[x]) for x in range(4))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    sbnetter = Sbnetter()
    sbnetter.show()

    sys.exit(app.exec_())