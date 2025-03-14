def total_fine(date, car, fine):
    total = 0
    is_even_date = (date % 2 == 0)
    
    for i in range(len(car)):
        is_odd_car = (car[i] % 2 != 0)
        
        # Collect fine if the car number follows the given rule
        if (is_even_date and is_odd_car) or (not is_even_date and not is_odd_car):
            total += fine[i]
    
    return total
