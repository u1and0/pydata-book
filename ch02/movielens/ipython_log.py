# IPython log file

# __2016/07/29 8:46:25__________________________




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
mean_ratings[:5]

# # __2016/07/29 11:48:03__________________________
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


