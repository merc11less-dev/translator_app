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
        self.setWindowTitle("merc11less-dev")
        self.setMinimumSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)

        title = QLabel("📖 Современный артиллерийский словарь")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont("Arial", 20, QFont.Weight.Bold)
        title.setFont(title_font)
        main_layout.addWidget(title)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(15)

        input_group = QGroupBox("Введите слово на английском")
        input_layout = QVBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Например: cat, house, beautiful...")
        self.search_input.setFont(QFont("Arial", 14))
        input_layout.addWidget(self.search_input)
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)

        result_group = QGroupBox("Перевод")
        result_layout = QVBoxLayout()
        self.translation_result = QTextEdit()
        self.translation_result.setReadOnly(True)
        self.translation_result.setFont(QFont("Arial", 16))
        self.translation_result.setMaximumHeight(150)
        self.translation_result.setPlaceholderText("Здесь появится перевод...")
        result_layout.addWidget(self.translation_result)
        result_group.setLayout(result_layout)
        left_layout.addWidget(result_group)

        buttons_layout = QHBoxLayout()

        self.translate_button = QPushButton("🔍 Перевести")
        self.translate_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        buttons_layout.addWidget(self.translate_button)

        self.clear_button = QPushButton("🗑 Очистить")
        self.clear_button.setFont(QFont("Arial", 12))
        buttons_layout.addWidget(self.clear_button)

        left_layout.addLayout(buttons_layout)

        self.info_label = QLabel("⏳ Словарь не загружен")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setFont(QFont("Arial", 10))
        left_layout.addWidget(self.info_label)

        left_layout.addStretch()

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        suggestions_group = QGroupBox("💡 Подсказки (похожие слова)")
        suggestions_layout = QVBoxLayout()

        hint_label = QLabel("🔍 Введите слово, и здесь появятся похожие варианты")
        hint_label.setFont(QFont("Arial", 9))
        hint_label.setStyleSheet("color: #666; padding: 5px;")
        hint_label.setWordWrap(True)
        suggestions_layout.addWidget(hint_label)

        self.suggestions_list = QListWidget()
        self.suggestions_list.setFont(QFont("Arial", 12))
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

        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QGroupBox {
                font-size: 13px;
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #cccccc;
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
            QTextEdit {
                border: 2px solid #cccccc;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton {
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton#translate_button {
                background-color: #2196F3;
                color: white;
            }
            QPushButton#translate_button:hover {
                background-color: #0b7dda;
            }
            QPushButton#clear_button {
                background-color: #ff9800;
                color: white;
            }
            QPushButton#clear_button:hover {
                background-color: #e68900;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #ddd;
            }
            QListWidget::item:hover {
                background-color: #e3f2fd;
            }
            QListWidget::item:selected {
                background-color: #2196F3;
                color: white;
            }
        """)

        self.translate_button.setObjectName("translate_button")
        self.clear_button.setObjectName("clear_button")