#!/usr/bin/env python

from Bio import SeqIO
import argparse
import sys

parser = argparse.ArgumentParser(description='Split a FASTA file into a number of chunks')
parser.add_argument('input_file', type=file, help='Input FASTA file')
parser.add_argument('output_prefix', help='Prefix of output files')
parser.add_argument('num_chunks', type=int, help='Number of chunks to split into')
args = parser.parse_args()

record_count = 0
for line in args.input_file:
    if line.lstrip().startswith('>'):
        record_count += 1

records_per_chunk = round(float(record_count) / args.num_chunks)

count = 1
args.input_file.seek(0)
output_filename = '%s%d.fasta' % (args.output_prefix, count)
chunk_record_count = 0 # how many lines have we written to the output file
records = []
for record in SeqIO.parse(args.input_file, 'fasta'):
    if count < args.num_chunks and chunk_record_count >= records_per_chunk:
        SeqIO.write(records, output_filename, 'fasta')
        records = []
        count += 1
        output_filename = '%s%d.fasta' % (args.output_prefix, count)
        chunk_record_count = 0
    records.append(record)
    chunk_record_count += 1

if records:
    SeqIO.write(records, output_filename, 'fasta')


