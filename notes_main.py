#начни тут создавать приложение с умными заметка
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,  QPushButton,
    QLabel, QVBoxLayout,QHBoxLayout,
    QTextEdit,QListWidget, QLineEdit, QInputDialog)
import json
def show_note():
    key = notes_list.selectedItems()[0].text()
    note_text.setText(notes[key]["текст"])
    tag_list.clear()
    tag_list.addItems(notes[key]["теги"])
def add_note():
    notes_name, ok = QInputDialog.getText(
        window, "Добавление заметки", "Название:"
    )
    if ok:
        notes[notes_name] = {
            "текст": "",
            "теги": []
        }
        notes_list.addItem(notes_name)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file,
            sort_keys=True,ensure_ascii=False)
def del_note():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        del notes[key]
        notes_list.clear()
        notes_list.addItems(notes)
        note_text.clear()
        tag_list.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file,
            sort_keys=True,ensure_ascii=False)
def save_note():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        notes[key]['текст'] = note_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file,
            sort_keys=True,ensure_ascii=False)
def add_tag():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = tag_edit.text()
        if tag != ''  and not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            tag_list.addItem(tag)
            tag_edit.clear()
            with open("notes_data.json", "w") as file:
                json.dump(notes, file,
                sort_keys=True,ensure_ascii=False)
def  del_tag():
    if tag_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = tag_list.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        tag_list.clear()
        tag_list.addItems(notes[key]['теги'])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file,
            sort_keys=True,ensure_ascii=False)
def search_tag():
    tag = tag_edit.text()
    if tag and btn6.text() == "Искать заметки по тегу":
        notes_filtered = dict()
        for key in notes:
            if tag in notes[key]['теги']:
                notes_filtered[key] = notes[key]
        btn6.setText('Сбросить поиск')
        notes_list.clear()
        tag_list.clear()
        note_text.clear()
        notes_list.addItems(notes_filtered)
    else:
        tag_edit.clear()
        btn6.setText('Искать заметки по тегу')
        notes_list.clear()
        notes_list.addItems(notes)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Умные заметки")
window.resize(900, 600)
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
note_text = QTextEdit()
tag_list = QListWidget()
notes_list = QListWidget()
btn1 = QPushButton("Создать заметку")
btn2 = QPushButton("Удалить заметку")
btn3 = QPushButton("Сохранить заметку")
btn4 = QPushButton("Добавить к заметке")
btn5 = QPushButton("Открепить от заметки")
btn6 = QPushButton("Искать заметки по тегу")
tag_edit = QLineEdit()
tag_edit.setPlaceholderText("Введите тег...")
notes_list_name = QLabel("Список заметок")
tag_list_name = QLabel("Список тегов")
v_line1.addWidget(note_text)
v_line2.addWidget(notes_list_name)
v_line2.addWidget(notes_list)
v_line2.addLayout(h_line2)
h_line2.addWidget(btn1)
h_line2.addWidget(btn2)
v_line2.addWidget(btn3)
v_line2.addWidget(tag_list_name)
v_line2.addWidget(tag_list)
v_line2.addWidget(tag_edit)
v_line2.addLayout(h_line3)
h_line3.addWidget(btn4)
h_line3.addWidget(btn5)
v_line2.addWidget(btn6)
h_line1.addLayout(v_line1)
h_line1.addLayout(v_line2)
window.setLayout(h_line1)
with open("notes_data.json", "r") as file:
    notes = json.load(file)
    notes_list.addItems(notes)
notes_list.itemClicked.connect(show_note)
btn1.clicked.connect(add_note)
btn2.clicked.connect(del_note)
btn3.clicked.connect(save_note)
btn4.clicked.connect(add_tag)
btn5.clicked.connect(del_tag)
btn6.clicked.connect(search_tag)
window.show()
app.exec()