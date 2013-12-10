    datetime
        
now_date = datetime.date.today() # Текущая дата (без времени)
now_time = datetime.datetime.now() # Текущая дата со временем
 
cur_year = now_date.year # Год текущий
cur_month = now_date.month # Месяц текущий
cur_day = now_date.day # День текущий
cur_hour = now_time.hour # Час текущий
cur_minute = now_time.minute # Минута текущая
cur_second = now_time.second # Секунда текущие
num_week = now_date.isoweekday() # узнаем номер недели (от 1 до 7)

now_date = now_date.replace(2011,6,30) # меняем полностью дату на 30.06.2011
now_date = now_date.replace(day=cur_day) # меняем только день
now_date = now_date.replace(month=cur_month) # меняем только месяц
now_date = now_date.replace(year=cur_year) # меняем только год

ny_2011 = datetime.date(2011,2,1) # создали дату: 1 февраля 2011 года
delta = ny_2011 - now_date # разница (дельта) в между 2-мя датами

delta = datetime.timedelta(days=2) # дельта в 2 дня
now_date = now_date + delta # Узнаем какое число будет через 2 дня
now_date = now_date - delta # или какое число было 2 дня назад
 
print(now_time.strftime("%d.%m.%Y %I:%M %p")) # форматируем дату
