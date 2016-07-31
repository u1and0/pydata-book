# %load ipython_log.py
# IPython log file
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
'''prop によって全出生数に対する各名前の出生数をはじき出してみる'''
# dataをyear,sexでグループ化し、新しい列に入れる





def add_prop(group):
	'''各名前の出生数の、全出生数に対する割合を出して、groupに列を追加'''
	births = group.births.astype(float)   # Integer division floors
	group['prop'] = births / births.sum()   #propというcolumnに結果を追加
	return group

names = names.groupby(['year', 'sex']).apply(add_prop)

np.allclose(names.groupby(['year','sex']).prop.sum(),1)   # propをすべて足すと1(100%)になることを確認
	# allclose によってチェックする　names.groupby(['year','sex']).prop.sum()と1が等しいか確認










#__Analyzing Naming Trends__________________________ 
def get_top1000(group):
	'''
	top1000の名前を各sex/year から抜き出す。別のグループ作る
	<旧形式>
	return group.sort_index(by='births', ascending=False)[:1000]
	'''
	return group.sort_values(by='births', ascending=False)[:1000]

grouped=names.groupby(['year','sex'])
top1000=grouped.apply(get_top1000)
'''
__top1000 Another Way__________________________ 
pieces = []
for year, group in names.groupby(['year', 'sex']):
	pieces.append(group.sort_index(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)
'''

boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']

total_births=top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)   #data munging(データ変換)を行うべくpivot tableで直す
subset=total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12,10),grid=False, title="Number of births per year")








# __Measuring the increase in naming diversity__________________________
table=top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)   # 名前の多様性を調べるべく、比率をpivot_tableにしてみる
table.plot(title='Sum of table1000.prop by year and sex',yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))

# __2010年データの比率をソートする__________________________ 
df=boys[boys.year==2010]
prop_cumsum=df.sort_values(by='prop',ascending=False).prop.cumsum()   # 累積和cumulativesum`cumsum`使って比率prop=0.5に届く名前を得る
prop_cumsum[:10]
prop_cumsum.searchsorted(0.5)   # その際のインデックスをsearchsorted関数を使って得て、ソートされた列に0.5のcumsumをinsertする

# __1990にも同様に__________________________
df=boys[boys.year==1900]
in1900=df.sort_values(by='prop',ascending=False).prop.cumsum()
in1900.searchsorted(0.5)+1
prop_cumsum[:10]
prop_cumsum=df.sort_values(by='prop',ascending=False).prop.cumsum()

# __1990, 2010年にやったことを全年数に対して実行__________________________
def get_quantile_count(group, q=0.5):
	'''
	propソートして累積和したものの0.5のインデックスを返す
	<旧形式>
		group = group.sort_index(by='prop', ascending=False)
		return group.prop.cumsum().searchsorted(q) + 1
	'''
	group = group.sort_values(by='prop', ascending=False)
	return group.prop.cumsum().values.searchsorted(q) + 1   #return group.prop.cumsum().values.searchsorted(q) + 1 に書き換え valuesくわわった 値がアレイ表示になってしまうのを防ぐ

diversity=top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity=diversity.unstack('sex')   #男女別

diversity.head()
diversity.plot(title="Number of popular names in top 50%")   # 女性のほうが名前の多様性がすべての年において多いことが分かる



# __The "Last letter" Revolution__________________________ 
get_last_letter=lambda x:x[-1]   # name columnsから最後の文字列だけ抜き出し
last_letters=names.name.map(get_last_letter)   #namesの名前すべてに最後の文字列抜出式(get_last_letter)を適用
last_letters.name='last_letter'
table=names.pivot_table('births',index=last_letters,columns=['sex','year'],aggfunc=sum)

subtable=table.reindex(columns=[1910,1960,2010],level='year')
subtable.head()


subtable.sum()   #全出生数
letter_prop=subtable/subtable.sum().astype(float)   # 文字列比率を取得

fig,axes=plt.subplots(2,1,figsize=(10,8))   #2段のサブプロットで表示
letter_prop['M'].plot(kind='bar',rot=0,ax=axes[0],title='Male')
letter_prop['F'].plot(kind='bar',rot=0,ax=axes[1],title='Female',legend=False)

#男性の名前の最後がnで終わる比率がダントツに高い
#以下で年推移of last 'n' nameを見ていく

letter_prop=table/table.sum().astype(float)   #last_letter各々の全体数に対する比率
dny_ts=letter_prop.ix[['d','n','y'],'M'].T   #d,n,yだけプロットしてみる
																				#'M'男性に対してだけ　
																				# .Tでデータフレームの転置行列作る
# dny_ts.head()
# dny_ts.plot()
# plt.show()













