def valid_triangle(a,b,c):
  if a+b>=c and b+c>=a and c+a>=b:
    return True
  else:
    return False
side_a = float(input("Enter length of side:"))
side_b = float(input("Enter length of side:"))
side_c = float(input("Enter length of side:"))
if valid_triangle(side_a,side_b,side_c):
   print("Triangle is valid")
else:
  print("Triangle is invalid")