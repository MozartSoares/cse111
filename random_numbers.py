from random import uniform

def append_random_numbers(numbers_list,quantity = 1):
    for number in quantity:
        random_number = uniform(1,quantity) 
        numbers_list.append(random_number)
    return numbers_list

def main():
    numbers = {16.2, 75.1, 52.3}
    print(numbers)

    numbers = append_random_numbers(numbers)
    print(numbers)

    numbers = append_random_numbers(numbers,1)
    print(numbers)

if __name__	== '__main__':
    main()