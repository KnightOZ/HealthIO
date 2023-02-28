"""
- HealthIO -
By Kaan Knight Oznacar

A personal project made to help myself lose weight and become healthier.

All algorithms used to calculate in this program are for Men only, inaccuracies may occur if doing so for a Woman.
"""
## Imports
# import dlc_1 as s # Support Module import for functions and clean code
import dlc_2 as h   # Support Module import for functions and clean code
import time

## Profiles
p1 = h.HealthIO(113, 179, 23)     # Profile 1 - Kaan Knight Oznacar
p2 = h.HealthIO(125, 176.5, 23)   # Profile 2 - Mikail Alejandro Castilla


## Welcome Message
print(" -HealthIO- ")
print("Your personal Health & Fitness assistant.")
print("-----------------------------------------")
print("\n")

## Menu creation
menu = """\t\t- Main Menu -
\t'a' to Calculate your BMR
\t'b' to Calculate Total Daily Energy Expenditure
\t'c' to Calculate Daily Calorie Target Intake
\t'd' to Calculate your Macronutrient Requirements

\t'q' to quit the program.

\n| HealthIO: What would you like to do?"""

## Main
def run(patient):
	"""Main Function for Running code"""
	tdee = 0
	dcti = 0

	while True:
		print(menu)
		choice = input("| You: ").strip().lower()

		if choice == 'a':				# Basal Metabolic Rate
			patient.calc_BMR()

		elif choice == 'b':				# Total Daily Energy Expenditure
			tdee = patient.calc_TDEE()

		elif choice == 'c':				# Daily Calorie Target Intake
			if tdee > 0:
				dcti = patient.calc_TDCI(tdee)

			else:
				print("| HealthIO: You must first calculate your Total Daily Energy Expenditure.")

		elif choice == 'd':
			if dcti > 0:
				patient.calc_MACROS(dcti)

			else:
				print("| HealthIO: You must first calculate your Total Daily Energy Expenditure, and Daily Calorie Target Intake.")

		elif choice == 'q':
			print("| HealthIO: Good-bye.")
			time.sleep(2)
			break
run(p1)  # Put Profile variable in the function argument for it to work