from Bio import SeqIO

def custom_parser(filename, fileType):
    """_summary_

    _args_:
        filename (_type_): name of the file
        fileType (_type_): either "fasta" or "genbank"
    """
    
    
    with open(filename) as handle:
        for seq_record in SeqIO.parse(handle, fileType):
            print(seq_record.id)
            # print a representable string of an object
            print(repr(seq_record.seq))
            print(len(seq_record))
        handle.close()
