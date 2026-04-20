#Parker Wood
#File handling

"""
#For a file in the same directory
#Read Mode
f=open('042026_testing.txt', 'r')

print("File Name: ", f.name)#Reads file name
print("File Mode: ", f.mode)
#print(f.read()) #Reads what is written inside of the file
#print(f.read(5)) #Reads only 5 characters in the file
#print(f.readline()) #Only reads one single line at a time
#print(f.readlines()) #Will put the lines as a list instead of a string

list_var = f.readlines()

print(list_var)


#For a file in the same directory
#Write Mode
f=open('042026_testing2.txt', 'w')

print("File Name: ", f.name)#Reads file name
print("File Mode: ", f.mode)

f.write("Plymouth State University")
print("Data is saved")
f.close()#You have to close to confirm changes

#For a file in the same directory
#Appened Mode
f=open('042026_testing2.txt', 'a')

print("File Name: ", f.name)#Reads file name
print("File Mode: ", f.mode)

f.write("\nD&M Room 442")
print("Data is saved")
f.close()#You have to close to confirm changes

#For a file in the same directory
#R+ Mode
f=open('042026_testing2.txt', 'r+')

print("File Name: ", f.name)#Reads file name
print("File Mode: ", f.mode)

print(f.read())
f.write("\nCS2370: Intro to Programming")
print("Data has been written")
f.close()#You have to close to confirm changes
"""
#For a file in the same directory
#W+ Mode
f=open('042026_testing2.txt', 'w+')

print("File Name: ", f.name)#Reads file name
print("File Mode: ", f.mode)

print(f.read())
f.write("\nCS2370: Intro to Programming")
print("Data has been over written")
f.close()#You have to close to confirm changes

