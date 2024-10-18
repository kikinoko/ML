from collections import Counter

def count_word(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().split()
        
   
    word_counts = Counter(words)

    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_words:
        print(word, count)


filename = 'sample.txt'
count_word(filename)
