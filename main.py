#to test: use GI Number 486126
# Import Functions
from seq.randGI import get_rand_GI
from seq.getFasta import get_fasta_sequence
from seq.formatSeq import format_sequence
from password.generatePassword import *

# Welcome the user and tell them some information about the system
print("Welcome to ProteinPass! We use proteins to generate secure passwords")
print("Note: It is recommended that you memorize your GI Number, so if you ever forget to put the password in a password manager, you are able to come back, enter the GI Num, and get the password again.")
print("This is STILL UNDER DEVELOPMENT! If there are any losses of accounts we are not liable.")
print("Also! this could throw an error when generating a RANDOM protein, if this happens, just rerun the program.")
print("The proteins could be pretty short, or long. So if you dont like the one that is given for you, just rerun the program")
# Print a break, so it looks more clean
print("-------------------------------")

isGIrand = input("Do you want a random GI Number for your protein? (y/n) ")

if isGIrand == "n":
	# Get input from the user about which GI Number they want, save to idNum as int
	idNum = int(input("What GI Number do you want to use to generate a password? (Integer) "))

	# Get Sequence and format to get rid of the title, then print to user
	sequence = format_sequence(get_fasta_sequence(idNum))
	print("Your sequence before generating the password is: ", sequence)

	# Generate Password
	sequence = add_symbols(sequence)
	sequence = add_numbers(sequence)
	sequence = add_lowercase(sequence)

	# Give the user their final password
	print("Your Final Password is: ")
	print(sequence)
elif isGIrand == "y":
	# Get Random GI Number & Print it for the user to refer back to if needed
	idNum = get_rand_GI()
	print("Your random GI Number is: ", idNum)

	# Get Sequence and format to get rid of the title, then print to user
	sequence = format_sequence(get_fasta_sequence(idNum))
	print("Your sequence before generating the password is: ", sequence)

	# Generate Password
	sequence = add_symbols(sequence)
	sequence = add_numbers(sequence)
	sequence = add_lowercase(sequence)

	# GI ve the user their final password
	print("Your Final Password is: ")
	print(sequence)