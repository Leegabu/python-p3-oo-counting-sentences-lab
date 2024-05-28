#!/usr/bin/env python3

class MyString:
    def __init__(self,value=''):
      self.value = value

    def get_value(self):
      return self.get_value
    
    def set_value(self, value):
      if isinstance(value,str):
        self._value = value
      else:
        print("The value must be a string.")

    value = property(get_value, set_value)
  
    def is_sentence(self):
      if self._value.endswith('.'):
        return True
      else:
        return False
    
    def is_question(self):
      if self._value.endswith('?'):
        return True
      else:
        return False

    def is_exclamation(self):
      if self._value.endswith('!'):
        return True
      else:
        return False

    number = property(is_exclamation,is_question,is_sentence)

    def count_sentences(self):
        parts = self._value.split('.') + self._value.split('?') + self._value.split('!')
        count = 0
        for part in parts:
          if part and part.strip():
            count += 1
        return count
    count = property(count_sentences)