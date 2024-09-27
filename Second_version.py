import pyttsx3 
import time
import PySimpleGUI as sg
import random as rn
import string


engine = pyttsx3.init()
def delete_bad_signes_from_words(word: str) -> str:
    for i in str(string.punctuation()):
        word = word.replace(i, '')
    return word

def reading_file() -> None:
    path = str(input('Input path to your file: ').strip())
    try:
        with open(path) as f:
            words = [delete_bad_signes_from_words(word.strip().lower()) for word in f.readlines()]
            return words
    except:
        print('file not found, try again')
        exit()
    if len(words) >= 0:
        return words
    return []

def find_errors(words: list, index: int, inp: str, errors: list) -> None:
    if inp == words[index]:
        engine.say('Правильно!')
        time.sleep(0.2)
        engine.runAndWait()
        return True
    engine.say('Неправильно!')
    time.sleep(0.2)
    engine.runAndWait()
    errors.append(words[index])
    return False

def main():
    errors = []
    words = reading_file()
    while True:
        word_index = rn.randint(0, len(words))
        print(words[word_index])
        engine.say(words[word_index])
        engine.runAndWait()
        time.sleep(0.2)
        print('Comands: след - пропустить слово, остановить - выход')
        inp = input('Введите слово: ').strip().lower()
        find_errors(words, word_index, inp, errors)

main()








