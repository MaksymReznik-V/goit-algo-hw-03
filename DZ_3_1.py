from datetime import datetime

#Розраховуємо кількість днів між датами
def get_days_from_today(date):
    
   try:
        date_string = datetime.strptime(date, "%Y-%m-%d")
        now_date = datetime.today()
        amount_day = date_string - now_date 
   except ValueError:
        print("Не вірний формат дати . Введіть дату у форматі 'PPPP-MM-ДД'")
        return 0
   
   return amount_day.days
  
print(get_days_from_today("2001-12-12"))




  
   

    