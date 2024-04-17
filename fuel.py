while True:
    try:
         frac = (input("Fraction: ").split("/"))
         x = int(frac[0])
         y = int(frac[1])
         if x > y:
             pass
         else:
             percent = (int(x) / int(y)) * 100
             break
    except (ValueError, ZeroDivisionError):
        pass
if percent >=99: 
    print("F")
elif percent <=1:
    print("E")
else:
    print(int(percent), "%")