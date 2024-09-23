# Programa básico em Python para
# visualizar o calendário dado o ano e o mês
import calendar 
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')



aa = 2024
mm = 9
obj_calendar_d0 = calendar.Calendar(firstweekday=6)
# obj_calendar_d1 = calendar.Calendar(firstweekday=1)

calendar.setfirstweekday(calendar.SUNDAY)

print("calendar.firstweekday(): \n")
print(calendar.firstweekday())

print("\n-------------\n")


print("calendar.month(aa, mm): \n") 
print(calendar.month(aa, mm)) 
print("\n-------------\n")

print("obj_calendar_d0.iterweekdays(): \n")
for d in obj_calendar_d0.iterweekdays():
    print(f"{ d = }", end="\t")
print("\n-------------\n")


# for d in obj_calendar_d1.iterweekdays():
#     print(f"{ d = }", end="\t")

# print("\n\n")


print("Dom\tSeg\tTer\tQua\tQui\tSex\tSab")
i = 1
for x in obj_calendar_d0.itermonthdays(2024, 9):
    if i < 7:
        print(f"{x}", end="\t")
        i += 1
    else:
        print(f"{x }")
        i = 1

print("\n-------------\n")

print("obj_calendar_d0.itermonthdates(2024, 10): \n")
for x in obj_calendar_d0.itermonthdates(2024, 9):
    print(f"{ x = }", end="\t")

print("\n-------------\n")
# print("D\tS\tT\tQ\tQ\tS\tS")
# i = 1
# for x in obj_calendar_d1.itermonthdays(2024, 9):
#     if i < 7:
#         print(f"{x}", end="\t")
#         i += 1
#     else:
#         print(f"{x }")
#         i = 1

# print("\n\n")  
