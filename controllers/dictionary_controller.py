from PySide6.QtCore import QTimer

from models.dictionary_model import DictionaryModel
from views.mainwindow import MainWindow


class DictionaryController:

    def __init__(self, model: DictionaryModel, view: MainWindow):
        self.model = model
        self.view = view

        self.search_timer = QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.perform_search)

        self.view.search_input.textChanged.connect(self.on_text_changed)
        self.view.clear_button.clicked.connect(self.on_clear)

    def on_text_changed(self, text: str) -> None:
        self.search_timer.start(300)

    def perform_search(self) -> None:
        word = self.view.search_input.text().strip()
        translation = self.model.get_translation(word)

        if translation:
            self.view.translation_result.setText(translation)
        else:
            self.view.translation_result.setText(word)

    def on_clear(self) -> None:
        self.view.search_input.clear()
        self.view.translation_result.clear()
        self.view.info_label.setText("Введите слово для поиска")
        self.view.status_bar.showMessage("Готов к работе")

    def run(self) -> None:
        self.view.show()