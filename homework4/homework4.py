import random

def find_multiples_of_x():
    numbers = [random.randint(0, 200) for _ in range(50)]
    
    x = int(input("Введите число X: "))
    
    multiples = list(filter(lambda num: num % x == 0, numbers))

    print(f"Сгенерированные числа: {numbers}")
    print(f"Числа, кратные {x}: {multiples}")

find_multiples_of_x()
