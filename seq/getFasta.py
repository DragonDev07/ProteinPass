from Bio import Entrez

Entrez.email = 'teowelton@gmail.com'

def get_fasta_sequence(idNum):
	handle = Entrez.efetch(db='nuccore', id=idNum, rettype='fasta')
	return handle.read()