#__Boy names that became girl names (and vice versa)__________________________ 
all_names=top1000.name.unique()   #全名前列挙
mask=np.array(['lesl' in x.lower() for x in all_names])   #lower() 小文字変換メソッド
															#'lesl'という文字含んでいたらTrue返す
#[In]# mask
#[Out]# array([False, False, False, ..., False, False, False], dtype=bool)




lesley_like=all_names[mask]   #all_namesの中の'lesl'含んでいるものだけlesley_likeに格納
#[In]# lesley_like
#[Out]# array(['Leslie', 'Lesley', 'Leslee', 'Lesli', 'Lesly'], dtype=object)





filtered=top1000[top1000.name.isin(lesley_like)]   #top1000の中からlesleyぽい奴だけ抜き出し
#[In]# filtered
#[Out]#                     name sex  births  year      prop
#[Out]# year sex                                            
#[Out]# 1880 F   654      Leslie   F       8  1880  0.000088
#[Out]#      M   1108     Leslie   M      79  1880  0.000715
#[Out]# 1881 F   2523     Leslie   F      11  1881  0.000120
#[Out]#      M   3072     Leslie   M      92  1881  0.000913
#[Out]# 1882 F   4593     Leslie   F       9  1882  0.000083
#[Out]#      M   5081     Leslie   M     122  1882  0.001073
#[Out]#          5865     Lesley   M       6  1882  0.000053
#[Out]# 1883 F   6850     Leslie   F       7  1883  0.000062
#[Out]#      M   7225     Leslie   M     120  1883  0.001147
#[Out]#          8093     Lesley   M       5  1883  0.000048
#[Out]# 1884 F   8697     Leslie   F      15  1884  0.000116
#[Out]#      M   9432     Leslie   M     125  1884  0.001092
#[Out]# 1885 F   11161    Leslie   F      10  1885  0.000075
#[Out]#      M   11751    Leslie   M     122  1885  0.001132
#[Out]# 1886 F   13601    Leslie   F       8  1886  0.000055
#[Out]#      M   14132    Leslie   M     136  1886  0.001228
#[Out]# 1887 F   15806    Leslie   F      12  1887  0.000082
#[Out]#      M   16524    Leslie   M     166  1887  0.001637
#[Out]# 1888 F   18030    Leslie   F      23  1888  0.000129
#[Out]#      M   19074    Leslie   M     175  1888  0.001448
#[Out]# 1889 F   20690    Leslie   F      23  1889  0.000129
#[Out]#      M   21737    Leslie   M     155  1889  0.001402
#[Out]# 1890 F   23332    Leslie   F      20  1890  0.000105
#[Out]#      M   24372    Leslie   M     181  1890  0.001630
#[Out]# 1891 F   25928    Leslie   F      28  1891  0.000151
#[Out]#      M   27068    Leslie   M     164  1891  0.001621
#[Out]# 1892 F   28704    Leslie   F      22  1892  0.000104
#[Out]#      M   29851    Leslie   M     207  1892  0.001696
#[Out]# 1893 F   31576    Leslie   F      26  1893  0.000122
#[Out]#      M   32765    Leslie   M     185  1893  0.001647
#[Out]# ...                  ...  ..     ...   ...       ...
#[Out]# 2000 F   1332261  Leslie   F    3619  2000  0.001995
#[Out]#          1332560   Lesly   F     742  2000  0.000409
#[Out]#          1332601  Lesley   F     658  2000  0.000363
#[Out]# 2001 F   1362012  Leslie   F    3610  2001  0.002007
#[Out]#          1362300   Lesly   F     801  2001  0.000445
#[Out]#          1362452  Lesley   F     509  2001  0.000283
#[Out]# 2002 F   1392272  Leslie   F    3520  2002  0.001962
#[Out]#          1392586   Lesly   F     717  2002  0.000400
#[Out]#          1392743  Lesley   F     471  2002  0.000262
#[Out]# 2003 F   1422818  Leslie   F    3635  2003  0.001992
#[Out]#          1423091   Lesly   F     838  2003  0.000459
#[Out]#          1423330  Lesley   F     451  2003  0.000247
#[Out]# 2004 F   1453982  Leslie   F    3497  2004  0.001908
#[Out]#          1454295   Lesly   F     747  2004  0.000408
#[Out]#          1454500  Lesley   F     450  2004  0.000245
#[Out]# 2005 F   1486010  Leslie   F    3120  2005  0.001692
#[Out]#          1486308   Lesly   F     783  2005  0.000425
#[Out]#          1486623  Lesley   F     381  2005  0.000207
#[Out]# 2006 F   1518523  Leslie   F    3035  2006  0.001600
#[Out]#          1518834   Lesly   F     761  2006  0.000401
#[Out]#          1519161  Lesley   F     370  2006  0.000195
#[Out]# 2007 F   1552581  Leslie   F    2689  2007  0.001403
#[Out]#          1552882   Lesly   F     765  2007  0.000399
#[Out]#          1553271  Lesley   F     351  2007  0.000183
#[Out]# 2008 F   1587484  Leslie   F    2323  2008  0.001233
#[Out]#          1587788   Lesly   F     699  2008  0.000371
#[Out]# 2009 F   1622503  Leslie   F    1975  2009  0.001081
#[Out]#          1622845   Lesly   F     598  2009  0.000327
#[Out]# 2010 F   1657142  Leslie   F    1558  2010  0.000886
#[Out]#          1657525   Lesly   F     502  2010  0.000285
#[Out]# 
#[Out]# [400 rows x 5 columns]











