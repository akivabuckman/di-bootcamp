number = int(input("number: "))
# for i in range(number):
#     if number % i == 0:
#
divisors = [i for i in range(number)[1:] if number % i == 0] #list of divisors
if sum(divisors) == number:
    print("True")
else:
    print("False") 