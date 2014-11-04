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
'Scale10', 'yn' [yes/no], 'OpenResponse', Time, 'intResponse'

Question id--unique id for each question
'''
	def askQuestion(prompt,typeString, id):
		if (typeString=='Scale10'):
			askQuestionScale10(prompt)
		elif (typeString=='yn')
			askQuestionyn(prompt)





	def askQuestionScale10(prompt):
		response=input(prompt+'\n[Enter Response as a digit 1-10]')
		# Check response
		while 1
			if (response.isdigit()):
				writeQuestionData(prompt, id, repsonse)
				break
			else:
				print "Please enter response as a digit 1-10"

	def askQuestionyn(prompt):
		response=input(prompt+'\n[Enter Response as yes or no]')
		# Check response
		while 1
			if (response == 'yes' or response == 'no'):
				writeQuestionData(prompt, id, repsonse)
				break
			else:
				print "Please yes or no lowercase"	
				




	'''
	Get the CSV header, figure out if the question has been asked before
	Header should look like this:
	prompt @id
	''' 
	def writeQuestionData(prompt,id,response):








		






