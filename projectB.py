# -*- coding: utf-8 -*-
codons = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
          "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
          "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",
          "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",
          "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
          "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
          "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
          "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
          "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
          "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
          "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
          "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
          "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
          "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
          "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
          "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}
        
def main():
    sequence_files = ["cftr1.txt", "cftr2.txt", "cftr3.txt", "cftr4.txt", "cftr5.txt"]
    for file in sequence_files:
        if cftr(readFile(file)) == True:
                print( f'Sequence {sequence_files.index(file) + 1} codes for normal CFTR')
        else:
                print( f'Sequence {sequence_files.index(file) + 1} codes for abnormal CFTR')
    """
    Write your code here
    """
    
def readFile(fileName):
    """
    Reads a text file.
    
    Parameters
    ----------
    fileName : str
        File path to read.

    Returns
    -------
    str
        Text from file.
    """
    with open(fileName,'r') as dnaFile:
        dna = "".join(dnaFile.readlines()).strip()
    return dna
    
    
def writeFile(fileName,text):
    """
    Writes a text file.

    Parameters
    ----------
    fileName : str
        File path to write.
    text : str
        Text to write.

    Returns
    -------
    None.

    """
    with open(fileName,'w') as textFile:
        textFile.write(text)
    
def restrict(dna, seq):
    '''
    

    Parameters
    ----------
    dna : String
        This is the dna sequence
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    fragment_list : TYPE
        DESCRIPTION.

    '''
    fragment_list = []
    i = 0
    start = 0
    end = 0
    l = len(seq) // 2
    char = 0
    
    while char < len(dna) - 1:
        if i != 0 and i < len(seq) and dna[char] != seq[i]:
            i = 0
        elif dna[char] == seq[i] and i < len(seq) - 1:
            i += 1 
            end += 1
            char += 1
        elif i == len(seq) - 1 and seq[i] == dna[char]:
            i = 0
            end -= l
            fragment_list.append(dna[start:end + 1])
            start = end + 1
            end += 1
            char = start
        elif end + 1 == len(dna) - 1:
            fragment_list.append(dna[start:len(dna)])
            char += 1
        else:
            end += 1
            char += 1
    return fragment_list

def transcribe(dna):
    mRNA_seq = ''
    for i in dna:
        if i == 'T':
            mRNA_seq += 'U'
        else:
            mRNA_seq += i
    return mRNA_seq
    
def translate(mrna):
    translated_seq = []
    for i in range(0,len(mrna)-1,3):
        if mrna[i:i+3] in codons:
            translated_seq.append(codons[mrna[i:i+3]])
    return translated_seq

def aminoAcids(dna):
    mrna = transcribe(dna)
    aminoacid_list = translate(mrna)
    return set(aminoacid_list)
    
def isolate(dna, start, end):
    if start == end:
        return False
    if start not in dna:
        return False
    elif end not in dna:
        return False
    else:
        start_index = dna.find(start) + len(start)
        end_index = dna.find(end)
        return dna[start_index:end_index]

def cftr(dna):
    cftr_found = isolate(dna,'ATTAAAGAAAATATC', 'GGTGTTTCCTATGAT')
    if cftr_found == 'ATCTTT':
        return True
    elif cftr_found == 'ATT':
        return False
    else:
        return False

 
if __name__ == "__main__":
    main()
        
    
    
    
    
    
    
    
    