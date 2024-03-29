import argparse
import os

def find_max_genetic_palindrome(my_string, l):
    max_start = 0
    max_end = l
    max_palindrome = "There is no palindromal sequence"
    max_pal_length = 0
    start_center = 0
    max_coord1 = 1
    center = ""

    while start_center <= len(my_string) - l:
        start = start_center
        end = start_center + l - 1
        pal_length = 0
        coord1 = 1
        compl = True

        while (start + 1 - coord1 >= 0) and (end + 1 + coord1 < len(my_string)) and compl:
            if ((my_string[start - coord1] == "G" and my_string[end + coord1] == "C")
                or (my_string[start - coord1] == "C" and my_string[end + coord1] == "G")
                or (my_string[start - coord1] == "A" and my_string[end + coord1] == "T")
                or (my_string[start - coord1] == "T" and my_string[end + coord1] == "A")):
                pal_length += 1
                coord1 += 1

                if pal_length > max_pal_length:
                    max_start = start
                    max_end = end
                    max_pal_length = pal_length + 1
                    max_coord1 = coord1
                    center = my_string[max_start - 1:max_end + 1]

                    max_palindrome = my_string[max_start - max_coord1 + 1:max_end + max_coord1]
            else:
                compl = False
        start_center += 1

    return max_palindrome, max_pal_length, center


def main():
    parser = argparse.ArgumentParser(description='Find the largest genetic palindrome in a DNA sequence.')
    parser.add_argument('--input', required=True, help='Path to the input FASTA file.')
    parser.add_argument('--center', type=int, required=True, help='Length of the center for palindrome detection.')
    args = parser.parse_args()
    
    input_file = args.input

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    with open(input_file, "r", encoding="utf-8") as file:
        my_string = file.read()
    l = args.center

    max_palindrome, max_pal_length, center = find_max_genetic_palindrome(my_string, l)

    print("RESULTS:\n", max_palindrome)
    print("Length of the maximal palindromic sequence with center=", center, "with a length of", l)
    print("The maximum palindromal sequence is:", max_palindrome)
    print("The length of the maximal palindromic sequence is", max_pal_length)

if __name__ == "__main__":
    main()
