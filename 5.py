def nom1():
    from random import randint
    a = [] #создаем пустой список
    for i in range(5):
        a.append(randint(1, 5))
    print(a)
    ch = int(input('Введите число: '))
    if ch in a:
        print('Поздравляю, Вы угадали число')
    else:
        print('Вы не угадали число')


def nom2():
    import collections
    from random import randint
    a = []
    for i in range(5):
        a.append(randint(1, 5))
    print(a)
    co = collections.Counter(a) #Модуль collections, Counter — предназначен для подсчёта количества элементов.
    print(co)


def nom3():
    a = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресение")
    num_v = int(input('Сколько дней недели вы хотели бы чтобы были выходными?'))
    index = len(a) - num_v #разделение на рабочие и выходные
    weekend = a[index:] #формирование отдельно выходных
    work = a[:index] #формирование рабочих дней
    print("Выходных дней: ", weekend)
    print("Рабочие дни: ", work)


def nom4():
    import random
    gr1 = ["Иванов", "Смирнов", "Синицин", "Поляков", "Морозов", "Скворцов", "Волков", "Зайцев", "Орлов", "Соловьев"]
    gr2 = ["Соколов", "Семенов", "Козлов", "Павлов", "Петров", "Александров", "Захаров", "Никитин", "Борисов",
           "Алексеев"]
    print("Первая команда: ", gr1)
    print("Вторая команда: ", gr2)
    gr = [] #создаем пустой список для будущей команды
    gr = random.sample(gr1, 5) + random.sample(gr2, 5) #Метод sample модуля random возвращает случайную выборку элементов из последовательности
    dlina = len(gr)                               #Из групп 1 и 2 берёт по 5 элементов
    gr_sort = sorted(gr)
    print("Количество человек в образованной команде: ", dlina)
    print("Получившаяся команда: ", gr)
    print("Отсортированная по алфавиту получившаяся команда: ", gr_sort)
    im = "Иванов"
    if im in gr:
        print("Иванов входит в команду")
    else:
        print("Иванов не входит в команду")
