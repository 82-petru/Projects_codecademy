# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:44:40 2019

@author: uidr1019
"""
sample = ['GTA','GGG','CAC'] #three codons retrieved from the computers keyboard . Have to be matched with suspect's DNA.
def read_dna(dna_file):
  dna_data = ""#variable will contain the suspect DNA 
  with open(dna_file, "r") as f: #open the file and also close it 
    for item in f:
      dna_data += item
  return dna_data#return data same indent as with block 

def dna_codons(dna):#method take the string and create list of codons from that string and return the list 
  codons = []#empty list to add the codons 
  for i in range(0, len(dna), 3):#codons are 3-letter-long units of genetic code. This loop is for creating codons
    if (i + 3) < len(dna):#the line code will make sure that you do not add a string to the codon list that isn't at least 3 letters long
      codons.append(dna[i:i + 3])# this code line is to add the first three characters only, using slicing method 
  return codons 
#Perfect - you just added a method that will iterate through a string, slice it into smaller strings that are 3 letters long, and add them to a list. This functionality will help us match the sample to a suspect’s DNA later
def match_dna(dna):#method to ierate through both the samples and suspects DNA, compare the samples containment with suspect's DNA 
  matches = 0#we will need a way to count the number of times codon from samples matches with suspects DNA's
  for codon in dna:
    if codon in sample:#this code line is to check if codons are in sample list 
      matches += 1#counter how many times are "increment matches by 1 using += operator "
  return matches

def is_criminal(dna_sample):#method used to to determine if a suspect is the criminal by using other methods we've created 
  dna_data = read_dna(dna_sample)#variable created to use called result of function read_dna() and parameter dna_samples
  codons = dna_codons(dna_data)##variable created to use called result of function dna_codons() with dna_data as argument 
  num_matches = match_dna(codons)#variable created to use called result of function matches_dna() with codons argument 
  if num_matches >= 3:
    print("%s matches found. Keep doing investigation for this fella." % num_matches)
  else:
    print("%s matches found. Free suspect." % num_matches)
is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')

      