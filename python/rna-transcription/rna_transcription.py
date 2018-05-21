def to_rna(dna_strand):
    temp = ''
    dna_rna_dict = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
    for base in dna_strand:
        temp += dna_rna_dict[base]
    return temp
        

