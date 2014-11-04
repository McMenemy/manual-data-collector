'''
This class deals with getting manual data input from the user.
@author Suyash Kumar (suyashkumar) and Josh McMenemy (mcmenemy)
'''
import os.path
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
	Write a [id].csv file. If exists, add row. 
	prompt @id
	''' 
	def writeQuestionData(prompt,id1,response):
		filename=''.join([id1,'.csv'])
		# Check if file already exists, if not then write header
		if !(os.path.isfile(filename)):
			writeHeader(filename,id1,prompt)

		f=open(filename, 'a') # Open a file for appending 
		f.write(response)
		f.close()

	def writeHeader(filename,id1,prompt):
		f=open(filename,'a')
		f.write(''.join([prompt,' @',id1]))
		f.close()











		






