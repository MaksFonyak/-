import pickle

# Класс для заметки
class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

# Класс для приложения заметок
class NoteApp:
    def __init__(self):
        self.notes = []
        self.load_notes()

    # Метод для загрузки заметок из файла
    def load_notes(self):
        try:
            with open('notes.dat', 'rb') as f:
                self.notes = pickle.load(f)
        except FileNotFoundError:
            self.notes = []

    # Метод для сохранения заметок в файл
    def save_notes(self):
        with open('notes.dat', 'wb') as f:
            pickle.dump(self.notes, f)

    # Метод для добавления новой заметки
    def add_note(self):
        title = input("Введите название заметки: ")
        text = input("Введите текст заметки: ")
        note = Note(title, text)
        self.notes.append(note)
        self.save_notes()
        print("Заметка успешно добавлена.")

    # Метод для просмотра списка заметок
    def view_notes(self):
        if not self.notes:
            print("Заметка не найдена.")
        else:
            for i, note in enumerate(self.notes):
                print(f"{i+1}. {note.title}")

    # Метод для просмотра выбранной заметки
    def view_note_detail(self):
        index = int(input("Введите номер заметки: "))
        note = self.notes[index-1]
        print(f"{note.title}\n{note.text}")

    # Метод для удаления выбранной заметки
    def delete_note(self):
        index = int(input("Введите номер заметки: "))
        self.notes.pop(index-1)
        self.save_notes()
        print("Заметка удалена.")

# Создаем экземпляр приложения заметок
app = NoteApp()

# Основной цикл приложения
while True:
    print("1. Добавление заметки")
    print("2. Просмотр заметки")
    print("3. Просмотр деталей заметки")
    print("4. Удаление заметки")
    print("5. Выход")
    choice = input("Ввведите номер (1-5): ")

    if choice == "1":
        app.add_note()
    elif choice == "2":
        app.view_notes()
    elif choice == "3":
        app.view_note_detail()
    elif choice == "4":
        app.delete_note()
    elif choice == "5":
        print("До встречи!")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
