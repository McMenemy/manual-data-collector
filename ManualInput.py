'''
This class deals with getting manual data input from the user.
@author Suyash Kumar (suyashkumar) and Josh McMenemy (mcmenemy)
'''
import os.path
class ManualInput:
	outputFileName=""
	def __init__(self):
		outputFileName=""
		
		#TODO: adjf;
		#self.outputFileName=outputFileName
		#f=open(outputFileName,'a') # Open file with append specifier
	
	'''
	This method asks the user a question with the prompt and of the type specified. 
	The type specifier is a string: 
	'Scale10', 'yn' [yes/no], 'OpenResponse', Time, 'intResponse'

	Question id1--unique id for each question
	'''
	def askQuestion(self,prompt,typeString, id1):
		if (typeString=='Scale10'):
			askQuestionScale10(prompt,id1)
		elif (typeString=='yn'):
			self.askQuestionYN(prompt,id1)


	def askQuestionScale10(self,prompt,id1):
		
		# Check response
		while 1:
			if (response.isdigit()):
				response=input(prompt+'\n[Enter Response as a digit 1-10]:\n')
				self.writeQuestionData(prompt, id1, repsonse)
				break
			else:
				print "Please enter response as a digit 1-10"

	def askQuestionYN(self,prompt,id1):
		
		# Check response
		while 1:
			response1=raw_input(prompt+'\n[Enter Response as y (yes) or n (no)]:\n')
			if (response1 == 'y' or response1 == 'n'):
				self.writeQuestionData(prompt, id1, response1)
				break
			else:
				print "Please enter a y or n:"


	'''
	Write a [id].csv file. One file per question. Change to Master Table later.
	If exists, add row. 
	prompt @id
	''' 
	def writeQuestionData(self,prompt,id1,response):
		filename=''.join([id1,'.csv'])
		# Check if file already exists, if not then write header
		if not (os.path.isfile(filename)):
			self.writeHeader(filename,id1,prompt)

		f=open(filename, 'a') # Open a file for appending 
		f.write(response)
		f.write('\n') # New Line
		f.close()

	def writeHeader(self,filename,id1,prompt):
		f=open(filename,'a')
		f.write(''.join([prompt,' @',id1,'\n']))
		f.close()











		






