
with open('Street_Centerlines.csv', "rt") as file:
 
 a = [tuple (line( [STR_NAME],[FULL_NAME],[FROM_STR],[TO_STR] ))for line in file]

print (a)

