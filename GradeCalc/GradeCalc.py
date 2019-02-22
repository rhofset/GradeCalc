#!/usr/bin/env python3

__author__ = "Runar Hofset"
__copyright__ = "Copyright 2019, Runar Hofset"
__credits__ = ["Runar Hofset"]
__license__ = "GPL"
__version__ = "0.1.4"
__maintainer__ = "Runar Hofset"
__email__ = "rhofset@gmail.com"
__status__ = "Development"


def __init__():
	pass

def main ():
	"""
	Main menu with choices
	"""
	menu()
	menuinput = input("Type in your choice: ")
	while menuinput.lower != "exit":
		if menuinput == "1":
			print("\nMenu 1 is working\n")
			main()
		elif menuinput == "2":
			print("\nMenu 2 is working\n")
			menu2()
		else:
			exit()

def menu1():
	pass

def menu2():
	courses = input("How many corses do you have")
	if courses.isdigit == True:
		
	print(courses)

def menu():
	"""
	Just the menu print.
	"""
	menu = ["1. load from file?",
			"2. Make a new file?"]
	for item in menu:
		print(item)

if __name__ == "__main__":
	main()

"""
# Text explaining what this program is doing
print("Calculate average grade for your grades at Noroff, use . as ,""\n")

# Enter your score/grade i each assessment of PBL

PBLassessment_1 = float(input("Enter your score off 100 points in PBL assessment 1:  "))
while PBLassessment_1 > 100:
	print("Your number is to high. Maximum is 100")
	PBLassessment_1 = float(input("Enter your score off 100 points in PBL assessment 1:  "))
else:
	print("Your score in assessment 1", PBLassessment_1)

PBLassessment_2 = float(input("Enter your score off 100 points in PBL assessment 2:  "))
while PBLassessment_2 > 100:
	print("Your number is to high. Maximum is 100")
	PBLassessment_2 = float(input("Enter your score off 100 points in PBL assessment 2:  "))
else:
	print("Your score in assessment 2", PBLassessment_2)

PBLassessment_3 = float(input("Enter your score off 100 points in PBL assessment 3:  "))
while PBLassessment_3 > 30:
	print("Your number is to high. Maximum is 30")
	PBLassessment_3 = float(input("Enter your score off 30 points in PBL assessment 3:  "))
else:
	print("Your score in assessment 3:", PBLassessment_3)

ISSassessment_1 = float(input("Enter your score off 100 points in ISS assessment 1:  "))
while ISSassessment_1 > 100:
	print("Your number is to high. Maximum is 100")
	ISSassessment_1 = float(input("Enter your score off 100 points in ISS assessment 1:  "))
else:
	print("Your score in assessment 3:", ISSassessment_1)

ISSassessment_2 = float(input("Enter your score off 100 points in ISS assessment 2:  "))
while ISSassessment_2 > 100:
	print("Your number is to high. Maximum is 100")
	ISSassessment_2 = float(input("Enter your score off 30 points in ISS assessment 2:  "))
else:
	print("Your score in assessment 3:", ISSassessment_2)

PACassessment_1 = float(input("Enter your score off 100 points in PAC assessment 1:  "))
while PACassessment_1 > 100:
	print("Your number is to high. Maximum is 100")
	PACassessment_1 = float(input("Enter your score off 100 points in PAC assessment 1:  "))
else:
	print("Your score in assessment 3:", PACassessment_1)

PACassessment_2 = float(input("Enter your score off 100 points in PAC assessment 2:  "))
while PACassessment_2 > 100:
	print("Your number is to high. Maximum is 100")
	PACassessment_2 = float(input("Enter your score off 100 points in PAC assessment 2:  "))
else:
	print("Your score in assessment 3:", PACassessment_2)

PACassessment_3 = float(input("Enter your score off 30 points in PAC assessment 3:  "))
while PACassessment_3 > 30:
	print("Your number is to high. Maximum is 30")
	PACassessment_3 = float(input("Enter your score off 30 points in PAC assessment 3:  "))
else:
	print("Your score in assessment 3:", PACassessment_3)

# calculate your score/grade, and check if your score is valid.
PBL1 = (PBLassessment_1 * 0.2) + (PBLassessment_2 * 0.6) + (((PBLassessment_3 / 30) * 100)* 0.2)
if PBL1 > 100:
	print("You have input some wrong numbers somewhere!! Try again!")
ISS1 = (ISSassessment_1 * 0.2) + (ISSassessment_2 * 0.8)
if ISS1 > 100:
	print("You have input some wrong numbers somewhere!! Try again!")
PAC1 = (PACassessment_1 * 0.2) + (PACassessment_2 * 0.6) + (((PACassessment_3 / 30) * 100) * 0.2)
if PAC1 > 100:
	print("You have input some wrong numbers somewhere!! Try again!")

# print to screen the total score/grade
print()
print("PBL score = ", round(PBL1, 2))
print("ISS score = ", round(ISS1, 2))
print("PAC score = ",round(PAC1, 2))
tgrade = (PBL1 + ISS1 + PAC1)/3
print()
print("You got", + round(tgrade, 2), "of 100")

# What letter Grade it relate to (A, B, C, D, E or F)
print()
if tgrade < 40:
	print("F, You have failed, need to take this course one more time!")
elif tgrade > 40 and tgrade < 49.9:
	print("Your Grade is: E")
elif tgrade > 50 and tgrade < 59.9:
	print("Your Grade is: D")
elif tgrade > 60 and tgrade < 79.9:
	print("Your Grade is: C")
elif tgrade > 80 and tgrade < 89.9:
	print("Your Grade is: B")
elif tgrade > 90 and tgrade <= 100:
	print("Your Grade is: A")
elif tgrade > 100:
	print("No Grade, You have done something wrong!")


# What grade you need to get in next course to be at the same level. (to digits behind comma)
print()
if tgrade < 40:
	print("You need a minimum score off", + (40 * 2) - round(tgrade, 2), "to keep your current to get a E")
elif tgrade > 40 and tgrade < 49.9:
	print("You need a minimum score off", + (40 * 2) - round(tgrade, 2), "to keep your current E after the next course.")
elif tgrade > 50 and tgrade < 59.9:
	print("You need a minimum score off", + (50 * 2) - round(tgrade, 2), "to keep your current D after the next course.")
elif tgrade > 60 and tgrade < 79.9:
	print("You need a minimum score off", + (60 * 2) - round(tgrade, 2), "to keep your current C after the next course.")
elif tgrade > 80 and tgrade < 89.9:
	print("You need a minimum score off", + (80 * 2) - round(tgrade, 2), "to keep your current B after the next course.")
elif tgrade > 90 and tgrade < 100:
	print("You need a minimum score off", + (90 * 2) - round(tgrade, 2), "to keep your current A after the next course.")
elif tgrade > 100:
	print("You don't need any advice! :-)")
print()

#test1
# What grade to get next so your average is going up one step (to digits behind comma)
if tgrade < 40:
	print("You need a minimum score off", + (40 * 2) - round(tgrade, 2), "to get a average of E")
	print("You need a minimum score off", + (50 * 2) - round(tgrade, 2), "to get a average of D.")
	print("You need a minimum score off", + (60 * 2) - round(tgrade, 2), "to get a average of C.")
	print("You need a minimum score off", + (80 * 2) - round(tgrade, 2), "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - round(tgrade, 2), "to get a average of A.")
elif tgrade > 40 and tgrade < 49.9:
	print("You need a minimum score off", + (50 * 2) - round(tgrade, 2), "to get a average of D.")
	print("You need a minimum score off", + (60 * 2) - round(tgrade, 2), "to get a average of C.")
	print("You need a minimum score off", + (80 * 2) - round(tgrade, 2), "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - round(tgrade, 2), "to get a average of A.")
elif tgrade > 50 and tgrade < 59.9:
	print("You need a minimum score off", + (60 * 2) - round(tgrade, 2), "to get a average of C.")
	print("You need a minimum score off", + (80 * 2) - round(tgrade, 2), "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - round(tgrade, 2), "to get a average of A.")
elif tgrade > 60 and tgrade < 79.9:
	print("You need a minimum score off", + (80 * 2) - round(tgrade, 2), "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - round(tgrade, 2), "to get a average of A.")
elif tgrade > 80 and tgrade < 89.9:
	print("You need a minimum score off", + (90 * 2) - round(tgrade, 2), "to get a average of A.")
elif tgrade > 90 and tgrade < 100:
	print("You have already a top score")
elif tgrade > 100:
	print("You have typed some wrong numbers! :-)")
print()
"""
