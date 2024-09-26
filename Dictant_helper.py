import pyttsx3
import time

path = str(input('Input path to your file: ').strip())
type_of_spliter = str(input('Type of spliter: ').strip())

try:
    with open(fr'path', encoding='utf-8') as file:
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
