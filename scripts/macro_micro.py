# Script to calculate microaverage and macroaverage scores, given
# an output of the MaltEval script that contains the precision, recall scores
# and count for each dependency

import sys

eval_file = sys.argv[1]

# Sums stored as arrays since counts may differ for each score type
micro_sum = [0, 0, 0]
micro_prec = 0
micro_rec = 0
micro_f1 = 0

macro_sum = [0, 0, 0]
macro_prec = 0
macro_rec = 0
macro_f1 = 0

for line in open(eval_file, 'r'):
    vals = line.split(' ')
    vals = [v for v in vals if v != ' ' and v != '']
    if len(vals) < 3:
        continue

    num = float(vals[2])

    if (vals[0] != '-'):
        precision = float(vals[0])
        micro_prec += num * precision
        macro_prec += precision
        micro_sum[0] += num
        macro_sum[0] += 1

    if (vals[1] != '-'):
        recall = float(vals[1])
        micro_rec += num * recall
        macro_rec += recall
        micro_sum[1] += num
        macro_sum[1] += 1

    if (vals[0] != '-' and vals[1] != '-'):
        f1 = (2*precision*recall)/(precision+recall) if precision+recall > 0 else 0
        micro_f1 += num * f1
        macro_f1 += f1
        micro_sum[2] += num
        macro_sum[2] += 1

print("Micro P/R/F1:", micro_prec/micro_sum[0], '&', micro_rec/micro_sum[1], '&', micro_f1/micro_sum[2], '&')
print("Macro P/R/F1:", macro_prec/macro_sum[0], '&', macro_rec/macro_sum[1], '&', macro_f1/macro_sum[2],'&')

