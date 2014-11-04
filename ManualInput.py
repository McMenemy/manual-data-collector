
'''
This class deals with getting manual data input from the user.
@author Suyash Kumar
'''
class ManualInput:
	outputFileName=""
	def __init__(self,outputFileName):
		self.outputFileName=outputFileName
		f=open(outputFileName,'a') # Open file with append specifier



