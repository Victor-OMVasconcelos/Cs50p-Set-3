

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}




while True:
    date = input("Date: ")
    if date[0].isdigit():
        new_date = date.split("/")
        first = new_date[2]
        second =  new_date[0]
        if int(second) < 10:
            second = "0" + second
        third =  new_date[1]
        if int(third) < 10:
            third = "0" + third
        if int(second) > 12 or int(third) > 31:
            pass
        else:
            break
      
    if date[0].isalpha():
        new_date = date.replace(",", "")
        new_date = new_date.split()
        first = new_date[2]
        second = new_date[0]
        second = months.get(second.capitalize())
        if int(second) < 10:
            second = "0" + str(second)
        third =  new_date[1]
        if int(third) < 10:
            third = "0" + str(third)
        if int(second) > 12 or int(third) > 31:
            pass
        else:
            break
        
    
       
        

newer_date = first + "-" + second + "-" + third
print(newer_date)
            
        
   
    
    

    
