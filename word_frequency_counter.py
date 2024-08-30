
def word_frequency_counter(text):
    # Split the text into words
    words = text.split()
    
    # Create an empty dictionary to store the word frequency
    word_count = {}
    
    # Iterate through each word in the list
    for word in words:
        # Convert the word to lowercase to make the counting case-insensitive
        word = word.lower()
        
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            word_count[word] = 1
    
    # Return the word count dictionary
    return word_count

def main():
    text = input("Enter a text: ")
    word_count = word_frequency_counter(text)
    print("Word Frequency: ")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
