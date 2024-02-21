import ipdb

katz_deli = []

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.") 

def line(katz_deli):
    if len(katz_deli) == 0: 
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for index, name in enumerate(katz_deli, start = 1):
            line_status += f" {index}. {name}"
        print(line_status)
    

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")

take_a_number(katz_deli, "Logan")
take_a_number(katz_deli, "Avi")
take_a_number(katz_deli, "Spencer")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
take_a_number(katz_deli, "Matz")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)