# A program that transports all even numbers to a empty list.
#
# List with numbers from 1 - 10.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
               16, 17, 18, 19, 20]
# Empty list to store even numbers.
even = []

# Logic for getting each even number of of the list with numbers from 1-10.
for number in number_list:
    if number % 2 == 0:
        even.append(number)
    else:
        pass

# Displaying list with even numbers.
print(even)


