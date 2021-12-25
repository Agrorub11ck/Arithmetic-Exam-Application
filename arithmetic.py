import random
import math


def save_result(new_dict, nums, result):
	print('What is your name?')
	name = input()
	new_file = open("results.txt", 'a', encoding='utf-8')
	if nums == 1:
		print(f'{name}: {result}/5 in level {nums} (simple operations with numbers 2-9)', file=new_file)
	elif nums == 2:
		print(f'{name}: {result}/5 in level {nums} (integral squares of 11-29)', file=new_file)
	new_file.close()
	print('The results are saved in "results.txt".')


def level_answer1(nums):
	num_arr = [str(elem) for elem in range(2, 10)]
	sign = ['+', '*', '-']
	count = 0
	new_dict = {}
	for elem in range(5):
		stroke = random.choice(num_arr) + ' ' \
		         + random.choice(sign) + ' ' \
		         + random.choice(num_arr)

		while True:
			print(stroke)
			result = eval(stroke)
			try:
				num = eval(input())
				if int(num) == result:
					new_dict[num] = True
					print('Right!')
					count += 1
					break
				else:
					print('Wrong!')
					new_dict[num] = False
					break
			except Exception:
				print('Wrong format! Try again.')

	print(f'Your mark is {count}/5. Would you like to save the result? Enter yes or no.')
	answer = input()
	if answer in ["Yes", "YES", "yes", "y", "Y"]:
		save_result(new_dict, nums, count)
	else:
		return


def level_answer2(nums):
	count = 0
	new_dict = {}
	for elem in range(5):
		num = random.randint(11, 29)
		while True:
			try:
				print(num)
				result = input()
				if num ** 2 == int(result):
					new_dict[num] = True
					print('Right!')
					count += 1
					break
				else:
					print('Wrong!')
					new_dict[num] = False
					break
			except Exception:
				print('Wrong format! Try again.')

	print(f'Your mark is {count}/5. Would you like to save the result? Enter yes or no.')
	answer = input()
	if answer in ["Yes", "YES", "yes", "y", "Y"]:
		save_result(new_dict, nums, count)
	else:
		return


def level_dificulty():
	while True:
		try:
			print('Which level do you want? Enter a number:')
			print('1 - simple operations with numbers 2-9')
			print('2 - integral squares of 11-29')
			answer = int(input())
			if answer == 1:
				level_answer1(1)
				break
			elif answer == 2:
				level_answer2(2)
				break
			else:
				print('Incorrect format.')
		except Exception:
			print('Incorrect format.')


level_dificulty()
