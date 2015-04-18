#John F. Lake, Jr. & Kyle Kozak
#CSE30151 Project 3
#Turing Machine
import sys
import re
#testing desktop github


#This will get all 6 Parts of the DPDA:
def getTM(filename):
	numTransitions =0
	trans={}
	n = {}
	fd =  open(filename,'r') 
	for line in fd:
		#read lines one by one:	
		if(line[0] == 'A'):
			#Get the alphabet. 
			alpha = []
			alpha = re.split(',|\n', line[2:-1])
			if len(alpha) == 1 and alpha[0] == "":
				return -1
		
			n['alphabet'] = alpha
		elif(line[0] == 'Z'):
			#Get the tape alphabet. 
			talpha = []
			talpha = re.split(',|\n', line[2:-1])
			if len(talpha) == 1 and talpha[0] == "":
				return -1
			n['talphabet'] = talpha

		elif(line[0] == 'Q'):
			#Get the states:
			states = []
			states = re.split(',|\n', line[2:-1])
			if len(states) == 1 and states[0] == "":
				return -1

			n['states'] = states


		elif(line[0] == 'T'):
			#Increase the number of transitions by one:
			numTransitions+=1
	
			#Place the transition function inside a list
			# t[0] is the starting point
			# t[1] is the input
			# t[2] is the next state
			# t[3] is the value to be written
			# t[4] is the direction to go
			t = []
			t = re.split(',|\n', line[2:-1])
			if len(t) == 1 and t[0] == "":
				return -1
			elif t[0] not in n['states'] or t[2] not in n['states']:
				return -1	
			elif t[1] not in n['talphabet']:
				return -1
			elif t[3] not in n['talphabet']:
				return -1
			elif t[4] is not 'R' and t[4] is not 'L':
				return -2

			trans[numTransitions] = t

		
		elif(line[0] == 'S'):
			#Obtain the starting state:
			s = []
			s = re.split(',|\n', line[2:-1])
			if len(s) == 1 and s[0] == "":
				return -1

			n['start'] = s


		elif(line[0] == 'F'):
			#Obtain the end states:
			f = []
			f = re.split(',|\n', line[2:-1])
			if len(f) == 1 and f[0] == "":
				return -1
			elif len(f) is not 2:
				return -1

			n['acceptStates'] = f
		else:
			return -1
	fd.close()
	n['transitions'] = trans
	return n


def processInput(tm):

 	numInputTapes = int(raw_input(""))

	#Get each input tape and delimit it. 
	for i in range(numInputTapes):

		#Get the input: 
		it = raw_input("")
		inputTape = re.split(',',it)
		stack = []

		#Used to make sure the input is valid: 
		validInput=1;

		#Set the css to whatever the start state is: 
		cs = tm['start'][0]



						
				
				
	

def main(argv):
	#DPDA is a dictionary. Set it up:
	tm = {}
	tm = getTM(argv[1])	
	for key,value in tm.iteritems():
		print tm[key]



	if(tm == -1):
	else:
		if(tm != 0):
			#There is a valid NFA: 
			processInput(tm)



if __name__ == "__main__":
	main(sys.argv);

