#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# deinterleave.py
# Usage: python3 deinterleave.py -i <fastq> -o <prefix>
# Description: Split a fastq file into pair1, pair 2 and single end reads. Each
# read must occupy 4 lines. Read description must end with /1 or /2.
# Dependencies: Python version 3.+ with Biopython.
# Warning: does not support file compression.

# Import modules and libraries
import argparse, re
from Bio import SeqIO

# Set arguments
parser=argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Path to input file in FastQ format", type = str, required = True)
parser.add_argument("-o", "--output", help = "Prefix for output files", type = str, required = False)
args=parser.parse_args()

# Define functions
def split():
	pair1  = {}
	pair2  = {}
	single = {}
	for rec in SeqIO.parse(args.input, "fastq"):
		des = str(rec.id)
		tag, r = re.compile("(.+)/([12])").findall(des)[0]
		if   r == "1":
			pair1[tag] = rec
		elif r == "2":
			pair2[tag] = rec
	return pair1, pair2

def pair(pair1, pair2):
	f1 = "{}.p1.fastq".format(args.output)
	f2 = "{}.p2.fastq".format(args.output)
	fe = "{}.se.fastq".format(args.output)
	all = []
	p1 = []
	p2 = []
	se = []
	for tag in pair1:
		all.append(tag)
	for tag in pair2:
		if not tag in all:
			all.append(tag)
	for tag in sorted(all):
		if tag in pair1 and tag in pair2:
			p1.append(pair1[tag])
			p2.append(pair2[tag])
		elif tag in pair1:
			se.append(pair1[tag])
			del pair1[tag]
		elif tag in pair2:
			se.append(pair2[tag])
			del pair2[tag]
	SeqIO.write(p1, f1, "fastq")
	SeqIO.write(p2, f2, "fastq")
	SeqIO.write(se, fe, "fastq")
	return

# Execute functions
pair1, pair2 = split()
pair(pair1, pair2)

# Quit
exit()
