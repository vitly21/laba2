def car_list(cars, func):
    for car in cars:
        print(func(car))
cars = ['BMW','LADA','HAVAL']
car_list(cars, lambda car: car.upper() + ' - машина')
