# Setting the input_file and output_file
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "TGA_genes.fa"
# open the input_file
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    # simplify the name of gene and sequence
    gene_name = ""
    gene_seq = ""
    # loop through each line in input file
    for line in f_in.readlines():
        # if line start with >, it is the start line
        if line.startswith(">"):
            # check the sequence that ends with TGA
            if gene_seq.endswith("TGA"):
                # write sequences to the output_file
                f_out.write(">{}\n{}\n".format(gene_name.split()[0], gene_seq))
            # reset gene name and sequence
            gene_name = line
            gene_seq = ""
    else:
        # Append sequence to gene sequence
         gene_seq += line.strip()
          
