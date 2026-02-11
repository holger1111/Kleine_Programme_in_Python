# DIFFICULTY: 1
# FizzBuzz ist eine klassische Programmier-Challenge.
# Es werden alle zahlen von 1 bis einer gewählten Obergrenze ausgegeben,
# wobei folgende Regeln gelten:
# 1. alle Zahlen, die durch 3 teilbar sind, werden durch "Fizz" ersetzt.
# 2. alle Zahlen, die durch 5 teilbar sind, werden durch "Buzz" ersetzt.
# 3. alle Zahlen, die sowohl durch 3 als auch 5 teilbar sind, werden durch 
#    "FizzBuzz" ersetzt.
#
#  TASK: Schreibe ein Programm, was diesen Regeln folgt und Zahlen bis zu 
#        einer wählbaren Obergrenze ausgibt.


def fizz_buzz_fizzbuzz(limit):
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz_fizzbuzz(100)