with open('Street_Centrelines.csv',"rt") as a, open('Bus_Stops.csv', "rt") as b:
 count=0
 
for line in a,b:
  if "Accessible" and "ARTERIAL" in line:
   if "Non-Standard" and "LOCAL STREET" in line:
    if "Inaccessible" and "MINOR COLLECTOR" in line:
     count += 1
print(count)

