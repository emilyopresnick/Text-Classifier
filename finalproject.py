# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:43:31 2020

@author: opres
"""
import math
def clean_text(txt):
        '''takes in a string txt and returns a list containing all of the words
        in txt after it has been cleaned of periods commas question marks exclamation marks 
        colons and semicolons'''
        txt=txt.replace('.','')
        txt=txt.replace(',','')
        txt=txt.replace('?','')
        txt=txt.replace('!','')
        txt=txt.replace(':','')
        txt=txt.replace(';','')
        txt=txt.replace('"','')
        txt=txt.lower()
        txt=txt.split()
        
        return txt
    
def sample_file_write(filename):
    """A function that demonstrates how to write a
    Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.
       
       
def sample_file_read(filename):
    """A function that demonstrates how to read a
    Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)
    
def stem(s):
    '''takes in a string and returns the stem of the string'''
    length=len(s)
    if length>=6 and s[-3:]=='ing':
        if s[-4]==s[-5]:
            return stem(s[:-4])
        else:
            return stem(s[:-3])
    elif length>=7 and s[-4::]=='ness':
        if s[-5]==s[-6]:
            return stem(s[:5])
        else:
            return stem(s[:-4])
    elif length>=5 and s[-3::]=='ier':
        return stem(s[:-3]+'y')
    elif length>=4 and s[-2::]=='er':
        if s[-3]==s[-4]:
            return stem(s[:-3])
        else:
            return stem(s[:-2])
    elif length>=5 and s[-3::]=='ies':
        return s[:-3]+'y'
    elif length>=3 and s[-1::]=='s':
        if s[-2]==s[-3]:
            return stem(s[:-2])
        else:
            return stem(s[:-1])
    elif length>=5 and s[-3::]=='ful':
        if s[-4]==s[-5]:
            return stem(s[:-4])
        else:
            return stem(s[:-3])
    elif length>= 5 and s[-3::]=='ely':
        if s[-4]==s[-5]:
            return stem(s[:-3])
        else:
            return stem(s[:-2])    
    elif length>=5 and s[-3::]=='ion':
        if s[-4]==s[-5]:
            return stem(s[:-4])
        else:
            s=s[:-3]
    elif length>=6 and s[-4::]=='ment':
        if s[-5]==s[-6]:
            return stem(s[:5])
        else:
            return stem(s[:-4])
    else:
        return s
        
        
def compare_dictionaries(d1,d2):
    '''takes in two dictionaries and computes and returns their log similarity'''
    score=0
    total=0
    for n in d1:
        total+=d1[n]
    for w in d2:
        amt=d2[w]
        if w in d1:
            score+=(amt*math.log(d1[w]/total))
        else:
            score+=(amt*math.log(.5/total))
    return score



class TextModel:
    def __init__(self, model_name):
        '''constructs a TextModel object by accepting a 
        string called model_name and initializes a name, words, 
        and word length varibales'''
        self.name=model_name
        self.words={}
        self.word_lengths={}
        self.stems={}
        self.sentence_lengths={}
        self.punct_freq={}
        
    def __repr__(self):
        '''returns a string that includes the name of the model and the size of 
        the dictionaries'''
        s='text model name: '+ self.name+ '\n'
        s+='  number of words: '+ str(len(self.words))+'\n'
        s+='  number of word lengths: '+ str(len(self.word_lengths))+'\n'
        s+='  number of stems: '+str(len(self.stems))+'\n'
        s+='  number of sentence lengths: '+str(len(self.sentence_lengths))+'\n'
        s+='  number of different punctuation: '+str(len(self.punct_freq))
        return s
    
    def add_string(self,s):
        '''analyzes and adds a string of text to the dictionaries in the model'''
        end_elipse=False
        for t in s:
            if t in ['/','?',';',':','"',',','(',')','*','#','!']:
                if t not in self.punct_freq:
                    self.punct_freq[t]=1
                else:
                    self.punct_freq[t]+=1
        for i in range(1,len(s)-1):
            if s[i]=='-' and s[i+1]=='-':
                if '--' not in self.punct_freq:
                    self.punct_freq['--']=1
                else:
                    self.punct_freq['---']+=1
            elif s[i]=='-' and s[i+1]!='-' and s[i-1]!='-':
                if '-' not in self.punct_freq:
                   self.punct_freq['-']=1
                else:
                    self.punct_freq['-']+=1
        for j in range(len(s)-2):
            if s[j]=='.' and s[j+1]=='.' and s[j+2]=='.':
                if(j==len(s)-3):
                    end_elipse=True
                if '...' not in self.punct_freq:
                    self.punct_freq['...']=1
                else:
                    self.punct_freq['...']+=1
            if s[j]=='.' and s[j+1]!='.':
                if '.' not in self.punct_freq:
                    self.punct_freq['.']=1
                else:
                    self.punct_freq['.']+=1
        if not end_elipse and s[-1]=='.':
            if '.' not in self.punct_freq:
                self.punct_freq['.']=1
            else:
                self.punct_freq['.']+=1
        s1=s.replace('!', '.')
        s1=s1.replace('?', '.')
        sentences=s1.split('. ')
        for x in sentences:
            words=x.split()
            if len(words) not in self.sentence_lengths:
               self.sentence_lengths[len(words)]=1
            else:
                self.sentence_lengths[len(words)]+=1
        word_list=clean_text(s)
        for w in word_list:
            if stem(w) not in self.stems:
                self.stems[stem(w)]=1
            else:
                self.stems[stem(w)]+=1
            if w not in self.words:
                self.words[w]=1
            else:
                self.words[w]+=1
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)]=1
            else:
                self.word_lengths[len(w)]+=1
    
    def add_file(self,filename):
        '''adds all of the text that is in the file, filename, to the model'''
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        text=file.read()
        file.close()
        self.add_string(text)
    
    def save_model(self):
        '''saves the TextModel object by writing the dictionaries to 
        files'''
        filename_word=self.name + '_words'
        filename_wl=self.name+ '_word_lengths'
        filename_stems=self.name+ '_stems'
        filename_sl=self.name+ '_sentence_lengths'
        filename_pf=self.name+ '_punctuation_frequency'
        fw=open(filename_word,'w')
        fwl=open(filename_wl,'w')
        fs=open(filename_stems,'w')
        fsl=open(filename_sl,'w')
        fpf=open(filename_pf,'w')
        fw.write(str(self.words))
        fwl.write(str(self.word_lengths))
        fs.write(str(self.stems))
        fsl.write(str(self.sentence_lengths))
        fpf.write(str(self.punct_freq))
        fw.close()
        fwl.close()
        fs.close()
        fsl.close()
        fpf.close()
        
    def read_model(self):
        '''reads the stored dictionaries for the TextModel
        object from theit files'''
        filename_word=self.name + '_words'
        filename_wl=self.name+ '_word_lengths'
        filename_stems=self.name+ '_stems'
        filename_sl=self.name+ '_sentence_lengths'
        filename_pf=self.name+ '_punctuation_frequency'
        fw=open(filename_word,'r')
        fwl=open(filename_wl,'r')
        fs=open(filename_stems,'r')
        fsl=open(filename_sl,'r')
        fpf=open(filename_pf,'r')
        d_fw=fw.read()
        d_fwl=fwl.read()
        d_fs=fs.read()
        d_fsl=fsl.read()
        d_fpf=fpf.read()
        fw.close()
        fwl.close()
        fs.close()
        fsl.close()
        fpf.close()
        self.words=dict(eval(d_fw))
        self.word_lengths=dict(eval(d_fwl))
        self.stems=dict(eval(d_fs))
        self.sentence_lengths=dict(eval(d_fsl))
        self.punct_freq=dict(eval(d_fpf))
    
    def similarity_scores(self,other):
        '''computes and returns a list of the log similarlity scores for self and other '''
        word_score = compare_dictionaries(other.words, self.words)
        wl_score=compare_dictionaries(other.word_lengths, self.word_lengths)
        stem_score=compare_dictionaries(other.stems,self.stems)
        sl_score=compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        pf_score=compare_dictionaries(other.punct_freq, self.punct_freq)
        return [word_score,wl_score,stem_score,sl_score,pf_score]
    
    
    
    def classify(self,source1,source2):
        '''compares the called textmodel object to two other source textmodel objects and determines
        which of the two are more likely the source of the called TextModel'''
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for '+ source1.name + ' '+ str(scores1) )
        print('scores for '+ source2.name + ' ' +str(scores2) )
        c1=0
        c2=0
        for i in range(len(scores1)):
            if scores1[i]>scores2[i]:
                c1+=1
            else:
                c2+=1
        if c1>c2:
            print(self.name+ ' is more likely to have come from '+ source1.name)
        elif c2>c1:
            print(self.name+ ' is more likely to have come from '+ source2.name)
        else:
            print(self.name+ ' is from neither '+ source1.name + ' nor '+ source2.name)


def test():
    print("hi")
    """ tests the classify method """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)    

def run_tests():
    """runs tests for the source models chosen against 4 tests cases """
    print('Test 1 Anakin: \n')
    source1 = TextModel('Anakin')
    source1.add_file('Anakin.txt')

    source2 = TextModel('Obiwan')
    source2.add_file('ObiWan.txt')

    new1 = TextModel('anakin_test')
    new1.add_file('AnakinTest.txt')
    new1.classify(source1, source2)
    print('\nTest 2 ObiWan: \n')
    new2= TextModel('ObiWan')
    new2.add_file('ObiwanTest.txt')
    new2.classify(source1, source2)
    print('\nTest 3 Darth Vader: \n')
    new3= TextModel('Vader')
    new3.add_file('DarthVader.txt')
    new3.classify(source1, source2)
    print('\nTest 3 Admiral Ackbar: \n')
    new4=TextModel('Ackbar')
    new4.add_file('Ackbar.txt')
    new4.classify(source1, source2)      
        
    
                
        

    
    
        
    