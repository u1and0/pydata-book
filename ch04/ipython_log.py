# IPython log file
# NumPy Basics: Arrays and Vectorized__________________________ 
Computation
from __future__ import division
from numpy.random import randn



## The NumPy ndarray: A Multidimensional Array Object__________________________ 

### 乱数生成されたarrayの計算__________________________
data=randn(2,3)
data
#[Out]# array([[-1.0343, -0.6674, -0.663 ],
#[Out]#        [ 0.4376, -0.403 ,  0.9471]])

data*10
#[Out]# array([[-10.343 ,  -6.6736,  -6.63  ],
#[Out]#        [  4.3762,  -4.0305,   9.4713]])

data+data
#[Out]# array([[-2.0686, -1.3347, -1.326 ],
#[Out]#        [ 0.8752, -0.8061,  1.8943]])

### data*2==data+dataは同じ？__________________________ 
# bool(data*2==data+data)   # <<<Error
np.allclose(data*2,data+data)   #data*2とdata+dataが同じか判断するときはallclose使うんだったね
#[Out]# True


### dataの形の確認__________________________ 
data.shape
#[Out]# (2, 3)
data.dtype
#[Out]# dtype('float64')








## Creating ndarrays__________________________
data1=[6,7.5,8,0,1]
data1
#[Out]# [6, 7.5, 8, 0, 1]


## array化__________________________
arr1=np.array(data1)   #リストをアレイ化(メソッド)
arr1
#[Out]# array([ 6. ,  7.5,  8. ,  0. ,  1. ])

np.asarray(data1)   # #リストをアレイ化(関数)
#[Out]# array([ 6. ,  7.5,  8. ,  0. ,  1. ])

data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
arr
arr2
#[Out]# array([[1, 2, 3, 4],
#[Out]#        [5, 6, 7, 8]])

### 次元・型の確認__________________________
arr2.ndim
#[Out]# 2
arr2.shape
#[Out]# (2, 4)
arr1.dtype
#[Out]# dtype('float64')
arr2.dtype
#[Out]# dtype('int32')




### 空のarrayを作るときはnp.zeroかnp.empty__________________________ 
np.zeros(10)
#[Out]# array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
np.zeros((3,6))
#[Out]# array([[ 0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.]])
np.empty((2,3,2))
#[Out]# array([[[ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.]],
#[Out]# 
#[Out]#        [[ 0.,  0.],
#[Out]#         [ 0.,  0.],
#[Out]#         [ 0.,  0.]]])


empty_unit32=np.empty(8,dtype='u4')
empty_unit32
#[Out]# array([1, 1, 1, 1, 1, 1, 1, 1], dtype=uint32)
empty_unit32=np.empty(8,dtype='f2')
empty_unit32
#[Out]# array([   0.  ,  249.25,    0.  ,    0.  ,    0.  ,  249.25,    0.  ,    0.  ], dtype=float16)
empty_unit32=np.empty(8,dtype='i8')
empty_unit32
#[Out]# array([0, 0, 0, 0, 0, 0, 0, 0], dtype=int64)






### range関数はイテレータを返すのに対してarange関数はarrayを返す__________________________ 
np.arange(15)
#Out# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])





### 引数を全部0か1にしたarrayを返す__________________________ 
np.ones(data1)
#[Out]# array([], shape=(6, 7, 8, 0, 1), dtype=float64)
np.ones_like(data1)
#[Out]# array([ 1.,  1.,  1.,  1.,  1.])
np.zeros_like(data1)
#[Out]# array([ 0.,  0.,  0.,  0.,  0.])




### 行列そろっていないとダメっぽい__________________________ 
np.zeros_like([3,3,3,2],[3,4,6])
np.zeros_like([3,3,3],[3,4,6])
np.zeros_like([[3,3,3],[3,4,6]])
#[Out]# array([[0, 0, 0],
#[Out]#        [0, 0, 0]])
np.zeros_like([[3,3,3,2],[3,4,6]])
#[Out]# array([0, 0], dtype=object)





### NxM行列の単位行列の作成　 kがつくとk列分左右に1を移動__________________________ 
np.eye(8,9)
#[Out]# array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.]])
np.eye(8,9,dtype=int,k=1)
#[Out]# array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 1, 0, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 0, 1, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 0, 0, 1, 0, 0, 0, 0],
#[Out]#        [0, 0, 0, 0, 0, 1, 0, 0, 0],
#[Out]#        [0, 0, 0, 0, 0, 0, 1, 0, 0],
#[Out]#        [0, 0, 0, 0, 0, 0, 0, 1, 0],
#[Out]#        [0, 0, 0, 0, 0, 0, 0, 0, 1]])
np.eye(8,9,dtype=int,k=-3)
#[Out]# array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#[Out]#        [1, 0, 0, 0, 0, 0, 0, 0, 0],
#[Out]#        [0, 1, 0, 0, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 1, 0, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 0, 1, 0, 0, 0, 0, 0],
#[Out]#        [0, 0, 0, 0, 1, 0, 0, 0, 0]])




















