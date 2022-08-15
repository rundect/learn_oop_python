# 1.2 Атрибуты класса

class Person:
    name = 'Ivan'
    age = 30


print(Person)
print(Person.name)
print(Person.age)

# Show all attributes of class
# __dict__ magic methods
print(Person.__dict__)
print(type(Person.__dict__))

# built-in function getattr()
print(getattr(Person, 'name'))
print(getattr(Person, 'x', 'attribute is missing'))

# Change name of attribute
Person.name = 'Misha'
print(Person.name)

# Create new attribute
Person.x = 100
print(Person.x)
print(Person.__dict__)

# Change attribute using settatr()
print(Person.x)
setattr(Person, 'x', 300)
print(Person.x)

# Create new attribute using settatr()
setattr(Person, 'y', 10)
print(Person.y)

# Delete attribute using del
print(Person.__dict__)
del Person.x
print(Person.__dict__)

# Delete attribute using delattr()
print(Person.__dict__)
delattr(Person, 'y')
print(Person.__dict__)


# Add attribute to class influence to attribute of exemplar
class Person:
    name = 'Ivan'
    age = 30


print(Person())

a = Person()
print(a)
print(getattr(a, 'name'))


b = Person()
print(b)
print(getattr(b, 'age'))

Person.z = 100
print(getattr(a, 'z'))
print(getattr(b, 'z'))

del Person.age
print(getattr(Person, 'age', 'attribute is missing'))
print(getattr(a, 'age', 'attribute is missing'))
print(getattr(b, 'age', 'attribute is missing'))

# If change(del, set, assignment) attributes of exemplar, it doesn't influence on attributes of class and another
# exemplars of class
a.b = 200
print(getattr(Person, 'b', 'attribute is missing'))
print(getattr(a, 'b', 'attribute is missing'))
print(getattr(b, 'b', 'attribute is missing'))

# If change attributes of class, it changes attributes of class and another exemplars of class
Person.d = 777
print(getattr(Person, 'd', 'attribute is missing'))
print(getattr(a, 'd', 'attribute is missing'))
print(getattr(b, 'd', 'attribute is missing'))

# Check attributes
print(hasattr(Person, 'd'))
print(getattr(Person, 'd'))
