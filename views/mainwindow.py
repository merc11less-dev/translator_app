from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QTextEdit,
                               QListWidget, QGroupBox, QSplitter, QStatusBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Современный артиллерийский словарь")
        self.setMinimumSize(900, 650)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QGroupBox {
                font-size: 15px;
                font-weight: bold;
                border: 1px solid #3a3a4a;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 8px;
                background-color: #2a2a3a;
                color: #cdd6f4;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #89b4fa;
            }
            QLineEdit {
                padding: 12px;
                border: 2px solid #3a3a4a;
                border-radius: 8px;
                font-size: 14px;
                background-color: #313244;
                color: #cdd6f4;
            }
            QLineEdit:focus {
                border-color: #89b4fa;
                background-color: #45475a;
            }
            QTextEdit {
                border: 2px solid #3a3a4a;
                border-radius: 8px;
                padding: 12px;
                background-color: #313244;
                color: #cdd6f4;
                font-size: 16px;
            }
            QListWidget {
                border: 1px solid #3a3a4a;
                border-radius: 8px;
                background-color: #313244;
                color: #cdd6f4;
                outline: none;
            }
            QListWidget::item {
                padding: 6px;
                border-bottom: 1px solid #3a3a4a;
            }
            QListWidget::item:hover {
                background-color: #45475a;
            }
            QListWidget::item:selected {
                background-color: #89b4fa;
                color: #1e1e2e;
            }
            QPushButton {
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 12px;
                background-color: #45475a;
                color: #cdd6f4;
                border: none;
            }
            QPushButton:hover {
                background-color: #585b70;
            }
            QPushButton:pressed {
                background-color: #313244;
            }
            QLabel {
                color: #cdd6f4;
            }
            QStatusBar {
                background-color: #181825;
                color: #a6adc8;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("📖 Современный артиллерийский словарь")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont("Courier new", 24, QFont.Weight.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #89b4fa; margin-bottom: 10px;")
        main_layout.addWidget(title)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(2)

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(15)

        input_group = QGroupBox("🔍 Введите слово на английском")
        input_layout = QVBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Например: AA artillery, AAA, AAAIS...")
        self.search_input.setFont(QFont("Courier new", 14))
        input_layout.addWidget(self.search_input)
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)

        result_group = QGroupBox("📝 Перевод")
        result_layout = QVBoxLayout()
        self.translation_result = QTextEdit()
        self.translation_result.setReadOnly(True)
        self.translation_result.setFont(QFont("Courier new", 16))
        self.translation_result.setMaximumHeight(200)
        self.translation_result.setPlaceholderText("Здесь появится перевод...")
        result_layout.addWidget(self.translation_result)
        result_group.setLayout(result_layout)
        left_layout.addWidget(result_group)

        self.clear_button = QPushButton("🗑 Очистить всё")
        self.clear_button.setFont(QFont("Courier new", 11))
        left_layout.addWidget(self.clear_button)

        self.info_label = QLabel("💡 Введите слово для автоматического перевода")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setFont(QFont("Courier new", 10))
        self.info_label.setStyleSheet("color: #a6adc8; padding: 5px;")
        left_layout.addWidget(self.info_label)

        left_layout.addStretch()

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        suggestions_group = QGroupBox("💡 Похожие слова")
        suggestions_layout = QVBoxLayout()

        hint_label = QLabel("🔍Здесь появятся похожие варианты")
        hint_label.setStyleSheet("color: #a6adc8; padding: 5px;")
        hint_label.setWordWrap(True)
        suggestions_layout.addWidget(hint_label)

        self.suggestions_list = QListWidget()
        self.suggestions_list.setFont(QFont("Courier new", 12))
        self.suggestions_list.setMinimumHeight(300)
        suggestions_layout.addWidget(self.suggestions_list)

        suggestions_group.setLayout(suggestions_layout)
        right_layout.addWidget(suggestions_group)

        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([450, 350])

        main_layout.addWidget(splitter)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Готов к работе")