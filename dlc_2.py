"""
- Fitssistant Support Module [DLC_2] -
By Kaan Knight Oznacar

Calculating:
	- BMR
	- Total Daily Expenditure
	- Target Daily Calorie Intake

	Energy Balancing
	Macronutrient Balancing
"""
import time
class HealthIO:
	def __init__(self, weight, height, age):
		self.weight = weight
		self.height = height
		self.age = age

## Data Retrival Methods
	def get_weight(self):
		return self.weight

	def get_height(self):
		return self.height

	def get_age(self):
		return self.age

## Modification Methods
	def change_weight(self, new_weight):
		self.weight = new_weight
		return self.weight

	def change_age(self, new_age):
		self.age = new_age
		return self.age

## Calculation Methods
	def calc_BMR(self):
		BMR = (10 * int(self.weight)) + (6.25 * int(self.height)) - (5 * int(self.age)) + 5
		print("\n| HealthIO: Your Basal Metabolic Rate (BMR) is:", int(BMR))
		print("") 
		return int(BMR)

	def calc_TDEE(self):
		TDEE = self.calc_BMR()
		menu = """\n| HealthIO: How active are you?
		\t1. Sedentary    (0hrs a week)
		\t2. Light        (1 to 3hrs a week)
		\t3. Moderate     (4 to 6hrs a week)
		\t4. Very Active  (7 to 9hrs a week)
		\t5. Extra Active (10+hrs a week)
		\n"""

		print(menu)
		choice = input("You: ")

		if choice == '1':		# Sedentary (0hrs)
			TDEE = TDEE * 1.15
			print("\n| Health IO: Your Total Daily Energy Expenditure (TDEE) is:", int(TDEE))
			print("")
			return int(TDEE)

		elif choice == '2':		# Light (1 to 3hrs)
			TDEE = TDEE * 1.25
			print("\n| Health IO: Your Total Daily Energy Expenditure (TDEE) is:", int(TDEE))
			print("")
			return int(TDEE)

		elif choice == '3':		# Moderate (4 to 6hrs)
			TDEE = TDEE * 1.45
			print("\n| Health IO: Your Total Daily Energy Expenditure (TDEE) is:", int(TDEE))
			print("")
			return int(TDEE)

		elif choice == '4':		# Very Active (7 to 9hrs)
			TDEE = TDEE * 1.65
			print("\n| Health IO: Your Total Daily Energy Expenditure (TDEE) is:", int(TDEE))
			print("")
			return int(TDEE)

		elif choice == '5':		# Extra Active (10+hrs)
			TDEE = TDEE * 1.85
			print("\n| Health IO: Your Total Daily Energy Expenditure (TDEE) is:", int(TDEE))
			print("")
			return int(TDEE)

		else:
			print("\n| HealthIO: I didn't understand your input. Returning you back to the main menu.")

	def calc_TDCI(self, TDEE):
		TDCI = 0
		menu = """\n| HealthIO: What Calorie Deificit route are you following?
		\t 1. Easy   10% Calorie Deficit
		\t 2. Medium 15% Calorie Deficit 
		\t 3. Hard   25% Calorie Deficit
		\n"""

		print(menu)
		choice = input("You: ")

		if choice == '1':		# Easy
			TDCI = TDEE * 0.85
			print("\n| HealthIO: Your Daily Total Calorie Intake is:", int(TDCI)) 
			print("")
			return int(TDCI)
		
		elif choice == '2':		# Medium
			TDCI = TDEE * 0.80
			print("\n| HealthIO: Your Daily Total Calorie Intake is:", int(TDCI))
			print("")
			return int(TDCI)

		elif choice == '3':		# Hard
			TDCI = TDEE * 0.75
			print("\n| HealthIO: Your Daily Total Calorie Intake is:", int(TDCI))
			print("")
			return int(TDCI)

		else:
			print("\n| HealthIO: I didn't understand your input. Returning you back to the main menu.")

	def calc_MACROS(self, DCTI):
		copy = DCTI
		MACROS = [] # [0] = Protein & Carbohydrate in GRAMS, [1] = Fat in GRAMS
		
		## Protein & Carbohydrate in GRAMS
		DCTI = (DCTI * 0.4) / 4
		MACROS.append(round(DCTI))

		## Fat in GRAMS
		copy = (copy * 0.2) / 9
		MACROS.append(round(copy))

		## Print Outs
		print("\n| Health IO: Your Daily Macronutrient Consumption goal (in grams):")
		print("-------------------------------")
		print("| Protein: ", str(MACROS[0]) + "g", "    | 40 percent of DCTI")
		print("| Carbohydrate:", str(MACROS[0]) + "g", "| 40 percent of DCTI")
		print("| Dietary Fat:", str(MACROS[1]) + "g", "  | 20 percent of DCTI")
		print("-------------------------------\n")

		#def calc_NUTRICAL(self, cal, protein, carb, fat, inc):