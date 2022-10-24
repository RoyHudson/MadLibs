import json
import os

#mad libs templates
# Class Define and Structure all of the objects that create from it
class MadLibs:
    #This is the constructor for MadLibs
    path = "./templates"
    #variables
    def __init__(self, word_descriptions, template): 
        self.template = template
        self.word_descriptions = word_descriptions
        self.user_input = [] 
        self.story = None
    #El ERROR ESTA AQUI!, era una estupidez mal escrita 

    @classmethod
    def from_json(cls, name, path = None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib

    #User Input
    def get_words_from_user(self):
        print ("Please Provide the Following words: ")
        for desc in self.word_descriptions:
            ui = input(desc + " ") #User Insert Noun and verbs Here!
            self.user_input.append(ui) #function that adds words to the list words
        return self.user_input #return the list of words that were added

    #Build the Story
    def build_story(self):
        self.story = self.template.format(*self.user_input) #Gives the Order of the words to the Templates
        return self.story
    
    def show_story(self):
        print (story)

def select_template():
    print("Select a Mad Lib From the Following List...")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    return template


temp_name = select_template()
# temp_name = "day_at_the_zoo.json"
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.show_story()
#Takes a string as a template with placeholder variables to be over written.