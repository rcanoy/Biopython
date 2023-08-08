from Bio import SeqIO
from Bio import Entrez
Entrez.email = 'recanoy@alum.up.edu.ph'


## parsing genbank records from net
#handle = Entrez.efetch(db='protein', rettype="genbank", id="6273291")
#seq_record = SeqIO.read(handle, "genbank")
#handle.close()

#print("%s with %i features" % (seq_record.id, len(seq_record.features)))

## parsing fasta records from net
#handle = Entrez.efetch(db='protein', rettype="fasta", id="6273291")
#seq_record = SeqIO.read(handle, "fasta")
#handle.close()
#print("%s with %i features" % (seq_record.id, len(seq_record.features)))


## parsing multiple genbank records
handle = Entrez.efetch(db="protein", rettype="genbank", \
    id="6273291, 6273290, 6273289")
for seq_record in SeqIO.parse(handle, "genbank"):
    print(seq_record.id, seq_record.description[:50] + "...")
    print("Sequence length %i" % len(seq_record))
    print("%i features," % len(seq_record.features)),
    print("from %s" % seq_record.annotations["source"])
handle.close()