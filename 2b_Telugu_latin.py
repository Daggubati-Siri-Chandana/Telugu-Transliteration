
import re
import csv

with open('telugu_latin.csv', mode='r',encoding='utf-8') as infile:
    reader = csv.reader(infile)
    conversiontable = {str(row[0]):str(row[1]) for row in reader}

consonants = '\u0C15-\u0C39\u0C58-\u0C5F\u0C78-\u0C7C\u0C7E-\u0C7F'
vowelsigns = '\u0C3E-\u0C4C\u0C3A-\u0C3B\u0C4E-\u0C4F\u0C55-\u0C57'
nukta = '\u0C3C'
virama = '\u0C4D'

devanagarichars = '\u0C00-\u0C7F\u1CD0-\u1CFF\uA8E0-\uA8FF'

def deva_to_latn(text):

    word = text.strip()

    # define a buffer to store the transliteration
    curr = ''

    for index, char in enumerate(word):
        # check if char is a Devanagari character. if true then continue processing.
        # otherwise, output char to curr

        if re.match('[' + devanagarichars + ']', char):

            # if char = consonant, then its transliteration is dependent upon various
            # factors. need to check if next char = nukta, virama, vowel sign.

            if re.match('[' + consonants + ']', char):

                # check next char
                nextchar = word[(index + 1) % len(word)]

                if nextchar:

                    # if next char = nukta, then add present char and nukta
                    # to 'cons'. else just add present char. set variable
                    # to test for nukta when processing next char

                    if re.match('[' + nukta + ']', nextchar):
                        cons = char + nextchar
                        nukta_present = 1
                    else:
                        cons = char
                        nukta_present = 0

                    # if present char is nukta, then check next char

                    if nukta_present:
                        nextchar = word[(index + 2) % len(word)]

                    # if next char = combining sign or virama, convert consonant
                    # without "a". else if next char != combining sign or virama,
                    # add "a" to consonant

                    if re.match('[' + vowelsigns + virama +']', nextchar):
                        trans = conversiontable.get(cons, '')
                        curr = curr + trans
                    else:
                        trans = conversiontable.get(cons, '')
                        trans = trans + "a"
                        curr = curr + trans

            # transliterate all other chars

            else:
                trans = conversiontable.get(char, '')
                curr = curr + trans

        # char is not Devanagari. output char to curr

        else:
             curr = curr + char

    return curr

def getLatin(inputtext):

    word_syllables = []
    all_words = []

    for word in inputtext.split():
        print(word)
        latin_output = deva_to_latn(word)
        all_words.append(latin_output)
        joined_all_words = ' '.join(all_words)

    return joined_all_words


text = "మూడు రాజధానులకు మొగ్గు, రైతులకు ప్యాకేజీ.. ఏపీ కేబినెట్ సంచలన నిర్ణయాలు"
print("Telugu Sentence: ",text)
print("Transliterated text in Latin: ",getLatin(text))



