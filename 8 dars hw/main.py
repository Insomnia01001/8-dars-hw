age = int(input("yoshingizni  kirirting : "))
if age >= 0 and age <= 4:
    print(f"sizni yoshiz {age} sizga bepul")
elif age >=5 and age <=15:
    print(f"sizni yoshiz {age} sizga  15 min ")
elif age >=16 and age <=65:
    print(f"sizni yoshiz {age} sizga 20 min ")
elif age > 65 :
    print("siz juda qarisiz sizga bepul ")
elif age <0 :
    print("unaqa yosh yoq")
else:
    print("siz yoshingizni kiritmadingiz")

temp=int(input("haroratni kiriting: ")) 
if temp < 0:
    print("havo jadayam sovuq ")  
elif temp >= 0 and temp <= 10:
    print("havo sovuq")
elif temp > 10 and temp <= 30:
    print("havo illiq")
elif temp > 30 and temp <= 50:
    print("havo issiq")
else:
    print("havoni haroratini kiritmadiz: ")

ball = int(input("ball kiriting 100 gacham: "))
if ball >= 90 and ball <= 100 :
    print(f"sizni ballingiz {ball} alo ")
elif ball >= 80 and ball < 90 :
    print(f"sizni balingiz {ball} yaxshi") 
elif ball >= 70 and ball < 80 :
    print(f"sizni balingiz {ball} qoniqarli") 
elif ball >= 0 and ball < 70 :
    print(f"sizni balingiz yomon")   
elif ball < 0:
    print("siz minus ball berolmaysiz")    
else:
    print("siz 0 dan 100 gacham ball berishingiz mumkun")     

