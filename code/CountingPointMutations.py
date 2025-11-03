"""
Title: Counting Point Mutations
Link: https://rosalind.info/problems/hamm/

Problem:
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all 
decimal answers unless otherwise stated; please see the note on absolute error below.


Sample Dataset:


Sample Output

"""
if __name__ == "__main__":
    filename = "data/rosalind_gc.txt"
    gc_content_dict = {}
    current_sequence_id = None
    current_sequence_length = 0
    current_gc_count = 0

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                # New sequence record
                if current_sequence_id is not None and current_sequence_length > 0:
                    # Calculate and store GC content for the previous sequence
                    gc_content = (current_gc_count / current_sequence_length) * 100
                    gc_content_dict[current_sequence_id] = gc_content

                current_sequence_id = line[1:]  # Remove '>'
                current_sequence_length = 0
                current_gc_count = 0
            else:
                # Sequence line
                current_sequence_length += len(line)
                for char in line:
                    if char.upper() in ('G', 'C'):
                        current_gc_count += 1

        # Process the last sequence in the file
        if current_sequence_id is not None and current_sequence_length > 0:
            gc_content = (current_gc_count / current_sequence_length) * 100
            gc_content_dict[current_sequence_id] = gc_content
    largestGCcontent = max(gc_content_dict, key=gc_content_dict.get)
    print(largestGCcontent)
    print(gc_content_dict[largestGCcontent])