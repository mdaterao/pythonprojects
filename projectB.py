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
    """
    Reads all five sequences and prints if each codes for normal CFTR 

    Returns
    -------
    None.

    """
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
    """
    This function simulates the actions of a 
    restriction enzyme. It should accept a 5’ to 3’ dna 
    and a restriction sequence seq as strings. 
    It should then return the list of cut fragments.

    Parameters
    ----------
    dna : String
        function accepts a 5' to 3' dna string
    seq : String
        recognition sequence

    Returns
    -------
    fragment_list : list
        returns the list of cut fragments based on 
        recognition sequences.

    """
    fragment_list = []
    if len(seq) % 2 != 0:
        return fragment_list
    else:
        while seq in dna:
            seq_half_len = int(len(seq) / 2)
            fragment_index = dna.find(seq) + seq_half_len
            fragment = dna[0:fragment_index]
            dna = dna[fragment_index:]
            fragment_list.append(fragment)
        fragment_list.append(dna)
    return fragment_list

def transcribe(dna):
    """
    This function accepts a 5’ to 3’ 
    sequence as a string and 
    returns the mRNA sequence

    Parameters
    ----------
    dna : string
        5' to 3' dna sequence

    Returns
    -------
    mRNA_seq : string
        mRNA sequence

    """
    mRNA_seq = ''
    for i in dna:
        if i == 'T':
            mRNA_seq += 'U'
        else:
            mRNA_seq += i
    return mRNA_seq
    
def translate(mrna):
    """
    Accepts an mRNA string and then uses the provided codons 
    dictionary to return the list translated amino acids.

    Parameters
    ----------
    mrna : string
        mRNA string

    Returns
    -------
    translated_seq : list
        list of translated amino acids

    """
    translated_seq = []
    for i in range(0,len(mrna)-1,3):
        if mrna[i:i+3] in codons:
            translated_seq.append(codons[mrna[i:i+3]])
    return translated_seq

def aminoAcids(dna):
    """
    takes in a DNA se- quence and returns the
    set of amino acids that it encodes

    Parameters
    ----------
    dna : string
        dna sequence

    Returns
    -------
   set of amino acids that this
   dna sequence encodes

    """
    mrna = transcribe(dna)
    aminoacid_list = translate(mrna)
    return set(aminoacid_list)
    
def isolate(dna, start, end):
    """
    accepts a DNA string with start and end sequences,
    returns the DNA sequence between the first instance
    of the start sequence and the end sequence following it

    Parameters
    ----------
    dna : string
        dna sequence
    start : string
        start sequence
    end : string
        end sequence

    Returns
    -------
    returns string in between start and end sequences.
    returns boolean value if either the start or end
    sequences can not be found

    """
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
    """
    

    Parameters
    ----------
    dna : string
        dna sequence

    Returns
    -------
    bool
        eturn a boolean value of True if the 
        given DNA sequence codes for normal CFTR. 
        Otherwise it should return False

    """
    cftr_found = isolate(dna,'ATTAAAGAAAATATC', 'GGTGTTTCCTATGAT')
    if cftr_found == 'ATCTTT':
        return True
    elif cftr_found == 'ATT':
        return False
    else:
        return False

 
if __name__ == "__main__":
    main()
        
    
    
    
    
    
    
    
    