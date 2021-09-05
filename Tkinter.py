def say_hello():
    print('hello')

def add_label():  #  Функиця для создания Виджет Label в нашем окне приложения win с текстом NEW
    label = tk.Label(win, text='new')
    label.pack()

def counter():  #  Счетчик, что при каждом нажатии на кнопке меняется число на +1
    global count
    count += 1
    btn4['text'] = f'Счетчик: {count}'
#     label = tk.Label(win, text=f'Счетчик: {count}')  # Для того, что бы выводить строчки на жкране
#     label.pack()

def get_entry():
    value = name.get()  # Получаем, то что напечатали в Entry. С помощью get()
    if value:  # Если текст не пустой
        print(value)
    else:
        print('Entry Empty')

def delete_entry():  # Функция удаления текста
    name.delete(0, tk.END)  # Мы удаялем с 0 индекса по tk.END - по последний

def submit():  # Выведем, что содержиться в окне name и password
    print(name.get())
    print(password.get())
    delete_entry()  # Выводим функцию удаления текста из Name
    password.delete(0, tk.END)  # удаялем текст из графы password


import tkinter as tk

# Создаем окно приложения: Tk - это класс tkinter
win = tk.Tk()

# Изменим ярлычек нашего приложения
photo = tk.PhotoImage(file = 'fun.png')  # Указываем путь нашей картинки
# Вставляем наше фото как иконку приложения
win.iconphoto(False, photo)

# Изменим фон приложения
# bg = background (перевод фон), ассоциация какой у тебя бекраунд
# config - от слова конфигурация
win.config(bg='white')  # Или так:  bg=#1AFF00

# Изменим title - название приложения
win.title('Мое первое приложение')

# Изменим размеры приложения: '500x600' geometry - геометрия приложения
# И Изменим область появления приложения: +100+200 Это отступ от левого верхнего края экрана
win.geometry('400x500+100+200')

# Настройка дает разрешение изменения ширины и высоты приложения, по умолчанию True
# resizable - изменяемый размер (ассоциация резать, то есть изменять)
win.resizable(True, True)

# Минимальный и максимальный размер окна для изменений
# size - размер (ассоциация size в покере = размер ставки)
win.minsize(300,400)
win.maxsize(700,800)

print('------Виджет Label---------')
# Знакоство с виджетами. Виджет Label - Лейбл, в переводе этикетка
# Для отображения текстовой информации, создадим лейбл:
# Первый параметр win, где мы будет располагать окно
label_1 = tk.Label(win, text = 'Hello!', # Второй параметр text, что мы будет показывать на экране
                   bg = 'red',  # Фон этого окна Лейбла
                   fg = 'white',  # font ground - цвет шрифта
                   font = ('Arial', 20, 'bold'),  # Шрифт: Стиль, Размер, Ширинра шрифта
                   padx = 20,  # Отступ фона по X лейбла от текста (горизонталь)
                   pady = 40,  # Отступ фона по Y лейбла от текста (вертикаль)
                   width = 20,  # Это кол-во букв, которые уместяться в этом Лейбле по горизонтали
                   height = 10, # Это кол-во букв, которые уместяться в этом Лейбле по вертикали
                   anchor = 'sw',  #  n=Север s=Юг w=Запад e=Восток. По умолчанию центр
                   relief = tk.RAISED,  # Оптикание нашей кнопки. RAISED - Поднятый, как в покере рейз
                   bd = 10,  #  на сколько поднять кнопку. Ширина оптикания
                   justify = tk.CENTER  # Отвечает за выравнивание текста. justify - Выравнивание
                   # justify - есть выравнивание по LEFT и RIGHT
                   )

# Теперь поместим этот Лейбл:
label_1.pack()  # pack - пакет, упаковка
'''
'''
print('------Виджет Button - КНОПКА---------')
# Первый параметр win, где мы будет располагать Кнопку
# Второй параметр text, какой текст мы будет показывать на кнопке
btn1 = tk.Button(win, text = 'Hello',
                 # Это наш обработчик, то есть что делать при нажатии на кнопку - вызывается функция
                 command = say_hello    # Вызываем функцию без скобок, что бы она работала только при вызове
                 )

