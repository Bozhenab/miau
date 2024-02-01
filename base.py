import os
def clear_console(): #очищает консоль
  os.system('clear')
#///////////////////////
vvod = "" #введенное слово
zel = [] # индекс букв с зеленым окрасом в текущем слове
gel = [] # индекс букв с желтым окрасом в екущем слове
lang = 0 #язык игры
name = ""
#///////////////////////
def rus_rules(): #правила
 clear_console()
 print('''У вас будет 6 шансов угадать 5-буквенное слово дня, поэтому учитывайте каждое угадывание!
Попробуйте использовать слово, содержащее много разных букв, чтобы сузить круг ваших будущих предположений.
Введите свое первое предположение, а затем нажмите Enter, чтобы увидеть, совпали ли какие-либо буквы.''')
 print('''
  После того, как вы введете слово, цвета плиток изменятся:

\033[42m Зеленое \033[0m выделение указывает на то, что вы угадали правильную букву в нужном месте слова.
\033[43m\033[30m Желтое \033[0m выделение означает, что вы угадали букву, которая есть в слове, но не в нужном месте.
Серое означает, что этой буквы нет в загаданном слове.''')
 print("Вводите слова до тех пор, пока у вас не закончаться попытки или вы не угадаете слово, которое было загаданно")
 #///////////////////////
def rus_five(use): #из файла с пятибуквенными словами достает то, которое будет загадано (проверяет не было ли его раньше) и добавляет в список с уже использованными
  import random
  with open('/content/drive/MyDrive/fivelet.txt') as file:
    words = [line.rstrip() for line in file]
  find = False
  chisl = int(len(words))
  ran = random.randint(0, chisl)
  while find == 0:
    if ran in use:
      ran = random(0, len(words))
    else:
      ranword = words[ran]
      use.append(ranword)
      game(ranword, 5)
      find = True
#///////////////////////
def game(word, letter): #основной алгоритм игры
  global vvod
  clear_console()
  answ = False
  att = 1 #номер попытки
  for i in range(letter):
    print("_ ", end='')
  print()
  while answ == False and att<=6:
    vvod = input()
    if vvod==word:
      answ==True
      break
    else:
     check(word)
     clear_console()
     vivod(word)
  if answ == True:
    win(vvod)
  else:
    lose(vvod)
  # здесь же ссылка на функцию лидерборд
#///////////////////////
def lose(word):
  if lang == 1:
    print(f"Загаданное слово: {word}")
    print("Вы проиграли")
  #ваш лидерборд
#///////////////////////
def win(word):
  print(f"\033[42m {word} \033[0m")
  if lang == 1:
    print(f"{name}, вы угадали слово, поздравляю!!!")
  # ваш лидерборд
#///////////////////////
def vivod(word): #вывод по цветам
  word_sp = word.split()
  vvod_sp = vvod.split()
  for i in range(len(word_sp)):
    if i in zel:
      print(f"\033[42m {word_sp[i]} \033[0m")
    if i in gel:
      print(f"\033[43m\033[30m {word_sp[i]} \033[0m")
    else:
      print(vvod_sp[i])
#///////////////////////
def check(word): #зелёненькие или желтенькие
  word_sp = word
  vvod_sp = vvod
  zel.clear()
  gel.clear()
  for i in range(0, len(word_sp)):
    if word_sp[i]==vvod_sp[i]:
      zel.append(i)
    elif vvod_sp[i] in word_sp:
      gel.append(i)
#///////////////////////
print("Hello! Welcome to Wordlie")
print("Choose wich language you prefer")
print("Write number of this language")
print("1. русский, 2. english")
lang = int(input())
clear_console()
use = [] #список исполльзованных сло, может стоит сделать для каждого варианта свой
#///////////////////////
if lang == 1:
  print("Введите свое имя")
  name = input()
  print(f"{name}, знаешь правила игры? (да/нет)")
  knowr = input()
  if knowr == "НЕТ" or knowr == "нет" or knowr == "Нет":
    rus_rules()    #функция с правилами на русском языке
  print("Выбирите количество букв в загаданных словах, с которым вы хотите играть (впишите число от 4 до 6)")
  let = int(input())
 # if let == 4:
    #rus_four() #функция со словарем из 4 букв
  if let == 5:
    rus_five(use) #функция со словарем из 5 букв
 # if let == 6:
  #  rus_six() #функция со словарем из 5 букв

#///////////////////////
