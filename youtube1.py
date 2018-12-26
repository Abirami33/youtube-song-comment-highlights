import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
from os import path
from PIL import Image
import csv
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
	return("hsl(0,0%%, %d%%)" % np.random.randint(10,50))


text=open('/home/stud/u.txt').read()
stopwords = set(STOPWORDS)
mask = Image.open("/home/stud/Pictures/rab.jpg")
mask = np.array(mask)
wordcloud = WordCloud(
                          background_color='lightcyan',
                          stopwords=stopwords,
                          max_words=3000,
			              mask=mask,
                          max_font_size=80, 
			              contour_width=3,
			              contour_color='royalblue',
	                      random_state=42
                         ).generate(text)


plt.figure(figsize=[7,7])
plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
plt.axis("off")
plt.show()




