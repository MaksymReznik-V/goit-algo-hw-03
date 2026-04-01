from datetime import datetime

#Розраховуємо кількість днів між датами
def get_days_from_today(date):
    
   try:
        date_string = datetime.strptime(date, "%Y-%m-%d")
        now_date = datetime.today()
        amount_day = (date_string.date() - now_date.date()).days
        return amount_day
   except ValueError:
        print("Не вірний формат дати . Введіть дату у форматі 'PPPP-MM-ДД'")
   

  
print(get_days_from_today("202-04-01"))






  
   

    