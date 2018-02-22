

```python
# http://pandas.pydata.org/pandas-docs/stable/advanced.html
# MultiIndex / Advanced Indexing
# pandas 0.22.0 
```


```python
import pandas as pd
import numpy as np
import random; random.shuffle(tuples)
```


```python
# Hierarchical indexing (MultiIndex)  分层索引 多重索引

# 创建多重索引对象，如同标准的索引类，他们存放轴axis标签labels
# 创建方式：
# from a list of arrays -- using MultiIndex.from_arrays
# from an array of tuples -- using MultiIndex.from_tuples
# from a crossed set of iterables -- using MultiIndex.from_product 

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
arrays
# *arrays
zip(*arrays)  # 这里的* 是“解开”list ， list[0] list[1] ……
list(zip(*arrays))
list(zip(arrays[0], arrays[1]))
tuples = list(zip(*arrays))
tuples
```




    [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
     ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]






    <zip at 0xf96f888>






    [('bar', 'one'),
     ('bar', 'two'),
     ('baz', 'one'),
     ('baz', 'two'),
     ('foo', 'one'),
     ('foo', 'two'),
     ('qux', 'one'),
     ('qux', 'two')]






    [('bar', 'one'),
     ('bar', 'two'),
     ('baz', 'one'),
     ('baz', 'two'),
     ('foo', 'one'),
     ('foo', 'two'),
     ('qux', 'one'),
     ('qux', 'two')]






    [('bar', 'one'),
     ('bar', 'two'),
     ('baz', 'one'),
     ('baz', 'two'),
     ('foo', 'one'),
     ('foo', 'two'),
     ('qux', 'one'),
     ('qux', 'two')]




```python
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index
```




    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
               labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
               names=['first', 'second'])




```python
s = pd.Series(np.random.randn(8), index=index)
s
```




    first  second
    bar    one       0.271000
           two      -1.276230
    baz    one      -1.018103
           two      -0.620292
    foo    one       1.008070
           two       0.759145
    qux    one      -2.141050
           two      -0.927688
    dtype: float64




```python
# 更简洁的方式, 当每个元素对都来自于可迭代对象时
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]  # 创建了与上面相同的index
pd.MultiIndex.from_product(iterables, names=['first', 'second'])  # 多重索引可以接受命名，默认为None
```




    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
               labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
               names=['first', 'second'])




```python
# 也可以直接在创建df或series时传入矩阵array 的 列表list
arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
          np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]
arrays  
```




    [array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
           dtype='<U3'),
     array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'],
           dtype='<U3')]




```python
s = pd.Series(np.random.randn(8), index=arrays)
s
```




    bar  one    0.817791
         two    0.510420
    baz  one   -0.494160
         two   -0.529997
    foo  one    0.641282
         two   -0.202762
    qux  one    0.050320
         two    2.097300
    dtype: float64




```python
df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>-2.090989</td>
      <td>0.001052</td>
      <td>1.467637</td>
      <td>0.267938</td>
    </tr>
    <tr>
      <th>two</th>
      <td>1.224610</td>
      <td>0.851894</td>
      <td>0.765531</td>
      <td>-0.505116</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>1.444246</td>
      <td>-0.247795</td>
      <td>0.267462</td>
      <td>-0.945641</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.836046</td>
      <td>0.274732</td>
      <td>0.530525</td>
      <td>-0.560081</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-3.709465</td>
      <td>-0.157089</td>
      <td>0.608778</td>
      <td>-0.003217</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.848818</td>
      <td>1.478306</td>
      <td>-0.389401</td>
      <td>-1.205956</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">qux</th>
      <th>one</th>
      <td>-1.069775</td>
      <td>1.272440</td>
      <td>-0.797613</td>
      <td>-0.194223</td>
    </tr>
    <tr>
      <th>two</th>
      <td>1.597218</td>
      <td>0.454815</td>
      <td>-0.756022</td>
      <td>0.481038</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 可以对不同的轴向（如行索引/行名或列索引/列名）设置
df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>first</th>
      <th colspan="2" halign="left">bar</th>
      <th colspan="2" halign="left">baz</th>
      <th colspan="2" halign="left">foo</th>
      <th colspan="2" halign="left">qux</th>
    </tr>
    <tr>
      <th>second</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>-0.007312</td>
      <td>1.048244</td>
      <td>-0.029907</td>
      <td>-0.437866</td>
      <td>-1.853398</td>
      <td>2.026875</td>
      <td>0.359521</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.272366</td>
      <td>-0.530191</td>
      <td>-0.689641</td>
      <td>-0.244362</td>
      <td>-1.476252</td>
      <td>0.818493</td>
      <td>0.353771</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>1.862253</td>
      <td>-0.118297</td>
      <td>-0.148326</td>
      <td>1.147616</td>
      <td>-1.389965</td>
      <td>0.817716</td>
      <td>0.787394</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 同时对两个方向设置index，注意index的长度与数据在不同方向上的长度
pd.DataFrame(np.random.randn(6, 6), index=index[:6], columns=index[:6])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>first</th>
      <th colspan="2" halign="left">bar</th>
      <th colspan="2" halign="left">baz</th>
      <th colspan="2" halign="left">foo</th>
    </tr>
    <tr>
      <th></th>
      <th>second</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>0.020204</td>
      <td>-0.549089</td>
      <td>0.381830</td>
      <td>0.326558</td>
      <td>-1.420590</td>
      <td>-1.551863</td>
    </tr>
    <tr>
      <th>two</th>
      <td>1.311775</td>
      <td>2.294908</td>
      <td>0.203981</td>
      <td>1.381199</td>
      <td>-0.743387</td>
      <td>2.119027</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>0.640856</td>
      <td>1.089627</td>
      <td>-1.463503</td>
      <td>0.727607</td>
      <td>-0.959549</td>
      <td>-0.037316</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.906859</td>
      <td>-0.720702</td>
      <td>0.862614</td>
      <td>0.082066</td>
      <td>0.209276</td>
      <td>-0.391039</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.328704</td>
      <td>-1.015117</td>
      <td>0.279826</td>
      <td>0.141166</td>
      <td>-0.053601</td>
      <td>-1.171920</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.342074</td>
      <td>-0.196049</td>
      <td>-0.387946</td>
      <td>0.196228</td>
      <td>-1.264932</td>
      <td>0.144251</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.Series(np.random.randn(8), index=tuples)  # 多重索引，相当于元组index
```




    (bar, one)   -0.267177
    (bar, two)   -0.239632
    (baz, one)    1.212249
    (baz, two)    0.289517
    (foo, one)    1.311922
    (foo, two)   -0.797733
    (qux, one)   -1.395485
    (qux, two)   -0.451327
    dtype: float64




