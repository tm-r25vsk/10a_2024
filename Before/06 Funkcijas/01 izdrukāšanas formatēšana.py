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