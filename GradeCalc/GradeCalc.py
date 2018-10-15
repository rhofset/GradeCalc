#!/usr/bin/env python

__author__ = "Runar Hofset"
__copyright__ = "Copyright 2018, Runar Hofset"
__credits__ = ["Runar Hofset"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Runar Hofset"
__email__ = "rhofset@gmail.com"
__status__ = "Development"

# Text explaining what this program is doing
print("Calculate grade for Project Based Learning, use . as ,")
print()

# Enter your score/grade i each assessment of PBL

PBLassessment_1 = float(input("Enter your score off 100 points in PBL assessment 1:  "))
if PBLassessment_1 > 100:
	print("You number is to high, try again!")
	float(input("Enter your score off 100 points in PBL assessment 1:  "))

PBLassessment_2 = float(input("Enter your score off 100 points in PBL assessment 2:  "))
if PBLassessment_2 > 100:
	print("You number is to high, try again!")
	float(input("Enter your score off 100 points in PBL assessment 2:  "))

PBLassessment_3 = float(input("Enter your score off 30 points in PBL assessment 3:  "))
if PBLassessment_3 > 30:
	print("You number is to high, try again!")
	float(input("Enter your score off 30 points in PBL assessment 3:  "))

# calculate your score/grade
PBL1 = (PBLassessment_1 * 0.2) + (PBLassessment_2 * 0.6) + (((PBLassessment_3 / 30) * 100)* 0.2)
if PBL1 > 100:
	print("You have input some wrong numbers somewhere!! Try again!")

# print to screen the total score/grade
tgrade = PBL1
print()
print("You got", + tgrade, "of 100")

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
elif tgrade > 90 and tgrade < 100:
	print("Your Grade is: A")
elif tgrade > 100:
	print("No Grade, You have done something wrong!")

# What grade you need to get in next course to be at the same level
print()
if tgrade < 40:
	print("You need a minimum score off", + (40 * 2) - tgrade, "to keep your current to get a E")
elif tgrade > 40 and tgrade < 49.9:
	print("You need a minimum score off", + (40 * 2) - tgrade, "to keep your current E after the next course.")
elif tgrade > 50 and tgrade < 59.9:
	print("You need a minimum score off", + (50 * 2) - tgrade, "to keep your current D after the next course.")
elif tgrade > 60 and tgrade < 79.9:
	print("You need a minimum score off", + (60 * 2) - tgrade, "to keep your current C after the next course.")
elif tgrade > 80 and tgrade < 89.9:
	print("You need a minimum score off", + (80 * 2) - tgrade, "to keep your current B after the next course.")
elif tgrade > 90 and tgrade < 100:
	print("You need a minimum score off", + (90 * 2) - tgrade, "to keep your current A after the next course.")
elif tgrade > 100:
	print("You don't need any advice! :-)")
print()

# What grade to get next so your average is going up one step
if tgrade < 40:
	print("You need a minimum score off", + (40 * 2) - tgrade, "to get a average of E")
	print("You need a minimum score off", + (50 * 2) - tgrade, "to get a average of D.")
	print("You need a minimum score off", + (60 * 2) - tgrade, "to get a average of C.")
	print("You need a minimum score off", + (80 * 2) - tgrade, "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - tgrade, "to get a average of A.")
elif tgrade > 40 and tgrade < 49.9:
	print("You need a minimum score off", + (50 * 2) - tgrade, "to get a average of D.")
	print("You need a minimum score off", + (60 * 2) - tgrade, "to get a average of C.")
	print("You need a minimum score off", + (80 * 2) - tgrade, "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - tgrade, "to get a average of A.")
elif tgrade > 50 and tgrade < 59.9:
	print("You need a minimum score off", + (60 * 2) - tgrade, "to get a average of C.")
	print("You need a minimum score off", + (80 * 2) - tgrade, "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - tgrade, "to get a average of A.")
elif tgrade > 60 and tgrade < 79.9:
	print("You need a minimum score off", + (80 * 2) - tgrade, "to get a average of B.")
	print("You need a minimum score off", + (90 * 2) - tgrade, "to get a average of A.")
elif tgrade > 80 and tgrade < 89.9:
	print("You need a minimum score off", + (90 * 2) - tgrade, "to get a average of A.")
elif tgrade > 90 and tgrade < 100:
	print("You have already a top score")
elif tgrade > 100:
	print("You have typed some wrong numbers! :-)")
print()