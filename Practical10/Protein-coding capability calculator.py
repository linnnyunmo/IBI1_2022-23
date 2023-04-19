# Create a function that determines whether a given DNA sequence is likely to be protein-coding or not
def is_protein_coding(dna_seq):
    # The start codon is ATG
    start_codon = 'ATG'
    # The stop codon is TGA
    stop_codon = 'TGA'
    coding_count = 0
    # The total count is DNA sequence
    total_count = len(dna_seq)
    # The start of sequence is start codon
    start = dna_seq.index(start_codon)
    # The stop of sequence is stop codon
    stop = dna_seq.index(stop_codon)
    # The length between the start codon and stop codon
    coding_length = stop - start
    # print the coding percentage
    coding_percentage = coding_length / total_count
    # There are three possible scenarios
    if coding_percentage > 0.5:
        return coding_percentage, 'protein-coding'
    elif coding_percentage < 0.1:
        return coding_percentage, 'non-coding'
    else:
        return coding_percentage, 'unclear'

# For example
dna_sequence ="ATGATTGTAATGTGA"
result = is_protein_coding(dna_sequence)
# Return the percentage of this sequence which is coding and whether the sequence should be
print(f'The DNA sequence is {result[0]*100:.2f}% " of the sequence in the start and stop codons as {result[1]}."')
