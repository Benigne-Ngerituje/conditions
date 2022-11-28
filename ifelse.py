a=int(input("first user age : "))
b=int(input("second user age : "))

if  b < a :
  print("first user can pass")
  c=str(input("names : "))
  print(c)
elif a < b :
    print("Second user can pass")
    c = input("Names : ")
    print(c)
else:
    print("Stay at home")