class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks / len(self.marks))
    @classmethod
    def friend(cls,origin, friend_name,*args,**kwargs):
        return cls(friend_name,origin.school,*args,**kwargs)
        #Using args and kwargs in the arguments and return will allow for accepting
        #both keyword and regular arguments and for future expansion of arguments in the WorkingStudent class


class WorkingStudent(Student):
    def __init__(self,name,school,salary,job_title):
        super().__init__(name,school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent("Anna","Oxford",20,"Software developer") #when creating anna there is no keyword for job title, passes as args
friend = WorkingStudent.friend(anna, "Greg",30,job_title ="Software Developer") #job title here is passed with keyword and will be handled as kwargs
print(anna.salary)
print(friend.name)
print(friend.salary)
print(friend.school)






