#Question 1
bradley_array=[[1,2,3],[3,4,5],[6,7,8]]
print(bradley_array[1][1])

#Question 2
ls=[60,45,32,12,21,87,90,170,121]
ls.sort()
print('Ascending order: ',ls)
ls.reverse()
print('Descending order: ',ls)

#Question 3
ls=[[1,2,3],[4,5,6]]
if max(ls[0])==max(ls[1]):
    print(max(ls[0]))
elif max(ls[0]) > max(ls[1]):
   print(max(ls[0]))
else:
    print(max(ls[1]))
          
#Question 4
total=0
marks=[0,0,0,0,0]
for i in range(5):
    marks[i]=int(input('Enter marks: '))
    total+=marks[i]
percentage=total/5
print('Total: ',total)
print('Percentage: ',percentage,'%')
if percentage < 50:
    print('Grade:C')
elif percentage == 50 and percentage < 80:
    print('Grade:B')
elif percentage >= 80:
    print('Grade:A')
else:
    pass

#Question 5
def email(txt_file):
    the_email=None
    f=open(txt_file, "r")
    for line in f.readlines():
        if '@'in line:
            the_email=line.strip()
    return the_email
print(email("txt_file.txt"))

#Question 6
def check_speed(speed):
    if speed < 70:
        print('Ok')
    elif speed > 70 and speed <130:
        print('Points: ',(speed-70)/5)
    elif speed >= 130:
        print('License suspended')
def main():
    check_speed(130)
main()

#Question 7
def show_stars(rows):
    ls=''
    for i in range(rows):
        ls+='*'
        print(ls)
show_stars(5)
        
#Question 8
for i in range(2000,3201):
    if (i%7 == 0) and (i%5 != 0):
        print(i,' ',end='')
print()

#Question 9
digits=input("Enter values: ")
def arrange(digits):
    new_list=list(digits.split(","))
    new_tuple=tuple(digits.split(","))
    print (new_list)
    print(new_tuple)
    return 
print(arrange(digits))

#Question 10
import math
C=50
H=30
digits=input("Enter values: ")
new_list=list(digits.split(","))
for i in range(len(new_list)):
    new_list[i]=int(new_list[i])
    new_list[i]=int(math.sqrt((2*C*new_list[i])/H))
    print(new_list[i],end=',')

#Question 11
def five(num):
    try:
        print(num/0)
    except:
        print("Something went wrong!")
print(five(5))

#Question 12
cars=[['Ferrari','Red'],['Jeep','Gold'],['Aston Martin','Blue']]
choice=input('Enter car choice: ')
for i in range(len(cars)):
    if choice == cars[i][0]:
        print(cars[i])

