from enum import Enum
from note import Note
import json, random
from time import time

class Command(Enum):
    Show = 1
    ShowFull = 2
    Add = 3
    Validate = 4
    Exit = 5
    Errors = 99

farewells = [
    'Пока!',
    'Прощай',
    'Goodbye',
    'Ok! Bye Bye',
    'Bye'
]

def main():
  notes = load_notes_from_file()
  if not notes:
      notes = [Note("The first starting note hash" + Note.Splitter + "The first starting note")]

  command = ""
  com = Command.Show

  while com != Command.Exit:
    # Очистка консоли
    print("\033[H\033[J")
    # Спрашивает, что пользователь хочет сделать
    print("\033[32mДействия: \033[0m")
    print("\033[37m1 - Посмотреть текст заметок\n2 - Посмотреть заметки\n3 - Добавить заметку\n4 - Проверить блокчейн\n5 - Выход)\n\033[0m")
    print("\033[32mВаш выбор: \033[0m")

    command = input().strip()

    try:
        com = Command(int(command))
    except ValueError:
        # Если ввод не был корректным
        com = Command.Errors
        print("Шо ты ввел?")

    if com == Command.Show:
        write_all_notes(notes)
    elif com == Command.ShowFull:
        write_full_notes(notes)
    elif com == Command.Add:
        print("\033[32mВведите текст заметки: \033[0m")
        text = input().strip()
        add_note(text, notes)
    elif com == Command.Validate:
        validate_notes(notes)
    elif com == Command.Exit:
        print(f"\033[34m{random.choice(farewells)}\033[0m")

    input("\nНажми Enter чтобы продолжить...")

def validate_notes(notes):
    for i in range(len(notes)):
        _, hash = notes[i - 1].HashString
        if i == 0:
            print(f"\033[32mЗаметка {notes[0].ClearText} - OK\033[0m")
        else:
            if notes[i].PreviousHash == hash:
                print(f"\033[32mЗаметка {notes[i].ClearText} - OK\033[0m")
            else:
                print(f"\033[31mЗаметка {notes[i].ClearText} - Изменена\033[0m")

def add_note(text, notes):
    _, hash = notes[-1].HashString
    notes.append(Note(hash + Note.Splitter + text))
    save_notes_to_json(notes)

def write_all_notes(notes):
    print("\033[32mЗаметки: \033[0m")
    for i, note in enumerate(notes):
        write_note(note, i)

def write_full_notes(notes):
    print("\033[32mЗаметки: \033[0m")
    for i, note in enumerate(notes):
        write_note_full(note)

def write_note(note, i):
    print(str(i+1) + " - " +note.ClearText)

def write_note_full(note):
    _, hash = note.HashString
    print(f"Текст: {note.Text}\nЧистый текст: {note.ClearText}\nХэш: {hash}\n")

def load_notes_from_file():
    try:
        with open('blockchain.json', 'r') as file:
            data = json.load(file)
            notes_data = data.get('response', {}).get('notes', [])
            #notes_data = notes_data = [block['Note'] for block in data.get('response', {}).get('blockchain', [])]
            notes = [Note(note_data['Text']) for note_data in notes_data]
            return notes
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файл не существует или пуст, возвращается пустой список заметок
        return []

def save_notes_to_json(notes):
    data = {
        "response": {
            "count": len(notes),
            "notes": []
        }
    }

    for i, note in enumerate(notes):
        proof, hash = note.HashString
        note_data = {
            "index": i + 1,
            "Text": note.Text,
            "ClearText": note.ClearText,
            "PreviousHash": note.PreviousHash,
            "Hash": hash,
            "Proof": proof,
            "Created_at": time()
        }
        data["response"]["notes"].append(note_data)

    with open("blockchain.json", "w") as file:
        json.dump(data, file, indent=2)

main()