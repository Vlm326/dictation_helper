## README

### Описание Проекта

Этот проект представляет собой интерактивную программу для проверки слов с помощью текста, преобразованного в речь используя библиотеку `pyttsx3`. Программа позволяет пользователю загрузить файл с текстом, после чего она случайным образом выбирает слова из файла и просит пользователя их повторить. Программа проверяет ввод пользователя и предоставляет обратную связь через голосовые сообщения и визуальные указания.

### Установка

Чтобы запустить этот проект, вам необходимо установить следующие библиотеки:

- `pyttsx3` для текста к речи
- `PySimpleGUI` для графического интерфейса

Установите эти библиотеки используя pip:

```bash
pip install pyttsx3 PySimpleGUI
```

Если во время установки  ошибки, убедитесь, что ваша версия `wheel` обновлена:

```bash
pip install --upgrade wheel
```

Для систем Linux, если голосовой вывод не работает, установите следующие пакеты:

```bash
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

### Использование

1. **Загрузка Файла**:
   - Программа запросит путь к файлу с текстом.
   - Файл должен быть в кодировке UTF-8.

2. **Проверка Слов**:
   - Программа случайным образом выбирает слова из файла и просит пользователя их повторить.
   - Пользователь может использовать команды:
     - `след` - пропустить текущее слово.
     - `остановить` - выйти из программы.

3. **Обратная Связь**:
   - Программа дает голосовую и визуальную обратную связь о правильности введенного слова.
   - Ошибочные слова отображаются в отдельном поле.

### Код

Код состоит из нескольких функций:
- `delete_bad_signes_from_words`: Удаляет ненужные символы из слов.
- `reading_file`: Читает файл и возвращает список слов.
- `Input_processing`: Обрабатывает ввод пользователя и дает обратную связь.
- `main`: Основная функция, управляющая графическим интерфейсом и логикой программы.

### Английская Версия

## README

### Project Description

This project is an interactive program for word checking using text-to-speech conversion with the `pyttsx3` library. The program allows the user to load a text file, then randomly selects words from the file and asks the user to repeat them. The program checks the user's input and provides feedback through voice messages and visual indications.

### Installation

To run this project, you need to install the following libraries:

- `pyttsx3` for text-to-speech
- `PySimpleGUI` for the graphical interface

Install these libraries using pip:

```bash
pip install pyttsx3 PySimpleGUI
```

If you encounter installation errors, ensure your `wheel` version is updated:

```bash
pip install --upgrade wheel
```

For Linux systems, if voice output does not work, install the following packages:

```bash
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

### Usage

1. **File Loading**:
   - The program will prompt for the path to a text file.
   - The file should be in UTF-8 encoding.

2. **Word Checking**:
   - The program randomly selects words from the file and asks the user to repeat them.
   - The user can use the following commands:
     - `next` - skip the current word.
     - `stop` - exit the program.

3. **Feedback**:
   - The program provides voice and visual feedback on the correctness of the entered word.
   - Incorrect words are displayed in a separate field.

### Code

The code consists of several functions:
- `delete_bad_signes_from_words`: Removes unnecessary characters from words.
- `reading_file`: Reads the file and returns a list of words.
- `Input_processing`: Processes the user's input and provides feedback.
- `main`: The main function that manages the graphical interface and program logic.