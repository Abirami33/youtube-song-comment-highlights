from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#vader sentiment analyser package
    
#comments of song 1 in youtube
comments = ["Vs and nayan acting performance is totally mind-blowing ",
			 "If you really feel the song without a doubt u will get tears",
			 "Amazing song",
			 "Superb visuals",
			 "Love Vijay Sethupathi and Nayan ",
			 "Both r amazing actors and their combo creates miracles",
			 "Tamil movies these days r extremely good , infact its another level say it in terms of script / acting / songs",
			 "LOVE FROM KERALA.",
			 "This magic would happen only when two extraordinary actors comes together on the screen...",
			 "Hatsof Hipop TamizhaRockstar Vijay Sethupathi mass hitttt",
			 "Had tears nonstop. Every girls dream is this.A friendly and lovable husband for ever.If she gets she ll be blessed. Superb"
             ]

#calling the analyzer function
analyzer = SentimentIntensityAnalyzer()
print("\n")
print("Analysis of song 1's comments:")
print("\n")

#scaling it to the polarity scores
for corpus in comments:
    score = analyzer.polarity_scores(corpus)
    print("{:-<70} {}".format(corpus, str(score)))
    #formatting the corpus on left and it's scores on right
    print("\n")
	
	
