
#xét tuổi đối tượng cấp 1, 2, 3 hay qua cấp 33
age = int(input("nhap tuoi"))
try:
     if age > 18:
          print("Tuoi:", str(age), "du tuoi lao dong")
     elif age == 16 and age <= 18:
          print("Tuoi:", str(age), "la hoc sinh cap 3")
     elif age == 11 and age <=15:
          print("Tuoi:", str(age), "la hoc sinh cap 2")
          print("Duoi tuoi lao dong")
     elif age == 6 and age <= 10:
          print("Tuoi", str(age), "la hoc sinh cap 1")
          print("Duoi tuoi lao dong")
     else:
          print("Tuoi", str(age), "gui nha tre chua vao cap 1")
except:
     print("Chua khai bao bien")
else:
     print("Khong co loi")
     
