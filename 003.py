# -*- coding: utf-8 -*-


from Bio import SeqIo

sequences = [] #Setup an empty list

for seq_record in SeqIo.parse("ls_orchid.fasta.txt","fasta"):
    # Add this record to our list
    sequences.append(str(seq_record.seq))
    # print sequence
    print(seq_record.seq)
    # print sequence identifier
    print(seq_record.id)
    # print length of the sequence
    print(len(seq_record))




