def main():
	item_name = input('\nFor refrence purposes, what are you High Alcing? (Press enter to skip)\nEnter here: ')
	cost_of_item = int(input('What is the price paid for the item in question?\nEnter here: '))
	High_Alc_Value = int(input('What is the High Alchemy (High Alc for short) value of the item in question?\nEnter here: '))
	cost_Of_Nature_Rune = int(input('What is the cost of the Nature Runes used at time of purchase?\n(Average price of Nature Runes are 210)\nEnter here: '))

	volume_Of_Items = int(input('What is the volume of items being High Alced?\nEnter here: '))
	cost_of_business = cost_of_item + cost_Of_Nature_Rune
	profit_margin = High_Alc_Value - cost_of_business
	total_profit = profit_margin * volume_Of_Items
	print("\nThe following information referes to: " + item_name)
	print("The profit margin of the item in question is: " + str(profit_margin) + " gp.")
	print("The total profit gained is: " + str(total_profit) + " gp.\n")
	run_again()
	
def run_again():
	again = input('Would you like to run the program again? (Y/N)\nEnter here: ')
	if again == "y":
		run_again = True
		main()
	elif again == "n":
		print('Have a good day, goodbye!')
	else:
		print('Please type a single lowercase "y" for yes or "n" for no.')
		run_again()
			
	
	
main()
