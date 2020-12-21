# Script to produce tikz_dependency diagrams for my report

import sys

sentence_number = sys.argv[1]

# Start latex diagram
print("\\begin{figure}[H]")
print("\\centering")

for (parser, parser_name) in [("unlex", "Unlexicalised"), ("neural", "Neural"), ("sr", "Shift Reduce"), ("gold", "Gold")]:
    
    in_file = "data/parses-conllu/{}/sentence-{}.conllu".format(parser, sentence_number) if parser != "gold" else "data/gold/sentence-{}.conllu".format(sentence_number)
    words = {}
    sentence_length = 0
    dependencies= []
    root = 0

    for line in open(in_file, 'r'):
        components = line.split("\t")
        if len(components) < 8:
            continue

        edge = components[7]
        word = components[1]
        index = int(components[0])
        edge_index = int(components[6])

        if (index < 0):
            continue
        
        words[index-0] = word
        if edge_index == 0:
            root = index
        else:
            dependencies.append((edge, edge_index-0, index-0))

    sentence_length = len(words)

    print("\\begin{subfigure}[b]{0.9\\textwidth}")
    print("\t\\centering")
    print("\t\\begin{dependency}")
    print("\t\t\\begin{deptext}[column sep=0.2cm, row sep=.5ex]")

    # Print the list of words
    print("\t\t\t", end="")
    for i in range(1, sentence_length):
        print(words[i] + " \\& ", end="")
    print(words[sentence_length] + " \\\\")
    print("\t\t\\end{deptext}")

    # Print the root
    print("\t\t\\deproot[edge unit distance=1cm]{"+str(root)+"}{root}")

    # Print the dependencies
    for (edge, left_pos, right_pos) in dependencies:
        print("\t\t\t\\depedge{"+str(left_pos)+"}{"+str(right_pos)+"}{"+edge+"}")

    # Finish the subfigure
    print("\t\\end{dependency}")
    print("\t\\caption{" + parser_name + (" Parser.}" if parser != "gold" else " Standard.}"))
    print("\t\\label{figure:"+parser+sentence_number+"}")
    print("\\end{subfigure}")
    
print("\\caption{Parses and Gold Standard for Sentence " + sentence_number + ".}")
print("\\label{figure:sentence"+sentence_number+"}")
print("\\end{figure}")
