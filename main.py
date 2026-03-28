import sys
from PySide6.QtWidgets import QApplication

from models.dictionary_model import DictionaryModel
from views.mainwindow import MainWindow
from controllers.dictionary_controller import DictionaryController


def main():
    app = QApplication(sys.argv)
    model = DictionaryModel(file_path='sources/words.xlsx')
    view = MainWindow()
    controller = DictionaryController(model, view)
    controller.run()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()