## Data Types for ndarrays__________________________
arr=np.array([1,2,3,4,5])
arr.dtype
#[Out]# dtype('int32')

float_arr=arr.astype(np.float64)
float_arr
#[Out]# array([ 1.,  2.,  3.,  4.,  5.])

float_arr.dtype
#[Out]# dtype('float64')

arr=np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
#[Out]# array([  3.7,  -1.2,  -2.6,   0.5,  12.9,  10.1])

arr.astype(np.int32)   # int型にするため少数点以下切り捨て
#[Out]# array([ 3, -1, -2,  0, 12, 10])








### 文字列で作ったarrayもastype使えばintにもfloatにもなれる__________________________ 
numeric_stringd=np.array(['1.25','-9.6','42'],dtype=np.string_)
numeric_stringd
#[Out]# array([b'1.25', b'-9.6', b'42'], 
#[Out]#       dtype='|S4')
numeric_stringd.astype(float)
#[Out]# array([  1.25,  -9.6 ,  42.  ])



### calibersのdtypeに合わせるdtypeメソッド__________________________ 
int_array=np.arange(10)
calibers=np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)

int_array.astype(calibers.dtype)   # astypeは新しいarray(arrayのコピーを作成する)
#[Out]# array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
int_array
#[Out]# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
int_array.astype(calibers.dtype)
#[Out]# array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])








## Operations between Arrays and Scalars__________________________ 
arr=np.array([[1., 2., 3.], [4., 5., 6.]])
arr
#[Out]# array([[ 1.,  2.,  3.],
#[Out]#        [ 4.,  5.,  6.]])

### array同士の計算は要素ごとに行われる__________________________ 
arr*arr
#[Out]# array([[  1.,   4.,   9.],
#[Out]#        [ 16.,  25.,  36.]])
arr-arr
#[Out]# array([[ 0.,  0.,  0.],
#[Out]#        [ 0.,  0.,  0.]])

### arrayとスカラーの計算はすべての要素に適用される__________________________
1/arr
#[Out]# array([[ 1.    ,  0.5   ,  0.3333],
#[Out]#        [ 0.25  ,  0.2   ,  0.1667]])
arr**0.5   
#[Out]# array([[ 1.    ,  1.4142,  1.7321],
#[Out]#        [ 2.    ,  2.2361,  2.4495]])








## Basic Indexing and Slicing__________________________ 
arr=np.arange(10)
arr
#[Out]# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[5]
#[Out]# 5

arr[5:8]
#[Out]# array([5, 6, 7])

arr[5:8]
#[Out]# array([5, 6, 7])

arr[5:8]=12   # arrの5-7要素目を12に変える
arr
#[Out]# array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])


### リストで同じことをしようとすると__________________________
x=list(range(10))
x
#[Out]# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x[5:8]
#[Out]# [5, 6, 7]

x[5:8]=12
#[Out]# Error

x[5:8]=[12,12,12]   ##python標準リストだとこのように書かないとできない
x
#[Out]# [0, 1, 2, 3, 4, 12, 12, 12, 8, 9]




### arr_sliceがarrの5-7要素目にジャンプするようになっていて、arr_sliceを変えればarrの5-7要素にも反映される__________________________ 
arr_slice=arr[5:8]
arr_slice[1]=12345
arr
#[Out]# array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,     9])
arr_slice[:]=64
arr
#[Out]# array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])




### N次元array__________________________ 
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
#[Out]# array([7, 8, 9])

arr2d[0][2]   # n次元配列のアクセス
#[Out]# 3

arr2d[0,2]   # これでも同じアクセス
#[Out]# 3

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d
#[Out]# array([[[ 1,  2,  3],
#[Out]#         [ 4,  5,  6]],
#[Out]# 
#[Out]#        [[ 7,  8,  9],
#[Out]#         [10, 11, 12]]])

arr3d[0]
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])




## np.copy()関数でコピーする__________________________
old_values=arr3d[0].copy()
arr3d
#[Out]# array([[[ 1,  2,  3],
#[Out]#         [ 4,  5,  6]],
#[Out]# 
#[Out]#        [[ 7,  8,  9],
#[Out]#         [10, 11, 12]]])
arr3d[0]=43
arr3d[0]
#[Out]# array([[43, 43, 43],
#[Out]#        [43, 43, 43]])
arr3d
#[Out]# array([[[43, 43, 43],
#[Out]#         [43, 43, 43]],
#[Out]# 
#[Out]#        [[ 7,  8,  9],
#[Out]#         [10, 11, 12]]])