btn2 = tk.Button(win, text = 'Add new label',
                 command = add_label    # Вызываем функцию, которая будет создавать Лейбл, то есть окно
                 )

btn3 = tk.Button(win, text = 'Add new label lambda',  # Создаем функцию через lambda
                 # Вызываем функцию, которая будет создавать Лейбл, то есть окно
                 command = lambda: tk.Label(win, text='new lambda').pack()
                 )

count = 0  # Это для нашего счетчика нажатий
btn4 = tk.Button(win, text = f'Счетчик: {count}',  #
                 command = counter,
                 bg = 'red',  # Меняем цвет кнопки
                 activebackground = 'blue',  # Это что происходит при нажатии кнопки, менятся цвет
                 state = tk.NORMAL  #  Кнопка не активна: DISABLED - Enabled
                 )

btn1.pack()  # Разместим нашу кнопку на экране
btn2.pack()
btn3.pack()
btn4.pack()
'''

'''
btn1 = tk.Button(win, text = 'Hello 1')
btn2 = tk.Button(win, text = 'Hello 2')
btn3 = tk.Button(win, text = 'Hello 3')
btn4 = tk.Button(win, text = 'Hello world')
btn5 = tk.Button(win, text = 'Hello 5')
btn6 = tk.Button(win, text = 'Hello 6')
btn7 = tk.Button(win, text = 'Hello 7')
btn8 = tk.Button(win, text = 'Hello 8')

# grid Это расположение кнопок слева вверху. grid - Сетка. Ассоциация: Горит - сетка горит
btn1.grid(row=0, column=0)  # Задается расположение row - рядов и column - столбцев
btn2.grid(row=0, column=1, stick = 'w')  # stick ассоциация Стикер - Наклейка. То есть нраклеить слева,справа..
btn3.grid(row=1, column=0, stick = 'we')
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1, stick = 'e')
# columnspan - это сколько кнопок должно занимать пространство кнопки
# stick - это растягивание кнопки по сторонам света: n=Север s=Юг w=Запад e=Восток
btn7.grid(row=3, column=0, columnspan = 2, stick = 'we')
btn8.grid(row=0, column=3, rowspan = 4, stick = 'ns')

#  То что мы расположили выше, можно сделать через циклы:
for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'Hello {i} {j}').grid(row=i, column = j, stick = 'we')

print('-------------ВИДЖЕТ ENTRY---------')
# ВИДЖЕТ ENTRY - Вход текстовой информации, от слова Enter

# Располагаем label1 на окне win с текстом 'Имя' в 0 ряду 0 столбце, придерживаться запада
label1 = tk.Label(win, text='Имя').grid(row=0, column=0, stick = 'w')

name = tk.Entry(win) # Располагаем Entry в нашем окне программы win
name.grid(row = 0, column = 1)  # Располагаем Entry-ввод текста в 0 ряду, 1 столбце.

# Создадим виджет где будет вводить пароль
label2 = tk.Label(win, text='Пароль').grid(row=1, column=0, stick = 'w')
password = tk.Entry(win, show = '*')  # show - Это для скрытия текста, и замены каждого символа на *
password.grid(row = 1, column = 1)

# Создадим кнопку
tk.Button(win, text = 'get', command = get_entry).grid(row=2, column = 0, stick = 'we')
# Создадим кнопку для удаления набранного текста
tk.Button(win, text = 'delete', command = delete_entry).grid(row=2, column = 1, stick = 'we')
#
tk.Button(win, text = 'submit', command = submit).grid(row=3, column = 0, stick = 'we')
# Создадим кнопку для вставки определенного текста в 0 позицию, текст: hello
tk.Button(win, text = 'insert', command = lambda: name.insert(0, 'hello')).grid(row=2, column = 2, stick = 'we')


# Для задания размера нашей колонки. columnconfigure - конфигурация колонки
# Первый параметр - это индекс колонки
win.grid_columnconfigure(0, minsize=100)  # Растягивается первая колонка до размеров 200
win.grid_columnconfigure(1, minsize=100)

# Что бы запустить окно, нужно запустить цикл: main loop - перевод основной цикл
win.mainloop()
# Запуститься окно, которое будет ожидать дальнейших дуйствий

