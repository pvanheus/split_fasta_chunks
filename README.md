#### split_fasta_chunks

This tool splits a FASTA file into a number of chunks and tries to assign an
equal number of sequences to each chunk. It does not check the size of
the sequences so if the input file includes files of very different
sizes then the output chunks could differ greatly in size.

It it designed to be used within Galaxy and, since Galaxy operates across
a data collection in parallel, can help parallelize workflows.