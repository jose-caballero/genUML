#!/usr/bin/env python 

from ConfigParser import SafeConfigParser

c = SafeConfigParser()
c.readfp(open("example.conf"))

class Class(object):
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.attributes = []
        self.methods = []

    def generate(self):

        print "class %s" %self.name

        for i in self.parents:
            print "%s <|-- %s" %(i, self.name)

        for i in self.attributes:
            print "%s : %s" %(self.name, i)

        for i in self.methods:
            print "%s : %s()" %(self.name, i)


def generate(list_classes):
    print "@startuml"
    for i in list_classes:
        i.generate()
    print "@enduml"
    


list_classes = []

for section in c.sections():

        newclass = Class(section)
        try:
            parents = c.get(section, "parents")
            parents = [i.strip() for i in parents.split(',')]
        except:
            parents = []
        newclass.parents = parents

        try:
            attributes = c.get(section, "attributes")
            attributes = [i.strip() for i in attributes.split(',')]
        except:
            attributes = []
        newclass.attributes = attributes

        try:
            methods = c.get(section, "methods")
            methods = [i.strip() for i in methods.split(',')]
        except:
            methods = []
        newclass.methods = methods

        list_classes.append(newclass)

generate(list_classes)
