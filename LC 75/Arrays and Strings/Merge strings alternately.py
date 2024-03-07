
def mergeAlternately( word1: str, word2: str) -> str:
    merged_word = ''
    counter = 0
    length_of_word1 = len(word1)
    length_of_word2 = len(word2)
    great_length = length_of_word1 if length_of_word1 >= length_of_word2 else length_of_word2
    for i in range(great_length):
        if counter < length_of_word1: merged_word += word1[i]        
        if counter < length_of_word2: merged_word += word2[i]        
        counter += 1
    return merged_word
    
word1 = 'ab'
word2 = 'pqrs'
print(mergeAlternately(word1, word2))