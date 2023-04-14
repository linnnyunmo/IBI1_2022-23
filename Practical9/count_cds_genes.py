# You can choose a stop codon here
stop_codon = input("Enter stop codon (TAA, TAG or TGA): ")
# Setting the input_file and output_file
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = f"{stop_codon}_stop_genes.fa"
# Create the output file name based on the stop codon
# Open the input file and output file,then collect data
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    # simplify the name of gene and sequence, and Initialization value
    gene_count=0
    gene_name = ""
    gene_seq = ""
    # loop through each line in input file
    for line in f_in.readlines():
        # if line start with >, it is the start line
        if line.startswith(">"):
            # if the sequence ends with the stop_codons you chose
            if gene_seq.endswith("stop_codons"):
                # write sequences to the output_file
                f_out.write(">{}\n{}\n".format(gene_name.split()[0], gene_seq))
            # reset gene name and sequence
            gene_name = line
            gene_seq = ""
        else:
            # Append sequence to gene sequence
            gene_seq += line.strip()
    # if the sequence ends with the stop_codons you chose
    if gene_seq.endswith("stop_codons"):
        f_out.write(">{}\n{}\n".format(gene_name.split()[0], gene_seq))
        # And then the count is calculated
        gene_count +=1
# print the number of genes with stop_codons, gene_count
print("Number of genes with stop_codons", stop_codon, ":" "gene_count" )
