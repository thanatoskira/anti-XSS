#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class XssScripts(object):
    '''
    XssScripts class useed as a global var.
    '''

    text = []

    def __init__(self):
        pass

    def addText(self, text):
        self.text.append(text)

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text
