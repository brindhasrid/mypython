class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # code here 
       words=s.split()
       reversed_words=words[::-1]
       return " ".join(reversed_words)
