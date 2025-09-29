def count_words(filepath, words_list):
    """ Count the total number of times these words appear.
    
    Args:
      filepath (str): location of input file
      
      words_list (list str): list of words to include as part of the count
    
    Returns:
      int: total count of words found in words_list
    """
    # Open the text file
    with open(filepath) as file:
        text = file.read()

    n = 0
    for word in text.split():
        # Count the number of times the words in the list appear
        if word.lower() in words_list:
            n += 1
            
    return n