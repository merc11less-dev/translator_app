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
        self.view.suggestions_list.itemClicked.connect(self.on_suggestion_clicked)

    def on_text_changed(self, text: str) -> None:
        self.search_timer.start(300)

    def perform_search(self) -> None:
        word = self.view.search_input.text().strip()

        if not word:
            self.view.translation_result.clear()
            self.view.suggestions_list.clear()
            self.view.info_label.setText("Введите слово для поиска")
            self.view.status_bar.showMessage("Готов к работе")
            return

        translation = self.model.get_translation(word)

        if translation:
            self.view.translation_result.setText(translation)
            self.view.status_bar.showMessage(f"Найден перевод для '{word}'")
            self.view.info_label.setText(f"✓ Перевод найден")
        else:
            self.view.translation_result.setText(word)
            self.view.status_bar.showMessage(f"Слово '{word}' не найдено в словаре")
            self.view.info_label.setText(f"⚠ Слово не найдено, показан введенный текст")

        suggestions = self.model.find_similar_words_with_priority(word, limit=10)
        self.update_suggestions(suggestions)

    def update_suggestions(self, suggestions: list) -> None:
        self.view.suggestions_list.clear()

        if not suggestions:
            self.view.suggestions_list.addItem("Нет похожих слов")
            return

        for word in suggestions:
            self.view.suggestions_list.addItem(word)

    def on_suggestion_clicked(self, item) -> None:
        selected_word = item.text()
        self.view.search_input.setText(selected_word)
        self.perform_search()

    def on_clear(self) -> None:
        self.view.search_input.clear()
        self.view.translation_result.clear()
        self.view.suggestions_list.clear()
        self.view.info_label.setText("Введите слово для поиска")
        self.view.status_bar.showMessage("Очищено")

    def run(self) -> None:
        self.view.show()