```python
# 可以控制索引的显示方式，通过在 pandas.set_options() 设置 multi_sparse 选项
pd.set_option('display.multi_sparse', False)
df
pd.set_option('display.multi_sparse', True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>first</th>
      <th>bar</th>
      <th>bar</th>
      <th>baz</th>
      <th>baz</th>
      <th>foo</th>
      <th>foo</th>
      <th>qux</th>
      <th>qux</th>
    </tr>
    <tr>
      <th>second</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>-0.007312</td>
      <td>1.048244</td>
      <td>-0.029907</td>
      <td>-0.437866</td>
      <td>-1.853398</td>
      <td>2.026875</td>
      <td>0.359521</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.272366</td>
      <td>-0.530191</td>
      <td>-0.689641</td>
      <td>-0.244362</td>
      <td>-1.476252</td>
      <td>0.818493</td>
      <td>0.353771</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>1.862253</td>
      <td>-0.118297</td>
      <td>-0.148326</td>
      <td>1.147616</td>
      <td>-1.389965</td>
      <td>0.817716</td>
      <td>0.787394</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>first</th>
      <th colspan="2" halign="left">bar</th>
      <th colspan="2" halign="left">baz</th>
      <th colspan="2" halign="left">foo</th>
      <th colspan="2" halign="left">qux</th>
    </tr>
    <tr>
      <th>second</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>-0.007312</td>
      <td>1.048244</td>
      <td>-0.029907</td>
      <td>-0.437866</td>
      <td>-1.853398</td>
      <td>2.026875</td>
      <td>0.359521</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.272366</td>
      <td>-0.530191</td>
      <td>-0.689641</td>
      <td>-0.244362</td>
      <td>-1.476252</td>
      <td>0.818493</td>
      <td>0.353771</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>1.862253</td>
      <td>-0.118297</td>
      <td>-0.148326</td>
      <td>1.147616</td>
      <td>-1.389965</td>
      <td>0.817716</td>
      <td>0.787394</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reconstructing the level labels 重建层级标签
# The method get_level_values will return a vector of the labels for each location at a particular level:
# get_level_values 方法返回指定层级的标签向量
index.get_level_values(0)  # 使用整数序号
index.get_level_values("second")  # 使用name
```




    Index(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], dtype='object', name='first')






    Index(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'], dtype='object', name='second')




```python
# Basic indexing on axis with MultiIndex # 在轴方向的基础索引
df['bar']
df['bar', 'one']
df['bar']['one']  # 不建议使用，链式
s['qux']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>second</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>-0.007312</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.272366</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>1.862253</td>
    </tr>
  </tbody>
</table>
</div>






    A   -1.608162
    B    1.207609
    C   -0.369463
    Name: (bar, one), dtype: float64






    A   -1.608162
    B    1.207609
    C   -0.369463
    Name: one, dtype: float64






    one    0.05032
    two    2.09730
    dtype: float64




```python
# Defined Levels 指定层级
df.columns  # 原index
df[['foo','qux']].columns  # 切片后的结果，层级levels中的项目没有减少，labels减少了
# 这样做避免了重新计算层级，使切片保持高效
```




    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
               labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
               names=['first', 'second'])






    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
               labels=[[2, 2, 3, 3], [0, 1, 0, 1]],
               names=['first', 'second'])




```python
# 查看切片实际选择levels
df[['foo','qux']].columns.values
df[['foo','qux']].columns.get_level_values(0)  # 指定层级
```




    array([('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('qux', 'two')],
          dtype=object)






    Index(['foo', 'foo', 'qux', 'qux'], dtype='object', name='first')




```python
# 用有效的used层级重建多重索引
df[['foo','qux']].columns.remove_unused_levels()
```




    MultiIndex(levels=[['foo', 'qux'], ['one', 'two']],
               labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
               names=['first', 'second'])




```python
# Data alignment and using reindex 数据定位和使用reindex
s
```




    bar  one    0.817791
         two    0.510420
    baz  one   -0.494160
         two   -0.529997
    foo  one    0.641282
         two   -0.202762
    qux  one    0.050320
         two    2.097300
    dtype: float64




```python
# 当两个index不同的对象计算时与一般的index一样
s + s[:-2]
s + s[::2]
```




    bar  one    1.635582
         two    1.020840
    baz  one   -0.988319
         two   -1.059993
    foo  one    1.282563
         two   -0.405523
    qux  one         NaN
         two         NaN
    dtype: float64






    bar  one    1.635582
         two         NaN
    baz  one   -0.988319
         two         NaN
    foo  one    1.282563
         two         NaN
    qux  one    0.100640
         two         NaN
    dtype: float64




```python
# reindex 可以被另外一个 multiindex 或者 元组的list 或 array 调用
index
index[:3]
s.reindex(index[:3])
s.reindex([('foo', 'two'), ('bar', 'one'), ('qux', 'one'), ('baz', 'one')])
```




    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
               labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
               names=['first', 'second'])






    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
               labels=[[0, 0, 1], [0, 1, 0]],
               names=['first', 'second'])






    first  second
    bar    one       0.817791
           two       0.510420
    baz    one      -0.494160
    dtype: float64






    foo  two   -0.202762
    bar  one    0.817791
    qux  one    0.050320
    baz  one   -0.494160
    dtype: float64




```python
# Advanced indexing with hierarchical index
# 使用层次索引的高级索引方法
df = df.T
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>-1.608162</td>
      <td>1.207609</td>
      <td>-0.369463</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.007312</td>
      <td>-0.272366</td>
      <td>1.862253</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>1.048244</td>
      <td>-0.530191</td>
      <td>-0.118297</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.029907</td>
      <td>-0.689641</td>
      <td>-0.148326</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.437866</td>
      <td>-0.244362</td>
      <td>1.147616</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.853398</td>
      <td>-1.476252</td>
      <td>-1.389965</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">qux</th>
      <th>one</th>
      <td>2.026875</td>
      <td>0.818493</td>
      <td>0.817716</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.359521</td>
      <td>0.353771</td>
      <td>0.787394</td>
    </tr>
  </tbody>
</table>
</div>




```python
# .loc 定位
df.loc["bar"]
df.loc["bar", "two"]  # 返回了一个series（不是一行，而是“一列”），其索引是原df的列名
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>-1.608162</td>
      <td>1.207609</td>
      <td>-0.369463</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.007312</td>
      <td>-0.272366</td>
      <td>1.862253</td>
    </tr>
  </tbody>
</table>
</div>






    A   -0.007312
    B   -0.272366
    C    1.862253
    Name: (bar, two), dtype: float64




```python
# loc 中使用切片，切片的值可以是元组
df.loc['baz':'foo']
df.loc[('baz', 'two'):('qux', 'one')]
df.loc[('baz', 'two'):'foo']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>1.048244</td>
      <td>-0.530191</td>
      <td>-0.118297</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.029907</td>
      <td>-0.689641</td>
      <td>-0.148326</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.437866</td>
      <td>-0.244362</td>
      <td>1.147616</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.853398</td>
      <td>-1.476252</td>
      <td>-1.389965</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baz</th>
      <th>two</th>
      <td>-0.029907</td>
      <td>-0.689641</td>
      <td>-0.148326</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.437866</td>
      <td>-0.244362</td>
      <td>1.147616</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.853398</td>
      <td>-1.476252</td>
      <td>-1.389965</td>
    </tr>
    <tr>
      <th>qux</th>
      <th>one</th>
      <td>2.026875</td>
      <td>0.818493</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baz</th>
      <th>two</th>
      <td>-0.029907</td>
      <td>-0.689641</td>
      <td>-0.148326</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.437866</td>
      <td>-0.244362</td>
      <td>1.147616</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.853398</td>
      <td>-1.476252</td>
      <td>-1.389965</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 可以给loc传入元组或标签列表，取得不连续的索引
df.loc[[('bar', 'two'), ('qux', 'one')]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <th>two</th>
      <td>-0.007312</td>
      <td>-0.272366</td>
      <td>1.862253</td>
    </tr>
    <tr>
      <th>qux</th>
      <th>one</th>
      <td>2.026875</td>
      <td>0.818493</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Using slicers 使用切片
# 可以用多重索引对象进行切片。可以用 切片值、 标签或标签列表、 布尔索引等选择器
# 可以用slice(None) 选择那一级的所有的内容。不用特别指定所有深度的级别，他们默认是slice(None)
# 注意：使用loc应该规定所有的轴方向，包括行index和列columns。
# 推荐方式：df.loc[(slice('A1','A3'),.....), :]   注意 冒号前面的逗号，逗号前表示行方向切片（选择器），逗号后面表示列方向切片（选择器）
# 不推荐：  df.loc[(slice('A1','A3'),.....)]  可能产生歧义
```


```python
def mklbl(prefix, n):
    # mklbl("a", 3) --> ['a0', 'a1', 'a2']
    return ["%s%s" % (prefix, i) for i in range(n)]
```


```python
mklbl("a", 3)
```




    ['a0', 'a1', 'a2']




```python
miindex = pd.MultiIndex.from_product([mklbl('A',4),
                                      mklbl('B',2),
                                      mklbl('C',4),
                                      mklbl('D',2)])
miindex  # 由列表生成4重（4级）索引对象，共生成4*2*4*2=64行
```




    MultiIndex(levels=[['A0', 'A1', 'A2', 'A3'], ['B0', 'B1'], ['C0', 'C1', 'C2', 'C3'], ['D0', 'D1']],
               labels=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]])




```python
micolumns = pd.MultiIndex.from_tuples([('a','foo'),('a','bar'),
                                       ('b','foo'),('b','bah')],
                                      names=['lvl0', 'lvl1'])
micolumns  # 由元组生成2重索引对象，共4行，并对2重（两级）分别命名
```




    MultiIndex(levels=[['a', 'b'], ['bah', 'bar', 'foo']],
               labels=[[0, 0, 1, 1], [2, 1, 2, 0]],
               names=['lvl0', 'lvl1'])




```python
row_l = len(miindex)
col_l = len(micolumns)
dfmi = pd.DataFrame(np.arange(row_l * col_l).reshape((row_l, col_l)),
                        index=miindex,
                        columns=micolumns).sort_index().sort_index(axis=1)
dfmi 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="16" valign="top">A0</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>5</td>
      <td>4</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>9</td>
      <td>8</td>
      <td>11</td>
      <td>10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>13</td>
      <td>12</td>
      <td>15</td>
      <td>14</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>17</td>
      <td>16</td>
      <td>19</td>
      <td>18</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>21</td>
      <td>20</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>25</td>
      <td>24</td>
      <td>27</td>
      <td>26</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>29</td>
      <td>28</td>
      <td>31</td>
      <td>30</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>33</td>
      <td>32</td>
      <td>35</td>
      <td>34</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>37</td>
      <td>36</td>
      <td>39</td>
      <td>38</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>41</td>
      <td>40</td>
      <td>43</td>
      <td>42</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>45</td>
      <td>44</td>
      <td>47</td>
      <td>46</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>49</td>
      <td>48</td>
      <td>51</td>
      <td>50</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>53</td>
      <td>52</td>
      <td>55</td>
      <td>54</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>57</td>
      <td>56</td>
      <td>59</td>
      <td>58</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>61</td>
      <td>60</td>
      <td>63</td>
      <td>62</td>
    </tr>
    <tr>
      <th rowspan="14" valign="top">A1</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>65</td>
      <td>64</td>
      <td>67</td>
      <td>66</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>69</td>
      <td>68</td>
      <td>71</td>
      <td>70</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>73</td>
      <td>72</td>
      <td>75</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>77</td>
      <td>76</td>
      <td>79</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>81</td>
      <td>80</td>
      <td>83</td>
      <td>82</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>85</td>
      <td>84</td>
      <td>87</td>
      <td>86</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>89</td>
      <td>88</td>
      <td>91</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>93</td>
      <td>92</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>97</td>
      <td>96</td>
      <td>99</td>
      <td>98</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>101</td>
      <td>100</td>
      <td>103</td>
      <td>102</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>105</td>
      <td>104</td>
      <td>107</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>109</td>
      <td>108</td>
      <td>111</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>113</td>
      <td>112</td>
      <td>115</td>
      <td>114</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>117</td>
      <td>116</td>
      <td>119</td>
      <td>118</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="14" valign="top">A2</th>
      <th rowspan="6" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>137</td>
      <td>136</td>
      <td>139</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>141</td>
      <td>140</td>
      <td>143</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>145</td>
      <td>144</td>
      <td>147</td>
      <td>146</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>149</td>
      <td>148</td>
      <td>151</td>
      <td>150</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>153</td>
      <td>152</td>
      <td>155</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>157</td>
      <td>156</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>161</td>
      <td>160</td>
      <td>163</td>
      <td>162</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>165</td>
      <td>164</td>
      <td>167</td>
      <td>166</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>169</td>
      <td>168</td>
      <td>171</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>173</td>
      <td>172</td>
      <td>175</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>177</td>
      <td>176</td>
      <td>179</td>
      <td>178</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>181</td>
      <td>180</td>
      <td>183</td>
      <td>182</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>185</td>
      <td>184</td>
      <td>187</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>189</td>
      <td>188</td>
      <td>191</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="16" valign="top">A3</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>193</td>
      <td>192</td>
      <td>195</td>
      <td>194</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>197</td>
      <td>196</td>
      <td>199</td>
      <td>198</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>201</td>
      <td>200</td>
      <td>203</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>205</td>
      <td>204</td>
      <td>207</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>209</td>
      <td>208</td>
      <td>211</td>
      <td>210</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>213</td>
      <td>212</td>
      <td>215</td>
      <td>214</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>217</td>
      <td>216</td>
      <td>219</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>221</td>
      <td>220</td>
      <td>223</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>225</td>
      <td>224</td>
      <td>227</td>
      <td>226</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>229</td>
      <td>228</td>
      <td>231</td>
      <td>230</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>233</td>
      <td>232</td>
      <td>235</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>237</td>
      <td>236</td>
      <td>239</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>241</td>
      <td>240</td>
      <td>243</td>
      <td>242</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>245</td>
      <td>244</td>
      <td>247</td>
      <td>246</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>249</td>
      <td>248</td>
      <td>251</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>253</td>
      <td>252</td>
      <td>255</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
<p>64 rows × 4 columns</p>
</div>




```python
# Basic multi-index slicing using slices, lists, and labels.
dfmi.loc[(slice('A1','A3'), slice(None), ['C1', 'C3']), :]  # slice('A1','A3') 相当于 ['A1':'A3']
# dfmi.loc[(slice('A1','A3'), slice(None), ['C1', 'C3']) :]  # 错误 冒号前面必须有逗号

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>73</td>
      <td>72</td>
      <td>75</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>77</td>
      <td>76</td>
      <td>79</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>89</td>
      <td>88</td>
      <td>91</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>93</td>
      <td>92</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>105</td>
      <td>104</td>
      <td>107</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>109</td>
      <td>108</td>
      <td>111</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>121</td>
      <td>120</td>
      <td>123</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>125</td>
      <td>124</td>
      <td>127</td>
      <td>126</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A2</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>137</td>
      <td>136</td>
      <td>139</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>141</td>
      <td>140</td>
      <td>143</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>153</td>
      <td>152</td>
      <td>155</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>157</td>
      <td>156</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>169</td>
      <td>168</td>
      <td>171</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>173</td>
      <td>172</td>
      <td>175</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>185</td>
      <td>184</td>
      <td>187</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>189</td>
      <td>188</td>
      <td>191</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A3</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>201</td>
      <td>200</td>
      <td>203</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>205</td>
      <td>204</td>
      <td>207</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>217</td>
      <td>216</td>
      <td>219</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>221</td>
      <td>220</td>
      <td>223</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>233</td>
      <td>232</td>
      <td>235</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>237</td>
      <td>236</td>
      <td>239</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>249</td>
      <td>248</td>
      <td>251</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>253</td>
      <td>252</td>
      <td>255</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>




```python
# You can use a pd.IndexSlice to have a more natural syntax using : 
# rather than using slice(None)
# 使用pd.IndexSlice 可以用冒号 : 代替 slice(None)

idx = pd.IndexSlice
dfmi.loc[idx[:, :, ['C1', 'C3']], idx[:, 'foo']]  # 默认必须是一个元组()来指定关键字，而且全选的话只能使用slice(None)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>foo</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A0</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>12</td>
      <td>14</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>24</td>
      <td>26</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>28</td>
      <td>30</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>40</td>
      <td>42</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>44</td>
      <td>46</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>56</td>
      <td>58</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>60</td>
      <td>62</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>76</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>92</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>104</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>108</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>120</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>124</td>
      <td>126</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A2</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>136</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>140</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>152</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>156</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>168</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>172</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>184</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>188</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A3</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>200</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>204</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>216</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>220</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>232</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>236</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>248</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>252</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 一次执行复杂选取
dfmi.loc['A1', (slice(None), 'foo')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>foo</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>64</td>
      <td>66</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>68</td>
      <td>70</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>76</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>84</td>
      <td>86</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>92</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>96</td>
      <td>98</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>100</td>
      <td>102</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>104</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>108</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>112</td>
      <td>114</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>116</td>
      <td>118</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>120</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>124</td>
      <td>126</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfmi.loc[idx[:, :, ['C1', 'C3']], idx[:, 'foo']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>foo</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A0</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>12</td>
      <td>14</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>24</td>
      <td>26</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>28</td>
      <td>30</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>40</td>
      <td>42</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>44</td>
      <td>46</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>56</td>
      <td>58</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>60</td>
      <td>62</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>76</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>92</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>104</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>108</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>120</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>124</td>
      <td>126</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A2</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>136</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>140</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>152</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>156</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>168</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>172</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>184</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>188</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A3</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>200</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>204</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>216</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>220</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>232</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>236</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>248</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>252</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Using a boolean indexer you can provide selection related to the values. 
# 使用布尔索引
mask = dfmi[('a', 'foo')] > 200
mask
dfmi.loc[idx[mask, :, ['C1', 'C3']], idx[:, 'foo']]
```




    A0  B0  C0  D0    False
                D1    False
            C1  D0    False
                D1    False
            C2  D0    False
                D1    False
            C3  D0    False
                D1    False
        B1  C0  D0    False
                D1    False
            C1  D0    False
                D1    False
            C2  D0    False
                D1    False
            C3  D0    False
                D1    False
    A1  B0  C0  D0    False
                D1    False
            C1  D0    False
                D1    False
            C2  D0    False
                D1    False
            C3  D0    False
                D1    False
        B1  C0  D0    False
                D1    False
            C1  D0    False
                D1    False
            C2  D0    False
                D1    False
                      ...  
    A2  B0  C1  D0    False
                D1    False
            C2  D0    False
                D1    False
            C3  D0    False
                D1    False
        B1  C0  D0    False
                D1    False
            C1  D0    False
                D1    False
            C2  D0    False
                D1    False
            C3  D0    False
                D1    False
    A3  B0  C0  D0    False
                D1    False
            C1  D0    False
                D1     True
            C2  D0     True
                D1     True
            C3  D0     True
                D1     True
        B1  C0  D0     True
                D1     True
            C1  D0     True
                D1     True
            C2  D0     True
                D1     True
            C3  D0     True
                D1     True
    Name: (a, foo), Length: 64, dtype: bool






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>foo</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="7" valign="top">A3</th>
      <th rowspan="3" valign="top">B0</th>
      <th>C1</th>
      <th>D1</th>
      <td>204</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>216</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>220</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>232</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>236</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>248</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>252</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 指定轴参数axis，说明传入的切片在一个轴上
dfmi.loc(axis=0)[:, :, ['C1', 'C3']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A0</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>9</td>
      <td>8</td>
      <td>11</td>
      <td>10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>13</td>
      <td>12</td>
      <td>15</td>
      <td>14</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>25</td>
      <td>24</td>
      <td>27</td>
      <td>26</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>29</td>
      <td>28</td>
      <td>31</td>
      <td>30</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>41</td>
      <td>40</td>
      <td>43</td>
      <td>42</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>45</td>
      <td>44</td>
      <td>47</td>
      <td>46</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>57</td>
      <td>56</td>
      <td>59</td>
      <td>58</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>61</td>
      <td>60</td>
      <td>63</td>
      <td>62</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>73</td>
      <td>72</td>
      <td>75</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>77</td>
      <td>76</td>
      <td>79</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>89</td>
      <td>88</td>
      <td>91</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>93</td>
      <td>92</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>105</td>
      <td>104</td>
      <td>107</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>109</td>
      <td>108</td>
      <td>111</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>121</td>
      <td>120</td>
      <td>123</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>125</td>
      <td>124</td>
      <td>127</td>
      <td>126</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A2</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>137</td>
      <td>136</td>
      <td>139</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>141</td>
      <td>140</td>
      <td>143</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>153</td>
      <td>152</td>
      <td>155</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>157</td>
      <td>156</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>169</td>
      <td>168</td>
      <td>171</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>173</td>
      <td>172</td>
      <td>175</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>185</td>
      <td>184</td>
      <td>187</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>189</td>
      <td>188</td>
      <td>191</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A3</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>201</td>
      <td>200</td>
      <td>203</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>205</td>
      <td>204</td>
      <td>207</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>217</td>
      <td>216</td>
      <td>219</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>221</td>
      <td>220</td>
      <td>223</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>233</td>
      <td>232</td>
      <td>235</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>237</td>
      <td>236</td>
      <td>239</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>249</td>
      <td>248</td>
      <td>251</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>253</td>
      <td>252</td>
      <td>255</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 可以使用这种指定轴方向的方式赋值
df2 = dfmi.copy()
df2.loc(axis=0)[:, :, ['C1', 'C3']] = -10
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="16" valign="top">A0</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>5</td>
      <td>4</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>17</td>
      <td>16</td>
      <td>19</td>
      <td>18</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>21</td>
      <td>20</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>33</td>
      <td>32</td>
      <td>35</td>
      <td>34</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>37</td>
      <td>36</td>
      <td>39</td>
      <td>38</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>49</td>
      <td>48</td>
      <td>51</td>
      <td>50</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>53</td>
      <td>52</td>
      <td>55</td>
      <td>54</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="14" valign="top">A1</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>65</td>
      <td>64</td>
      <td>67</td>
      <td>66</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>69</td>
      <td>68</td>
      <td>71</td>
      <td>70</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>81</td>
      <td>80</td>
      <td>83</td>
      <td>82</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>85</td>
      <td>84</td>
      <td>87</td>
      <td>86</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>97</td>
      <td>96</td>
      <td>99</td>
      <td>98</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>101</td>
      <td>100</td>
      <td>103</td>
      <td>102</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>113</td>
      <td>112</td>
      <td>115</td>
      <td>114</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>117</td>
      <td>116</td>
      <td>119</td>
      <td>118</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="14" valign="top">A2</th>
      <th rowspan="6" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>145</td>
      <td>144</td>
      <td>147</td>
      <td>146</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>149</td>
      <td>148</td>
      <td>151</td>
      <td>150</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>161</td>
      <td>160</td>
      <td>163</td>
      <td>162</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>165</td>
      <td>164</td>
      <td>167</td>
      <td>166</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>177</td>
      <td>176</td>
      <td>179</td>
      <td>178</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>181</td>
      <td>180</td>
      <td>183</td>
      <td>182</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="16" valign="top">A3</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>193</td>
      <td>192</td>
      <td>195</td>
      <td>194</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>197</td>
      <td>196</td>
      <td>199</td>
      <td>198</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>209</td>
      <td>208</td>
      <td>211</td>
      <td>210</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>213</td>
      <td>212</td>
      <td>215</td>
      <td>214</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>225</td>
      <td>224</td>
      <td>227</td>
      <td>226</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>229</td>
      <td>228</td>
      <td>231</td>
      <td>230</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>241</td>
      <td>240</td>
      <td>243</td>
      <td>242</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>245</td>
      <td>244</td>
      <td>247</td>
      <td>246</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
      <td>-10</td>
    </tr>
  </tbody>
</table>
<p>64 rows × 4 columns</p>
</div>




```python
# You can use a right-hand-side of an alignable object as well.
# 可以在右侧使用可定位的对象？
df2 = dfmi.copy()
df2.loc[idx[:, :, ['C1', 'C3']], :] = df2 * 1000
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="16" valign="top">A0</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>5</td>
      <td>4</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>9000</td>
      <td>8000</td>
      <td>11000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>13000</td>
      <td>12000</td>
      <td>15000</td>
      <td>14000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>17</td>
      <td>16</td>
      <td>19</td>
      <td>18</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>21</td>
      <td>20</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>25000</td>
      <td>24000</td>
      <td>27000</td>
      <td>26000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>29000</td>
      <td>28000</td>
      <td>31000</td>
      <td>30000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>33</td>
      <td>32</td>
      <td>35</td>
      <td>34</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>37</td>
      <td>36</td>
      <td>39</td>
      <td>38</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>41000</td>
      <td>40000</td>
      <td>43000</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>45000</td>
      <td>44000</td>
      <td>47000</td>
      <td>46000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>49</td>
      <td>48</td>
      <td>51</td>
      <td>50</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>53</td>
      <td>52</td>
      <td>55</td>
      <td>54</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>57000</td>
      <td>56000</td>
      <td>59000</td>
      <td>58000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>61000</td>
      <td>60000</td>
      <td>63000</td>
      <td>62000</td>
    </tr>
    <tr>
      <th rowspan="14" valign="top">A1</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>65</td>
      <td>64</td>
      <td>67</td>
      <td>66</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>69</td>
      <td>68</td>
      <td>71</td>
      <td>70</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>73000</td>
      <td>72000</td>
      <td>75000</td>
      <td>74000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>77000</td>
      <td>76000</td>
      <td>79000</td>
      <td>78000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>81</td>
      <td>80</td>
      <td>83</td>
      <td>82</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>85</td>
      <td>84</td>
      <td>87</td>
      <td>86</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>89000</td>
      <td>88000</td>
      <td>91000</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>93000</td>
      <td>92000</td>
      <td>95000</td>
      <td>94000</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>97</td>
      <td>96</td>
      <td>99</td>
      <td>98</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>101</td>
      <td>100</td>
      <td>103</td>
      <td>102</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>105000</td>
      <td>104000</td>
      <td>107000</td>
      <td>106000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>109000</td>
      <td>108000</td>
      <td>111000</td>
      <td>110000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>113</td>
      <td>112</td>
      <td>115</td>
      <td>114</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>117</td>
      <td>116</td>
      <td>119</td>
      <td>118</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="14" valign="top">A2</th>
      <th rowspan="6" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>137000</td>
      <td>136000</td>
      <td>139000</td>
      <td>138000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>141000</td>
      <td>140000</td>
      <td>143000</td>
      <td>142000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>145</td>
      <td>144</td>
      <td>147</td>
      <td>146</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>149</td>
      <td>148</td>
      <td>151</td>
      <td>150</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>153000</td>
      <td>152000</td>
      <td>155000</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>157000</td>
      <td>156000</td>
      <td>159000</td>
      <td>158000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>161</td>
      <td>160</td>
      <td>163</td>
      <td>162</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>165</td>
      <td>164</td>
      <td>167</td>
      <td>166</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>169000</td>
      <td>168000</td>
      <td>171000</td>
      <td>170000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>173000</td>
      <td>172000</td>
      <td>175000</td>
      <td>174000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>177</td>
      <td>176</td>
      <td>179</td>
      <td>178</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>181</td>
      <td>180</td>
      <td>183</td>
      <td>182</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>185000</td>
      <td>184000</td>
      <td>187000</td>
      <td>186000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>189000</td>
      <td>188000</td>
      <td>191000</td>
      <td>190000</td>
    </tr>
    <tr>
      <th rowspan="16" valign="top">A3</th>
      <th rowspan="8" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>193</td>
      <td>192</td>
      <td>195</td>
      <td>194</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>197</td>
      <td>196</td>
      <td>199</td>
      <td>198</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>201000</td>
      <td>200000</td>
      <td>203000</td>
      <td>202000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>205000</td>
      <td>204000</td>
      <td>207000</td>
      <td>206000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>209</td>
      <td>208</td>
      <td>211</td>
      <td>210</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>213</td>
      <td>212</td>
      <td>215</td>
      <td>214</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>217000</td>
      <td>216000</td>
      <td>219000</td>
      <td>218000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>221000</td>
      <td>220000</td>
      <td>223000</td>
      <td>222000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">B1</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>225</td>
      <td>224</td>
      <td>227</td>
      <td>226</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>229</td>
      <td>228</td>
      <td>231</td>
      <td>230</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>233000</td>
      <td>232000</td>
      <td>235000</td>
      <td>234000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>237000</td>
      <td>236000</td>
      <td>239000</td>
      <td>238000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>241</td>
      <td>240</td>
      <td>243</td>
      <td>242</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>245</td>
      <td>244</td>
      <td>247</td>
      <td>246</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>249000</td>
      <td>248000</td>
      <td>251000</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>253000</td>
      <td>252000</td>
      <td>255000</td>
      <td>254000</td>
    </tr>
  </tbody>
</table>
<p>64 rows × 4 columns</p>
</div>




```python
# Cross-section 断面
# xs 方法 另外提供了一个级别level参数 用来选择多重索引中的部分级别
# xs 当提供轴参数时，也可用于列的选择
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>-1.608162</td>
      <td>1.207609</td>
      <td>-0.369463</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.007312</td>
      <td>-0.272366</td>
      <td>1.862253</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>1.048244</td>
      <td>-0.530191</td>
      <td>-0.118297</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.029907</td>
      <td>-0.689641</td>
      <td>-0.148326</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.437866</td>
      <td>-0.244362</td>
      <td>1.147616</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.853398</td>
      <td>-1.476252</td>
      <td>-1.389965</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">qux</th>
      <th>one</th>
      <td>2.026875</td>
      <td>0.818493</td>
      <td>0.817716</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.359521</td>
      <td>0.353771</td>
      <td>0.787394</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.xs("one", level="second")
df.loc[(slice(None), "one"), :]  # 使用切片得到同样的选择
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-1.608162</td>
      <td>1.207609</td>
      <td>-0.369463</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>1.048244</td>
      <td>-0.530191</td>
      <td>-0.118297</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-0.437866</td>
      <td>-0.244362</td>
      <td>1.147616</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>2.026875</td>
      <td>0.818493</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <th>one</th>
      <td>-1.608162</td>
      <td>1.207609</td>
      <td>-0.369463</td>
    </tr>
    <tr>
      <th>baz</th>
      <th>one</th>
      <td>1.048244</td>
      <td>-0.530191</td>
      <td>-0.118297</td>
    </tr>
    <tr>
      <th>foo</th>
      <th>one</th>
      <td>-0.437866</td>
      <td>-0.244362</td>
      <td>1.147616</td>
    </tr>
    <tr>
      <th>qux</th>
      <th>one</th>
      <td>2.026875</td>
      <td>0.818493</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df.T
df.xs('one', level='second', axis=1)  # 在列方向选择
df.loc[:, (slice(None),'one')]  # 使用切片方式
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>first</th>
      <th>bar</th>
      <th>baz</th>
      <th>foo</th>
      <th>qux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>1.048244</td>
      <td>-0.437866</td>
      <td>2.026875</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.530191</td>
      <td>-0.244362</td>
      <td>0.818493</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>-0.118297</td>
      <td>1.147616</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>first</th>
      <th>bar</th>
      <th>baz</th>
      <th>foo</th>
      <th>qux</th>
    </tr>
    <tr>
      <th>second</th>
      <th>one</th>
      <th>one</th>
      <th>one</th>
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>1.048244</td>
      <td>-0.437866</td>
      <td>2.026875</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.530191</td>
      <td>-0.244362</td>
      <td>0.818493</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>-0.118297</td>
      <td>1.147616</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>




```python
# xs 方法使用多重关键字keys，关键字元组
df.xs(('one', 'bar'), level=('second', 'first'), axis=1)  # 关键字元组可以与级层顺序不一致，与给定level顺序一致
df.loc[:, ("bar", "one")]
# df.loc[:, ("one", "bar")]  # 错误，元组元素的顺序与级层顺序一致
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>first</th>
      <th>bar</th>
    </tr>
    <tr>
      <th>second</th>
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
    </tr>
  </tbody>
</table>
</div>






    A   -1.608162
    B    1.207609
    C   -0.369463
    Name: (bar, one), dtype: float64




```python
# drop_level=False 参数可以使xs保留选定的层级，而不是舍弃，这样的话，与切片得到的结果完全相同
df.xs('one', level='second', axis=1, drop_level=False)  # 默认 drop_level=True
df.loc[:, (slice(None) ,"one")]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>first</th>
      <th>bar</th>
      <th>baz</th>
      <th>foo</th>
      <th>qux</th>
    </tr>
    <tr>
      <th>second</th>
      <th>one</th>
      <th>one</th>
      <th>one</th>
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>1.048244</td>
      <td>-0.437866</td>
      <td>2.026875</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.530191</td>
      <td>-0.244362</td>
      <td>0.818493</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>-0.118297</td>
      <td>1.147616</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>first</th>
      <th>bar</th>
      <th>baz</th>
      <th>foo</th>
      <th>qux</th>
    </tr>
    <tr>
      <th>second</th>
      <th>one</th>
      <th>one</th>
      <th>one</th>
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-1.608162</td>
      <td>1.048244</td>
      <td>-0.437866</td>
      <td>2.026875</td>
    </tr>
    <tr>
      <th>B</th>
      <td>1.207609</td>
      <td>-0.530191</td>
      <td>-0.244362</td>
      <td>0.818493</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.369463</td>
      <td>-0.118297</td>
      <td>1.147616</td>
      <td>0.817716</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Advanced reindexing and alignment 高级索引和定位
# level参数加在索引reindex和定位align方法中。可用于通过级层进行广播值。

midx = pd.MultiIndex(levels=[['zero', 'one'], ['x','y']],
                         labels=[[1,1,0,0],[1,0,1,0]])  # 指定了labels,指定了层级间对应关系
midx
```




    MultiIndex(levels=[['zero', 'one'], ['x', 'y']],
               labels=[[1, 1, 0, 0], [1, 0, 1, 0]])




```python
df = pd.DataFrame(np.random.randn(4,2), index=midx)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-1.388542</td>
      <td>-1.170054</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.240534</td>
      <td>-0.656707</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>-0.848351</td>
      <td>-1.394871</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.212248</td>
      <td>0.051445</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 不同层级索引的广播计算
df2 = df.mean(level=1)
df2
df2 = df.mean(level=0)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>y</th>
      <td>-1.118447</td>
      <td>-1.282462</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.014143</td>
      <td>-0.302631</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>-0.574004</td>
      <td>-0.913381</td>
    </tr>
    <tr>
      <th>zero</th>
      <td>-0.530300</td>
      <td>-0.671713</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 重构索引
df2.reindex(df.index, level=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-0.574004</td>
      <td>-0.913381</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.574004</td>
      <td>-0.913381</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>-0.530300</td>
      <td>-0.671713</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.530300</td>
      <td>-0.671713</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 定位/对齐
df
df2
df.align(df2, level=0)
df_aligned, df2_aligned = df.align(df2, level=0)  # ??
df_aligned
df2_aligned
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-1.388542</td>
      <td>-1.170054</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.240534</td>
      <td>-0.656707</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>-0.848351</td>
      <td>-1.394871</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.212248</td>
      <td>0.051445</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>-0.574004</td>
      <td>-0.913381</td>
    </tr>
    <tr>
      <th>zero</th>
      <td>-0.530300</td>
      <td>-0.671713</td>
    </tr>
  </tbody>
</table>
</div>






    (               0         1
     one  y -1.388542 -1.170054
          x  0.240534 -0.656707
     zero y -0.848351 -1.394871
          x -0.212248  0.051445,                0         1
     one  y -0.574004 -0.913381
          x -0.574004 -0.913381
     zero y -0.530300 -0.671713
          x -0.530300 -0.671713)






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-1.388542</td>
      <td>-1.170054</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.240534</td>
      <td>-0.656707</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>-0.848351</td>
      <td>-1.394871</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.212248</td>
      <td>0.051445</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-0.574004</td>
      <td>-0.913381</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.574004</td>
      <td>-0.913381</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>-0.530300</td>
      <td>-0.671713</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.530300</td>
      <td>-0.671713</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 交换层级 swaplevel()
df.swaplevel(0, 1, axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>y</th>
      <th>one</th>
      <td>-1.388542</td>
      <td>-1.170054</td>
    </tr>
    <tr>
      <th>x</th>
      <th>one</th>
      <td>0.240534</td>
      <td>-0.656707</td>
    </tr>
    <tr>
      <th>y</th>
      <th>zero</th>
      <td>-0.848351</td>
      <td>-1.394871</td>
    </tr>
    <tr>
      <th>x</th>
      <th>zero</th>
      <td>-0.212248</td>
      <td>0.051445</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reorder_levels 概况了 swaplevel 函数， 可以一步交换层级索引
df.reorder_levels([1,0], axis=0)  # 看上去结果与swaplevel一样，传入参数不一样
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>y</th>
      <th>one</th>
      <td>-1.388542</td>
      <td>-1.170054</td>
    </tr>
    <tr>
      <th>x</th>
      <th>one</th>
      <td>0.240534</td>
      <td>-0.656707</td>
    </tr>
    <tr>
      <th>y</th>
      <th>zero</th>
      <td>-0.848351</td>
      <td>-1.394871</td>
    </tr>
    <tr>
      <th>x</th>
      <th>zero</th>
      <td>-0.212248</td>
      <td>0.051445</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 多重索引排序
# 排序是为了搞笑的索引和切片。任何索引都可以使用sort_index

tuples
s = pd.Series(np.random.randn(8), index=pd.MultiIndex.from_tuples(tuples))
s
```




    [('baz', 'two'),
     ('qux', 'two'),
     ('bar', 'one'),
     ('foo', 'one'),
     ('qux', 'one'),
     ('baz', 'one'),
     ('foo', 'two'),
     ('bar', 'two')]






    baz  two    1.365155
    qux  two   -1.331225
    bar  one   -1.512430
    foo  one    0.468294
    qux  one   -0.667115
    baz  one   -0.502417
    foo  two    1.685553
    bar  two   -1.611271
    dtype: float64




```python
s.sort_index()
s.sort_index(level=1)  # 默认是level=0排序
s.sort_index(level=0)
```




    bar  one   -1.512430
         two   -1.611271
    baz  one   -0.502417
         two    1.365155
    foo  one    0.468294
         two    1.685553
    qux  one   -0.667115
         two   -1.331225
    dtype: float64






    bar  one   -1.512430
    baz  one   -0.502417
    foo  one    0.468294
    qux  one   -0.667115
    bar  two   -1.611271
    baz  two    1.365155
    foo  two    1.685553
    qux  two   -1.331225
    dtype: float64






    bar  one   -1.512430
         two   -1.611271
    baz  one   -0.502417
         two    1.365155
    foo  one    0.468294
         two    1.685553
    qux  one   -0.667115
         two   -1.331225
    dtype: float64




```python
# level参数除了可以用整型序号，还可以使用层级的names
s.index.set_names(['L1', 'L2'], inplace=True)
s
s.sort_index(level="L1")
s.sort_index(level="L2")
```




    L1   L2 
    baz  two    1.365155
    qux  two   -1.331225
    bar  one   -1.512430
    foo  one    0.468294
    qux  one   -0.667115
    baz  one   -0.502417
    foo  two    1.685553
    bar  two   -1.611271
    dtype: float64






    L1   L2 
    bar  one   -1.512430
         two   -1.611271
    baz  one   -0.502417
         two    1.365155
    foo  one    0.468294
         two    1.685553
    qux  one   -0.667115
         two   -1.331225
    dtype: float64






    L1   L2 
    bar  one   -1.512430
    baz  one   -0.502417
    foo  one    0.468294
    qux  one   -0.667115
    bar  two   -1.611271
    baz  two    1.365155
    foo  two    1.685553
    qux  two   -1.331225
    dtype: float64




```python
# 可以指定排序的轴方向
df.T
df.T.sort_index(level=1, axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">one</th>
      <th colspan="2" halign="left">zero</th>
    </tr>
    <tr>
      <th></th>
      <th>y</th>
      <th>x</th>
      <th>y</th>
      <th>x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.388542</td>
      <td>0.240534</td>
      <td>-0.848351</td>
      <td>-0.212248</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.170054</td>
      <td>-0.656707</td>
      <td>-1.394871</td>
      <td>0.051445</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>zero</th>
      <th>one</th>
      <th>zero</th>
      <th>one</th>
    </tr>
    <tr>
      <th></th>
      <th>x</th>
      <th>x</th>
      <th>y</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.212248</td>
      <td>0.240534</td>
      <td>-0.848351</td>
      <td>-1.388542</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.051445</td>
      <td>-0.656707</td>
      <td>-1.394871</td>
      <td>-1.170054</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 即使数据没有排序也可以索引，但是这样效率低下。
# 返回值是拷贝
dfm = pd.DataFrame({'jim': [0, 0, 1, 1],
                    'joe': ['x', 'x', 'z', 'y'],
                    'jolie': np.random.rand(4)})
dfm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>jim</th>
      <th>joe</th>
      <th>jolie</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>x</td>
      <td>0.844228</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>x</td>
      <td>0.317508</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>z</td>
      <td>0.413824</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>y</td>
      <td>0.074264</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfm = dfm.set_index(["jim", "joe"])
dfm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>jolie</th>
    </tr>
    <tr>
      <th>jim</th>
      <th>joe</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">0</th>
      <th>x</th>
      <td>0.844228</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.317508</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>z</th>
      <td>0.413824</td>
    </tr>
    <tr>
      <th>y</th>
      <td>0.074264</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfm.loc[(1, "z")]  # 会提示PerformanceWarning
```

    d:\python\36-64\lib\site-packages\ipykernel_launcher.py:1: PerformanceWarning: indexing past lexsort depth may impact performance.
      """Entry point for launching an IPython kernel.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>jolie</th>
    </tr>
    <tr>
      <th>jim</th>
      <th>joe</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <th>z</th>
      <td>0.413824</td>
    </tr>
  </tbody>
</table>
</div>




```python
# dfm.loc[(0,'y'):(1, 'z')]  # 错误 无法定位
dfm.index.is_lexsorted()
dfm.index.lexsort_depth
```




    False






    1




```python
dfm = dfm.sort_index()  # 索引排序，默认对所有层级
dfm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>jolie</th>
    </tr>
    <tr>
      <th>jim</th>
      <th>joe</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">0</th>
      <th>x</th>
      <td>0.844228</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.317508</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>y</th>
      <td>0.074264</td>
    </tr>
    <tr>
      <th>z</th>
      <td>0.413824</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfm.index.is_lexsorted()
dfm.index.lexsort_depth
dfm.loc[(0,'y'):(1, 'z')]

```




    True






    2






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>jolie</th>
    </tr>
    <tr>
      <th>jim</th>
      <th>joe</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>y</th>
      <td>0.074264</td>
    </tr>
    <tr>
      <th>z</th>
      <td>0.413824</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Take Methods take 方法 (拿、取)
# 与numpy的数组类似，padas的index、series、Dataframe也提供take方法
# 用来检索给定轴方向上给定的指数indices（必须是整数列表或者整数数组，可以是负整数）

# 在性能方面，由于take方法管理了一个更窄的输入范围，它能提供比想象的索引更快的性能


index = pd.Index(np.random.randint(0, 1000, 10))
index
```




    Int64Index([523, 532, 386, 998, 832, 71, 965, 274, 389, 59], dtype='int64')




```python
positions = [0, 9, 3]
index[positions]
index.take(positions)
```




    Int64Index([523, 59, 998], dtype='int64')






    Int64Index([523, 59, 998], dtype='int64')




```python
ser = pd.Series(np.random.randn(10))
ser
```




    0    0.733196
    1    0.975773
    2   -0.261602
    3   -0.055134
    4    0.959253
    5    1.189025
    6   -0.434102
    7    0.653628
    8    0.248894
    9   -0.203562
    dtype: float64




```python
ser.iloc[positions]
ser.take(positions)
```




    0    0.733196
    9   -0.203562
    3   -0.055134
    dtype: float64






    0    0.733196
    9   -0.203562
    3   -0.055134
    dtype: float64




```python
# 对DataFrame，indices应该是一个一维 的列表或数组，规定了行或列的位置
frm = pd.DataFrame(np.random.randn(5, 3))
frm
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.722107</td>
      <td>-1.758271</td>
      <td>0.580805</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.555332</td>
      <td>-0.856173</td>
      <td>-1.143862</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.636994</td>
      <td>1.312340</td>
      <td>0.046131</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.154813</td>
      <td>0.311931</td>
      <td>0.933192</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.277001</td>
      <td>-0.144097</td>
      <td>-1.871135</td>
    </tr>
  </tbody>
</table>
</div>




```python
frm.take([1, 4, 3])  # 默认取行方向
frm.take([0, 2], axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.555332</td>
      <td>-0.856173</td>
      <td>-1.143862</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.277001</td>
      <td>-0.144097</td>
      <td>-1.871135</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.154813</td>
      <td>0.311931</td>
      <td>0.933192</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.722107</td>
      <td>0.580805</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.555332</td>
      <td>-1.143862</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.636994</td>
      <td>0.046131</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.154813</td>
      <td>0.933192</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.277001</td>
      <td>-1.871135</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 注意：take方法不要用于布尔indices
arr = np.random.randn(10)
arr
```




    array([-0.00772525,  0.95419469,  1.80636718, -2.46742236, -0.025503  ,
            0.44203691,  0.48626739, -0.74160374, -0.22453771,  0.8813933 ])




```python
arr.take([False, False, True, True])  # 相当于取了[0,0,1,1]
arr[[0, 1]]
```




    array([-0.00772525, -0.00772525,  0.95419469,  0.95419469])






    array([-0.00772525,  0.95419469])




```python
ser = pd.Series(np.random.randn(10))
ser
```




    0    1.782426
    1    0.531882
    2   -0.339277
    3    0.500497
    4   -0.333816
    5   -1.713753
    6   -0.125252
    7   -0.857100
    8    0.385080
    9    1.247962
    dtype: float64




```python
ser.take([False, False, True, True])  # 相当于取了[0,0,1,1]
ser.iloc[[0, 1]]
```




    0    1.782426
    0    1.782426
    1    0.531882
    1    0.531882
    dtype: float64






    0    1.782426
    1    0.531882
    dtype: float64




```python
# Index Types 索引 index 对象
# 其他一些索引对象

```


```python
# CategoricalIndex   绝对索引？类别索引？
# 用于支持重复的索引
from pandas.api.types import CategoricalDtype
```


```python
df = pd.DataFrame({'A': np.arange(6),
                   'B': list('aabbca')})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>a</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>b</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>b</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>c</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>a</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['B'] = df['B'].astype(CategoricalDtype(list('cab')))
df
df.dtypes
df.B.cat.categories
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>a</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>b</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>b</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>c</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>a</td>
    </tr>
  </tbody>
</table>
</div>






    A       int32
    B    category
    dtype: object






    Index(['c', 'a', 'b'], dtype='object')




```python
df2 = df.set_index('B')
df2
df2.index
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
    <tr>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
    </tr>
    <tr>
      <th>a</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>






    CategoricalIndex(['a', 'a', 'b', 'b', 'c', 'a'], categories=['c', 'a', 'b'], ordered=False, name='B', dtype='category')




```python
# 使用 __getitem__/.iloc/.loc 索引时，索引对象 必须 在类别里面，否则操作将挂起
df2.loc['a']
df2.loc['a'].index  # 保留了全部的 CategoricalIndex 
df2.sort_index()  # 按照categoies给定的顺序排序
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
    <tr>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1</td>
    </tr>
    <tr>
      <th>a</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>






    CategoricalIndex(['a', 'a', 'a'], categories=['c', 'a', 'b'], ordered=False, name='B', dtype='category')






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
    <tr>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>4</td>
    </tr>
    <tr>
      <th>a</th>
      <td>0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1</td>
    </tr>
    <tr>
      <th>a</th>
      <td>5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.groupby(level=0)
df2.groupby(level=0).sum()
df2.groupby(level=0).sum().index  # 也保留了category
```




    <pandas.core.groupby.DataFrameGroupBy object at 0x00000000117AC710>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
    <tr>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>4</td>
    </tr>
    <tr>
      <th>a</th>
      <td>6</td>
    </tr>
    <tr>
      <th>b</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>






    CategoricalIndex(['c', 'a', 'b'], categories=['c', 'a', 'b'], ordered=False, name='B', dtype='category')




```python
df2.reindex(['a','e'])  # reindex 传入普通列表 返回一个 普通的 index
df2.reindex(['a','e']).index
df2.reindex(pd.Categorical(['a','e'],categories=list('abcde')))  # 指定catgorical index，即使原来的index没有的类别，也可以reindex
df2.reindex(pd.Categorical(['a','e'],categories=list('abcde'))).index
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
    <tr>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>






    Index(['a', 'a', 'a', 'e'], dtype='object', name='B')






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
    <tr>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>






    CategoricalIndex(['a', 'a', 'a', 'e'], categories=['a', 'b', 'c', 'd', 'e'], ordered=False, name='B', dtype='category')




```python
# 注意：变形和比较操作必须有同样的categories，否则报错

```


```python
# Int64Index and RangeIndex
# Int64Index 是pandas基础索引。
# RangeIndex是Int64Index的一个子集，现在作为所有NDFrame对象的默认索引。
```


```python
# Float64Index 当创建索引index时，传入浮点数或者浮点与整数混合值，就默认是Float64Index

indexf = pd.Index([1.5, 2, 3, 4.5, 5])
indexf
```




    Float64Index([1.5, 2.0, 3.0, 4.5, 5.0], dtype='float64')




```python
sf = pd.Series(range(5), index=indexf)
sf
```




    1.5    0
    2.0    1
    3.0    2
    4.5    3
    5.0    4
    dtype: int64




```python
# [] .loc 基于 label，整数将被转为浮点值
sf[1.5:4.5]
sf[1:4]
sf.loc[3]  # label，不是位置索引
# sf[3.2]  # 错误，传入值必须在labels中
```




    1.5    0
    2.0    1
    3.0    2
    4.5    3
    dtype: int64






    1.5    0
    2.0    1
    3.0    2
    dtype: int64






    2




```python
sf.iloc[3]  # 基于位置，传入整数，不能传入浮点数
```




    3




```python
# 例子： 有不规则的数据表，其索引类似时间间隔，但数值是浮点型的
dfir1 = pd.DataFrame(np.random.randn(5,2),
                               index=np.arange(5) * 250.0,
                               columns=list('AB'))
dfir1
dfir2 = pd.DataFrame(np.random.randn(6,2),
                               index=np.arange(4,10) * 250.1,
                               columns=list('AB'))
dfir2
dfir = pd.concat([dfir1,dfir2])
dfir
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.0</th>
      <td>1.158461</td>
      <td>0.595743</td>
    </tr>
    <tr>
      <th>250.0</th>
      <td>1.457556</td>
      <td>0.268541</td>
    </tr>
    <tr>
      <th>500.0</th>
      <td>-0.437650</td>
      <td>-0.299700</td>
    </tr>
    <tr>
      <th>750.0</th>
      <td>-1.095812</td>
      <td>-2.079684</td>
    </tr>
    <tr>
      <th>1000.0</th>
      <td>0.242220</td>
      <td>-0.868812</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1000.4</th>
      <td>-0.858327</td>
      <td>-0.364968</td>
    </tr>
    <tr>
      <th>1250.5</th>
      <td>-1.445806</td>
      <td>-2.129608</td>
    </tr>
    <tr>
      <th>1500.6</th>
      <td>0.799049</td>
      <td>1.232102</td>
    </tr>
    <tr>
      <th>1750.7</th>
      <td>-1.132538</td>
      <td>0.283472</td>
    </tr>
    <tr>
      <th>2000.8</th>
      <td>-1.157884</td>
      <td>0.398119</td>
    </tr>
    <tr>
      <th>2250.9</th>
      <td>-1.330821</td>
      <td>-0.563333</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.0</th>
      <td>1.158461</td>
      <td>0.595743</td>
    </tr>
    <tr>
      <th>250.0</th>
      <td>1.457556</td>
      <td>0.268541</td>
    </tr>
    <tr>
      <th>500.0</th>
      <td>-0.437650</td>
      <td>-0.299700</td>
    </tr>
    <tr>
      <th>750.0</th>
      <td>-1.095812</td>
      <td>-2.079684</td>
    </tr>
    <tr>
      <th>1000.0</th>
      <td>0.242220</td>
      <td>-0.868812</td>
    </tr>
    <tr>
      <th>1000.4</th>
      <td>-0.858327</td>
      <td>-0.364968</td>
    </tr>
    <tr>
      <th>1250.5</th>
      <td>-1.445806</td>
      <td>-2.129608</td>
    </tr>
    <tr>
      <th>1500.6</th>
      <td>0.799049</td>
      <td>1.232102</td>
    </tr>
    <tr>
      <th>1750.7</th>
      <td>-1.132538</td>
      <td>0.283472</td>
    </tr>
    <tr>
      <th>2000.8</th>
      <td>-1.157884</td>
      <td>0.398119</td>
    </tr>
    <tr>
      <th>2250.9</th>
      <td>-1.330821</td>
      <td>-0.563333</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 选取第1秒前的数据
dfir[:1000]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.0</th>
      <td>1.158461</td>
      <td>0.595743</td>
    </tr>
    <tr>
      <th>250.0</th>
      <td>1.457556</td>
      <td>0.268541</td>
    </tr>
    <tr>
      <th>500.0</th>
      <td>-0.437650</td>
      <td>-0.299700</td>
    </tr>
    <tr>
      <th>750.0</th>
      <td>-1.095812</td>
      <td>-2.079684</td>
    </tr>
    <tr>
      <th>1000.0</th>
      <td>0.242220</td>
      <td>-0.868812</td>
    </tr>
  </tbody>
</table>
</div>




```python
# IntervalIndex  区间索引  (数学上的开闭区间)
df = pd.DataFrame({'A': [1, 2, 3, 4]},
                  index=pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4]))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(0, 1]</th>
      <td>1</td>
    </tr>
    <tr>
      <th>(1, 2]</th>
      <td>2</td>
    </tr>
    <tr>
      <th>(2, 3]</th>
      <td>3</td>
    </tr>
    <tr>
      <th>(3, 4]</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[2]  # loc 可以是区间的边缘
df.loc[2.5]
df.loc[1.5:2.5]
```




    A    2
    Name: (1, 2], dtype: int64






    A    3
    Name: (2, 3], dtype: int64






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(1, 2]</th>
      <td>2</td>
    </tr>
    <tr>
      <th>(2, 3]</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Interval and IntervalIndex are used by cut and qcut
# 区间数值类型和区间类型索引可以使用 cut qcut 方法??
c = pd.cut(range(4), bins=2)
c
c.categories
```




    [(-0.003, 1.5], (-0.003, 1.5], (1.5, 3.0], (1.5, 3.0]]
    Categories (2, interval[float64]): [(-0.003, 1.5] < (1.5, 3.0]]






    IntervalIndex([(-0.003, 1.5], (1.5, 3.0]]
                  closed='right',
                  dtype='interval[float64]')




```python
pd.cut([0, 3, 5, 1], bins=c.categories)  # 允许一个interval类型去bin（分隔）其他数据
```




    [(-0.003, 1.5], (1.5, 3.0], NaN, (-0.003, 1.5]]
    Categories (2, interval[float64]): [(-0.003, 1.5] < (1.5, 3.0]]




```python
# Miscellaneous indexing FAQ 杂项 常见问题


```


```python
# Integer indexing  整数型索引
# 整型的索引是label，应满足label的要求
# 在pandas中，一般认为标签label事项大于整数定位。

s = pd.Series(range(5))
s
# s[-1]  # 异常
# s.loc[-1]  # 异常
s.loc[-1:]  # 允许
s.iloc[-1]  # 允许
df = pd.DataFrame(np.random.randn(5, 4))
df
df.loc[-2:]
# df.loc[-2]  # 异常
```




    0    0
    1    1
    2    2
    3    3
    4    4
    dtype: int64






    0    0
    1    1
    2    2
    3    3
    4    4
    dtype: int64






    4






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.021033</td>
      <td>0.127054</td>
      <td>-0.864734</td>
      <td>-1.835828</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.400611</td>
      <td>0.594981</td>
      <td>-1.758866</td>
      <td>-1.059539</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.108597</td>
      <td>0.784000</td>
      <td>0.306035</td>
      <td>-0.695933</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.078048</td>
      <td>-1.742895</td>
      <td>-0.159740</td>
      <td>0.934115</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.524633</td>
      <td>0.433224</td>
      <td>-0.732334</td>
      <td>0.442827</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.021033</td>
      <td>0.127054</td>
      <td>-0.864734</td>
      <td>-1.835828</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.400611</td>
      <td>0.594981</td>
      <td>-1.758866</td>
      <td>-1.059539</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.108597</td>
      <td>0.784000</td>
      <td>0.306035</td>
      <td>-0.695933</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.078048</td>
      <td>-1.742895</td>
      <td>-0.159740</td>
      <td>0.934115</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.524633</td>
      <td>0.433224</td>
      <td>-0.732334</td>
      <td>0.442827</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Non-monotonic indexes require exact matches 非单调索引要求精确匹配
# 如果series或Dataframe的索引是单调增或单调减的，则基于标签的切片可以超出索引的范围。
# 就像对一般python列表list的索引切片。
# 可以用is_monotonic_increasing和is_monotonic_decreasing测试单调属性

df = pd.DataFrame(index=[2,3,3,4,5], columns=['data'], data=list(range(5)))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index.is_monotonic_increasing
df.index.is_monotonic_decreasing
```




    True






    False




```python
df.loc[0:4, :]  # 没有0和1行，但是返回了label为2、3、4的行
df.loc[13:15, :]  # 超出界限，返回空
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
# 非单调索引，切片必须在index内，而且边界的值必须是唯一的

df = pd.DataFrame(index=[2,3,1,4,3,5], columns=['data'], data=list(range(6)))
df
df.index.is_monotonic_increasing
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>






    False




```python
df.loc[2:4, :]
# df.loc[0:4, :]  # 错误没有0标签
# df.loc[2:3, :]  # 错误，边界标签3不是唯一的
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Index.is_monotonic_increasing() and Index.is_monotonic_decreasing() 只检测弱单调（可以有重复值）
# 结合使用 Index.is_unique()  可以检测严格单调性

weakly_monotonic = pd.Index(['a', 'b', 'c', 'c'])
weakly_monotonic
weakly_monotonic.is_monotonic_increasing
weakly_monotonic.is_monotonic_increasing & weakly_monotonic.is_unique
```




    Index(['a', 'b', 'c', 'c'], dtype='object')






    True






    False




```python
# Endpoints are inclusive 端点（边界）包括在内
# 与标准的python切片（不包括右端点值）相比，pandas中的标签切片包含端点值。
# 主要原因是经常不可能轻易断定 在索引的局部标签后 的 后继或者下一个元素
```


```python
s = pd.Series(np.random.randn(6), index=list('abcdef'))
s
```




    a    1.280483
    b    1.562738
    c    0.904503
    d   -0.470785
    e   -0.008048
    f   -0.413812
    dtype: float64




```python
s[2:5]  # 基于整型的索引，与既有标签的不同，不包括右端点
```




    c    0.904503
    d   -0.470785
    e   -0.008048
    dtype: float64




```python
# 如果用标签，不容易取得下一个标签
# s.loc['c':'e'+1]  # 错误
s.loc['c':'e']
```




    c    0.904503
    d   -0.470785
    e   -0.008048
    dtype: float64




```python
# Indexing potentially changes underlying Series dtype 
# 在series类型下索引可能出现变化
# The different indexing operation can potentially change the dtype of a Series.
# 不同的索引操作可能会潜在的改变series的类型

series1 = pd.Series([1, 2, 3])
series1.dtype  # int
series1
res = series1.reindex([0, 4])
res.dtype  # float
res
```




    dtype('int64')






    0    1
    1    2
    2    3
    dtype: int64






    dtype('float64')






    0    1.0
    4    NaN
    dtype: float64




```python
series2 = pd.Series([True])
series2.dtype  # 布尔类型
series2
res = series2.reindex_like(series1)
res.dtype  # '0' 型  （空？）
res
```




    dtype('bool')






    0    True
    dtype: bool






    dtype('O')






    0    True
    1     NaN
    2     NaN
    dtype: object




```python
# 由于默认插入NaN，引起了dtype的改变。
# 这会导致一些问题，当使用如 numpy.logical_and. 的np ufuncs 时
```


```python

#  2018-02-22
```
