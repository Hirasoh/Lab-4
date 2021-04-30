# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations
import random
### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        comp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        dic={}
        empty=''
        vowels='aeiou'
        capital='AEIOU'
        ind=0
        inj=0
        CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        perms=vowels_permutation 
        for item in comp:
            if item in CONSONANTS_LOWER :
                dic[item]=item
            elif  item in capital:
                ind=capital.index(item)
                empty=perms[ind]
                empty=empty.upper()
                dic[item]=empty
            elif item in vowels:
                inj=vowels.index(item)
                dic[item]=perms[inj]
        return dic
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionar
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        st3=''
        for item in self.message_text:
           if item in transpose_dict:
                st3+=transpose_dict[item]
           else:
               st3+=item
        return st3
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        empty_dic={}
        decode=' '
        perm=get_permutations('aeiou')
        get=''
        word=[]
        mm=''
        counting=0
        get_max=0
        for item in perm:
            get=self.build_transpose_dict(item)
            decode=self.apply_transpose(get)
            mm=decode.split()
            word.clear()
            for item in mm:
                word.append(is_word(self.valid_words, item))
                counting=word.count(True)
                empty_dic[counting]=decode
        if max(empty_dic)==0:
            return self.message_text
        else:
            get_max=max(empty_dic)
            return (empty_dic[get_max])
    
            
            
    

if __name__ == '__main__':

   ## Example test case
    message=SubMessage('Hairy Chest')
    permutation = 'iauoe'
    outcome=message.build_transpose_dict(permutation)
    print("Expected encryption:", "Hiury Chast!")
    print("Actual encryption:", message.apply_transpose(outcome))
    out = EncryptedSubMessage(message.apply_transpose(outcome))
    print("Decrypted message:", out.decrypt_message())
    
    ## Example test case
    message=SubMessage('Hello World!')
    permutation = 'eaiuo'
    outcome=message.build_transpose_dict(permutation)
    print("Expected encryption:", "Hallu Wurld")
    print("Actual encryption:", message.apply_transpose(outcome))
    out = EncryptedSubMessage(message.apply_transpose(outcome))
    print("Decrypted message:", out.decrypt_message())
    ## Exapmle test case
    message=SubMessage('Hira')
    permutation = 'iauoe'
    outcome=message.build_transpose_dict(permutation)
    print("Expected encryption:", "Huri")
    print("Actual encryption:", message.apply_transpose(outcome))
    out = EncryptedSubMessage(message.apply_transpose(outcome))
    print("Decrypted message:", out.decrypt_message())
    ## Example test case
    message=SubMessage('Nice')
    permutation = 'eaiou'
    outcome=message.build_transpose_dict(permutation)
    print("Expected encryption:", "Nica")
    print("Actual encryption:", message.apply_transpose(outcome))
    out = EncryptedSubMessage(message.apply_transpose(outcome))
    print("Decrypted message:", out.decrypt_message())
    
    