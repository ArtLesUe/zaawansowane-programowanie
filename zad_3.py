def is_even_number(my_number: int) -> bool:
    return not my_number % 2


check_even = is_even_number(11)

if check_even:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