filtered.groupby('name').births.sum()   #nameでグループ化してその出生数を合計する
#[Out]# name
#[Out]# Leslee      1082
#[Out]# Lesley     35022
#[Out]# Lesli        929
#[Out]# Leslie    370429
#[Out]# Lesly      10067
#[Out]# Name: births, dtype: int64







table=filtered.pivot_table('births',index='year',columns='sex',aggfunc=sum)   # sex, yearごとに集計
#[Out]# sex        F      M
#[Out]# year               
#[Out]# 1880     8.0   79.0
#[Out]# 1881    11.0   92.0
#[Out]# 1882     9.0  128.0
#[Out]# 1883     7.0  125.0
#[Out]# 1884    15.0  125.0
#[Out]# 1885    10.0  122.0
#[Out]# 1886     8.0  136.0
#[Out]# 1887    12.0  166.0
#[Out]# 1888    23.0  175.0
#[Out]# 1889    23.0  155.0
#[Out]# 1890    20.0  181.0
#[Out]# 1891    28.0  164.0
#[Out]# 1892    22.0  207.0
#[Out]# 1893    26.0  185.0
#[Out]# 1894    36.0  223.0
#[Out]# 1895    22.0  235.0
#[Out]# 1896    27.0  237.0
#[Out]# 1897    34.0  222.0
#[Out]# 1898    24.0  236.0
#[Out]# 1899    18.0  181.0
#[Out]# 1900    30.0  285.0
#[Out]# 1901    29.0  204.0
#[Out]# 1902    37.0  251.0
#[Out]# 1903    24.0  244.0
#[Out]# 1904    30.0  243.0
#[Out]# 1905    35.0  247.0
#[Out]# 1906    29.0  263.0
#[Out]# 1907    34.0  273.0
#[Out]# 1908    41.0  290.0
#[Out]# 1909    35.0  292.0
#[Out]# ...      ...    ...
#[Out]# 1981  5796.0  500.0
#[Out]# 1982  5814.0  430.0
#[Out]# 1983  4975.0  414.0
#[Out]# 1984  4419.0  367.0
#[Out]# 1985  4168.0  331.0
#[Out]# 1986  3741.0  379.0
#[Out]# 1987  3666.0  290.0
#[Out]# 1988  3555.0  318.0
#[Out]# 1989  3259.0  327.0
#[Out]# 1990  3268.0  295.0
#[Out]# 1991  2920.0  277.0
#[Out]# 1992  2836.0  216.0
#[Out]# 1993  2607.0  201.0
#[Out]# 1994  2685.0  207.0
#[Out]# 1995  2782.0  186.0
#[Out]# 1996  3584.0  176.0
#[Out]# 1997  3847.0  158.0
#[Out]# 1998  4289.0    NaN
#[Out]# 1999  4693.0    NaN
#[Out]# 2000  5019.0    NaN
#[Out]# 2001  4920.0    NaN
#[Out]# 2002  4708.0    NaN
#[Out]# 2003  4924.0    NaN
#[Out]# 2004  4694.0    NaN
#[Out]# 2005  4284.0    NaN
#[Out]# 2006  4166.0    NaN
#[Out]# 2007  3805.0    NaN
#[Out]# 2008  3022.0    NaN
#[Out]# 2009  2573.0    NaN
#[Out]# 2010  2060.0    NaN
#[Out]# 
#[Out]# [131 rows x 2 columns]



table=table.div(table.sum(1),axis=0)   #正規化
# table.tail()
#[Out]# sex     F   M
#[Out]# year         
#[Out]# 2006  1.0 NaN
#[Out]# 2007  1.0 NaN
#[Out]# 2008  1.0 NaN
#[Out]# 2009  1.0 NaN
#[Out]# 2010  1.0 NaN
# table.head()
#[Out]# sex          F         M
#[Out]# year                    
#[Out]# 1880  0.091954  0.908046
#[Out]# 1881  0.106796  0.893204
#[Out]# 1882  0.065693  0.934307
#[Out]# 1883  0.053030  0.946970
#[Out]# 1884  0.107143  0.892857



table.plot(style={'M':'k-','F':'k--'})
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x227b78e6400>
