# %load ipython_log.py
# IPython log file





# __file__________________________
path='./usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()
import json
record=[json.loads(line) for line in open(path)]   #json形式で読み込み
record[0]   #recordの内容は長いのでとりあえず1要素だけ見てみる
record[0]['tz']   #そのうちtzがキーのもの
time_zone=[rec['tz'] for rec in record if 'tz' in rec]   #recordの中のtzだけ見る。ただしtzがあったときのみ
time_zone[:10]   #上から10行目だけを見る






# __tzを数えてディクショナリに格納__________________________
def get_counts(seq):
	'''
		seq内の文字列と同じものが何個あるかをカウントし、ディクショナリ{'文字列':個数,...}として返す
	def get_counts(seq):# これと同じ意味だけどdefaultdict使うと簡単
		count=defaultdict(int)   #count={}
		for x in seq:
			if x in counts:
				counts[x]+=1
			else:
				count[x]=1
			return counts
	'''
	from collections import defaultdict
	counts=defaultdict(int)   #returns `defaultdict(<class 'int'>, {})`
	for x in seq:
		counts[x]+=1
	return counts

counts=get_counts(time_zone)
counts['America/New_York']
len(time_zone)











# __top10を探す__________________________
##__関数作る__________________________
def top_counts(count_dict,n=10):
	value_key_pairs=[(count,tz) for tz, count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:]

top_counts(counts)


## __class使う__________________________
from collections import Counter
counts= Counter(time_zone)
counts.most_common(10)


## __pandas使う__________________________
from pandas import DataFrame,Series
import pandas as pd
frame=DataFrame(record)
frame['tz'][:10]
tz_counts=frame['tz'].value_counts()
tz_counts[:10]





# __NAの補完__________________________
clean_tz=frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='UNknown'
clean_tz
tz_counts=clean_tz.value_counts()
tz_counts[:10]




# __2016/07/28 15:55:54__________________________


# __tz_countのPLOT__________________________ 
tz_counts[:10].plot(kind='barh',rot=0)
import matplotlib.pyplot as plt
# plt.show()



# __要素数カウント__________________________
frame['a'][1]
frame['a'][50]
frame['a'][51]
results=Series([x.split()[0] for x in frame.a.dropna()])   #.dropna() pandasメソッド　空白行を削除　引数で削除する行指定
   #str.split(x) xを区切り文字にしてstrを分割してリストに収める
   #空白で区切った文字列をリストに収めて(リスト内法表記)、Seriesクラスでpandas dataframeにする
results[:5]
results.value_counts()[:8]   #value_counts()で同じ要素の数を数える


## __要素数カウント(別の方法)__________________________
cframe=frame[frame.a.notnull()]   #frameのa列のnullじゃない奴だけ集めた(cframe['a']==frame.a.dropna())
bool(map(list,[cframe['a'],frame.a.dropna()]))   #list関数をcframe['a']とframe.a.dropna()に適用させて同じかどうか見る





# __'Windows' or Not?__________________________
import numpy as np
operating_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')   #cframe['a']が'Windows'という文字を含む　Trueで'Windows'　falseで'Not Windows'を返す
   #` ['Windows' if 'Windows' in x else 'Not Windows' for x in cframe['a']]`と同じ
operating_system[:5]


## __operating_system Another Way__________________________
operating_system2=['Windows' if 'Windows' in x else 'Not Windows' for x in cframe['a']]
bool(list(operating_system)==operating_system2)   #True


by_tz_os=cframe.groupby(['tz',operating_system])
agg_counts=by_tz_os.size().unstack().fillna(0)
agg_counts[:10]



																	# __2016/07/28 22:56:30__
indexer=agg_counts.sum(1).argsort()   #argsort()ソート後のインデックスをnp.array形式で返す
   #np.sum() 基本的に、arrayの中身全部足したやつ返す

'''
# ABOUT np.sum()

>>> np.sum([[0, 1], [0, 5]], axis=0)
array([0, 6])   #return array([0+0],[1+5])
>>> np.sum([[0, 1], [0, 5]], axis=1)
array([1, 5])   #return array([0+1],[0+5])

'''

indexer[:10]


count_subset=agg_counts.take(indexer)[-10:]   #indexerの最後から10分だけのagg_countsを返す(take=取得する)

count_subset.plot(kind='barh', stacked=True)
# plt.show()


# __正規化(終端が 0,1つまり比率を示す)__________________________
normed_subset=count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)
# plt.show()





# __2016/07/29 8:46:25__________________________












