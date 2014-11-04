'''
This class deals with getting manual data input from the user.
@author Suyash Kumar (suyashkumar) and Josh McMenemy (mcmenemy)
'''

class ManualInput:
	outputFileName=""
	def __init__(self,outputFileName):
		#TODO: adjf;
		self.outputFileName=outputFileName
		f=open(outputFileName,'a') # Open file with append specifier

'''
This method asks the user a question with the prompt and of the type specified. 
The type specifier is a string: 
'Scale10', 'yn' [yes/no], 'OpenResponse', Time, 'intResponse'
'''
	def askQuestion(prompt,typeString):
		if (typeString=='Scale10'):
			askQuestionScale10(prompt)

	def askQuestionScale10(prompt):
		response=input(prompt+'\n[Enter Response as a digit 1-10]')
		# Check response
		if (response.isdigit()):
			#TODO Add methods 


	'''
	Get the CSV header, figure out if the questions has been asked before
	'''







		






