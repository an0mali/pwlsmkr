import names

class NameGen(object):

    def __init__(self, name):
        print("Initializing NameGen object...")
        #self.name = name
        self.props = {}
        self.props['names'] = []
        
    def get_names_list(self):
        print(self.props['names'])
        return self.props['names']
    
    def generate_names(self, amt, incmale=True, incfemale=True, incfirst=True, incmiddle=True, inclast=True):
        #Generate and return a list of names, might be useful for a target that utilizes names in passwords
        print("NameGen: Generating names...")
        setgender = 'male'
        alternate_genders = False
        #Set gender based on args
        if not (incmale and incfemale):
            if incmale:
                setgender = 'male'
            else:
                setgender = 'female'
        else:
            alternate_genders = True
            
        
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
