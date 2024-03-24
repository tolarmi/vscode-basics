import random
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min_num <= max_num <=1000) or quantity < 0:
        print("Неправильне число.")
        return[]
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))
    return sorted(list(numbers_set))