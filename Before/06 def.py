import os 
os.system('cls') # attīra termināla logu pašā sākumā
print("\n")  # ieliek tukšu rindiņu pirms izdrukas 

# https://video.cs50.io/JP7ITIXGpHk?start=5174


# def hello():
#     print("hello") 
    
# name = input("Kā tevi sauc?")
# hello()
# print(name)   
    

# def hello(to):
#     print("hello,", to) 
    
# name = input("Kā tevi sauc?")
# hello(name)


# def hello(to="pasaule"):
#     print("hello,", to) 

# hello()    
# name = input("Kā tevi sauc?")
# hello(name)

# funkcijai jābūt definētai pirms izsaukšanas

# def main():

#     # Output using our own function
#     name = input("What's your name? ")
#     hello(name)

#     # Output without passing the expected arguments
#     hello()


# # Create our own function
# def hello(to="world"):
#     print("hello,", to)

# main()


# Vērtības atgriešana - return

def main():
    x = int(input("x - ? "))
    print("x kvadrātā ir", kvadrats(x))


def kvadrats(n):
    return n * n


main()



# Funkcija var atgriezt vienu vai vairākas vērtības – bet ja neatgriež neko, tad atgriež speciālo
# vērtību None. Atgriežot vairākas vērtības, tās return operatora izsaukumā jāatdala ar
# komatiem
# def intdivide(a,b):
#  return a // b, a % b # gan dalījums, gan atlikums
# d,r = intdivide(13,5)
# print(d,r)

# Create a def function with No Arguments
# Create def function to find the subtraction of two Numbers
# Create def function with the first 10 prime numbers
# Create a function to find the factorial of a Number
# Python def keyword example with *args
# Python def keyword example with **kwargs
# Passing Function as an Argument
# Python def keyword example with the class