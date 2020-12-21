#!/bin/bash
# Parse all sentences using a Stanford Parser
# Example usage:
# 	~ scripts/parse_all.sh neural conllu

PARSER=$1
EXTENSION=${2:-"txt"}
FORMAT=${2:-"text"}

parsers/stanford-corenlp-4.2.0/corenlp.sh -file data/pre-processed \
-props "parsers/$1.properties" -outputDirectory data/parses -outputFormat "$FORMAT" \
-outputExtension ".out"

for i in {1..26}
do
mv "data/parses/sentence-$i.txt.out" "data/parses-$FORMAT/$PARSER/sentence-$i.$EXTENSION"
done
exit 0
