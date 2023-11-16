import math
class GrammarStats:
    def __init__(self):
        self.checked = 0

  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text[0].isupper() and text[-1] == ".":
            return True
        else:
            self.checked = self.checked + 1
            return False


    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        percentage = 100
        if self.checked == 0:
            print(percentage)
            return percentage
        if self.checked > 0:
            false_detected = self.checked/(self.checked + 1)
            percentage_detected = false_detected * 100
            print(self.checked)
            print(self.checked + 1)
            print(percentage_detected)
            return math.ceil(percentage_detected)
        


grammar = GrammarStats()
grammar.check("This is a string.")
grammar.percentage_good()