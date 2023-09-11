# Bioinformatics-Palindrome-Finder

A python program that reads a FASTA file and returns the largest palindrome sequence within the DNA strand.
Note: The FASTA file in the project folder is the DNA sequence for E. Coli.
- Read more about the palindrome in E. Coli here --> https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4245961/

FOR THOSE UNFAMILAR WITH PALINDROMES IN GENETICS ---

- Brief explanation on nucletides: DNA strands are made up of nucleotide bases known as Adenine, Thiamine, Guanine, Cytosine, abbreviated as A, T, G, C. The double helix structure is comprised of these nucleotides in unique ways. These nucleotide bases are complement to one another (i.e., Adenine is compliment with Thiamine and Guinine is complement with Cytosine). It is important to understand each of these compliments are absolute, in other words, Adenine and Thiamine cannot be complemented with Cytosine and Guanine. None of these nucleotides can be complimented with themselves, either.
- Palindromes in genetics are not like normal palindromes (i.e., racecar is a normal palindrome and AGTACT is a genetic palindrome). Instead of each character on both sides being the same, the nucleotide's compliment must be present.
- Genetic palindromes can tell us a lot about a particular DNA sequence, such as recognition sites for enzymes, disease associations, structural stability, evolutionary significance, etc.

## Examples:

AGTACT -- Palindrome (each nucleotide has its compliment)
AACTGC -- Not a palindrome (compliments are not present)

# Installation
1. Before getting started, make sure you have the following prerequisites installed:
- Python 3.x: [Download Python](https://www.python.org/downloads/)

2. Install the genetic-palindrome-finder package using pip:
   ```bash
   pip install genetic-palindrome-finder

# Usage

To find genetic palindromes in a DNA sequence, you can use the `genetic_palindrome_finder` command followed by the necessary options. For example:
```bash
python palindromefinder.py --input ecoli.fasta --center 20
