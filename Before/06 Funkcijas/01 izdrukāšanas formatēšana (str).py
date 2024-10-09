# prasa lietotājam vārdu
name = input("Kā tevi sauc? ")

# saka Sveiks lietotājam
print("Sveiks, ")
print(name)

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# lai izdrukātu sveicienu vienā rindā:

print("Sveiks, ", end="")
print(name)

# end= "viss kaut kas"

# ja sep="kaut_kas" 

print("Sveiks, ", name, sep="%%%%")

# ja jāizvada pēdiņas:

print('hello, "friend"')
# vai
print("hello, \"friend\"")

# sakām, ka izdrukājam speciālu formatēšanas rindu- rakstām "f":

print(f "Sveiks, {name}")

# 45:10, https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@263dc9ef9c66490aa5511e9f8633de34

# STR
# Simbolu virknēs ir daudz iebūvētu gatavu risinājumu

# docs.python.org/3/library/stdtypes.html#string-methods 

# Nekad nevajadzētu gaidīt, ka lietotājs sadarbosies, kā paredzēts. 
# Tādēļ jums būs jānodrošina, lai jūsu lietotāja ievadītā informācija tiktu labota vai pārbaudīta.
# Izrādās, ka virknēs ir iebūvēta iespēja noņemt atstarpes no virknes.
# ja lietotājs ievada ar daudziem tukšumiem un mazajiem burtiem:
#      janis  
# 
By utilizing the method strip on name as name = name.strip(), 
will strip all the whitespaces on the left and right of the users input. 
You can modify your code to be:  

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")

# Rerunning this program, regardless of how many spaces you type before or after the name, 
# it will strip off all the whitespace.

# Using the title method, it would title case the user’s name:

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.capitalize() # tikai pirmo burtu. ja vairāki vārdi ,tad tikai pirmais burts
name = name.title()

# Print the output
print(f"hello, {name}")

# By this point, you might be very tired of typing python repeatedly in the terminal window. 
# You cause use the up arrow of your keyboard to recall the most recent terminal commands you have made.
# Notice that you can modify your code to be more efficient:

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()

# Print the output
print(f"hello, {name}")

# Rezultāts tāds pats kā iepriekš

# We could even go further!

# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")

# ???????
# Uzdevums: Ja lietotājs ievada vārdu un uzvārdu, tad sveicināt tikai ar vārdu.
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")

