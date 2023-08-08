from Bio import SeqIO

class seq_parse(object):
    
    def __init__(self):
        self.file_type = ["fasta", "genbank"]

    def extract(self, filename, file_type):
        with open(filename) as handle:
            records = list(SeqIO.parse(handle, file_type))
        handle.close()
        
        return records

seq_parser = seq_parse()


# FASTA file
filename_fasta = 'ls_orchid.fasta'
file_type_fasta = seq_parser.file_type[0]
records_fasta = seq_parser.extract(filename_fasta, file_type_fasta)
first_record = records_fasta[0]
print('\n')
print(dir(first_record))
print('\n')
print('ID: ', first_record.id)
print('Name: ', first_record.name)
print('Description: ', first_record.description)
print('Source: ', first_record.annotations)
print('Sequence: ', repr(first_record.seq))
print('Length: ', len(first_record))

## List of the species each orchid sequence is from
all_species = [seq_record.description.split()[1] for seq_record in records_fasta]
print('/n')
print(all_species)

## GENBANK file
filename_gbk = 'ls_orchid.gbk'
file_type_gbk = seq_parser.file_type[1]
records_gbk = seq_parser.extract(filename_gbk, file_type_gbk)
first_record = records_gbk[0]
print('\n')
print(dir(first_record))
print('\n')
print('ID: ', first_record.id)
print('Name: ', first_record.name)
print('Description: ', first_record.description)
print('Annotations: ', first_record.annotations)
print('Source: ', first_record.annotations["source"])
print('Sequence: ', repr(first_record.seq))
print('Length: ', len(first_record))


## List of the species each orchid sequence is from:
all_species = [seq_record.annotations["organism"] for seq_record in records_gbk]
print('\n')
print(all_species)
