
with open("Street_Centerlines.csv") as file:
 
 a = [tuple (line( [STR_NAME],[FULL_NAME],[FROM_STR],[TO_STR] ))for line in file]

print (a)


def histogram ():
 d = {}
 for row in file:
  key="MAINTENANCE" 
  val=number of streets
  (key,val) = row
  d[int(key)] = val
 print(d)
