day = int(input("ваша дата рождения: "))
month = input("ваш месяц рождения: ")
if (month == "март" and day >= 21 ) or (month =="апрель" and day <= 20):
    print("овен")
elif (month == "апрель" and day >= 21 ) or (month =="май" and day <= 20):
    print("телец")
elif (month == "май" and day >= 21) or (month == "июнь" and day <= 20):
    print("близнецы")
elif (month == "июнь" and day >= 21 ) or (month =="июль" and day <= 20):
    print("рак")
elif (month == "июль" and day >= 21 ) or (month =="август" and day <= 20):
    print("лев")
elif (month == "август" and day >= 21 ) or (month =="сентябрь" and day <= 20):
    print("дева")
elif (month == "сентябрь" and day >= 21 ) or (month =="октябрь" and day <= 20):
    print("весы")
elif (month == "октябрь" and day >= 21 ) or (month =="ноябрь" and day <= 20):
    print("скорпион")
elif (month == "ноябрь" and day >= 21 ) or (month =="декабрь" and day <= 20):
    print("стрелец")
elif (month == "декабрь" and day >= 21 ) or (month =="январь" and day <= 20):
    print("козерог")
elif (month == "январь" and day >= 21 ) or (month =="февраль" and day <= 20):
    print("водолей")
elif (month == "февраль" and day >= 21 ) or (month =="март" and day <= 20):
    print("рыбы")
else:
    print("не распознано. пожалуйста введите вашу дату рождения точнее.")