
#Pasre a singe FASTA record from stdin and print it



import sys

class FASTAReader(object):
    def __init__(self, file):
        self.file= file
        self.last_ident= None
        
    def next(self):
        if self.last_ident is None:
            #get the header
            line= self.file.readline()
            assert line.startswith( ">" ), "Not valid fasta"
            ident = line[1:].rstrip( "\r\n" ) #removes something at end of string (>)
        else:
            ident= self.last_ident
             
            #get sequence
        sequences = []
        while True: #while loops as long as the condition is met 
            line= self.file.readline()
            if not line:
                break
            if line.startswith(">"):
                self.last_ident = line[1:].rstrip( "\r\n" ) 
                break
            else:
                sequences.append(line.strip()) #strip removes from both side (white space)
       
        if len(sequences)==0:
            raise StopIteration 
            
        
        sequence= "".join(sequences) #combines a list of strings with "" as a seperater

        return ident, sequence

    def __iter__(self):
        return self
        
        
        
        