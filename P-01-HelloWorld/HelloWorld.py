# A class to store data received
class Person(object):
  def __init__(self):
    self.name = ""
    self.firstName = ""
    self.lastName = ""
    self.age = 0
  def __init__(self, name, firstName, lastName, age):
    self.name = name
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
  def printSelf(self):
    string = "----------------------------\nPerson data:\n"
    string += "->Name: {0}\n->First name: {1}\n->Last name: {2}\n->Age: {3}\n".format(self.name, self.firstName, self.lastName, self.age)
    return string

''' 
  Start of the execution 

  Reads a person data and prints it
'''
print('Hello', 'World', sep=' ', end='')
print('!', '--Type your data--', sep="\n\n")
person = Person(input('-Name: '), input('-First name: '), input('-Last name: '), input('-Age: '))
print(person.printSelf())
