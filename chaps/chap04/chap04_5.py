from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid


with open("ls_orchid.gbk") as handle:
    seguid_dict = SeqIO.to_dict(SeqIO.parse(handle, "genbank"), lambda rec : seguid(rec.seq))
    handle.close()
 
keys_list = []   
with open("ls_orchid.gbk") as handle:
    for seq_record in SeqIO.parse(handle, "genbank"):
        keys_list.append(seguid(seq_record))
        print(seq_record.id, seguid(seq_record))
    
#record = seguid_dict[keys_list[0]]
record = seguid_dict["H+JfaShya/4yyAj7IbMqgNkxdxQ"]
print(record.id)
print(record.description)