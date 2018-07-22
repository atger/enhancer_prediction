from itertools import product
from Bio import SeqIO
import sys
import pandas as pd

def generate_kmer(n):
    kmer = []
    for k in range(1,n+1):
        kmer.extend([''.join(i) for i in product('ATGC',repeat=k)])
    return kmer

def calculate_freq(s,kmer):
    freq = []
    for i in kmer:
        freq.append(s.count(i))
    return freq

sequence = []
for record in SeqIO.parse(sys.argv[1],"fasta"):
    sequence.append(record.seq.upper())

kmer = generate_kmer(6)
df = pd.DataFrame([calculate_freq(i,kmer) for i in sequence])
df.columns = kmer
df.to_csv("kmer_data.csv")
