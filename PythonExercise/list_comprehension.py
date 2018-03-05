#List comprehension will help to create smarter creation
#of lists in your code.
my_list = [1,2,3,4]
an_equal_list = [x for x in range(5)]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

print(8%3) #calculates the remaind of a division
print (8%2) #is used to check that a number is even.

print([n for n in range(10) if n % 2 == 0]) #creates a list of only even numbers.

people_you_know = ["Nisse"," Emil", "sam", "EVA"]
normalised_people = [person.strip().lower() for person in people_you_know] #will remove whitespaces and make all names lowercase in a new list.
print(normalised_people)
