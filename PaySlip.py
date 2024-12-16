bs = int(input("Enter Basic Salary: "))
exp = int(input("Enter Experience: "))
name = input("Enter name: ")

da = bs * 0.05
ta = bs * 0.065
cca = bs * 0.08
hra = bs * 0.10
pf = bs * 0.125


if exp > 25:
    bonus = bs * 0.25
elif exp > 20:
    bonus = bs * 0.20
elif exp > 15:
    bonus = bs * 0.15
else:
    bonus = bs * 0.10


total_salary = bs + da + ta + cca + hra + pf + bonus
net_salary = total_salary - pf

print("\nPayslip for:", name)
print("-" * 30)
print("Basic Salary:", bs)
print("DA:", da)
print("TA:", ta)
print("CCA:", cca)
print("HRA:", hra)
print("PF:", pf)
print("Bonus:", bonus)
print("Total Salary:", total_salary)
print("Net Salary:", net_salary)
