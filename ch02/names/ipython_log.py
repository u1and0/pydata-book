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

fig,axes=plt.subplots(2,1,figsize=(10,8))
letter_prop['M'].plot(kind='bar',rot=0,ax=axes[0],title='Male')
letter_prop['F'].plot(kind='bar',rot=0,ax=axes[1],title='Female',legend=False)
plt.show()
