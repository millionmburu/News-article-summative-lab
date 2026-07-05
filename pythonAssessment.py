import string
from collections import Counter
import re 

try:
    with open("article.txt", "r") as article_file:
        # function to find the amount of times a specified word appears 

        article_text = article_file.read()

        def count_specific_word(text: str, specified_word: str) -> int:
            text_lower = text.lower() # turns text to lowercase
            specified_word_lower = specified_word.lower() #turns the search_word to lowercase

            perfect_text = text_lower.translate(str.maketrans("","", string.punctuation)) # removes the punctuation 

            word_list = perfect_text.split() #splits the text to individual words 

            word_count = word_list.count(specified_word_lower) # counts the amount of times a specified word appears

            if not word_list:
                return 0

            return word_count
    

        # function to identify the most common word in the article
    
        def identify_most_common_word(text: str) -> str:
            # repeats the lowercase, removal punctuation and split cycle
            text_lower = text.lower()

            perfect_text = text_lower.translate(str.maketrans("","",string.punctuation))

            word_list = perfect_text.split()

            if not word_list:
                return ("None") # Incase of an empty string 
        
            words_count = Counter(word_list) #Uses counter to tally up every word in the article

            most_common_word = words_count.most_common(1)[0][0] #Identifies the most common word in the article
        
            return most_common_word
    

        # function to calculate the average word length

        def calculate_average_word_length(text: str) ->float:
            # repeats the lowercase, removal punctuation and split cycle
            text_lower = text.lower()

            perfect_text = text_lower.translate(str.maketrans("","",string.punctuation))

            word_list = perfect_text.split()

            if not word_list: # Incase of an empty string 
                return 0

            total_words = len(word_list) #Gets the total words in the article

            #sets character value to 0 and loops through words in the article adding the length of each word to total_chars
            total_chars = 0
            i = 0
            
            while i < total_words:
                word = word_list[i]
                total_chars += len(word)
                i += 1

                average_word_length = total_chars/total_words

            return average_word_length
    

        # function to count the number of paragraphs

        def count_paragraphs(text: str) -> int:

            if not text.strip(): #Incase of an empty string
                return 1

            raw_gaps = text.split("\n\n") #splits the text where there is a blank space

            valid_paragraphs = []

            # to remove any accidental gaps in the text
            for gap in raw_gaps:
                #removes whitespace characters using .strip
                if gap.strip():
                    valid_paragraphs.append(gap) 
            
            return len(valid_paragraphs) # counts the number of valid paragraphs
    

        # function to count number of sentences

        def count_sentences(text: str) -> int:

            if not text.strip(): # Incase of an empty string
                return 1
        
            raw_sentences = re.split(r'[\.!?]', text) #splits whenever it detects a regular expression pattern(exclamation marks etc)

            valid_sentences = []

            #filter out invalid sentences
            for sentence in raw_sentences:
                if sentence.strip():
                    valid_sentences.append(sentence)

            return len(valid_sentences)
        

        print(f"Total Sentences: {count_sentences(article_text)}")
        print(f"Total Paragraphs: {count_paragraphs(article_text)}")
        print(f"Most Common Word: {identify_most_common_word(article_text)}")
        print(f"Average Word Length: {calculate_average_word_length(article_text):.2f}")
        print(f"Occurrences of 'the': {count_specific_word(article_text, 'the')}")



# 3. Catch the missing file error at the very end
except FileNotFoundError:
    print("Error: 'article.txt' was not found. Please ensure it is in the same directory.")
        




    
    


        







