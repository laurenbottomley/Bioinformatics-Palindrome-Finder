import argparse

parser = argparse.ArgumentParser(description='Find the largest genetic palindrome in a DNA sequence.')
parser.add_argument('--input', required=True, help='Path to the input FASTA file.')
parser.add_argument('--center', type=int, required=True, help='Length of the center for palindrome detection.')

args = parser.parse_args()
