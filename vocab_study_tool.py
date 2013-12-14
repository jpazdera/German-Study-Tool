from vocab_lists_by_chapter import *
from vocab_dictionary_generator import Generate_Vocab_List
from random import randrange


######### GLOBAL VARIABLES ###########################################

PROGRAM_MODE = 'STUDY' # 'STUDY' for study tool, 'GEN' for new vocab list generator

active_vocab_list = []
recently_used = []
user_answer = ''
correct_answer = ''
vocab_dictionary = {
                    # 1: chapter_1_vocab,
                    # 2: chapter_2_vocab,
                    # 3: chapter_3_vocab,
                    # 4: chapter_4_vocab,
                    # 5: chapter_5_vocab,
                    6: chapter_6_vocab}


######### HELPER FUNCTIONS ###########################################

def get_vocab_list(chapter):
    global vocab_dictionary
    global active_vocab_list
    if (type(chapter) == int) and (chapter in vocab_dictionary):
        active_vocab_list = vocab_dictionary[chapter]
    elif type(chapter) == list:
        n = chapter[0]
        max = chapter[1]
        while (n <= max) and (n in vocab_dictionary):
            active_vocab_list == active_vocab_list + vocab_dictionary[n]
            n += 1
    else:
        raise Exception ('Error: invalid input')
    
def generate_question():
    global active_vocab_list
    global recently_used
    global user_answer
    global correct_answer
    while True: # generate random number to choose a word pair; reduces chance of duplicate results by ignoring the first duplicate of each used word pair
        i = randrange(0, len(active_vocab_list))
        if i in recently_used:
            recently_used.remove(i)
        else:
            recently_used = recently_used + [i]
            active_pair = active_vocab_list[i]
            break
    n = randrange(0,2)
    if n == 0:
        user_answer = raw_input('What is the English translation of... \n\n' + active_pair.german + '\n\n')
        correct_answer = active_pair.english
    else:
        user_answer = raw_input('What is the German translation of... \n\n' + active_pair.english + '\n\n')
        correct_answer = active_pair.german
     
            
######### MAIN UI ###########################################

def Study_Tool():
    global user_answer
    global correct_answer
    print 'Welcome to the German vocabulary study tool!'
    chapter = input('Please enter chapter number(s) to test on: ')
    get_vocab_list(chapter)
    print ('Loaded ' + str(len(active_vocab_list)) + ' words.\nPress enter to begin. Type \"EXIT\" at any point afterwards to quit.')
    raw_input()
    while True:
        generate_question()
        if user_answer == 'EXIT':
            break
        else:
            if user_answer == correct_answer:
                print '\nCorrect! Press enter to continue.'
                raw_input()
            else:
                print ('\nThe correct answer is: ' + correct_answer + '\n\nPress enter to continue.')
                raw_input()
    print 'Thank you for using this program. Now exiting...'

def main():
    global PROGRAM_MODE
    if PROGRAM_MODE == 'STUDY':
        Study_Tool()
    elif PROGRAM_MODE == 'GEN':
        Generate_Vocab_List()
    else:
        raise Exception ('ERROR: INVALID PROGRAM MODE')
    
main()