"""
while True:
    try:
      x = int(input("Whats x ? "))
    except ValueError:
     print("x is not an integer ")
    else:
      break

print(f"x is {x}")
"""
#simplified version of the top
"""
while True:
    try:
      x = int(input("Whats x ? "))
      break
    except ValueError:
     print("x is not an integer ")

print(f"x is {x}")
"""
def main():
   x = get_int()
   print(f"x is {x}")



def get_int():
    while True:
      try:
        return int(input("Whats x ? "))
      except ValueError:
        pass
        #pass ignores the input if its a value error
     
main()