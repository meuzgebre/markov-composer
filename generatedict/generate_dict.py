from collections import defaultdict
import os

def markov_chain(text):

    # Tokenize the text data in to smaller corpus with punctuation
    words = text.split(' ')

    # Initialize default dictionary
    ly_dict = defaultdict(list)

    # Create dictionary for words
    for current_word, next_word in zip(words[0:-1], words[1:]):

        ly_dict[current_word].append(next_word)

    # Convert the default dictionary back to dictionary
    ly_dict = dict(ly_dict)

    # Return the dictionary
    return ly_dict

def generate_dict(file_path, save_path='', save_file=False):

    '''
        Generate dictionary and save it to text file
        :params str file_path: The location for the lyrics file e.g: songs/lyrics.txt
        :params str save_path: The location to save the final dictionary e.g: dicts/
        :params bool save_file: (True) save the dictionary to text file
    '''

    data = ''

    with open(file_path, 'r') as line:
        data += line.read()

    data = markov_chain(data)

    if save_file == True:
        with open(os.path.join(save_path, '_dictionary.txt'), 'a') as file:
            file.write(str(data))

    return data


def generate_lyrics_from_dir(dir_path, save_dir='', one_file=False):
    '''
        Generate dictionary for all files in a directory and save them to text file
        :params str file_path: The location for the lyrics file e.g: songs/artist_name
        :params str save_path: The location to save the final dictionary e.g: dicts/
        :params bool one_file: (True) Generate only one text file for all text files: (False) Generate individual
        text files for all
    '''
    if one_file == True:
        # TODO Required implemenetaion
        pass
    else:
        data = ''
        all_files = os.listdir(dir_path)

        # get all files from dir
        for file in all_files:
            
            # Check file extension
            if os.path.splitext(file)[1] == '.txt':
                # data += str(generate_dict(os.path.join(dir_path, file), dir_path))                
                with open(os.path.join(dir_path, file), 'r') as line:
                    data += line.read()

        data = markov_chain(data)

        # print(f'Dictionary Succesfully generated! Check file "{dir_path}/_dictionary_list.txt"')
        
        return data


# if __name__ == '__main__':
#     # generate_dict('songs/taylor_swift/4__Look-What-You-Made-Me-Do.txt', 'test/')
#     generate_lyrics_from_dir('songs/queen')