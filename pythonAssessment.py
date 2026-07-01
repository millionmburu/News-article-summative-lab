import string
from collections import Counter

with open("article.txt", "r") as article_file:
    # function to find the amount of times a specified word appears 

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

        total_words = len(word_list) #Gets the total words in the article

        #sets character value to 0 and loops through words in the article adding the length of each word to total_chars
        total_chars = 0
        for word in word_list:
            word_length = len(word)
            total_chars += word_length
        
        average_word_length = total_chars/total_words #calculates the average word length

        if not word_list: # Incase of an empty string 
            return 0

        return average_word_length
    

    
    


        







