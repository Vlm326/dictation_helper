import pyttsx3
from PySimpleGUI import popup_get_file, popup
from random import randint
from time import time

def delete_bad_signes_from_words(word: str) -> str:
    for i in '!"#$%&()*+,-./:;<]^_`|~':
        word = word.replace(i, '')
    return word

while True:
    path = popup_get_file('Введите путь к файлу:', no_window=True)
    if not path:
        popup('Файл не найден, попробуйте снова')
        continue
    try:
        with open(path, encoding="utf-8") as f:
            content = []
            for line in f:
                if line == ' ':
                    continue
                if len(line.split()) > 1:
                    for word in line.split():
                        if len(word) > 1 and word != ' nh':
                            content.append(delete_bad_signes_from_words(word.strip().lower()))
                else:
                    content.append(delete_bad_signes_from_words(line.strip().lower()))
        break
    except FileNotFoundError:
        popup('Файл не найден, попробуйте снова')
    except Exception as e:
        print(e)
        popup(f"Произошла ошибка: {e}")

words = content
errors = []
engine = pyttsx3.init()
start = time()
seen_words = []
for j in range(len(words)):
    end = abs(start - time())
    i = randint(0, len(words) - 1)
    while i in seen_words:
        i = randint(0, len(words) - 1)
    seen_words.append(i)
    left = len(words) - j
    engine.say(words[i])
    engine.runAndWait()
    print(f'Words: {len(words)}, words left: {left}, time: {end}')
    inp = str(input("Введите слово: ")).strip()
    if inp == words[i]:
        print('Correct!')
    elif inp == 'след':
        continue
    else:
        engine.say('Неправильно!')
        engine.runAndWait()
        print('Incorrect!')
        print(f'The correct word is: {words[i].strip()}')
        errors.append(words[i])
for i in errors:
    print(i)
