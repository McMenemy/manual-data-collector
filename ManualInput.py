'''
This class deals with getting manual data input from the user.
@author Suyash Kumar (suyashkumar) and Josh McMenemy (mcmenemy)
'''

class ManualInput:
	outputFileName=""
	def __init__(self,outputFileName):
		#TODO: adjf;
		self.outputFileName=outputFileName
		#f=open(outputFileName,'a') # Open file with append specifier

'''
This method asks the user a question with the prompt and of the type specified. 
The type specifier is a string: 
<<<<<<< HEAD
'Scaleten', 'yn' [yes/no], 'OpenResponse', Time, 'intResponse'
'''
	def askQuestion(prompt,typeString):
		if (typeString=='Scaleten'):
			askQuestionScaleten(prompt)
=======
'Scale10', 'yn' [yes/no], 'OpenResponse', Time, 'intResponse'

Question id--unique id for each question
'''
	def askQuestion(prompt,typeString, id):
		if (typeString=='Scale10'):
			askQuestionScale10(prompt)
>>>>>>> FETCH_HEAD

	def askQuestionScaleten(prompt):
		response=input(prompt+'\n[Enter an integer 1-10]')
		if (response.isdigit()):
			write


	'''
	Get the CSV header, figure out if the question has been asked before
	Header should look like this:
	prompt @id
	'''
	def writeQuestionData(prompt,id,response):







		






