from Bio import SeqIO

class seq_parser(object):
    
    def __init__(self):
        self.file_type = ['fasta', 'genbank']
    
    def get_accession(record):
        """_summary_:
            Given a SeqRecord, return the accession number as a string.

        _args_:
            record (_type_): _description_
        """
        parts = record.id.split("|")
        assert len(parts) == 5 and parts[0] == 'gi' and parts[2] == 'emb'
        return parts[3]
        
    def extract(self, filename, file_type, get_accession=get_accession):
        with open(filename) as handle:
            if file_type == 'genbank':
                orchid_dict = SeqIO.to_dict(SeqIO.parse(handle, file_type))
            else:
                orchid_dict = SeqIO.to_dict(SeqIO.parse(handle, file_type), key_function=get_accession)
            handle.close()
        
        return orchid_dict

parser = seq_parser()

## genbank
fileName = "ls_orchid.gbk"
fileType = parser.file_type[1]

orchid_dict = parser.extract(fileName, fileType)
print(orchid_dict.keys())

first_record = orchid_dict['Z78533.1']
print("ID: ", first_record.id)
print("Description: ", first_record.description)
print("Organism: ", first_record.annotations["source"])
print("Sequence: ", repr(first_record.seq))

## FASTA
fileName = "ls_orchid.fasta"
fileType = parser.file_type[0]

orchid_dict = parser.extract(fileName, fileType)
print(orchid_dict.keys())
