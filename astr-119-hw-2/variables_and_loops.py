import numpy as np      #we use numpy for lots of things

def main():
	i=0 					#integers can be declared with a number
	n=10 					#here is another integer
	x=190.0 				#floating point nums are declared with a "."

	# we can use numpy to declare arrays quickly

	y = np.zeroes(n,dtype=float) #declares 10 zeroes as floats using np

	# we can use for loops to iterate with a variable 

	for i in range(n): 		#1 in range [0,n-1]
		y[i] = 2.0 * float(i) +1 		#set y = 2i+1 as floats

	#we can also simply iterate through a variable
	for y_element in y:
		print(y_element)

	#execute the main function			#professor Brant said to type something towards the end of some slides on tuesday's lecture.
	if __name__ == "__main__":
		main()