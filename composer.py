from generatedict import generate_dict
import random, sys

# Import the data
def read_lyrics(file_path):
    '''
        Read text file with the dictionary
        :params str file_path: The location for the lyrics text file e.g: songs/lyrics.txt        
    '''

    data = ''
    with open(file_path, 'r') as line:
        data += line.read()

    return data


# Genearte the lyrics
def generate_lyrics(ly_dict, count=50, first_word=''):

    '''
        Generate the lyrics
        :params str ly_dict: The location for the lyrics dictionary file e.g: songs/dict.txt        
        :params int count: The maximum number of words to be generated
        :params str first_word: The starter key-word for the lyrics
    '''

    senetence = ''

    # Randomly select the first word from the dictionary
    if first_word == '':
        first_word = random.choice(list(ly_dict.keys()))

    # Generate the next word
    for _ in range(count - 1):
        second_word = random.choice(ly_dict[first_word])
        first_word = second_word
        senetence += ' ' + second_word

    # End it with period 


    return senetence


def main():
    # Usage python composer.py ['path to lyrics text file'] e.g python composer.py songs/queen/sample.txt
    args = sys.argv

    if len(args) != 2:
        print(f'Usage: {args[0]} [path to text file], e.g python composer.py songs/queen/sample.txt ')
        quit()
    else:
        
        ts_lyrics = generate_dict.generate_dict(args[1])
        full_lyrics = generate_lyrics(ly_dict=ts_lyrics, count=200, first_word="I'm")

        print(full_lyrics)

        # return full_lyrics

# Test code
if __name__ == '__main__':
    main()
