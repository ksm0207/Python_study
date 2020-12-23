val = ""
while True:
      val = input("Enter x and y: ")
      try:
          x, y = str(val).split(",")
          print(x,y)
          break
      except:
          print("give me good input")