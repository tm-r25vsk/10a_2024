# Float Basics
# A floating point value is a real number that has a decimal point in it, such as 0.52.
# You can change your code to support floats as follows:

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

# This change allows your user to enter 1.2 and 3.4 to present a total of 4.6.

# Let’s imagine, however, that you want to round the total to the nearest integer. 
# Looking at the Python documentation for round, 
# you’ll see that the available arguments are round(number[n, ndigits]). 
# Those square brackets indicate that something optional can be specified by the programmer. 
# Therefore, you could do round(n) to round a digit to its nearest integer. Alternatively, you could code as follows:

# docs.python.org/3/library/functions.html#round
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)
h = round(x / y, 2)
# Print the result
print(z)
print(h)

# Izvade tiks noapaļota līdz tuvākajam veselam skaitlim.

# Ko darīt, ja mēs vēlētos formatēt garo skaitļu izvadi?
# Piemēram, tā vietā, lai redzētu 1000, jūs varētu vēlēties redzēt 1,000. Jūs varat modificēt savu kodu šādi:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the formatted result
print(f"{z:,}")

# Though quite cryptic, that print(f"{z:,}") creates a scenario 
# where the outputted z will include commas where the result could look like 1,000 or 2,500.

# Python piedāvā iespēju pielāgot tūkstošu atdalītāju, izmantojot virknes formatēšanu. 
# Lai kā tūkstošu atdalītāju izmantotu atstarpi, var modificēt formāta specifikatoru šādi:

z = 1234567
print(f"{z:,}".replace(',', ' '))
# Šajā piemērā f"{z:,}" izmanto komatu kā noklusējuma tūkstošu atdalītāju, 
# un tad .replace(',', ' ') aizvieto komatu ar atstarpi.

# vai

# Oficiālāks risinājums: izmantojot locale moduli
# Python nodrošina arī locale moduli, 
# lai strādātu ar dažādām valodām un tām atbilstošiem tūkstošu atdalītājiem. 
# Ja vēlies lietot atstarpi kā tūkstošu atdalītāju, to vari panākt, 
# uzstādot atbilstošu lokalizāciju.

import locale

# Iestatīt lokalizāciju, kurā atstarpe ir tūkstošu atdalītājs
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Izmanto, ja nepieciešama noklusējuma lokalizācija

z = 1234567
print(locale.format_string("%d", z, grouping=True).replace(",", " "))  # Izdrukās: 1 234 567

# Izmantojot locale.format_string(), vari formatēt skaitļus, bet aizstājot komatus ar atstarpēm, iegūsi pielāgotu izkārtojumu, kur atstarpe ir tūkstošu atdalītājs.


# More on Floats
# How can we round floating point values? First, modify your code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(z)
# When inputting 2 as x and 3 as y, 
# the result z is 0.6666666666, seemingly going on to infinite as we might expect.

# Let’s imagine that we want to round this down. 
# We could modify our code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result and round
z = round(x / y, 2)

# Print the result
print(z)
# As we might expect, this will round the result to the nearest two decimal points.

# We could also use fstring to format the output as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")
# This cryptic fstring code displays the same as our prior rounding strategy.

# https://docs.python.org/3/library/string.html#format-string-syntax

# You can learn more in Python’s documentation of float.