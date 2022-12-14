#Serch in String

text ="This is python course"
print(text.find('is'))
print(text.rfind('is'))

#split
print(text.split())


#valdation
value1="3789792"
value2="AMKCNCK"
value3="3789EFL>."

print(value1.isalnum())
print(value2.isalpha())
print(value1.isdigit())
print(value1.isidentifier())





#List advance :
value= [[1,2,3],3,4]
print(value[0][2])
#we can select specific index at List 






#filter function :
age=[10,15,30,22,27,18,12,40]

def filter_age(age):
    return age >=18
           #filter(condition,List)
print (list(filter(filter_age,age)))















