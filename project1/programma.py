def main(req):
 if 'Расписание занятий' in req() or 'Дни недели' in req():
        Raspisanie()
 if 'Тренер' in req() or 'Контакты тренера' in req():
        Trener()
 if 'Оплата' in req() or 'Стоимость' in req() or 'Сумма' in req():
        Oplata()
 if 'Посещаемость' in req() or 'Пропуск' in req() or 'Режим' in req():
        Poseshaemost()
 if 'Как добраться' in req() or 'Куда ехать' in req() or 'Место' in req():
        Doroga()

def Raspisanie():
    print('Расписание:')
    print('Среда - 19:00')
    print('Пятница - 19:30')
    print('Воскресенье - 17:00')

def Trener():
    print('Тренер:')
    print('Номер: 88005553535')

def Oplata():
    print('оплата:')
    print('500р.')

def Poseshaemost():
    print('Дни посещения:')
    print('Среда, пятница, воскресенье')

def Doroga():
    print('Вы можете узнать адресс и маршрут в приложении')
