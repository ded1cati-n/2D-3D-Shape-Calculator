# int
import numpy
import os
import time

# selection
selection = input("┏━┳━━┳┓┏━┳┳┳┓┏━━┳━━┳━┳━┓\n┃┏┫┏┓┃┃┃┏┫┃┃┃┃┏┓┣┓┏┫┃┃╋┃\n┃┗┫┣┫┃┗┫┗┫┃┃┗┫┣┫┃┃┃┃┃┃┓┫\n┗━┻┛┗┻━┻━┻━┻━┻┛┗┛┗┛┗━┻┻┛ \n[1] 2D Shape Area Calculator \n[2] 3D Shape Calculator \n[3] Credits \n\nChoice: ")

if selection == "1":
  os.system('clear')
  selection2 = input("[1] Triangle \n[2] Circle \n[3] Trapezoid \n[4] Hexagon \n\nChoice: ")
  if selection2 == "1": #[1] Triangle
    os.system('clear')
    base = float(input("Base: "))
    height = float(input("Height: "))
    res = (base * height) / 2
    print("Area: " + str(res))
  elif selection2 == "2": #[2] Circle
    os.system('clear')
    radius = float(input("Radius: "))
    res = (radius * radius) * numpy.pi
    print("Area: " + str(res))
  elif selection2 == "3": #[3] Trapezoid
    os.system('clear')
    topbase = float(input("Top Base: "))
    bottombase = float(input("Bottom Base: "))
    height = float(input("Height: "))
    res = ((topbase + bottombase) / 2) * height
    print("Area: " + str(res))
  elif selection2 == "4": #[4] Hexagon
    os.system('clear')
    print("WIP")
    
elif selection == "2":
  os.system('clear')
  selection2 = input("[1] Surface Area \n[2] Volume \n\nChoice: ")
  if selection2 == "1":
    os.system('clear')
    selection3 = input("[1] Cylinder \n[2] Cone \n[3] Pyramid \n\nChoice: ")
    if selection3 == "1": #[1] Cylinder
      os.system('clear')
      baseR = float(input("Radius: "))
      height = float(input("Height: "))
      res = ((baseR * baseR * numpy.pi * 2) + (baseR * 2 * numpy.pi * height))
      print("Surface area: " + str(res))
    elif selection3 == "2": #[2] Cone
      os.system('clear')
      baseR = float(input("Radius: "))
      height = float(input("Slant Height: "))
      res = ((baseR * baseR * numpy.pi) + height * numpy.pi * baseR)
      print("Surface area: " + str(res))
    elif selection3 == "3": #[3] Pyramid
      os.system('clear')
      selection4 = input("[1] Triangular \n[2] Rectangular \n[3] Pentagonal \n[4] Hexagonal \n\nChoice: ")
      if selection4 == "1": #[1] Triangular Base
        os.system('clear')
        sidelength = float(input("Base side length: "))
        basearea = (((3**0.5) / 4) * sidelength * sidelength)
        res = (basearea * 4)
        print("Surface area: " + str(res))
      elif selection4 == "2": #[2] Rectangular Base
        os.system('clear')
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Slant Height: "))
        res = ((length + width) * height) + length * width
        print("Surface area: " + str(res))
      elif selection4 == "3": #[3] Pentagonal Base
        os.system('clear')
        print("WIP")
      elif selection4 == "4": #[4] Hexagonal Base
        os.system('clear')
        print("WIP")

  elif selection2 == "2":
    os.system('clear')
    selection3 = input("[1] Cylinder \n[2] Cone \n[3] Pyramid \n\nChoice: ")
    if selection3 == "1": #[1] Cylinder
      os.system('clear')
      baseR = float(input("Radius: "))
      height = float(input("Height: "))
      res = (baseR * baseR * height * numpy.pi)
      print("Volume: " + str(res))
    elif selection3 == "2": #[2] Cone
      os.system('clear')
      baseR = float(input("Radius: "))
      height = float(input("Height: "))
      res = (baseR * baseR * height * numpy.pi / 3)
      print("Volume: " + str(res))
    elif selection3 == "3": #[3] Pyramid
      os.system('clear')
      selection4 = input("[1] Triangular \n[2] Rectangular \n[3] Pentagonal \n[4] Hexagonal \n\nChoice: ")
      if selection4 == "1": #[1] Triangular Base
        os.system('clear')
        sidelength = float(input("Base side length: "))
        height = float(input("Height: "))
        basearea = (((3**0.5) / 4) * sidelength * sidelength)
        res = (basearea * height) / 3
        print("Volume: " + str(res))
      elif selection4 == "2": #[2] Rectangular Base
        os.system('clear')
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Height: "))
        res = (length * width * height) / 3
        print("Volume: " + str(res))
      elif selection4 == "3": #[3] Pentagonal Base WIP
        os.system('clear')
        print("WIP")
      elif selection4 == "4": #[4] Hexagonal Base WIP
        os.system('clear')
        print("WIP")
elif selection == "3":
  os.system('clear')
  print("Made by ded1cati0n")
  time.sleep(5)
  print("I hate niggers")
  time.sleep(1)
  os.system('clear')