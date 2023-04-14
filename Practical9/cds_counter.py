# This is a given sequence
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# Find the index of start codon
start_codons = 'ATG'
# Find the index of stop codons
stop_codons = ['TAA', 'TAG', 'TGA']
# count from zero
count = 0
# setting the start codon and begin finding
for i in range(len(seq)-2):
    if seq[i:i+3] == start_codons:
        # Loop search from start codon ATG to the stop_codon
        for j in range(i+3, len(seq)-2, 3):
            # Find and output
            if seq[j:j+3] in stop_codons:
                # count and break it
                count += 1
                break
# Count the total number of possible coding sequences formed by this sequence.
print("Total number of coding sequences: ", count)
