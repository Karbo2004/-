def main(req):
 if 'Расписание занятий' in req.lower() or 'Дни недели' in req.lower():
        Raspisanie()
 if 'Тренер' in req.lower() or 'Контакты тренера' in req.lower():
        Trener()
 if 'Оплата' in req.lower() or 'Стоимость' in req.lower() or 'Сумма' in req.lower():
        Oplata()
 if 'Посещаемость' in req.lower() or 'Пропуск' in req.lower() or 'Режим' in req.lower():
        Poseshaemost()
 if 'Как добраться' in req.lower() or 'Куда ехать' in req.lower() or 'Место' in req.lower():
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