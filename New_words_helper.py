import pyttsx3
import PySimpleGUI as sg
import random
import re


engine = pyttsx3.init()

def delete_bad_signes_from_words(word: str) -> str:
    return re.sub(fr'!"#$%&()*+,-./:;<=>?@[\]^_`|~', '', word)

def reading_file() -> list:
    while True:
        path = sg.popup_get_file('Введите путь к файлу:', no_window=True)
        if not path:
            sg.popup('Файл не найден, попробуйте снова')
            continue
        try:
            with open(path, encoding="utf-8") as f:
                words = [delete_bad_signes_from_words(word.strip().lower()) for word in f.readlines()]
                return words
        except FileNotFoundError:
            sg.popup('Файл не найден, попробуйте снова')
        except Exception as e:
            sg.popup(f"Произошла ошибка: {e}")
            return []

def Input_processing(words: list, index: int, inp: str, errors: list, correct_word_display) -> bool:
    if inp == words[index]:
        engine.say('Правильно!')
        correct_word_display.update('Правильно!')  
    elif inp == 'след':
        return True
    elif inp == 'остановить':
        return False
    else:
        engine.say('Неправильно!')
        errors.append(words[index])
        correct_word_display.update(f'Неправильно! Верное слово: {words[index]}') 
    
    engine.runAndWait()
    return True

def main():
    errors = []
    words = reading_file()
    if not words:
        sg.popup("Нет слов для обработки.")
        return

    layout = [
        [sg.Text('Введите слово (Команды: след - пропустить слово, остановить - выход):', justification='center')],
        [sg.Input(key='-INP-', justification='center')],
        [sg.Button('Проверить', bind_return_key=True), sg.Button('Выход')],
        [sg.Text('Результат:', justification='center')],
        [sg.Text('', key='-WORD-', size=(40, 1), justification='center', text_color='Black')],
        [sg.Text('', key='-ERRORS-', size=(40, 10), justification='center')]
    ]
    
    layout = [[sg.Column(layout, element_justification='center', vertical_alignment='center')]]
    
    window = sg.Window('Проверка слов', layout, location=(None, None), finalize=True, resizable=True)
    window['-INP-'].set_focus() 
    
    while True:
        word_index = random.randint(0, len(words) - 1)
        engine.say(words[word_index])
        engine.runAndWait()
        
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Выход':
            break
        
        inp = values['-INP-'].strip().lower()
        
        if not Input_processing(words, word_index, inp, errors, window['-WORD-']):
            break
        
        window['-INP-'].update('')
        window['-ERRORS-'].update("\n".join(errors)) 
        window.refresh()  

    window.close()

if __name__ == "__main__":
    main()
