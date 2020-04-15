numero = int(input());

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")

if numero % 3 == 0 and not numero % 5 == 0:
    print("Fizz")

if numero % 5 == 0 and not numero % 3 == 0:
    print("Buzz")
