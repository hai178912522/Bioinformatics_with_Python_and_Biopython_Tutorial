# -*- coding: utf-8 -*-



"""Finding a Motif in DNA
Motif:
• interval of nucleotides (in nucleic acids) or of amino acids (in proteins) that has biological importance
• common task in molecular biology: search an organism's genome for a known motif
• represented by a substring of a genetic string that we wish to locate
• of possible interests are repeats - an interval of DNA in the genome that occurs often, possibly with minor changes
• these repeats occur far more often than would be dictated by random chance, indicating that genomes are anything but random
• most common repeat in humans: Alu repeat, 300 bp long and recurs around a million times throughout every human genome
• parasitic purpose: when a new Alu repeat is inserted into a genome, it frequently causes genetic disorders"""

#Define s and t
s = "GATATATGCATATACTT"
t = "ATAT"

for position in range(len(s)):
    if s[position:].startswith(t):
        print(position+1)