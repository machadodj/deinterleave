# Project's name
This is the README file for deinterleave.

# Short description
Split a fastq file into pair1, pair 2 and single end reads.

# Usage
python3 deinterleave.py -i FILENAME -o PREFIX

# Dependencies
Python version 3.+ with Biopython.

# Description
Split a fastq file into pair1, pair 2 and single end reads.

Each read must occupy 4 lines. Read description must end with /1 or /2.

## Warning
Does not support file compression.
