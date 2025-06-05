import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolButton, QLabel,
                             QScrollArea, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import QPropertyAnimation, Qt


class CollapsibleWidget(QWidget):
    def __init__(self, layout, title="", parent=None):
        super().__init__(parent)

        self.setGeometry(500, 500, 600, 500)

        # Кнопка для сворачивания/разворачивания
        self.toggle_button = QToolButton(text=title, checkable=True, checked=False)
        self.toggle_button.setStyleSheet("QToolButton { border: none; font-weight: bold; }")
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.RightArrow)
        self.toggle_button.toggled.connect(self.on_toggle)

        # Область с контентом (скрываемая)
        self.content_area = QScrollArea()
        self.content_area.setStyleSheet("background: #f8f8f8;")
        self.content_area.setWidgetResizable(True)
        self.content_area.setMaximumHeight(0)  # Начальное состояние - свернуто
        self.content_area.setMinimumHeight(0)

        # Внутренний контент
        self.content_widget = QWidget()
        self.content_widget.setMinimumSize(400, 400)

        self.content_widget.setLayout(layout)
        self.content_area.setWidget(self.content_widget)


        # Основной макет
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.addWidget(self.toggle_button)
        main_layout.addWidget(self.content_area)

    def on_toggle(self, checked):
        # Меняем стрелку
        self.toggle_button.setArrowType(Qt.DownArrow if checked else Qt.RightArrow)

        # Вычисляем высоту контента
        content_height = self.content_widget.sizeHint().height()

        # Анимация
        animation = QPropertyAnimation(self.content_area, b"maximumHeight")
        animation.setDuration(50)
        animation.setStartValue(0 if checked else content_height)
        animation.setEndValue(content_height if checked else 0)
        animation.start()

