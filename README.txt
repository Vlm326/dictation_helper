## README File for Text-to-Speech Learning Project

### Project Description

#### Русский
Этот проект предназначен для создания интерактивной учебной программы, которая помогает пользователям学习 и запоминать слова из файла используя текст-to-speech технологию. Программа читает слова из файла, а пользователь должен повторить их. Программа проверяет правильность ответов и предоставляет обратную связь.

#### English
This project is designed to create an interactive learning program that helps users learn and memorize words from a file using text-to-speech technology. The program reads words from a file, and the user must repeat them. The program checks the correctness of the answers and provides feedback.

### Installation

#### Русский
Чтобы запустить этот проект, вам необходимо установить библиотеку `pyttsx3`. Вы можете сделать это используя следующую команду в терминале:

```bash
pip install pyttsx3
```

Если出现 ошибки установки, убедитесь, что вы обновили версию `wheel`:

```bash
pip install --upgrade wheel
```

#### English
To run this project, you need to install the `pyttsx3` library. You can do this using the following command in the terminal:

```bash
pip install pyttsx3
```

If you encounter installation errors, ensure you have upgraded your `wheel` version:

```bash
pip install --upgrade wheel
```

### Usage

#### Русский
1. **Ввод пути к файлу**: Программа запрашивает путь к файлу, содержащему слова для обучения.
2. **Ввод разделителя**: Программа запрашивает тип разделителя, используемого в файле для разделения слов.
3. **Чтение и проверка**: Программа читает слова из файла, а пользователь должен повторить каждое слово. Программа проверяет правильность ответов и предоставляет обратную связь.

#### English
1. **File Path Input**: The program prompts for the path to the file containing the words for learning.
2. **Delimiter Input**: The program prompts for the type of delimiter used in the file to separate the words.
3. **Reading and Checking**: The program reads the words from the file, and the user must repeat each word. The program checks the correctness of the answers and provides feedback.

### Code Explanation

```python
import pyttsx3
import time

# Input path to the file and type of delimiter
path = str(input('Input path to your file: ').strip())
type_of_spliter = str(input('Type of spliter: ').strip())

try:
    # Read the file and split the content into words
    with open(path, encoding='utf-8') as file:
        words = []
        lst = [line.strip() for line in file if line != ' ']
        for i in range(len(lst)):
            if len(lst[i]) > 1:
                for i in lst[i].replace("'", '').strip().split(type_of_spliter):
                    words.append(i)
except:
    print('file not found, try again')
    exit()

errors = []
engine = pyttsx3.init()

# Iterate through the words, speak them, and check user input
for i in range(len(words)):
    engine.say(words[i])
    engine.runAndWait()
    time.sleep(2)
    inp = str(input()).strip()
    if inp == words[i]:
        print('Correct!')
    elif inp == 'след':  # Skip to the next word
        continue
    else:
        engine.say('Неправильно!')
        time.sleep(1)
        engine.runAndWait()
        print('Incorrect!')
        print(f'The correct word is: {words[i].strip()}')
        errors.append(words[i])

# Print the list of incorrect words
for i in errors:
    print(i)
```

### Features

- **Offline Text-to-Speech**: Программа работает без подключения к интернету.
- **Interactive Learning**: Пользователь взаимодействует с программой, повторяя слова и получая обратную связь.
- **Customizable**: Пользователь может выбрать тип разделителя и путь к файлу.

### Supported Platforms

- **Windows**: Использует SAPI5.
- **Mac OS X**: Использует NSSpeechSynthesizer.
- **Linux**: Использует eSpeak.

### Additional Requirements for Linux

Если на Linux голосовой вывод не работает, необходимо установить следующие пакеты:

```bash
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```