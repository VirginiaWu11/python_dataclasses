from dataclasses import dataclass, field

# normal Class:
class Person:
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
    # def __str__(self):
    #     return f"{self.name} is a {self.job} and is {self.age} years old."

person1 = Person("John", "Teacher", 35)
person2 = Person("Jane", "Doctor", 32)
person3 = Person("Jack", "Student", 15)
person4 = Person("Jack", "Student", 15)

print(id(person1))
print(id(person2))
print(person3)
print(person3 == person4)

# prints:
# 140226522309712
# 140226522309776
# <__main__.Person object at 0x7f89080ce4d0>
# False

# dataclasses will have an easy way to print the object instead of showing <__main__.Person object at 0x7f89080ce4d0>
# deep comparison is also possible, if the data is the same, it will return True

@dataclass(order=True, frozen=True) #Freezing means creating objects that are read-only
class DataClassPerson:
    # type hinting is used in dataclasses to indicate the type of the data it's dealing with
    sort_index: int = field(init=False, repr=False) 
    #to define how to sort the objects # to tell the class sort_index is a field only used for sorting and we do not want to initialize it (not required to create the class)
    # repr=False: to tell the class to not print the sort_index when printing the object
    name: str
    job: str
    age: int
    strength: int = 100 # dataclasses also allow default values; now this defaults to 100

    def __post_init__(self):
        ##### self.sort_index = self.age ---#sort by age. if you want to sort by strength, you can change it to self.strength
        # once the dataclass has been frozen, we can no longer change the sort_index
        #instead, we do this! same effect as above:
        object.__setattr__(self, 'sort_index', self.age)

    def __str__(self):
        return f"{self.name}, {self.job}, {self.age}" # this is the default __str__ method that can be use to provied a nice string representation of the object

# dataclass will do this initialization for us, so the below is not needed:
    # def __init__(self, name, job, age):
    #     self.name = name
    #     self.job = job
    #     self.age = age
    # # def __str__(self):
    # #     return f"{self.name} is a {self.job} and is {self.age} years old."

DataClassPerson1 = DataClassPerson("John", "Teacher", 35)
DataClassPerson2 = DataClassPerson("Jane", "Doctor", 32)
DataClassPerson3 = DataClassPerson("Jack", "Student", 15,90)
DataClassPerson4 = DataClassPerson("Jack", "Student", 15)

print(id(DataClassPerson1))
print(id(DataClassPerson2))
print(DataClassPerson3)
print(DataClassPerson3 == DataClassPerson4)
# DataClassPerson1.age = 20 #this will not work because the dataclass is frozen ## dataclasses.FrozenInstanceError: cannot assign to field 'age'
print(DataClassPerson1>DataClassPerson2) # can define the order of the objects and what is greater

# prints:
# 140598440066320
# 140598708436176
# DataClassPerson(name='Jack', job='Student', age=15)  ----shows nicely printed object
# True  ---contents are the same so this returns true.