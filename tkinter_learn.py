from tkinter import *

root = Tk()  # создал главное окно (всегда называйте его root)

"""
Listbox - это виджет, который представляет собой список, из элементов которого пользователь может выбирать 
один или несколько пунктов. Имеет дополнительное свойство selectmode, которое, при значении SINGLE, 
позволяет пользователю выбрать только один элемент списка, а при значении EXTENDED - любое количество. Пример: 
"""
listbox1 = Listbox(root, height=5, width=15, selectmode=EXTENDED)
listbox2 = Listbox(root, height=5, width=15, selectmode=SINGLE)
list1 = [u"Москва", u"Санкт-Петербург", u"Саратов", u"Омск"]
list2 = [u"Канберра", u"Сидней", u"Мельбурн", u"Аделаида"]
for i in list1:
    listbox1.insert(END, i)
for i in list2:
    listbox2.insert(END, i)
listbox1.pack()
listbox2.pack()
"""Виджет Frame (рамка) предназначен для организации виджетов внутри окна. Рассмотрим пример: """
frame1 = Frame(root, bg='green', bd=5)
frame2 = Frame(root, bg='red', bd=5)
button1 = Button(frame1, text=u'Первая кнопка')
button2 = Button(frame2, text=u'Вторая кнопка')
frame1.pack()
frame2.pack()
button1.pack()
button2.pack()
"""Checkbutton - это виджет, который позволяет отметить „галочкой“ определенный пункт в окне. 
При использовании нескольких пунктов нужно каждому присвоить свою переменную. Разберем пример: """
var1 = IntVar()
var2 = IntVar()
check1 = Checkbutton(root, text=u'1 пункт', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(root, text=u'2 пункт', variable=var2, onvalue=1, offvalue=0)
check1.pack()
check2.pack()
"""
Checkbutton - это виджет, который позволяет отметить „галочкой“ определенный пункт в окне. 
При использовании нескольких пунктов нужно каждому присвоить свою переменную. Разберем пример: 
"""
var1 = IntVar()
var2 = IntVar()
check1 = Checkbutton(root, text=u'1 пункт', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(root, text=u'2 пункт', variable=var2, onvalue=1, offvalue=0)
check1.pack()
check2.pack()
"""
Виджет Radiobutton выполняет функцию, схожую с функцией виджета Checkbutton. Разница в том, 
что в виджете Radiobutton пользователь может выбрать лишь один из пунктов. 
Реализация этого виджета несколько иная, чем виджета Checkbutton:
"""
var = IntVar()
rbutton1 = Radiobutton(root, text='1', variable=var, value=1)
rbutton2 = Radiobutton(root, text='2', variable=var, value=2)
rbutton3 = Radiobutton(root, text='3', variable=var, value=3)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
"""
Scale (шкала) - это виджет, позволяющий выбрать какое-либо значение из заданного диапазона. Свойства:
    orient - как расположена шкала на окне. Возможные значения: HORIZONTAL, VERTICAL (горизонтально, вертикально).
    length - длина шкалы.
    from_ - с какого значения начинается шкала.
    to - каким значением заканчивается шкала.
    tickinterval - интервал, через который отображаются метки шкалы.
    resolution - шаг передвижения (минимальная длина, на которую можно передвинуть движок)
"""


def getv(root):
    a = scale1.get()
    print("Значение", a)


scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=50, to=80, tickinterval=5, resolution=5)
button1 = Button(root, text=u"Получить значение")
scale1.pack()
button1.pack()
button1.bind("<Button-1>", getv)
"""
Scrollbar
Этот виджет даёт возможность пользователю "прокрутить" другой виджет (например текстовое поле) 
и часто бывает полезен. Использование этого виджета достаточно нетривиально. 
Необходимо сделать две привязки: command полосы прокрутки привязываем к методу xview/yview виджета, 
а xscrollcommand/yscrollcommand виджета привязываем к методу set полосы прокрутки.
Рассмотрим на примере: 
"""
text = Text(root, height=3, width=60)
text.pack(side='left')
scrollbar = Scrollbar(root)
scrollbar.pack(side='left')
# первая привязка
scrollbar['command'] = text.yview
# вторая привязка
text['yscrollcommand'] = scrollbar.set
"""
BitmapImage
Конструктор класса принимает следующие аргументы:
    background и foreground - цвета фона и переднего плана для изображения. 
    Поскольку изображение двухцветное, то эти параметры определяют соответственно чёрный и белый цвет.
    file и maskfile - пути к файлу с изображением и к маске (изображению, указывающему какие пиксели будут 
    прозрачными).
    data и maskdata - вместо пути к файлу можно указать уже загруженные в память данные изображения. 
    Данная возможность удобна для встраивания изображения в программу.
Пример: 
"""
data = '''#define image_width 15
#define image_height 15
static unsigned char image_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x1c, 0x30, 0x0c, 0x60, 0x06,
   0x60, 0x06, 0xc0, 0x03, 0xc0, 0x03, 0x60, 0x06, 0x60, 0x06, 0x30, 0x0c,
   0x38, 0x1c, 0x00, 0x00, 0x00, 0x00 };'''

image = BitmapImage(data=data, background='red', foreground='green')
button = Button(root, image=image)
button.pack()
# ===================================================
btn = Button(root, text='The button', width=10, height=2, bg='white', fg='black', font='Arial 8')  # создание кнопки
lab = Label(root, text='Enter your female:', font='Arial 8')  # создание надписи
Edit = Entry(root, width=10)  # создание поля ввода
# ===================================================
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
frame = tk.Frame(root)
frame.grid()
combobox = ttk.Combobox(frame, values=[u"ОДИН", u"ДВА", u"ТРИ"], height=3)
# frame - задает родительский виджет, на его территории будет располагаться Combobox
# values - задает набор значений, которые будут содержаться в Combobox изначально
# height - задает высоту выпадающего списка. Если число элементов списка меньше 11, то можно не задавать.
# Если не задано при количестве элементов больше 10, то с правой стороны появится полоса прокрутки.
# Если в нашем примере задать значение height меньше трех, то с правой стороны появится полоса прокрутки,
# но она будет недоступна, а все элементы будут отображаться одновременно.
combobox.set(u"ОДИН")  # с помощью этой строчки мы установим Combobox в значение ОДИН изначально
combobox.grid(column=0, row=0)  # Позиционируем Combobox на форме

"""
Progressbar
Виджет отображает уровень загрузки.
length - длина полосы.
start - Запускает бесконечный цикл загрузки. Шаг длиною 1 выполняется один раз в указанное время (в миллисекундах).
stop - Останавливает цикл загрузки.
step - Продвигает загрузку на заданное количество шагов. 
"""
# pb = ttk.Progressbar(root, length=100)
# pb.pack()
# pb.start(100)

btn.pack()  # размещение кнопки на форме
lab.pack()  # размещение надписи на форме
Edit.pack()  # размещение поля ввода на форме
root.mainloop()  # отображение главного окна
