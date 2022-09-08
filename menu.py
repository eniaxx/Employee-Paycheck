import commands as do

#Menu Class with __init__, __err__, which_case, print_menu, case_0 to case_6
class Menu:

	dir = './Menu/'

	def __init__(self, menu_choice):

		self.menu_choice = menu_choice

	def command_selection(self):
		
		match self.menu_choice:
			
			case 'Start':
				
				print(open((self.dir + 'start_menu.txt')).read())
			
			case 'Employee':

				print(open((self.dir + 'employee_menu.txt')).read())

		#infinite loop with exception for anything else than int and break
		while True:
			try:
				argument = 'case_' + str(int(input('\n Type a number. \n')))
				break
			
			except ValueError:
				print('\n Invalid. Use valid number.')

		print(argument)

		getattr(self, argument, lambda: (print('\n Incorrect choice. Choose again.'), self.command_selection()))()

	#Defined case functions and their behavior
	def case_0(self):

		match self.menu_choice:
			
			case 'Start':

				print('\n See you soon.')

				exit()

			case 'Employee':

				self.command_selection('Start')
				#self('Start').command_selection()

	def case_1(self):

		match self.menu_choice:
			
			case 'Start':

				Menu('Employee').command_selection()

			case 'Employee':

				pass
		
	def case_2(self):

		match self.menu_choice:
			
			case 'Start':

				file_name = do.Database.database_name()

				file_data = do.Database.read(file_name)

				do.Operation.store(file_name, file_data)

				Menu(self).command_selection()

			case 'Employee':

				Menu('Start').command_selection()

	def case_3(self):

		match self.menu_choice:
			
			case 'Start':

				do.Operation.empty_database_check()

				do.Operation.sum('Salary')

				do.Operation.sum('Bonus')

			case 'Employee':

				pass

	def case_4(self):

		match self.menu_choice:
			
			case 'Start':

				print('\n See you soon.')

				exit()

			case 'Employee':

				Menu('Start').command_selection()
	
	def case_5(self):

		match self.menu_choice:
			
			case 'Start':

				pass

			case 'Employee':

				pass
	
	def case_6(self):

		match self.menu_choice:
			
			case 'Start':

				pass

			case 'Employee':

				pass