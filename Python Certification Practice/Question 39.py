distance = int(input("Enter the distance traveled in feet: "))

distance_miles = distance/ 5280    #convert to miles

time = float(input("Enter the time elapsed in seconds: "))

time_hours = time/3600     #convert to hours

velocity = distance_miles/time_hours

print("The average velocity is :", velocity, "miles/hour.")