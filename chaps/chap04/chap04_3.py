## parsing SwissProt sequences from the net
from Bio import SeqIO
from Bio import ExPASy

#with ExPASy.get_sprot_raw("023729") as handle:
#    seq_record = SeqIO.read(handle, "swiss")
#    
#    handle.close()

handle = ExPASy.get_sprot_raw("023729")
seq_record = SeqIO.read(handle, "swiss")
handle.close()

print("ID: ", seq_record.id)
print("Name: ", seq_record.name)
print("Description: ", seq_record.description)
print("Sequence: ", repr(seq_record.seq))
print("Keywords: ", seq_record.annotations["keywords"])