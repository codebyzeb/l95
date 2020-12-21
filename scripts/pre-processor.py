# Script to pre-process sentences copied from a pdf into a plaintext file
# Filters page numbers, strips newlines and deals with EOL dashes
# Outputs each sentence on a single line in an individual file

import sys, re

in_file = open("raw-sentences.txt", 'r')

sentence_count = 0
next_start = "(1) "
out_file = None

current_sentence = ""

for line in in_file:

    # Filter out page numbers
    if len(line) <= 2:
        continue
    
    # Find new sentences by matching to the pattern "(d)"
    if line[:len(next_start)] == next_start:
        
        # Write out old sentence
        if out_file != None:
            out_file.write(current_sentence)
            out_file.close()

        # Start new sentence
        current_sentence = ""
        sentence_count += 1
        out_file = open("pre-processed/sentence-{0}.txt".format(str(sentence_count)), 'w')
        line = line[len(next_start):]
        next_start = "({0}) ".format(str(sentence_count+1))

    # Strip newlines
    line = line[:-1]

    # Deal with EOL dashes
    if line[-1] == "-":
        line = line[:-1]
    else:
        line = line + " "

    # Add line to the sentence
    current_sentence += line

if out_file != None:
    out_file.write(current_sentence)
    out_file.close()
