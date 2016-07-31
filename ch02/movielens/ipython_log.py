'''
* 環境
	* win10 64bit
	* Python 3.5.2 
	* Anaconda 4.1.1 (64-bit)
* 著書
	* [Python for Data Analysis( by Wes McKinney )(Final Release Date: October 2012 )](http://www.cin.ufpe.br/~embat/Python%20for%20Data%20Analysis.pdf)
* データ
	* [https://github.com/wesm/pydata-book](https://github.com/wesm/pydata-book)
'''
# IPython log file



# __DATA DEFINE__________________________
import pandas as pd
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.dat',sep='::',header=None,names=unames)

rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('ratings.dat',sep='::',header=None,names=rnames)

mnames=['user_id','title','genres']
movies=pd.read_table('movies.dat',sep='::',header=None,names=mnames)





# __MERGING__________________________
data=pd.merge(pd.merge(ratings,users),movies)
data.ix[0]

mean_ratings=data.pivot_table('rating', index='title',columns='gender',aggfunc='mean')
'''もしかしてこうすればいい？？？あとでためす2016/07/29 21:05:54
mean_ratings=data.pivot_table(data, index='title',columns='gender',aggfunc='mean')'''
mean_ratings[:5]

# data
# get_ipython().magic('pwd ')
# mean_ratings
# ratings
# data
# data.ix[0:50]
# data.ratings.ix[0:50]
# data.rating.ix[0:50]
# data.rating.ix[0:]
# data.rating.ix[0:].isnull()
# data.rating.ix[0:].isnull
# data.rating.ix[0:].nonnull
# data.rating.ix[0:].notnull
# mean_ratings=data.pivot_table('rating', rows='title',cols='gender', aggfunc='mean')
# mean_ratings=data.pivot_table('rating', index='title',columns='gender', aggfunc='mean')
# mean_ratings
# get_ipython().magic('logstart')
# ratings_by_title=data.groupby('title').size()
# ratings_by_title[:10]
# data.ix[0]
# active_titles=ratings_by_title.index[ratings_by_title>=250]
# active_titles[:10]
# data
# data.titile
# data.title
# data.title.counts()
# data.title.count
# get_ipython().magic('pinfo data.title.count')
# data.title.count(10)
# data.title.count(1)
# data.title.count(0)
# mean_ratings=mean_ratings.ix[active_titles]
# mean_ratings
# top_female_ratings=mean_ratings.sort_index(by='F',ascending=False)
# top_female_ratings[:10]
# get_ipython().magic('paste')





# ",engine='python'"を入れなければならないのはわかったが、それでもmean_rating[:5]でNaNがでてくる
import pandas as pd
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.dat',sep='::',header=None,names=unames,engine='python')
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('ratings.dat',sep='::',header=None,names=rnames,engine='python')
mnames=['user_id','title','genres']
movies=pd.read_table('movies.dat',sep='::',header=None,names=mnames,engine='python')
data=pd.merge(pd.merge(ratings,users),movies)
data.ix[0]
mean_ratings=data.pivot_table('rating', index='title',columns='gender',aggfunc='mean')
mean_ratings[:5]
'''↑の結果になぜNANが出てくるんだ'''



'''
# ここでの学び
* 読み込みエラー出たときは、read_tableでengine='python'オプション入れる
* .ixでインデックス
* pd.merge()はかぶった列を消してマージしてくれる
# mean_ratings=data.pivot_table('rating', rows='title',cols='gender', aggfunc='mean')
	以下に変更
	mean_ratings=data.pivot_table('rating', index='title',columns='gender', aggfunc='mean')
'''







