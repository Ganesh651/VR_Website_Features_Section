def cube_of_numbers(given_number):
    for each_number in range(1,given_number+1):
        print(each_number**3)
given_number = int(input())
cube_of_numbers(given_number)