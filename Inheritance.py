class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def name(self):
    print(self.firstname, self.lastname)



x = Person("naman", "sharma")
x.name()
