#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
       return self._value
    
    @value.setter
    def value(self, the_value):
      if isinstance (the_value, str):
         self._value = the_value
      else: 
          value = 'The value must be a string.'
          print(value)

    def is_sentence(self):
       if self._value[-1] == '.':
          return True
       else: 
          return False
       
    def is_question(self):
        if self._value[-1] == '?':
          return True
        else: 
          return False
        
    def is_exclamation(self):
        if self._value[-1] == '!':
          return True
        else: 
          return False
        
    def count_sentences(self):
       all_sentences = self._value.replace('?', '.').replace('!', '.')

       sentences = all_sentences.split('.')
       
       sentences = [sentence for sentence in sentences if sentence.strip()]

       return len(sentences)