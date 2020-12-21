# Generates a latex table from the MaltEval results for each parser

import sys

neural = open("eval_neural.txt", 'r').readlines()
unlex = open("eval_unlex.txt", 'r').readlines()
sr = open("eval_sr.txt", 'r').readlines()

def get_vals(line):
    vals = line.split(' ')
    vals = [v for v in vals if v != ' ' and v != '']
    if len(vals) < 4:
        return ""
    f1 = '-'
    if (vals[0] != '-' and vals[1] != '-'):
        if (float(vals[0])+float(vals[1]) == 0):
            f1 = '0'
        else:
            f1 = (2 * float(vals[0]) * float(vals[1]))/(float(vals[0]) + float(vals[1]))
    vals = vals[:2] + [f1]

    return " & ".join([str(round(float(v)*100, 1)) if v != '-' else '-' for v in vals])

for i in range(len(neural)):
    dep = neural[i].split(' ')[-1][:-1]
    print(dep, '&', get_vals(neural[i]), '&', get_vals(unlex[i]), '&', get_vals(sr[i]), '\\\\')

