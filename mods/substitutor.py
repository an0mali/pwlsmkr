
class Substitutor(object):

    def __init__(self):

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
        # test > t3st > te$t > t3$t > t
    def test(self):
        self.substitute('test')

    def substitute(self, charstr):
        #convert string to array
        charar = list(charstr)
        #get substitution data
        subcountar, combocount, allsubs = self.get_sub_data(charar)
        self.sub_cycle(subcountar, allsubs)
        #permutate = self.get_permutation([0,0,0,0], allsubs)
        #print(permutate)

       # print(subar)
       # print(combocount)

    def sub_cycle(self, subcountar=[], allsubs=[]):
        #This is fucked tho, shit is kind of confusing if you think about it
        #all subs contain array of subs with allsubs[string position][sub character position]
        permutations = []
        cycle_counter = []
        #always starts at 0 for each character, for 'test',             [0,0,0,0]
        #always ends at max subcountar for each character, for 'test'   [1,1,2,1]

        #Set up cycle counter
        for x in range(0, len(subcountar)):
            cycle_counter.append(0)

        cycle_position = 0
        while cycle_position < len(subcountar):
            if cycle_counter[cycle_position] > subcountar[cycle_position]:
                if cycle_position +1 > len(cycle_counter) - 1:
                    break
                cycle_counter[cycle_position + 1] += 1
                for x in range(0, cycle_position):
                    cycle_counter[x] = 0
                cycle_position = 0

            permutation = self.get_permutation(cycle_counter, allsubs)
            permutations.append(permutation)
            cycle_counter[cycle_position] += 1

        print(permutations)

    def get_permutation(self, current_subcount, allsubs):
        #Good as fuck
        permutation = ''
        #current subcount would be array, such as [0,0,0,0]
        for position in range(0, len(current_subcount)):
            value = current_subcount[position]
            ch = allsubs[position][value]
            permutation += ch

        return permutation

    def get_sub_data(self, charar=[]):
        #convert string to char array
        combocount = 1
        #create array for keeping track of possible substitutions
        subcountar = []
        subar = []

        #create an array of arrays containing all possible substitutions for characters
        allsubs = []
        for ch in charar:
            sublen = 0
            subcharar = [ch]
            if ch in self.leetsubs:
                #get length of substitution reference array for calculations and position tracking
                sublen = len(self.leetsubs[ch])
                #Add each substituion item into substituion reference array
                for item in self.leetsubs[ch]:
                    subcharar.append(ch)
            #add substituion array to array of substitutions XD this shit is confusing
            allsubs.append(subcharar)

            combocount *= 1 + sublen
            #add length of substituion array to reference counter
            subar.append(sublen)

        return subar, combocount, allsubs

        #create an array of each substitution maximums

a = Substitutor()