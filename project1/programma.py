def main(req):
     if 'расписание занятий' in req or 'дни недели' in req:
        Raspisanie()
     elif 'тренер' in req or 'контакты тренера' in req:
        Trener()
     elif 'оплата' in req or 'стоимость' in req or 'сумма' in req:
        Oplata()
     elif 'посещаемость' in req or 'пропуск' in req or 'режим' in req:
        Poseshaemost()
     elif 'как добраться' in req or 'куда ехать' in req or 'место' in req:
        Doroga()
def Raspisanie():
     print('расписание:')
     print('среда - 19:00')
     print('пятница - 19:30')
     print('воскресенье - 17:00')
def Trener():
     print('тренер:')
     print('номер: 88005553535')
def Oplata():
     print('оплата:')
     print('500р.')
def Poseshaemost():
     print('дни посещения:')
     print('среда, пятница, воскресенье')
def Doroga():
     print('вы можете узнать адресс и маршрут в приложении')