users = pd.read_csv('users.dat', sep='::', header=None, names=unames, encoding='latin1',engine='python')
ratings = pd.read_csv('ratings.dat', sep='::', header=None, names=rnames, encoding='latin1',engine='python')
movies = pd.read_csv('movies.dat', sep='::', header=None, names=mnames, encoding='latin1',engine='python')
data.ix[0]
#[Out]# user_id                                 1
#[Out]# movie_id                             1193
#[Out]# rating                                  5
#[Out]# timestamp                       978300760
#[Out]# gender                                  F
#[Out]# age                                     1
#[Out]# occupation                             10
#[Out]# zip                                 48067
#[Out]# title                    Toy Story (1995)
#[Out]# genres        Animation|Children's|Comedy
#[Out]# Name: 0, dtype: object
data
#[Out]#         user_id  movie_id  rating  timestamp gender  age  occupation    zip  \
#[Out]# 0             1      1193       5  978300760      F    1          10  48067   
#[Out]# 1             1       661       3  978302109      F    1          10  48067   
#[Out]# 2             1       914       3  978301968      F    1          10  48067   
#[Out]# 3             1      3408       4  978300275      F    1          10  48067   
#[Out]# 4             1      2355       5  978824291      F    1          10  48067   
#[Out]# 5             1      1197       3  978302268      F    1          10  48067   
#[Out]# 6             1      1287       5  978302039      F    1          10  48067   
#[Out]# 7             1      2804       5  978300719      F    1          10  48067   
#[Out]# 8             1       594       4  978302268      F    1          10  48067   
#[Out]# 9             1       919       4  978301368      F    1          10  48067   
#[Out]# 10            1       595       5  978824268      F    1          10  48067   
#[Out]# 11            1       938       4  978301752      F    1          10  48067   
#[Out]# 12            1      2398       4  978302281      F    1          10  48067   
#[Out]# 13            1      2918       4  978302124      F    1          10  48067   
#[Out]# 14            1      1035       5  978301753      F    1          10  48067   
#[Out]# 15            1      2791       4  978302188      F    1          10  48067   
#[Out]# 16            1      2687       3  978824268      F    1          10  48067   
#[Out]# 17            1      2018       4  978301777      F    1          10  48067   
#[Out]# 18            1      3105       5  978301713      F    1          10  48067   
#[Out]# 19            1      2797       4  978302039      F    1          10  48067   
#[Out]# 20            1      2321       3  978302205      F    1          10  48067   
#[Out]# 21            1       720       3  978300760      F    1          10  48067   
#[Out]# 22            1      1270       5  978300055      F    1          10  48067   
#[Out]# 23            1       527       5  978824195      F    1          10  48067   
#[Out]# 24            1      2340       3  978300103      F    1          10  48067   
#[Out]# 25            1        48       5  978824351      F    1          10  48067   
#[Out]# 26            1      1097       4  978301953      F    1          10  48067   
#[Out]# 27            1      1721       4  978300055      F    1          10  48067   
#[Out]# 28            1      1545       4  978824139      F    1          10  48067   
#[Out]# 29            1       745       3  978824268      F    1          10  48067   
#[Out]# ...         ...       ...     ...        ...    ...  ...         ...    ...   
#[Out]# 645803     3952      3155       4  974595248      F   45           1  12449   
#[Out]# 645804     3952      3179       3  974595183      F   45           1  12449   
#[Out]# 645805     3952      2520       2  974594704      F   45           1  12449   
#[Out]# 645806     3952      2384       4  974595505      F   45           1  12449   
#[Out]# 645807     3952       116       5  974595248      F   45           1  12449   
#[Out]# 645808     3952      2531       4  974595712      F   45           1  12449   
#[Out]# 645809     3952      2706       4  974594897      F   45           1  12449   
#[Out]# 645810     3952      3363       4  974594897      F   45           1  12449   
#[Out]# 645811     3952      3364       4  974595401      F   45           1  12449   
#[Out]# 645812     3952       150       4  974595297      F   45           1  12449   
#[Out]# 645813     3952      3524       4  974595366      F   45           1  12449   
#[Out]# 645814     3952      1784       4  974595366      F   45           1  12449   
#[Out]# 645815     3952      3548       5  974595430      F   45           1  12449   
#[Out]# 645816     3952       344       3  974594538      F   45           1  12449   
#[Out]# 645817     3952      1021       3  974595183      F   45           1  12449   
#[Out]# 645818     3952       356       5  965676493      F   45           1  12449   
#[Out]# 645819     3952        34       4  974595505      F   45           1  12449   
#[Out]# 645820     3952      1031       3  974595772      F   45           1  12449   
#[Out]# 645821     3952      1032       4  974594749      F   45           1  12449   
#[Out]# 645822     3952      2791       2  974594704      F   45           1  12449   
#[Out]# 645823     3952      3599       4  974595143      F   45           1  12449   
#[Out]# 645824     3952      1210       4  965676528      F   45           1  12449   
#[Out]# 645825     3952      2015       4  974594538      F   45           1  12449   
#[Out]# 645826     3952      2017       4  974595505      F   45           1  12449   
#[Out]# 645827     3952      2018       5  974595601      F   45           1  12449   
#[Out]# 645828     3952        85       3  974595183      F   45           1  12449   
#[Out]# 645829     3952      2032       3  974595637      F   45           1  12449   
#[Out]# 645830     3952      1230       5  965676609      F   45           1  12449   
#[Out]# 645831     3952      2971       4  974594814      F   45           1  12449   
#[Out]# 645832     3952      2043       4  965676638      F   45           1  12449   
#[Out]# 
#[Out]#                         title                       genres  
#[Out]# 0            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 1            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 2            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 3            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 4            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 5            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 6            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 7            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 8            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 9            Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 10           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 11           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 12           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 13           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 14           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 15           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 16           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 17           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 18           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 19           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 20           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 21           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 22           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 23           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 24           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 25           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 26           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 27           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 28           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# 29           Toy Story (1995)  Animation|Children's|Comedy  
#[Out]# ...                       ...                          ...  
#[Out]# 645803  Contender, The (2000)               Drama|Thriller  
#[Out]# 645804  Contender, The (2000)               Drama|Thriller  
#[Out]# 645805  Contender, The (2000)               Drama|Thriller  
#[Out]# 645806  Contender, The (2000)               Drama|Thriller  
#[Out]# 645807  Contender, The (2000)               Drama|Thriller  
#[Out]# 645808  Contender, The (2000)               Drama|Thriller  
#[Out]# 645809  Contender, The (2000)               Drama|Thriller  
#[Out]# 645810  Contender, The (2000)               Drama|Thriller  
#[Out]# 645811  Contender, The (2000)               Drama|Thriller  
#[Out]# 645812  Contender, The (2000)               Drama|Thriller  
#[Out]# 645813  Contender, The (2000)               Drama|Thriller  
#[Out]# 645814  Contender, The (2000)               Drama|Thriller  
#[Out]# 645815  Contender, The (2000)               Drama|Thriller  
#[Out]# 645816  Contender, The (2000)               Drama|Thriller  
#[Out]# 645817  Contender, The (2000)               Drama|Thriller  
#[Out]# 645818  Contender, The (2000)               Drama|Thriller  
#[Out]# 645819  Contender, The (2000)               Drama|Thriller  
#[Out]# 645820  Contender, The (2000)               Drama|Thriller  
#[Out]# 645821  Contender, The (2000)               Drama|Thriller  
#[Out]# 645822  Contender, The (2000)               Drama|Thriller  
#[Out]# 645823  Contender, The (2000)               Drama|Thriller  
#[Out]# 645824  Contender, The (2000)               Drama|Thriller  
#[Out]# 645825  Contender, The (2000)               Drama|Thriller  
#[Out]# 645826  Contender, The (2000)               Drama|Thriller  
#[Out]# 645827  Contender, The (2000)               Drama|Thriller  
#[Out]# 645828  Contender, The (2000)               Drama|Thriller  
#[Out]# 645829  Contender, The (2000)               Drama|Thriller  
#[Out]# 645830  Contender, The (2000)               Drama|Thriller  
#[Out]# 645831  Contender, The (2000)               Drama|Thriller  
#[Out]# 645832  Contender, The (2000)               Drama|Thriller  
#[Out]# 
#[Out]# [645833 rows x 10 columns]
mean_ratings=data.pivot_table('rating', index='title',columns='gender',aggfunc='mean')
mean_ratings
#[Out]# gender                                                 F         M
#[Out]# title                                                             
#[Out]# $1,000,000 Duck (1971)                               NaN  3.560000
#[Out]# 'Night Mother (1986)                                 NaN  3.389671
#[Out]# 'Til There Was You (1997)                            NaN  3.333333
#[Out]# 'burbs, The (1989)                              4.000000       NaN
#[Out]# ...And Justice for All (1979)                   4.354545       NaN
#[Out]# 1-900 (1994)                                         NaN  2.840580
#[Out]# 10 Things I Hate About You (1999)                    NaN  4.185430
#[Out]# 101 Dalmatians (1961)                                NaN  3.661765
#[Out]# 101 Dalmatians (1996)                                NaN  3.777251
#[Out]# 12 Angry Men (1957)                             3.707152       NaN
#[Out]# 13th Warrior, The (1999)                             NaN  3.609848
#[Out]# 187 (1997)                                      3.420613       NaN
#[Out]# 2 Days in the Valley (1996)                          NaN  3.186893
#[Out]# 20 Dates (1998)                                 3.764045       NaN
#[Out]# 20,000 Leagues Under the Sea (1954)                  NaN  3.010776
#[Out]# 200 Cigarettes (1999)                                NaN  3.558140
#[Out]# 2001: A Space Odyssey (1968)                         NaN  3.989950
#[Out]# 2010 (1984)                                     4.000000       NaN
#[Out]# 24 7: Twenty Four Seven (1997)                  3.342857       NaN
#[Out]# 24-hour Woman (1998)                                 NaN  3.805195
#[Out]# 28 Days (2000)                                       NaN  4.072727
#[Out]# 3 Ninjas: High Noon On Mega Mountain (1998)          NaN  3.769231
#[Out]# 3 Strikes (2000)                                4.270833       NaN
#[Out]# 301, 302 (1995)                                      NaN  2.886364
#[Out]# 39 Steps, The (1935)                                 NaN  4.116883
#[Out]# 400 Blows, The (Les Quatre cents coups) (1959)       NaN  4.271429
#[Out]# 42 Up (1998)                                         NaN  3.846154
#[Out]# 52 Pick-Up (1986)                               4.054054       NaN
#[Out]# 54 (1998)                                       3.056790       NaN
#[Out]# 7th Voyage of Sinbad, The (1958)                3.613636       NaN
#[Out]# ...                                                  ...       ...
#[Out]# Wyatt Earp (1994)                               3.571429       NaN
#[Out]# X-Files: Fight the Future, The (1998)                NaN  3.526316
#[Out]# X-Men (2000)                                         NaN  2.789474
#[Out]# X: The Unknown (1956)                                NaN  3.950413
#[Out]# Xiu Xiu: The Sent-Down Girl (Tian yu) (1998)         NaN  2.984127
#[Out]# Yankee Zulu (1994)                              4.016949       NaN
#[Out]# Yards, The (1999)                                    NaN  3.753425
#[Out]# Year My Voice Broke, The (1987)                      NaN  3.507246
#[Out]# Year of Living Dangerously (1982)                    NaN  3.769231
#[Out]# Year of the Horse (1997)                             NaN  3.370370
#[Out]# Yellow Submarine (1968)                              NaN  3.159748
#[Out]# Yojimbo (1961)                                       NaN  3.769231
#[Out]# You Can't Take It With You (1938)                    NaN  3.084746
#[Out]# You So Crazy (1994)                             3.280315       NaN
#[Out]# You've Got Mail (1998)                               NaN  3.292517
#[Out]# Young Doctors in Love (1982)                    3.668571       NaN
#[Out]# Young Frankenstein (1974)                            NaN  4.000000
#[Out]# Young Guns (1988)                               4.534483       NaN
#[Out]# Young Guns II (1990)                            3.250000       NaN
#[Out]# Young Poisoner's Handbook, The (1995)                NaN  3.299010
#[Out]# Young Sherlock Holmes (1985)                         NaN  4.159483
#[Out]# Young and Innocent (1937)                            NaN  3.434783
#[Out]# Your Friends and Neighbors (1998)                    NaN  4.093333
#[Out]# Zachariah (1971)                                     NaN  2.913043
#[Out]# Zed & Two Noughts, A (1985)                          NaN  3.557377
#[Out]# Zero Effect (1998)                                   NaN  3.213636
#[Out]# Zero Kelvin (Kj誡lighetens kjere) (1995)        4.000000       NaN
#[Out]# Zeus and Roxanne (1997)                              NaN  3.494764
#[Out]# Zone 39 (1997)                                  4.000000       NaN
#[Out]# eXistenZ (1999)                                      NaN  2.978022
#[Out]# 
#[Out]# [3883 rows x 2 columns]
mean_ratings[:5]
#[Out]# gender                                F         M
#[Out]# title                                            
#[Out]# $1,000,000 Duck (1971)              NaN  3.560000
#[Out]# 'Night Mother (1986)                NaN  3.389671
#[Out]# 'Til There Was You (1997)           NaN  3.333333
#[Out]# 'burbs, The (1989)             4.000000       NaN
#[Out]# ...And Justice for All (1979)  4.354545       NaN


'''
2016/07/31 14:30:41
なんでNaNなんだ！！
'''