class Person:
    def __init__(self, name, age, job, future):
        self.name_ = name
        self.age_ = age
        self.job_ = job
        self.future_ = future

    def name(self):
            return "this person's name is {}".format(self.name_)
        
    def age(self):
            return "this person's age is {}".format(self.age_)
        
    def job(self):
            return "this person works as a {}".format(self.job_)
        
    def future(self):
          return "this person has a {} future".format(self.future_)
    
human1 = Person("Ben", 26, "Engineer", "bright")

print(human1.name())
print(human1.age())
print(human1.job())
print(human1.future())