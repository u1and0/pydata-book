# IPython log file
import pandas as pd

# __IMPORT DATA__________________________
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.dat',sep='::',header=None,names=unames)

rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('ratings.dat',sep='::',header=None,names=rnames)

mnames=['user_id','title','genres']
movie=pd.read_table('movies.dat',sep='::',header=None,names=mnames)


