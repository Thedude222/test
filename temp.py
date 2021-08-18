salary = float(input("Insert salary: "))
TAX1 = 6310
TAX2 = 9050
TAX3 = 14530
TAX4 = 20200
TAX5 = 42030
TAX6 = 54130
TAX7 = 54131
tax = 0
if salary > TAX7:
    partial_salary = salary - TAX7
    tax = tax+partial_salary * 0.5
    salary = TAX7
    print("youll pay " + str(tax) + "at the 7th tax bracket")
if salary > TAX6:
    partial_salary = TAX6 - TAX5
    tax = tax + partial_salary * 0.47
    salary = TAX6
    str(tax)
    print("youll pay " + str(tax) + "at the 6th tax bracket")
    float(tax)
if  salary > TAX5:
    partial_slary = salary - TAX5
    tax = tax + partial_salary * 0.35
    salary = TAX5
    str(tax)
    print("youll pay " + str(tax) + "at the 5th tax bracket")
    float(tax)
if  salary > TAX4:
    partial_slary = salary - TAX4
    tax = tax + partial_salary * 0.31
    salary = TAX4
    str(tax)
    print("youll pay " + str(tax) + "at the 4th tax bracket")
    float(tax)
if  salary > TAX3:
    partial_slary = salary - TAX3
    tax = tax + partial_salary * 0.20
    salary = TAX3
    str(tax)
    print("youll pay " + str(tax) + "at the 3rd tax bracket")
    float(tax)
if  salary > TAX2:
    partial_slary = salary - TAX2
    tax = tax + partial_salary * 0.14
    salary = TAX2
    str(tax)
    print("youll pay " + str(tax) + "at the 2nd tax bracket")
    float(tax)
if  salary > TAX1:
    partial_slary = salary - TAX1
    tax = tax + partial_salary * 0.10
    salary = TAX1
    str(tax)
    print("youll pay " + str(tax) + "at the 1st tax bracket")
    float(tax)