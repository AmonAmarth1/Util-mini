from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_mix_camera(QWidget):
    def __init__(self):
        super().__init__()

        self.mix_use = False

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()

        self.layout_mix = QVBoxLayout()

        self.mix_name = QLabel("Камера смешения:")
        self.layout_mix.addWidget(self.mix_name)

        self.mix_use_layout = QHBoxLayout()
        self.mix_use_label = QLabel("Используется:")
        self.mix_use_combo = QComboBox()
        self.mix_use_combo.addItems(['Нет', 'Используется'])
        self.mix_use_layout.addWidget(self.mix_use_label)
        self.mix_use_layout.addWidget(self.mix_use_combo)
        (self.layout_mix.addLayout(self.mix_use_layout))

        self.main_layout.addLayout(self.layout_mix)

        self.setLayout(self.main_layout)

    def clear(self):
        self.mix_use_combo.setCurrentIndex(0)
