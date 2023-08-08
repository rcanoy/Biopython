from Bio.Seq import Seq, MutableSeq, transcribe, translate
#from Bio.Alphabet import IUPAC
from Bio.SeqUtils import gc_fraction

# Defining the template DNA
my_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
for index, letter in enumerate(my_seq):
    print(index, letter)

print("\n")
print(my_seq)
print("\n")
print("Percent GC:", gc_fraction(my_seq)*100)

# Transcribing the template DNA
messenger_rna = transcribe(my_seq)
print("\n")
print(messenger_rna)

# Translating the template DNA
protein = translate(messenger_rna)
print('\n')
print(protein)
print("\n")
print(translate(my_seq))

# Convert a seq into a mutable sequence
mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print("\n")
print(mutable_seq)

mutable_seq[6] = "T"
print("\n")
print(mutable_seq)