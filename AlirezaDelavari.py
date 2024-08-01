from math import sqrt

def is_positive_integer(value):
    try:
        num = int(value)
        if num > 0:
            return True
    except ValueError:
        pass
    return False


def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_triangle(x1, y1, x2, y2, x3, y3):
    zel1 = calculate_distance(x1, y1, x2, y2)
    zel2 = calculate_distance(x2, y2, x3, y3)
    zel3 = calculate_distance(x3, y3, x1, y1)

    if zel1 + zel2 > zel3 and zel1 + zel3 > zel2 and zel2 + zel3 > zel1:
        return True
    return False

def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

def triangle_type(zel1, zel2, zel3):
    if zel1 == zel2 == zel3:
        return "motasavi azla"
    elif zel1 == zel2 or zel1 == zel3 or zel2 == zel3:
        return "motasavi saghein"
    elif (zel1**2 + zel2**2 == zel3**2) or (zel1**2 + zel3**2 == zel2**2) or (zel2**2 + zel3**2 == zel1**2):
        return "ghaem zavieh"
    else:
        return "mokhtalef azla"


point1 = input("Enter coordinates for point 1 with comma in between them (x,y): ").split(',')
point2 = input("Enter coordinates for point 2 with comma in between them (x,y): ").split(',')
point3 = input("Enter coordinates for point 3 with comma in between them (x,y): ").split(',')

x1, y1 = int(point1[0]), int(point1[1])
x2, y2 = int(point2[0]), int(point2[1])
x3, y3 = int(point3[0]), int(point3[1])


valid_input = True
for i in (x1, y1, x2, y2, x3, y3):
    if not is_positive_integer(i):
        print("Invalid Input. Please enter positive and integer numbers")
        valid_input = False
        break

if valid_input:
  if is_triangle(x1, y1, x2, y2, x3, y3):
      print("These points can form a triangle.")
      area = calculate_area(x1, y1, x2, y2, x3, y3)
      print("Area of the triangle is:", area)

      zel1 = calculate_distance(x1, y1, x2, y2)
      zel2 = calculate_distance(x2, y2, x3, y3)
      zel3 = calculate_distance(x3, y3, x1, y1)

      print("Type of triangle:", triangle_type(zel1, zel2, zel3))
  else:
      print("These points cannot form a triangle.")