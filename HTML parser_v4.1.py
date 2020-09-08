from html.parser import *
from formatter import *
import codecs

with codecs.open('C:/Users/Dan.Mapes/Documents/Python parse HTML Project/Untitled-2.html', 'r') as html:
    fcontent = html.readlines()

print (fcontent)
