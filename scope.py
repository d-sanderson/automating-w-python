def spam():
  eggs = 99 #  assignment statements = Local Variable
  #  no assigment statement = Global variable
  bacon()
  print(eggs) #  print 99, not 0

def bacon():
  ham = 101
  eggs = 0
#  the 2 eggs variables both have local scope and are two separate variables
#  local variables in one function are completely separate from local variabls in other functions

eggs = 42
spam()