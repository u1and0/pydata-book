# IPython log file

get_ipython().magic('cd python/pydata-book/ch02')
get_ipython().magic('ls ')
get_ipython().magic('load ipython_log.py')
# %load ipython_log.py
# IPython log file
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










get_ipython().magic('logstart')



