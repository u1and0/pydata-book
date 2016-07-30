# IPython log file


get_ipython().system('head -n 5 yob*.txt')   #`!head -n 5 yob*.txt`でyobナントカ.txtの中身5行標準出力に表示

import pandas as pd
# __まずは1ファイルをフレームに取り込んでみる__________________________
names1880=pd.read_csv('yob1880.txt',names=['name', 'sex', 'births'])
names1880.groupby('sex').births.sum()


# __すべてのyobﾅﾝﾄｶ.txtを1つのフレームに取り入れたいとき__________________________
pieces=[]
columns=['name', 'sex', 'births']
years=range(1880,2011)
for year in years:
	path='yob%d.txt' % year
	frame=pd.read_csv(path,names=columns)
	frame['year']=year
	pieces.append(frame)
	names=pd.concat(pieces,ignore_index=True)   #インデックスを無視するTrueにするとtext左列のインデックスを適当に変えてくれる
				   #1690783行の巨大なフレームが出来上がる。それでも検索は高速


# __出生数の推移__________________________
total_births=names.pivot_table(names, index='year', columns='sex', aggfunc=sum)
'''
本では
 total_births = names.pivot_table('births', rows='year',cols='sex', aggfunc=sum)
 のようにあるが、これは古い
 rows=>index
 cols=>columns
 に変更され、
 第一引数にデータフレーム入れないといけない
 (第二引数に'birth'入れなきゃと思ったけどはじかれた・・・？)
'''
total_births.tail()
total_births.plot(title='Total births by sex and year')


