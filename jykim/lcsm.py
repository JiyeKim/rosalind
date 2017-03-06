"""
Problem

A common substring of a collection of strings is a substring of every member of the collection.
We say that a common substring is a longest common substring if there does not exist a longer common substring.

For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA",
but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique;
for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k<=100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset

>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA


Sample Output

AC
"""
from Bio import SeqIO

def split_kmer(seq, k):
    return [seq[start:start+k] for start in range(len(seq)) if len(seq[start:start+k]) == k]

def compare_kmers(motifs, kmers):
    matchs = list()
    for motif in motifs:
        if motif in kmers:
            matchs.append(motif)
    return matchs

def get_matched_kmers(infile, k, longest_kmers=None):
    handle = SeqIO.parse(infile, "fasta")
    seed = next(handle)
    if longest_kmers:
        kmerset = [kmer for kmer in split_kmer(str(seed.seq), k) if kmer[:k-1] in longest_kmers]
    else:
        kmerset = split_kmer(str(seed.seq), k)
        
    for seq in handle:
        kmerset = compare_kmers(split_kmer(str(seq.seq), k), kmerset)
    return kmerset

def run_from_small_kmer():
    infile = "lcsm.fasta"
    k = 2
    longest_kmers = list()
    longest_k = None
    while True:
        print("k = {} is processing...".format(k))
        matched_kmers = get_matched_kmers(infile, k, longest_kmers)

        if not matched_kmers:
            break
        else:
            longest_k = k
            longest_kmers = matched_kmers 
            k += 1
    print(longest_kmers)
    
def run_from_large_kmer():
    infile = "lcsm.fasta"
    k = len(next(SeqIO.parse(infile, "fasta")).seq)
    longest_kmers = list()
    longest_k = None
    while True:
        print("k = {} is processing...".format(k))
        matched_kmers = get_matched_kmers(infile, k)

        if not matched_kmers:
            k -= 1
        else:
            longest_kmers = matched_kmers
            break
    print(longest_kmers)

if __name__ == '__main__':
    
    import time
    '''
    start_time = time.time()
    run_from_small_kmer()
    print("--- %s seconds ---" % (time.time() - start_time))
    '''
    start_time = time.time()
    run_from_large_kmer()
    print("--- %s seconds ---" % (time.time() - start_time))


        

    
