#პროგრამირებაში არის ამდენი ცვლადი რადგან კომპიტერმა იცოდეს რა სახის ინფრმაცია ინახება მასში
#მაგალით ცხოვრებიდან: input-ბარათის ჩადება ბანკომატში და პინ კოდის ჩაწერა , output: ფულის მიღება
name = "Alex"   
age = 14
height = 1.72

print(type(name))
print(type(age))
print(type(height))



km = float(input("შეიყვანე მანძილი კილომეტრებში: "))

meters = km * 1000

print("მანძილი მეტრებში არის:", meters)

num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

print("ჯამი:", num1 + num2)
print("სხვაობა:", num1 - num2)
print("ნამრავლი:", num1 * num2)
print("გამყოფი:", num1 / num2)


weight = float(input("შეიყვანე შენი წონა: "))
height = float(input("შეიყვანე შენი სიმაღლე-+: "))

bmi = weight / (height * height)

print("შენი BMI არის:", bmi)