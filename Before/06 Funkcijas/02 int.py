# Python valodā vesels skaitlis tiek saukts par int.
# Matemātikas pasaulē mēs pazīstam operatorus +, -, *, / un %. 
# Lai palaistu Python kodu, kompilatorā nav jāizmanto teksta redaktora logs. 
# Savā terminālī varat palaist tikai python. Termināl logā ieraksta python. 
# Termināļa logā jums tiks parādīts >>>. Pēc tam varat palaist tiešraides interaktīvu kodu. 
# Varat ierakstīt 1+1, un tas veiks šo aprēķinu. var ierakstīt print("hello") un tas tiks izpildīts.
# Šis režīms šī kursa laikā parasti netiks izmantots - interaktīvais režīms.
# Atkal atverot VS Code, terminālī varam ierakstīt kodu calculator.py. 
# Tādējādi tiks izveidots jauns fails, kurā mēs izveidosim savu kalkulatoru.
# Pirmkārt, mēs varam deklarēt dažus mainīgos.

x = 1
y = 2

z = x + y

print(z)

# Naturally, when we run python calculator.py we get the result in the terminal window of 3. 
# We can make this more interactive using the input function.

x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)

# Running this program, we discover that the output is incorrect as 12. Why might this be?
# Prior, we have seen how the + sign concatenates two strings. 
# Because your input from your keyboard on your computer comes into the compiler as text, it is treated as a string. 
# We, therefore, need to convert this input from a string to an integer. We can do so as follows:

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

# The result is now correct. 
# The use of int(x) is called “casting,” where a value is temporarily changed 
# from one type of variable (in this case, a string) to another (here, an integer).

# We can further improve our program as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

# This illustrates that you can run functions on functions. 
# The inner function is run first, and then the outer one is run. 
# First, the input function is run. Then, the int function.

# You can learn more in Python’s documtenation of int.

# Readability Wins
# When deciding on your approach to a coding task, 
# remember that one could make a reasonable argument for many approaches to the same problem.
# Regardless of what approach you take to a programming task, 
# remember that your code must be readable. 
# You should use comments to give yourself and others clues about what your code is doing. 
# Further, you should create code in a way that is readable.
# Slikts piemērs:

print("Slikti lasāma rinda: ")
print(int(input("What's x? ")) + int(input("What's y? ")))