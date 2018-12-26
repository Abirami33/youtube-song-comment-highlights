import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
from os import path
from PIL import Image
import csv
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

'''
def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
	return("hsl(0,0%%, %d%%)" % np.random.randint(10,50))
'''

text=open('/home/stud/youtube_comments.txt').read()
stopwords = set(STOPWORDS)
mask = Image.open("/home/stud/Pictures/rab.jpg")
mask = np.array(mask)
wordcloud = WordCloud(
	                      width = 512,
	                      height = 512,
                          background_color='white',
                          stopwords=stopwords,
                          max_words=3000,
			              mask=mask,
                          max_font_size=120, 
			              contour_width=3,
			              contour_color='darkblue',
	                      random_state=42
                         ).generate(text)

plt.figure(figsize=[7,7],facecolor = 'white', edgecolor='blue')
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()





