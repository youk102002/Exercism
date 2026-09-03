def to_rna(dna_strand):
    dna_sequence = "GCTA"
    rna_sequence = "CGAU"
    table = str.maketrans(dna_sequence, rna_sequence)
    return dna_strand.translate(table)
