#Created by Manav Patni
#Program to get the number of charcters/words in a string

text = input("Enter any text over here:- ")
text_length = len(text)
text_count = input("Enter a word to count its occurrence in the above text:- ")
word_count = text.count(text_count)
print("The total length of the above text is", text_length, "including spaces and tabs",
      "\n", text_count, "came", word_count, "time(s) in the above text.")
