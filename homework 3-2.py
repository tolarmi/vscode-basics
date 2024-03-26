import random
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <=1000) or quantity < 0:
        print("Неправильне число.")
        return[]
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max))
    return sorted(list(numbers_set))