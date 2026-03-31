import random

#Створюємо список з випадковими, унікальними, впорядкованими числами
def get_numbers_ticket(min, max, quantity):
    random_number = []
    if min >= 1 and max <= 1_000 and 1 < quantity < max:
        while len(random_number) < quantity:
              gen_number = random.randint(min, max)
              if random_number.count(gen_number) == 0: 
                  random_number.append(gen_number)
        random_number.sort()
        return random_number
    else:
         return []

#Приймаємо данні, виводимо результат
min_number      = int(input("Введіть мінімально можливе число у наборі (не менше 1):"))
max_number      = int(input("Введіть максимально можливе число у наборі (не більше 1_000):"))
quantity_number = int(input("Введіть кількість чисел, які потрібно вибрати (значення між min і max):"))     
 
print(get_numbers_ticket(min_number, max_number, quantity_number))
    
     
     