from ops import *

###############################
class Word(object):
  type: str

  def __init__(self):
    pass

  def execute(self, stack, env):
    pass
###############################

class Num_Literal(Word):
  def __init__(self, value):
    super().__init__()
    self.value = value
  
  def execute(self, stack, env):
    PUSH(self.value, stack)

###############################

class Operation(Word):
  def __init__(self, FUNC):
    super().__init__()
    self.FUNC = FUNC

  def execute(self, stack, env):
    self.FUNC(stack)

###############################

class Variable_Declaration(Word):
    def __init__(self, name):
      super().__init__()
      self.name = name
    
    def execute(self, stack, env):
      env["VARIABLES"][self.name] = len(env["VARIABLES"]["vars"])
      env["VARIABLES"]["vars"].append(0)

###############################

class Const_Declaration(Word):
    def __init__(self, name):
      super().__init__()
      self.name = name
    
    def execute(self, stack, env):
      env["CONSTANTS"][self.name] = POP(stack)

###############################
# !
class Store_Memory(Word):
  def __init__(self):
    super().__init__()

  def execute(self, stack, env):
    location = POP(stack)
    value = POP(stack)

    if location != None and value != None:
      env["VARIABLES"]["vars"][location] = value
    else:
      print("Memory store requires a location and a value." +
            "Got: LOC[" + str(location) + "] and VAL[" + str(value) + "]")


###############################
# @
class Fetch_Memory(Word):
  def __init__(self):
    super().__init__()

  def execute(self, stack, env):
    location = POP(stack)

    if location != None:
      value = env["VARIABLES"]["vars"][location]
      PUSH(value, stack)
    
    else:
      print("Memory fetch requires a location. Got: None")

###############################

class Allocate_Memory(Word):
    def __init__(self):
      super().__init__()
    
    def execute(self, stack, env):
      env["VARIABLES"]["vars"] += [0] * (POP(stack) - 1)

###############################

class Function_Declaration(Word):
    def __init__(self, name, body):
      super().__init__()
      self.name = name
      self.body = body

    def execute(self, stack, env):
      env["FUNCTIONS"][self.name] = self.body

###############################

class Identifier(Word):
    def __init__(self, name):
      super().__init__()
      self.name = name

    def execute(self, stack, env):
      # If it's a function
      if self.name in env["FUNCTIONS"]:
        for word in env["FUNCTIONS"].get(self.name):
          word.execute(stack,env)

      elif self.name in env["VARIABLES"]:
        PUSH(env["VARIABLES"].get(self.name), stack)

      elif self.name in env["CONSTANTS"]:
        PUSH(env["CONSTANTS"].get(self.name), stack)

      else:
        print("Unexpected identifier")

###############################

class Do_Loop(Word):
  def __init__(self, body):
    super().__init__()
    self.body = body

  def execute(self, stack, env):
    # Get top two values on stack
    x_y = get_x_y(stack)
    
    if x_y[0] == None or x_y[1] == None:
      print("Do loop requires a min and max")
      return

    # Get start and end of the loop
    start = x_y[1]
    end = x_y[0]

    # While i < end value
    while(start <= end):

      # Set the value for i in constants
      env["CONSTANTS"]["i"] = start
      
      # Loop through the body and execute each value
      for word in self.body:
        word.execute(stack, env)
      
      # Increment i
      start += 1
  
###############################

class Begin_Until_Loop(Word):
  def __init__(self, body):
    super().__init__()
    self.body = body

  def execute(self, stack, env):
    # Until the top of the stack is 0, 
    # keep running the body
    while(True):
      for word in self.body:
        word.execute(stack, env)
      
      if stack.pop() != 0:
        break;
###############################

class String_Print(Word):
    def __init__(self, content):
      super().__init__()
      self.content = content

    def execute(self, stack, env):
      print(self.content, end="")

###############################

class Conditional_Statement(Word):

  def __init__(self, if_body, else_body):
    super().__init__()
    self._if = if_body
    self._else = else_body

  def execute(self, stack, env):
    # If the top of the stack isn't false
    # run the if block
    if POP(stack) != 0:
      for word in self._if:
        word.execute(stack, env)

    # Else run the else block
    elif self._else != None:
      for word in self._else:
        word.execute(stack, env)

###############################

def make_env():
  return {
      "FUNCTIONS" : {},
      "VARIABLES" : {
        "vars": []
      },
      
      "CONSTANTS" : {}
  }

###############################