# L95 Parser Evaluation Project

This repository contains the report, scripts, parses and gold standards produced for my project for the L95 course of the Computer Science Part III course. 

## Report

The report can be found at `report.pdf`.

## Gold standards

The gold standards are under `data/gold/`, numbered by sentence.

## Parses

The raw sentences are in `data/raw-sentence.txt` with the pre-processed sentences in `data/pre-processed/`. The output of the parsers can be found in `data/parses-text/` and `data/parsers-conllu/` in text and CoNLL-U format respectively. 

## Scripts

All scripts can be found in `scripts/`. The `dep_to_latex.py` and `table_generator.py` scripts are utility scripts used to produce latex diagrams and tables for the report. The `macro_micro.py` script is used to calculate macroaverage and microaverage scores, given a file containing the output of the MaltEval script. The `pre-processor.py` script was used to produce the sentences in `data/pre-processed/` given the input `data/raw-sentences.txt`. 

The `parse_all.sh` script runs the Stanford parsers (not distributed here). The `parsers/` directory does include the three configuration files used for parsing. To run the script, install [Stanford CoreNLP](https://github.com/stanfordnlp/CoreNLP) in the `parsers/` directory and also download the Stanford [Shift Reduce parser models](https://nlp.stanford.edu/software/srparser.html) and place them in the CoreNLP folder. The parsing script can then be run:

  $ scripts/parse_all.sh neural conllu

This runs the Neural parser and outputs the sentences in CoNLL-U format.

## Evaluation

The `evaluation/` directory contains the gold standards and outputs of the parsers combined into single CoNLL-U files, `gold.conllu`, `neural.conllu`, `sr.conllu` and `unlex.conllu`. The `eval_both_right.xml` and `eval_label_right.xml` are configuration files for running MaltEval using the LabelRight and BothRight metrics, used to produce the results found in the `evaluation/both_right/` and `evaluation/label_right/` directories respectively. An example command to run MaltEval is:

  $ java -jar MaltEval.jar -e eval_label_right.xml -s neural.conllu sr.conllu unlex.conllu -g gold.conllu
  
This requires placing the MaltEval script in the `evaluation/` directory.
