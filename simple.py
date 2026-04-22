# def steps(number):

#     if number < 0:
#         raise ValueError("Only positive integers are allowed")
#     num_of_steps = 0

#     while number != 1:
#         if number % 2 == 0:
#             number = number // 2
#             num_of_steps += 1
#         else:
#             number = (number * 3) + 1
#             num_of_steps += 1

#         print(num_of_steps)
        

# steps(-12)

num_of_loops = int(input("How many loops?: "))
data = []

for i in range(num_of_loops):
    num_of_stick = input("Enter a number: ").split()

    if len(num_of_stick) == 4 and len(set(num_of_stick)) == 1:
        print("YES")
    else:
        print("NO")
