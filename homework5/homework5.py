def get_number():
    for num in range(30):
        if num % 2 != 0: 
            yield num

odd_numbers_generator = get_number()

odd_numbers = [num for i, num in enumerate(odd_numbers_generator)]

if len(odd_numbers) >= 5:
    print(f"Первое нечетное число: {odd_numbers[0]}")
    print(f"Пятое нечетное число: {odd_numbers[4]}")
    print(f"Последнее нечетное число: {odd_numbers[-1]}")
else:
    print("В диапазоне недостаточно нечетных чисел.")