arr3d[0]=old_values   #old_value入れれば元に戻る
arr3d
#[Out]# array([[[ 1,  2,  3],
#[Out]#         [ 4,  5,  6]],
#[Out]# 
#[Out]#        [[ 7,  8,  9],
#[Out]#         [10, 11, 12]]])

arr3d[1,0]
#[Out]# array([7, 8, 9])















### Indexing with slices__________________________ 
### 高次元アレイのスライスいろいろ__________________________ 
arr[1:6]
#[Out]# array([ 1,  2,  3,  4, 64])

arr2d
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])

arr2d[:2]
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])

arr2d[:2,1:]
#[Out]# array([[2, 3],
#[Out]#        [5, 6]])

arr2d[1,:2]
#[Out]# array([4, 5])

arr2d[2,:1]
#[Out]# array([7])

arr2d[:,:1]   # :のみだと全要素をスライシング
#[Out]# array([[1],
#[Out]#        [4],
#[Out]#        [7]])

## 要素の変更 with slicing__________________________ 
arr2d[:2,1:]=0
arr2d
#[Out]# array([[1, 0, 0],
#[Out]#        [4, 0, 0],
#[Out]#        [7, 8, 9]])












## Boolean Indexing__________________________ 
names=np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data=randn(7,4)

names
#[Out]# array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], 
#[Out]#       dtype='<U4')

data
#[Out]# array([[-0.7601,  0.3894, -0.0167,  0.7664],
#[Out]#        [-0.0372,  0.339 ,  2.1351, -0.028 ],
#[Out]#        [ 0.659 , -0.9057,  0.0155,  0.1909],
#[Out]#        [-0.5999, -1.1038,  1.6584, -2.1756],
#[Out]#        [ 1.3238, -0.3191, -1.0407,  0.0837],
#[Out]#        [ 0.3411,  0.0639, -0.4442,  0.7177],
#[Out]#        [ 0.4036,  0.8886, -0.2347,  1.4748]])

names=='Bob'
#[Out]# array([ True, False, False,  True, False, False, False], dtype=bool)

data[names=='Bob']   # Trueとなったdataのarrayの行だけ抜き出し
#[Out]# array([[-0.7601,  0.3894, -0.0167,  0.7664],
#[Out]#        [-0.5999, -1.1038,  1.6584, -2.1756]])

data[names=='Bob',3]   # 各行の3要素目だけ
#[Out]# array([ 0.7664, -2.1756])

names!='Bob'
#[Out]# array([False,  True,  True, False,  True,  True,  True], dtype=bool)

data[-(names=='Bob')]   # "!="や"-"は否定
#[Out]# array([[-0.0372,  0.339 ,  2.1351, -0.028 ],
#[Out]#        [ 0.659 , -0.9057,  0.0155,  0.1909],
#[Out]#        [ 1.3238, -0.3191, -1.0407,  0.0837],
#[Out]#        [ 0.3411,  0.0639, -0.4442,  0.7177],
#[Out]#        [ 0.4036,  0.8886, -0.2347,  1.4748]])

mask=(names=='Bob')|(names=='Will')   # BobかWillならTrue
mask
#[Out]# array([ True, False,  True,  True,  True, False, False], dtype=bool)

data[mask]
#[Out]# array([[-0.7601,  0.3894, -0.0167,  0.7664],
#[Out]#        [ 0.659 , -0.9057,  0.0155,  0.1909],
#[Out]#        [-0.5999, -1.1038,  1.6584, -2.1756],
#[Out]#        [ 1.3238, -0.3191, -1.0407,  0.0837]])

data[data<0]=0   # 負の要素は0に直す
data
#[Out]# array([[ 0.    ,  0.3894,  0.    ,  0.7664],
#[Out]#        [ 0.    ,  0.339 ,  2.1351,  0.    ],
#[Out]#        [ 0.659 ,  0.    ,  0.0155,  0.1909],
#[Out]#        [ 0.    ,  0.    ,  1.6584,  0.    ],
#[Out]#        [ 1.3238,  0.    ,  0.    ,  0.0837],
#[Out]#        [ 0.3411,  0.0639,  0.    ,  0.7177],
#[Out]#        [ 0.4036,  0.8886,  0.    ,  1.4748]])

data[names!='Joe']=7   # Joe以外の0,2,3,4行目の要素は7に変わる
data
#[Out]# array([[ 7.    ,  7.    ,  7.    ,  7.    ],
#[Out]#        [ 0.    ,  0.339 ,  2.1351,  0.    ],
#[Out]#        [ 7.    ,  7.    ,  7.    ,  7.    ],
#[Out]#        [ 7.    ,  7.    ,  7.    ,  7.    ],
#[Out]#        [ 7.    ,  7.    ,  7.    ,  7.    ],
#[Out]#        [ 0.3411,  0.0639,  0.    ,  0.7177],
#[Out]#        [ 0.4036,  0.8886,  0.    ,  1.4748]])
