import pyttsx3
import time
from PySimpleGUI import popup_get_file
import PySimpleGUI as sg
import re

def delete_bad_signes_from_words(word: str) -> str:
    return re.sub(fr'!"#$%&()*+,-./:;<]^_`|~', '', word)

while True:
    path = sg.popup_get_file('Введите путь к файлу:', no_window=True)
    if not path:
        sg.popup('Файл не найден, попробуйте снова')
        continue
    try:
        with open(path, encoding="utf-8") as f:
            content = []
            for line in f:
                if len(line.split()) > 1:
                    for word in line.split():
                        content.append(delete_bad_signes_from_words(word.lower()))

                else:
                    content.append(delete_bad_signes_from_words(line.lower()))
        break
    except FileNotFoundError:
        sg.popup('Файл не найден, попробуйте снова')
    except Exception as e:
        print(e)
        sg.popup(f"Произошла ошибка: {e}")

words = content
errors = []
engine = pyttsx3.init()
for i in range(len(words)):
    engine.say(words[i])
    engine.runAndWait()
    time.sleep(2)
    inp = str(input()).strip()
    if inp == words[i]:
        print('Correct!')
    elif inp == 'след':
        continue
    else:
        engine.say('Неправильно!')
        time.sleep(1)
        engine.runAndWait()
        print('Incorrect!')
        print(f'The correct word is: {words[i].strip()}')
        errors.append(words[i])
for i in errors:
    print(i)
