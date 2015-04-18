#John F. Lake, Jr. & Kyle Kozak
#CSE30151 Project 3
#Turing Machine
import sys
import re


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

			n['endStates'] = f
		else:
			return -1
	fd.close()
	n['transitions'] = trans
	return n



#Function to write down the current state of the Turing machine
def printState(tape,pos,currentState):
	if pos is 0:
		sys.stdout.write('()')
		sys.stdout.write("%s(" % currentState)
		for i in range(pos,len(tape)):
			if i is len(tape)-1:
				sys.stdout.write("%s" % tape[i])
			else:
				sys.stdout.write("%s," % tape[i])
		print ")"
	else: 
		sys.stdout.write('(')
		for i in range(0,pos):
			if i is pos-1:
				sys.stdout.write("%s" % tape[i])
			else:
				sys.stdout.write("%s," % tape[i])
		sys.stdout.write(')')
		sys.stdout.write("%s(" % currentState)
		for i in range(pos,len(tape)):
			if i is len(tape)-1:
				sys.stdout.write("%s" % tape[i])
			else:
				sys.stdout.write("%s," % tape[i])
		print ")"


def processInput(tm):

	
	
	#Get the number of input tapes, with error checking
 	numInputTapes = raw_input("")
	if not numInputTapes.isdigit():
		print "Number of inputs needs to be a positive number."
		return
	else:
		numInputTapes = int(numInputTapes)
		if numInputTapes == 0:
			print "Number of inputs needs to be a positive number."
			return
			

	#Get each input tape and delimit it. 
	for i in range(numInputTapes):
		pos = 0
		done = 0

		#Get the input: 
		it = raw_input("")

		#The tape is infinite in one direction (to the right)
		tape = re.split(',',it)
		for input in tape:
			if input not in tm['alphabet']:
				print "REJECT: Input not in input alphabet!"
				return

		#Set the current state to whatever the start state is: 
		currentState = tm['start'][0]

		#for each input character (item), interpret its effect:
		while not done:

			#run through the transitinos and find the rule that governs the state we are in:
			for key,value in tm['transitions'].iteritems():


				#If the currentState matches the state from a transition AND the input matches
				if currentState == value[0] and tape[pos] == value[1]:

					
										
					printState(tape,pos,currentState)
					if currentState == tm['endStates'][0]:
						print "ACCEPT"
						done = 1
						break
					elif currentState == tm['endStates'][1]:
						print "REJECT"
						done = 1
						break
					#if the state matched, we do this:
					currentState = value[2]#set the next state we are going to
					output = value[3]#symbol to be written
					dir = value[4]#tape head direction
		

					#If you're moving right on the tape: 
					if dir is "R":
						tape[pos] = output
						pos = pos + 1
						if pos is len(tape):
							tape.append(' ')
							currentState = tm['endStates'][1]

					#If you're moving left: 
					elif dir is "L":
						tape[pos] = output
						pos = pos - 1
					if currentState == tm['endStates'][0]:
						printState(tape,pos,currentState)
						print "ACCEPT"
						done = 1
						break
					elif currentState == tm['endStates'][1]:
						printState(tape,pos,currentState)
						print "REJECT"
						done = 1
						break



def main(argv):
	
	#The Turing Machine is described by a dictionary
	tm = {}
	tm = getTM(argv[1])	


	if(tm == -1):
		print "ERROR, INVALID TM INPUT!"
	else:
		if(tm != 0):
			#There is a valid NFA: 
			processInput(tm)



if __name__ == "__main__":
	main(sys.argv);

