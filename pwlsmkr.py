
import argparse
#requires ntlk
import nltk
from nltk.corpus import words
import names

class pwlsmkr(object):

    def __init__(self, args):

        self.props = {}
       
        for keyword in vars(args):
            if type(eval('args.' + keyword)) != str:
                self.props[keyword] = eval('args.' + keyword)

            #Special treatment for CSV file location, set csvwords to file location path
            elif keyword == "keywords":
                self.props['csvkeywords'] = eval('args.' + keyword)
            else:
                #all else are true if 'y' or false if else
                self.props[keyword] = eval('args.' + keyword) == 'y'

        if self.props['dictionary']:
           
            try:
                self.props['wordlist'] = words.words()
            except:
                nltk.download()
                self.props['wordlist'] = words.words()
            #requires ntlk.download() to get current list of all words
            
            print('length of english word list: ' + str(len(self.props['wordlist'])))
        self.props['names'] = []
        #Define list of commonly used l33tsp3@k substitutions
        
        self.leetsubs = {
            '0': ['o', 'O'],
            '1': ['I', 'i', 'l', '|', '!'],
            '2': ['S', 's'],
            '3': ['E'],
            #4
            '5': ['s', 'S'],
            '6': ['G'],
            '7': ['T', 't'],
            '8': ['B'],
            '9': ['P'],
            'a': ['@', '&'],
            'b': ["8"],
            'c': ['('],
            'd': {'p', 'P'},
            'e': ["3"],
            #f
            'g': ['6', '&'],
            'h': ['#'],
            'i': ['1'],
            #j
            #k
            'l': ['1', '|', '!'],
            #m
            #n
            'o': ["0", "()"],
            'p': ['9'],
            #q
            #r
            's': ["$", '5'],
            't': ['7'],
            #u
            'v': ['\/'],
            #w
            'x': ['%', '*'],
            #y
            #z
            'and': ['&'],
        }

        self.test()

    def test(self):
        print('Initiating test...')
        self.generate_names(42)
        print('length of names list: ' + str(len(self.props['names'])))
        for keyword in self.props:
            if keyword != 'wordlist':
                print(keyword + ': ' + str(self.props[keyword]))

    def generate_names(self, amt, incmale=True, incfemale=True, incfirst=True, incmiddle=True, inclast=True):
        #Generate and return a list of names

        setgender = False
        alternate_genders = False
        #Set gender based on args
        if not (incmale and incfemale):
            if incmale:
                setgender = 'male'
            else:
                setgender = 'female'
        else:
            alternate_genders = True
            setgender = 'male'
        
        #Generate names
        for x in range(0, amt):
            #Generate first name based on gender arg
            name = ''

            if incfirst:
                name = names.get_first_name(gender=setgender)
            #Generate middle name based on arg
            if incmiddle:
                while True:
                    midname = names.get_first_name(gender=setgender)
                    if midname != name:
                        name += midname
                        break
           
            if inclast:
                name += names.get_last_name()

            if not name in self.props['names']:
                self.props['names'].append(name)
                if alternate_genders:
                    if setgender == 'male':
                        setgender = 'female'
                    else:
                        setgender = 'male'

#Create argument parser
parser = argparse.ArgumentParser(
    prog='pwlsmkr',
    description='Generate a targeted bruteforce password list based on specified parameters. By An0m@ly, Cortana, and 10 beers'
)

#Add arguments and descriptions
parser.add_argument("-m", "--minlen", type=int, help="Minimum password length", default=7)
parser.add_argument("-x", "--maxlen", type=int, help="Maximum password length", default=14)
parser.add_argument("-l", "--letters", type=str, help="Include letters [y/n]", default='y')
parser.add_argument("-n", "--numbers", type=str, help="Include numbers [y/n]", default='y')
parser.add_argument("-s", "--symbols", type=str, help="Include symbols [y/n]", default='y')
parser.add_argument("-st", "--string", type=str, help="Include a specific string [string]", default=False)
parser.add_argument("-k", "--keywords", type=str, help="Add CSV list of keywords [file location]", default=False)
parser.add_argument("-d", "--dictionary", type=str, help="Include complete english dictionary [y/n]", default='y') #TO DO: Conflicts with interest dictionary, add logic gate
parser.add_argument("-nd", "--namesdictionary", type=str, help="Include a names dictionary [file location]", default=False)
parser.add_argument("-e", "--leetspeak", type=str, help="If using keywords, automatically substitutes all combinations of l33tsp3@k (ex. 3 for e, @ for a, etc.) [y/n]", default='n')
parser.add_argument("-amin", "--minimumappend", type=int, help="If using keywords, minimum character appending to end of keywords (Ex. keyword is 'foo', -amin 1  w/include numbers would add all possible combos of foo0, foo1, etc. )", default=0)
parser.add_argument("-amax", "--maximumappend", type=int, help="If using keywords, maximum character appending to end of keywords (Ex. keyword is 'foo', -amax 3 w/include numbers would add all possible combos of foo0-foo999)", default=1)
parser.add_argument("-al", "--appendletters", type=str, help="If using keywords and append, include letters (disabled by default) [y/n]", default='n')
parser.add_argument("-an", "--appendnumbers", type=str, help="If using keywords and append, Include numbers (disabled by default) [y/n]", default='n')
parser.add_argument("-as", "--appendsymbols", type=str, help="If using keywords and append, Include symbols (enabled by default) [y/n]", default='y')
parser.add_argument("-minw", "--minimumwords", type=int, help="If using keywords/names/dictionary, minimum words to use", default=1)
parser.add_argument("-maxw", "--maximumwords", type=int, help="If using keywords/names/dictionary, maximum words to use", default=2)
args = parser.parse_args()

#Run program
a274269 = pwlsmkr(args)