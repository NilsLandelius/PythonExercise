#class LotteryPlayer:
#    def __init__(self,name):
#        self.name = name
#        self.numbers = (5,9,12,3,1,21)

#    def total(self):
#        return sum(self.numbers)

#player_one = LotteryPlayer()
#player_two = LotteryPlayer()
#print(player_one.name)
#print(player_one.total())


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def go_to_school(cls): #passing the class instead of object = Student
        print("I'm going to school")

    @staticmethod
    def statMeth():
        print("just a static Method")

Anna = Student("Anna","MIT")
Anna.marks.append(99)
Anna.marks.append(44)
Student.go_to_school() #works because it's a classmethod, works for staticmethods aswell
Student.statMeth()
Anna.go_to_school()
print(Anna.average())


