

```python
# from http://pandas.pydata.org/pandas-docs/stable/indexing.html
# pandas 0.22.0 
```


```python
import pandas as pd
import numpy as np
```


```python
"""
尽量利用pandas提供的专用索引方式，而不是python通用的切片方式。
三种主要的索引方式：indexers
.loc label based 基于标签， 可以是标签名，可以是布尔值，可以是一元函数
.iloc integer psition based 基于整数位置(from 0 to length-1 of the axis)，和python切片类似
[]

"""

"""
Object Type 		Selection 			Return Value Type
------------------------------------------------------------
Series 				series[label] 		scalar value
DataFrame 			frame[colname] 		Series corresponding to colname
Panel 				panel[itemname] 	DataFrame corresponding to the itemname
"""
```




    '\n尽量利用pandas提供的专用索引方式，而不是python通用的切片方式。\n三种主要的索引方式：indexers\n.loc label based 基于标签， 可以是标签名，可以是布尔值，可以是一元函数\n.iloc integer psition based 基于整数位置(from 0 to length-1 of the axis)，和python切片类似\n[]\n\n'






    '\nObject Type \t\tIndexers\nSeries \t\t\t\ts.loc[indexer]\nDataFrame \t\t\tdf.loc[row_indexer,column_indexer]\nPanel \t\t\t\tp.loc[item_indexer,major_indexer,minor_indexer]\n'




```python
# Here we construct a simple time series data set to use for illustrating the indexing functionality 
# 构造时间序列，举例说明索引的功能

dates = pd.date_range('1/1/2000', periods=8)
dates
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df

```




    DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
                   '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-08'],
                  dtype='datetime64[ns]', freq='D')






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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.136628</td>
      <td>0.324097</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.113819</td>
      <td>-0.718630</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.603598</td>
      <td>-0.143643</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.486200</td>
      <td>-0.136663</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.835318</td>
      <td>1.036607</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-2.376205</td>
      <td>0.362577</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.193371</td>
      <td>1.330468</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.476533</td>
      <td>-0.476653</td>
      <td>-0.434356</td>
      <td>0.744500</td>
    </tr>
  </tbody>
</table>
</div>




```python
panel = pd.Panel({'one' : df, 'two' : df - df.mean()})  # 多维表格
panel
panel['one']
panel['two']
```




    <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 8 (major_axis) x 4 (minor_axis)
    Items axis: one to two
    Major_axis axis: 2000-01-01 00:00:00 to 2000-01-08 00:00:00
    Minor_axis axis: A to D






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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.136628</td>
      <td>0.324097</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.113819</td>
      <td>-0.718630</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.603598</td>
      <td>-0.143643</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.486200</td>
      <td>-0.136663</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.835318</td>
      <td>1.036607</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-2.376205</td>
      <td>0.362577</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.193371</td>
      <td>1.330468</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.476533</td>
      <td>-0.476653</td>
      <td>-0.434356</td>
      <td>0.744500</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.350419</td>
      <td>0.126827</td>
      <td>1.251866</td>
      <td>-0.047518</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.327611</td>
      <td>-0.915900</td>
      <td>0.411770</td>
      <td>-1.473522</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.389806</td>
      <td>-0.340913</td>
      <td>-0.747511</td>
      <td>-0.327524</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.272408</td>
      <td>-0.333933</td>
      <td>-1.620467</td>
      <td>-0.717772</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.049110</td>
      <td>0.839337</td>
      <td>-0.107366</td>
      <td>0.976422</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-2.162413</td>
      <td>0.165307</td>
      <td>-0.089201</td>
      <td>-0.380969</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.407163</td>
      <td>1.133198</td>
      <td>0.939713</td>
      <td>1.128641</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.690325</td>
      <td>-0.673923</td>
      <td>-0.038803</td>
      <td>0.842241</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Thus, as per above, we have the most basic indexing using []:
# 最基本的索引方法，使用[]

s = df['A']
s
dates[5]  # 注意切片从0计数
s[dates[5]]
```




    2000-01-01    0.136628
    2000-01-02    0.113819
    2000-01-03   -0.603598
    2000-01-04   -0.486200
    2000-01-05    0.835318
    2000-01-06   -2.376205
    2000-01-07    0.193371
    2000-01-08    0.476533
    Freq: D, Name: A, dtype: float64






    Timestamp('2000-01-06 00:00:00', freq='D')






    -2.376204948581219




```python
# 在[]中传入列名的列表，如[ 'A', "B" ]
columns_l = ['A', 'B']
df[columns_l]  
df[[ 'A', "B" ]]  # 相当于上面，注意两重[]
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
      <th>2000-01-01</th>
      <td>0.324097</td>
      <td>0.136628</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.718630</td>
      <td>0.113819</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.143643</td>
      <td>-0.603598</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.136663</td>
      <td>-0.486200</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.036607</td>
      <td>0.835318</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.362577</td>
      <td>-2.376205</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.330468</td>
      <td>0.193371</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.476653</td>
      <td>0.476533</td>
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
      <th>2000-01-01</th>
      <td>0.324097</td>
      <td>0.136628</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.718630</td>
      <td>0.113819</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.143643</td>
      <td>-0.603598</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.136663</td>
      <td>-0.486200</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.036607</td>
      <td>0.835318</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.362577</td>
      <td>-2.376205</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.330468</td>
      <td>0.193371</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.476653</td>
      <td>0.476533</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.324097</td>
      <td>0.136628</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.718630</td>
      <td>0.113819</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.143643</td>
      <td>-0.603598</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.136663</td>
      <td>-0.486200</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.036607</td>
      <td>0.835318</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.362577</td>
      <td>-2.376205</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.330468</td>
      <td>0.193371</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.476653</td>
      <td>0.476533</td>
      <td>-0.434356</td>
      <td>0.744500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['A', 'B']] = df[['B', 'A']]  # 交换两列的值
df
df.loc[:,['B', 'A']]

# 下式不能交换两列的值
# This will not modify df because the column alignment is before value assignment. ? 不理解？
# 列赋值在值赋值之前？
df.loc[:,['B', 'A']] = df[['A', 'B']]  
df

# df.loc[:,['B', 'A']] = df[:, ['A', 'B']]   # 错误？
# df

# 正确的方式：
df.loc[:,['B', 'A']] = df[['A', 'B']].values  # 取列的值
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.136628</td>
      <td>0.324097</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.113819</td>
      <td>-0.718630</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.603598</td>
      <td>-0.143643</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.486200</td>
      <td>-0.136663</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.835318</td>
      <td>1.036607</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-2.376205</td>
      <td>0.362577</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.193371</td>
      <td>1.330468</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.476533</td>
      <td>-0.476653</td>
      <td>-0.434356</td>
      <td>0.744500</td>
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
      <th>B</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.324097</td>
      <td>0.136628</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.718630</td>
      <td>0.113819</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.143643</td>
      <td>-0.603598</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.136663</td>
      <td>-0.486200</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.036607</td>
      <td>0.835318</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.362577</td>
      <td>-2.376205</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.330468</td>
      <td>0.193371</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.476653</td>
      <td>0.476533</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.136628</td>
      <td>0.324097</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.113819</td>
      <td>-0.718630</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.603598</td>
      <td>-0.143643</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.486200</td>
      <td>-0.136663</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.835318</td>
      <td>1.036607</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-2.376205</td>
      <td>0.362577</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.193371</td>
      <td>1.330468</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.476533</td>
      <td>-0.476653</td>
      <td>-0.434356</td>
      <td>0.744500</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.324097</td>
      <td>0.136628</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.718630</td>
      <td>0.113819</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.143643</td>
      <td>-0.603598</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.136663</td>
      <td>-0.486200</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.036607</td>
      <td>0.835318</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.362577</td>
      <td>-2.376205</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.330468</td>
      <td>0.193371</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.476653</td>
      <td>0.476533</td>
      <td>-0.434356</td>
      <td>0.744500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Attribute Access¶
# 属性访问，属性存取
# You may access an index on a Series, column on a DataFrame, 
# and an item on a Panel directly as an attribute:

sa = pd.Series([1,2,3],index=list('abc'))
sa

dfa = df.copy()
dfa
```




    a    1
    b    2
    c    3
    dtype: int64






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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.324097</td>
      <td>0.136628</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.718630</td>
      <td>0.113819</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.143643</td>
      <td>-0.603598</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.136663</td>
      <td>-0.486200</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.036607</td>
      <td>0.835318</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.362577</td>
      <td>-2.376205</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.330468</td>
      <td>0.193371</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.476653</td>
      <td>0.476533</td>
      <td>-0.434356</td>
      <td>0.744500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 对item column等赋值
# 就像属性一样的存取，但需要注意：
# 1. 名称应符合python命名规则，由字母、数字和下划线组成
# 2. 不能和已有的方法名称重名，例如 min
# 3. 不能与pandas内部“关键字”重名，例如 index axis items labels
# 以上情况，可以使用 [ "" ] 引用

sa.a = 5
sa

dfa.index
dfa.A = list(range(len(dfa.index)))
dfa
```




    a    5
    b    2
    c    3
    dtype: int64






    DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
                   '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-08'],
                  dtype='datetime64[ns]', freq='D')






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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0</td>
      <td>0.136628</td>
      <td>0.856313</td>
      <td>-0.145259</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>1</td>
      <td>0.113819</td>
      <td>0.016217</td>
      <td>-1.571263</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>2</td>
      <td>-0.603598</td>
      <td>-1.143063</td>
      <td>-0.425266</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>3</td>
      <td>-0.486200</td>
      <td>-2.016020</td>
      <td>-0.815514</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>4</td>
      <td>0.835318</td>
      <td>-0.502919</td>
      <td>0.878680</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>5</td>
      <td>-2.376205</td>
      <td>-0.484754</td>
      <td>-0.478711</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>6</td>
      <td>0.193371</td>
      <td>0.544160</td>
      <td>1.030900</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>7</td>
      <td>0.476533</td>
      <td>-0.434356</td>
      <td>0.744500</td>
    </tr>
  </tbody>
</table>
</div>




```python
x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})  # 字典key值为列名
x
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
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
dict(x=9, y=99)
x.iloc[1]
x.iloc[1] = dict(x=9, y=99)
x
```




    {'x': 9, 'y': 99}






    x    2
    y    4
    Name: 1, dtype: int64






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
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame({'one': [1., 2., 3.]})
df
df.two = [4, 5, 6]  # 错误，不能增加一列，利用属性的方式不能对没有的列赋值
df.two  # 但是增加了一项属性，而且可以取得这项属性
df
df['two'] = [4, 5, 6]  # 可以增加一列
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
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



    d:\python\36-64\lib\site-packages\ipykernel_launcher.py:3: UserWarning: Pandas doesn't allow columns to be created via a new attribute name - see https://pandas.pydata.org/pandas-docs/stable/indexing.html#attribute-access
      This is separate from the ipykernel package so we can avoid doing imports until
    




    [4, 5, 6]






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
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Slicing ranges
# 切片范围
# iloc 方法是最稳健和兼容的
# 下面介绍 方括号 [] 操作符 作为切片

# 对series操作
# 取值
s
s[:5]
s[::2]
s[::-1]
```




    2000-01-01    0.324097
    2000-01-02   -0.718630
    2000-01-03   -0.143643
    2000-01-04   -0.136663
    2000-01-05    1.036607
    2000-01-06    0.362577
    2000-01-07    1.330468
    2000-01-08   -0.476653
    Freq: D, Name: A, dtype: float64






    2000-01-01    0.324097
    2000-01-02   -0.718630
    2000-01-03   -0.143643
    2000-01-04   -0.136663
    2000-01-05    1.036607
    Freq: D, Name: A, dtype: float64






    2000-01-01    0.324097
    2000-01-03   -0.143643
    2000-01-05    1.036607
    2000-01-07    1.330468
    Freq: 2D, Name: A, dtype: float64






    2000-01-08   -0.476653
    2000-01-07    1.330468
    2000-01-06    0.362577
    2000-01-05    1.036607
    2000-01-04   -0.136663
    2000-01-03   -0.143643
    2000-01-02   -0.718630
    2000-01-01    0.324097
    Freq: -1D, Name: A, dtype: float64




```python
# 赋值
s2 = s.copy()
s2
s2[:5] = 0
s2
```




    2000-01-01    0.324097
    2000-01-02   -0.718630
    2000-01-03   -0.143643
    2000-01-04   -0.136663
    2000-01-05    1.036607
    2000-01-06    0.362577
    2000-01-07    1.330468
    2000-01-08   -0.476653
    Freq: D, Name: A, dtype: float64






    2000-01-01    0.000000
    2000-01-02    0.000000
    2000-01-03    0.000000
    2000-01-04    0.000000
    2000-01-05    0.000000
    2000-01-06    0.362577
    2000-01-07    1.330468
    2000-01-08   -0.476653
    Freq: D, Name: A, dtype: float64




```python
# 对DataFrame操作
# [] 操作 选择的是行
df
df[:3]
df[::-1]
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>6</td>
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>6</td>
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Selection By Label
# 通过标签选择

# 这种方式可能依靠上下文关系，有时候会调用链式赋值，这应该避免。参考：
# Returning a view versus a copy 返回视图 对比 拷贝

# When setting values in a pandas object, 
# care must be taken to avoid what is called chained indexing. 
# Here is an example.

[list('abcd'),list('efgh'),list('ijkl'),list('mnop')]
[['one','two'],['first','second']]

dfmi = pd.DataFrame([list('abcd'),list('efgh'),list('ijkl'),list('mnop')],  # 定义四列数值
        columns=pd.MultiIndex.from_product(
         [['one','two'],['first','second']])) # 定义多重索引，第一个list是第一层，以下类推

dfmi

```




    [['a', 'b', 'c', 'd'],
     ['e', 'f', 'g', 'h'],
     ['i', 'j', 'k', 'l'],
     ['m', 'n', 'o', 'p']]






    [['one', 'two'], ['first', 'second']]






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
      <th colspan="2" halign="left">two</th>
    </tr>
    <tr>
      <th></th>
      <th>first</th>
      <th>second</th>
      <th>first</th>
      <th>second</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
      <td>c</td>
      <td>d</td>
    </tr>
    <tr>
      <th>1</th>
      <td>e</td>
      <td>f</td>
      <td>g</td>
      <td>h</td>
    </tr>
    <tr>
      <th>2</th>
      <td>i</td>
      <td>j</td>
      <td>k</td>
      <td>l</td>
    </tr>
    <tr>
      <th>3</th>
      <td>m</td>
      <td>n</td>
      <td>o</td>
      <td>p</td>
    </tr>
  </tbody>
</table>
</div>




```python
#  Compare these two access methods:
dfmi['one']['second']  # chained
dfmi.loc[:,('one','second')]
```




    0    b
    1    f
    2    j
    3    n
    Name: second, dtype: object






    0    b
    1    f
    2    j
    3    n
    Name: (one, second), dtype: object




```python
# 两种方式分析

# 第一种方式：链式 使用两个 []
dfmi['one']  # 第一个[] 先生成了一个DataFrame
dfmi['one']['second']  # pandas 把两个[] 作为分开的事件，他们执行分开的两步调用 __getitem__
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
      <th>first</th>
      <th>second</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
    </tr>
    <tr>
      <th>1</th>
      <td>e</td>
      <td>f</td>
    </tr>
    <tr>
      <th>2</th>
      <td>i</td>
      <td>j</td>
    </tr>
    <tr>
      <th>3</th>
      <td>m</td>
      <td>n</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 第二种方式：loc
# 通过嵌套的元组切片
df_s = (slice(None), ('one', 'second'))
dfmi.loc[df_s]  # 只调用了一次 __getitem__
```




    0    b
    1    f
    2    j
    3    n
    Name: (one, second), dtype: object




```python
# Selection By Label
# 通过标签选择

# loc要注意索引的数据类型，必须与索引的数据类型一致才可以，
# 例如 datetimeIndex 中，使用loc[2:3] ，即整数型的slice 将会出现TypeError


dfl = pd.DataFrame(np.random.randn(5,4), columns=list('ABCD'), 
                   index=pd.date_range('20130101',periods=5))

dfl
# dfl.loc[2:3]  # 错误的loc
dfl.loc['20130102':'20130104']  # 使用可转换为datetime的字符串
dfl.loc['20130202':'20130204']  # 不报错，返回为空DataFrame
# dfl.loc['20130202']  # 报错，错误信息是index无此值
dfl.loc['20130104':'20130114']  # 只返回存在的数据
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.887358</td>
      <td>1.068362</td>
      <td>0.551961</td>
      <td>-0.378400</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>1.239840</td>
      <td>-0.986149</td>
      <td>-0.880655</td>
      <td>2.112731</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.785526</td>
      <td>1.583703</td>
      <td>-0.871005</td>
      <td>-0.659880</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-1.267462</td>
      <td>2.500886</td>
      <td>-0.980569</td>
      <td>1.308624</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.842107</td>
      <td>-0.921086</td>
      <td>1.020196</td>
      <td>-0.055930</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1.239840</td>
      <td>-0.986149</td>
      <td>-0.880655</td>
      <td>2.112731</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.785526</td>
      <td>1.583703</td>
      <td>-0.871005</td>
      <td>-0.659880</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-1.267462</td>
      <td>2.500886</td>
      <td>-0.980569</td>
      <td>1.308624</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-04</th>
      <td>-1.267462</td>
      <td>2.500886</td>
      <td>-0.980569</td>
      <td>1.308624</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.842107</td>
      <td>-0.921086</td>
      <td>1.020196</td>
      <td>-0.055930</td>
    </tr>
  </tbody>
</table>
</div>




```python
# loc可以使用整数，但此时的整数不代表位置，而是label
# loc是基本的取值方法
# 给loc的输入，即在[]中的值，可以是：
# 1. 单独的label  e.g. 5 or 'a
# 2. labels的list   ['a', 'b', 'c']
# 3. slice对象  'a':'f'  !! 注意：与python的切片不同，pandas的切片包括开始和结尾，而python不包括结尾
# 4. 布尔值
# 5. 调用函数  [lambda df: df.A > 0, :]

# Series
s1 = pd.Series(np.random.randn(6),index=list('abcdef'))
s1
s1.loc['c':]
s1.loc['b']
s1.loc['c':] = 0
s1
```




    a    0.796911
    b   -1.341250
    c    0.008152
    d   -0.745881
    e    0.674385
    f    1.108411
    dtype: float64






    c    0.008152
    d   -0.745881
    e    0.674385
    f    1.108411
    dtype: float64






    -1.3412499335785426






    a    0.796911
    b   -1.341250
    c    0.000000
    d    0.000000
    e    0.000000
    f    0.000000
    dtype: float64




```python
# DataFrame
df1 = pd.DataFrame(np.random.randn(6,4),  # 6X4 阵列
                   index=list('abcdef'),  # 索引
                   columns=list('ABCD'))  # 行号
df1
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-1.912141</td>
      <td>-0.835589</td>
      <td>-0.188341</td>
      <td>-1.024797</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-0.977498</td>
      <td>-2.050214</td>
      <td>0.355172</td>
      <td>-0.291794</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-0.183401</td>
      <td>-0.376330</td>
      <td>-0.188848</td>
      <td>-2.116438</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.008359</td>
      <td>0.230593</td>
      <td>-0.099235</td>
      <td>-0.426229</td>
    </tr>
    <tr>
      <th>e</th>
      <td>-0.027338</td>
      <td>2.125459</td>
      <td>0.066200</td>
      <td>-0.247813</td>
    </tr>
    <tr>
      <th>f</th>
      <td>-1.132103</td>
      <td>1.945235</td>
      <td>1.891179</td>
      <td>1.549750</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.loc[['a', 'b', 'd'], :]  # 先是行label选择，再是列label选择
df1.loc['d':, 'A':'C']

# 取得 a cross section 截面，用单个的label，返回Series
# 以下三式等同
df1.loc['a']
df1.loc['a',:]
df1.xs('a')
type(df1.loc['a'])
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-1.912141</td>
      <td>-0.835589</td>
      <td>-0.188341</td>
      <td>-1.024797</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-0.977498</td>
      <td>-2.050214</td>
      <td>0.355172</td>
      <td>-0.291794</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.008359</td>
      <td>0.230593</td>
      <td>-0.099235</td>
      <td>-0.426229</td>
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
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>d</th>
      <td>-1.008359</td>
      <td>0.230593</td>
      <td>-0.099235</td>
    </tr>
    <tr>
      <th>e</th>
      <td>-0.027338</td>
      <td>2.125459</td>
      <td>0.066200</td>
    </tr>
    <tr>
      <th>f</th>
      <td>-1.132103</td>
      <td>1.945235</td>
      <td>1.891179</td>
    </tr>
  </tbody>
</table>
</div>






    A   -1.912141
    B   -0.835589
    C   -0.188341
    D   -1.024797
    Name: a, dtype: float64






    A   -1.912141
    B   -0.835589
    C   -0.188341
    D   -1.024797
    Name: a, dtype: float64






    A   -1.912141
    B   -0.835589
    C   -0.188341
    D   -1.024797
    Name: a, dtype: float64






    pandas.core.series.Series




```python
# 通过布尔值数组取值
df1.loc['a'] > 0
df1.loc[:, df1.loc['a'] > 0]
```




    A    False
    B    False
    C    False
    D    False
    Name: a, dtype: bool






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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
    </tr>
    <tr>
      <th>b</th>
    </tr>
    <tr>
      <th>c</th>
    </tr>
    <tr>
      <th>d</th>
    </tr>
    <tr>
      <th>e</th>
    </tr>
    <tr>
      <th>f</th>
    </tr>
  </tbody>
</table>
</div>




```python
# 获取一个值
# this is also equivalent to ``df1.at['a','A']``
df1.loc['a', 'A']
df1.at['a','A']
```




    -1.9121410098540752






    -1.9121410098540752




```python
# Slicing with labels¶
# 用labels切片
s = pd.Series(list('abcde'), index=[0,3,2,5,4])
s
s.loc[3:5]  # 包含 5， 注意不是 3 4 5 ，而是从 标签3 到 标签5
```




    0    a
    3    b
    2    c
    5    d
    4    e
    dtype: object






    3    b
    2    c
    5    d
    dtype: object




```python
# s.loc[3:6]  # 2个错误，ValueError: index must be monotonic increasing or decreasing  KeyError: 6
# 如果排序的话，可以超出范围
s.sort_index()  # 不改变原值
s
s.sort_index().loc[1:6]  # 可以超出范围
s.sort_index().loc[6:8]  # 即使一个都没有
# s.sort_index().loc[8]  # 但不能是单值，必须是切片
```




    0    a
    2    c
    3    b
    4    e
    5    d
    dtype: object






    0    a
    3    b
    2    c
    5    d
    4    e
    dtype: object






    2    c
    3    b
    4    e
    5    d
    dtype: object






    Series([], dtype: object)




```python
# Selection By Position
# 通过位置选择，仅通过基于索引的整数，与python和numpy类似，从0开始，且不包括最后一个
# iloc的输入：
# 1. 整数
# 2. 整数的list
# 3. 整数的切片
# 4. 布尔值数组
# 5. 调用函数

# Series
s1 = pd.Series(np.random.randn(5), index=list(range(0,10,2)))
s1
s1.iloc[:3]
s1.iloc[3]
s1.iloc[:3] = 0
s1
```




    0   -0.312716
    2    1.425936
    4    1.716575
    6    2.099666
    8    0.262365
    dtype: float64






    0   -0.312716
    2    1.425936
    4    1.716575
    dtype: float64






    2.099665679869975






    0    0.000000
    2    0.000000
    4    0.000000
    6    2.099666
    8    0.262365
    dtype: float64




```python
# DataFrame
df1 = pd.DataFrame(np.random.randn(6,4),
                  index=list(range(0,12,2)),
                  columns=list(range(0,8,2)))
df1
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
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.635993</td>
      <td>-0.512450</td>
      <td>1.786760</td>
      <td>-0.002533</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.173188</td>
      <td>0.275977</td>
      <td>-0.044987</td>
      <td>-1.077772</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.985020</td>
      <td>1.604020</td>
      <td>0.127853</td>
      <td>-1.003384</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.250428</td>
      <td>-0.102090</td>
      <td>1.566787</td>
      <td>-1.708521</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-2.111103</td>
      <td>-1.232141</td>
      <td>0.863753</td>
      <td>-0.545229</td>
    </tr>
    <tr>
      <th>10</th>
      <td>-1.762999</td>
      <td>1.009840</td>
      <td>0.274013</td>
      <td>0.786940</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.iloc[:3]
df1.iloc[1:5, 2:4]
df1.iloc[[1, 3, 5], [1, 3]]
df1.iloc[1:3, :]
df1.iloc[:, 1:3]
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
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.635993</td>
      <td>-0.512450</td>
      <td>1.786760</td>
      <td>-0.002533</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.173188</td>
      <td>0.275977</td>
      <td>-0.044987</td>
      <td>-1.077772</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.985020</td>
      <td>1.604020</td>
      <td>0.127853</td>
      <td>-1.003384</td>
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
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>-0.044987</td>
      <td>-1.077772</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.127853</td>
      <td>-1.003384</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.566787</td>
      <td>-1.708521</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.863753</td>
      <td>-0.545229</td>
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
      <th>2</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0.275977</td>
      <td>-1.077772</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.102090</td>
      <td>-1.708521</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.009840</td>
      <td>0.786940</td>
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
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0.173188</td>
      <td>0.275977</td>
      <td>-0.044987</td>
      <td>-1.077772</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.985020</td>
      <td>1.604020</td>
      <td>0.127853</td>
      <td>-1.003384</td>
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
      <th>2</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.512450</td>
      <td>1.786760</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.275977</td>
      <td>-0.044987</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.604020</td>
      <td>0.127853</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.102090</td>
      <td>1.566787</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-1.232141</td>
      <td>0.863753</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.009840</td>
      <td>0.274013</td>
    </tr>
  </tbody>
</table>
</div>




```python
# this is also equivalent to ``df1.iat[1,1]``
# 取单个的值
df1.iloc[1, 1]
df1.iat[1, 1]
```




    0.2759774784621013






    0.2759774784621013




```python
# For getting a cross section using an integer position (equiv to df.xs(1))
# 取截面，得到Series
df1.iloc[1]
df1.iloc[:,1]
```




    0    0.173188
    2    0.275977
    4   -0.044987
    6   -1.077772
    Name: 2, dtype: float64






    0    -0.512450
    2     0.275977
    4     1.604020
    6    -0.102090
    8    -1.232141
    10    1.009840
    Name: 2, dtype: float64




```python
# Out of range slice indexes are handled gracefully just as in Python/Numpy.
# 超过索引的切片处理，与python和numpy一样
# 注意：不能是单独索引，或列表中，有超过界限的值，只可以是slice，即带冒号的切片才不会提示错误

x = list('abcdef')
x[4:10]
x[8:10]
s = pd.Series(x)
s.iloc[4:10]
s.iloc[8:10]  # 超过界限bound返回空
```




    ['e', 'f']






    []






    4    e
    5    f
    dtype: object






    Series([], dtype: object)




```python
dfl = pd.DataFrame(np.random.randn(5,2), columns=list('AB'))
dfl
dfl.iloc[:, 2:3]
dfl.iloc[:, 1:3]
dfl.iloc[4:6]
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
      <td>-0.069941</td>
      <td>1.124145</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.025781</td>
      <td>0.940736</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.117417</td>
      <td>0.503736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.882286</td>
      <td>0.302845</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.136374</td>
      <td>0.276822</td>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
    </tr>
    <tr>
      <th>1</th>
    </tr>
    <tr>
      <th>2</th>
    </tr>
    <tr>
      <th>3</th>
    </tr>
    <tr>
      <th>4</th>
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
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.124145</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.940736</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.503736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.302845</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.276822</td>
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
      <th>4</th>
      <td>-0.136374</td>
      <td>0.276822</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Selection By Callable
# 通过调用函数进行选择

df1 = pd.DataFrame(np.random.randn(6,4),
                  index=list("abcdef"),
                  columns=list("ABCD"))
df1
df1.A
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-1.947578</td>
      <td>0.874286</td>
      <td>1.139484</td>
      <td>-3.004564</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.565255</td>
      <td>0.028440</td>
      <td>0.685688</td>
      <td>0.973264</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-1.275992</td>
      <td>0.732339</td>
      <td>-0.324490</td>
      <td>1.116887</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.433325</td>
      <td>0.002567</td>
      <td>-1.310127</td>
      <td>0.844756</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.341412</td>
      <td>-0.606646</td>
      <td>0.034623</td>
      <td>0.772968</td>
    </tr>
    <tr>
      <th>f</th>
      <td>1.518936</td>
      <td>-0.590351</td>
      <td>0.604839</td>
      <td>-1.461750</td>
    </tr>
  </tbody>
</table>
</div>






    a   -1.947578
    b    0.565255
    c   -1.275992
    d    0.433325
    e    0.341412
    f    1.518936
    Name: A, dtype: float64




```python
df1.loc[lambda df: df.A > 0, :]
df1.loc[:, lambda df: ['A', 'B']]
df1.iloc[:, lambda df: [0, 1]]
df1[lambda df: df.columns[0]]
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>0.565255</td>
      <td>0.028440</td>
      <td>0.685688</td>
      <td>0.973264</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.433325</td>
      <td>0.002567</td>
      <td>-1.310127</td>
      <td>0.844756</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.341412</td>
      <td>-0.606646</td>
      <td>0.034623</td>
      <td>0.772968</td>
    </tr>
    <tr>
      <th>f</th>
      <td>1.518936</td>
      <td>-0.590351</td>
      <td>0.604839</td>
      <td>-1.461750</td>
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
      <th>a</th>
      <td>-1.947578</td>
      <td>0.874286</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.565255</td>
      <td>0.028440</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-1.275992</td>
      <td>0.732339</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.433325</td>
      <td>0.002567</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.341412</td>
      <td>-0.606646</td>
    </tr>
    <tr>
      <th>f</th>
      <td>1.518936</td>
      <td>-0.590351</td>
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
      <th>a</th>
      <td>-1.947578</td>
      <td>0.874286</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.565255</td>
      <td>0.028440</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-1.275992</td>
      <td>0.732339</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.433325</td>
      <td>0.002567</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.341412</td>
      <td>-0.606646</td>
    </tr>
    <tr>
      <th>f</th>
      <td>1.518936</td>
      <td>-0.590351</td>
    </tr>
  </tbody>
</table>
</div>






    a   -1.947578
    b    0.565255
    c   -1.275992
    d    0.433325
    e    0.341412
    f    1.518936
    Name: A, dtype: float64




```python
df1.A
df1.A.loc[lambda s: s > 0]
df1.A.loc[df1.A > 0]
```




    a   -1.947578
    b    0.565255
    c   -1.275992
    d    0.433325
    e    0.341412
    f    1.518936
    Name: A, dtype: float64






    b    0.565255
    d    0.433325
    e    0.341412
    f    1.518936
    Name: A, dtype: float64






    b    0.565255
    d    0.433325
    e    0.341412
    f    1.518936
    Name: A, dtype: float64




```python
# 使用这些方法或索引，可以使用链式的选择方法，而不用中间的临时变量。链式方法，不是链式[]
bb = pd.read_csv('data/baseball.csv', index_col='id')
bb.groupby(['year', 'team']).sum().loc[lambda df: df.r > 100]
```


```python
# IX Indexer is Deprecated
# 不推荐使用ix
# in favor of the more strict .iloc and .loc indexers.
# 使用.iloc和.loc代替.ix

dfd = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]},index=list('abc'))
dfd
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
      <th>a</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfd.ix[[0, 2], 'A']
```

    d:\python\36-64\lib\site-packages\ipykernel_launcher.py:1: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
      """Entry point for launching an IPython kernel.
    




    a    1
    c    3
    Name: A, dtype: int64




```python
dfd.index[[0, 2]]  # 取得索引的名称
dfd.loc[dfd.index[[0, 2]], 'A']
dfd.columns.get_loc('A')  # 取得列的索引值
dfd.iloc[[0, 2], dfd.columns.get_loc('A')]
```




    Index(['a', 'c'], dtype='object')






    a    1
    c    3
    Name: A, dtype: int64






    0






    a    1
    c    3
    Name: A, dtype: int64




```python
# Indexing with list with missing labels is Deprecated
# 不推荐用有缺失标签的list进行索引
# using .loc or [] with a list with one or more missing labels, is deprecated, in favor of .reindex.
# 推荐使用.reindex

s = pd.Series([1, 2, 3])
s
```




    0    1
    1    2
    2    3
    dtype: int64




```python
s.loc[[1, 2]]  # list中的keys都存在，则没有变化
```




    1    2
    2    3
    dtype: int64




```python
s.loc[[1, 2, 3]]  # 当有缺失时，赋值为NaN 
```

    d:\python\36-64\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: 
    Passing list-likes to .loc or [] with any missing label will raise
    KeyError in the future, you can use .reindex() as an alternative.
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate-loc-reindex-listlike
      """Entry point for launching an IPython kernel.
    




    1    2.0
    2    3.0
    3    NaN
    dtype: float64




```python
# Reindexing

s.reindex([1, 2, 3])
```




    1    2.0
    2    3.0
    3    NaN
    dtype: float64




```python
# 如果仅选择有效的keys
labels = [1, 2, 3]
s.index.intersection(labels)  # index和labes的交集
s.loc[s.index.intersection(labels)]
```




    Int64Index([1, 2], dtype='int64')






    1    2
    2    3
    dtype: int64




```python
# reindex 索引中不能有重复的项
s = pd.Series(np.arange(4), index=['a', 'a', 'b', 'c'])
s
labels = ['c', 'd']
# s.reindex(labels)  # 不能reindex
```




    a    0
    a    1
    b    2
    c    3
    dtype: int32




```python
# 可以先把交集切出来，再进行reindex
# 但是交集不能有重复的index
s.index.intersection(labels)
s.loc[s.index.intersection(labels)]
s.loc[s.index.intersection(labels)].reindex(labels)
```




    Index(['c'], dtype='object')






    c    3
    dtype: int32






    c    3.0
    d    NaN
    dtype: float64




```python
# Selecting Random Samples
# 随机取样选择
# 默认行取样

s = pd.Series([0,1,2,3,4,5])
s
```




    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64




```python
s.sample()  # 默认取1行
s.sample(n=3)  # 取3行
s.sample(frac=0.5)  # 小数，行数百分数
s.sample(frac=0.8)  # 小数
s
```




    1    1
    dtype: int64






    3    3
    4    4
    5    5
    dtype: int64






    2    2
    3    3
    4    4
    dtype: int64






    2    2
    1    1
    3    3
    0    0
    5    5
    dtype: int64






    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64




```python
s.sample(n=6, replace=False)  # 默认
s.sample(n=6, replace=True)  # replace，不改变本身
s
```




    5    5
    4    4
    1    1
    0    0
    2    2
    3    3
    dtype: int64






    0    0
    4    4
    0    0
    2    2
    0    0
    0    0
    dtype: int64






    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64




```python
# 默认每行都有同样的概率被抽样到，也可以指定每行的概率比重
example_weights = [0, 0, 0.2, 0.2, 0.2, 0.4]
s.sample(n=3, weights=example_weights)

example_weights2 = [0.5, 0, 0, 0, 0, 0]  # 权重将会自动的归一化
s.sample(n=1, weights=example_weights2)
```




    2    2
    3    3
    5    5
    dtype: int64






    0    0
    dtype: int64




```python
# 可以指定DataFrame的某列作为权重
df2 = pd.DataFrame({'col1':[9,8,7,6], 'weight_column':[0.5, 0.4, 0.1, 0]})
df2.sample(n = 3, weights = 'weight_column')
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
      <th>col1</th>
      <th>weight_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 对列进行抽样
df3 = pd.DataFrame({'col1':[1,2,3], 'col2':[2,3,4], 'col3':[3,4,5]})
df3
df3.sample(n=2, axis=1)  # 指定axis=1，对列抽样，抽取的是列的组合
df3.sample(n=2, axis=0)
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
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
      <th>col3</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>4</td>
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 可以指定random seed 或者 numpy 的 randomState 对象，作为sample 随机数生成器的种子
# 一旦seed确定，随机数不变
df3.sample(n=2, random_state=2)
df3.sample(n=2, random_state=2)
df3.sample(n=2, random_state=200)
df3.sample(n=2, random_state=200)
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Setting With Enlargement
# loc或[] 操作 可以通过赋值不存在的键扩大Series或Dataframe

# Series
se = pd.Series([1,2,3])
se
se[5] = 5  # append
se
```




    0    1
    1    2
    2    3
    dtype: int64






    0    1
    1    2
    2    3
    5    5
    dtype: int64




```python
# DataFrame

dfi = pd.DataFrame(np.arange(6).reshape(3,2),columns=['A','B'])
dfi
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
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfi.loc[:,'C'] = dfi.loc[:,'A']  # enlarge 增加列
dfi
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfi.loc[3] = 5  # append 增加行
dfi
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Fast scalar value getting and setting
# 快速取得或设置标量的值
# [] 可以进行很多操作，所以它为了知道你要进行那种操作，会有一点计算开销
# 最快的标量访问方式是使用 at 和 iat 方法，他们可以在所有的数据结构上使用
# at 类似于 loc 基于 label
# iat 类似于 iloc 基于 整数index
s = pd.Series([0,1,2,3,4,5])
s
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df
```




    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64






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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.845046</td>
      <td>-0.119758</td>
      <td>1.354224</td>
      <td>-0.134199</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.935579</td>
      <td>-1.469185</td>
      <td>-2.581439</td>
      <td>0.355347</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.038740</td>
      <td>-1.524056</td>
      <td>1.376257</td>
      <td>1.572331</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.846971</td>
      <td>0.189231</td>
      <td>-0.287885</td>
      <td>-0.561706</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.127290</td>
      <td>-0.043918</td>
      <td>0.103347</td>
      <td>-1.055387</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.406437</td>
      <td>1.917624</td>
      <td>0.810463</td>
      <td>0.367583</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.438904</td>
      <td>-0.230190</td>
      <td>0.593607</td>
      <td>-0.438856</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-1.955122</td>
      <td>1.531260</td>
      <td>0.889124</td>
      <td>-0.014259</td>
    </tr>
  </tbody>
</table>
</div>




```python
# get value
s.iat[5]
df.at[dates[5], 'A']
df.iat[3, 0]
```




    5






    0.40643702489386246






    -0.8469710793801154




```python
# set value
df.at[dates[5], 'E'] = 7  # 没有列就增加一列，没有值的默认赋值为nan
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
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.845046</td>
      <td>-0.119758</td>
      <td>1.354224</td>
      <td>-0.134199</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.935579</td>
      <td>-1.469185</td>
      <td>-2.581439</td>
      <td>0.355347</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.038740</td>
      <td>-1.524056</td>
      <td>1.376257</td>
      <td>1.572331</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.846971</td>
      <td>0.189231</td>
      <td>-0.287885</td>
      <td>-0.561706</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.127290</td>
      <td>-0.043918</td>
      <td>0.103347</td>
      <td>-1.055387</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.406437</td>
      <td>1.917624</td>
      <td>0.810463</td>
      <td>0.367583</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.438904</td>
      <td>-0.230190</td>
      <td>0.593607</td>
      <td>-0.438856</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-1.955122</td>
      <td>1.531260</td>
      <td>0.889124</td>
      <td>-0.014259</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iat[3, 0] = 7
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
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.845046</td>
      <td>-0.119758</td>
      <td>1.354224</td>
      <td>-0.134199</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.935579</td>
      <td>-1.469185</td>
      <td>-2.581439</td>
      <td>0.355347</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.038740</td>
      <td>-1.524056</td>
      <td>1.376257</td>
      <td>1.572331</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>7.000000</td>
      <td>0.189231</td>
      <td>-0.287885</td>
      <td>-0.561706</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.127290</td>
      <td>-0.043918</td>
      <td>0.103347</td>
      <td>-1.055387</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.406437</td>
      <td>1.917624</td>
      <td>0.810463</td>
      <td>0.367583</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.438904</td>
      <td>-0.230190</td>
      <td>0.593607</td>
      <td>-0.438856</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-1.955122</td>
      <td>1.531260</td>
      <td>0.889124</td>
      <td>-0.014259</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.at[dates[-1]+1, 0] = 7  # 行和列都扩展了
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
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.845046</td>
      <td>-0.119758</td>
      <td>1.354224</td>
      <td>-0.134199</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.935579</td>
      <td>-1.469185</td>
      <td>-2.581439</td>
      <td>0.355347</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.038740</td>
      <td>-1.524056</td>
      <td>1.376257</td>
      <td>1.572331</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>7.000000</td>
      <td>0.189231</td>
      <td>-0.287885</td>
      <td>-0.561706</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.127290</td>
      <td>-0.043918</td>
      <td>0.103347</td>
      <td>-1.055387</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.406437</td>
      <td>1.917624</td>
      <td>0.810463</td>
      <td>0.367583</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.438904</td>
      <td>-0.230190</td>
      <td>0.593607</td>
      <td>-0.438856</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-1.955122</td>
      <td>1.531260</td>
      <td>0.889124</td>
      <td>-0.014259</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-09</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Boolean indexing
# 使用布尔向量过滤数据
# 操作符包括：| for or, & for and, and ~ for not ，必须用括号进行分组

```


```python
s = pd.Series(range(-3, 4))  # 不用把range先list，直接可以series
s
```




    0   -3
    1   -2
    2   -1
    3    0
    4    1
    5    2
    6    3
    dtype: int64




```python
s[s >= 0]  # 直接用series，不用取其值
s[~(s < 0)]
s[(s < -1) | (s > 0.5)]

```




    3    0
    4    1
    5    2
    6    3
    dtype: int64






    3    0
    4    1
    5    2
    6    3
    dtype: int64






    0   -3
    1   -2
    4    1
    5    2
    6    3
    dtype: int64




```python
df[df['A'] > 0]
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
      <th>D</th>
      <th>E</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.845046</td>
      <td>-0.119758</td>
      <td>1.354224</td>
      <td>-0.134199</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>7.000000</td>
      <td>0.189231</td>
      <td>-0.287885</td>
      <td>-0.561706</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.406437</td>
      <td>1.917624</td>
      <td>0.810463</td>
      <td>0.367583</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.438904</td>
      <td>-0.230190</td>
      <td>0.593607</td>
      <td>-0.438856</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# List comprehensions and map method of Series can also be used to produce more complex criteria:
# 列表生成式和map方法 也可以用来生成 更复杂的条件判断

df2 = pd.DataFrame({'a' : ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                     'b' : ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                     'c' : np.random.randn(7)})
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>x</td>
      <td>1.706402</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>y</td>
      <td>0.491977</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>y</td>
      <td>1.357986</td>
    </tr>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>x</td>
      <td>-1.023513</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>y</td>
      <td>-0.653028</td>
    </tr>
    <tr>
      <th>5</th>
      <td>one</td>
      <td>x</td>
      <td>0.041052</td>
    </tr>
    <tr>
      <th>6</th>
      <td>six</td>
      <td>x</td>
      <td>1.021882</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 判别式
criterion = df2['a'].map(lambda x: x.startswith('t'))  # 选择 two 和 three
criterion
```




    0    False
    1    False
    2     True
    3     True
    4     True
    5    False
    6    False
    Name: a, dtype: bool




```python
df2[criterion]  # 根据 a 列的判别式 选择数据表的一部分，包含其他列
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>y</td>
      <td>1.357986</td>
    </tr>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>x</td>
      <td>-1.023513</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>y</td>
      <td>-0.653028</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 等价的方式，但是速度慢一些 
df2[[x.startswith('t') for x in df2['a']]]  # 不适用map，而是用列表生成式
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>y</td>
      <td>1.357986</td>
    </tr>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>x</td>
      <td>-1.023513</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>y</td>
      <td>-0.653028</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 复合判断
df2[criterion & (df2['b'] == 'x')]  # a 列 和 b 列 均符合某类要求
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>x</td>
      <td>-1.023513</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 布尔向量选择 可以与索引选择一并使用
df2.loc[criterion & (df2['b'] == 'x'),'b':'c']  # 只选择 b 和 c 两列，不选择c列

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
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>x</td>
      <td>-1.023513</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Indexing with isin
# 用isin索引

```


```python
# series
# 对列数据进行判断
s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
s
```




    4    0
    3    1
    2    2
    1    3
    0    4
    dtype: int64




```python
s.isin([2, 4, 6])  # 列数据中是否存在列表中的值，返回布尔值
s[s.isin([2, 4, 6])]  # 可以利用返回的布尔值进行选择
```




    4    False
    3    False
    2     True
    1    False
    0     True
    dtype: bool






    2    2
    0    4
    dtype: int64




```python
# 也可以对index obj 进行筛选
s[s.index.isin([2, 4, 6])]
s.reindex([2, 4, 6])  # reindex不同，列表中没有的值返回了nan，且原来的int64返回了float64数据类型
```




    4    0
    2    2
    dtype: int64






    2    2.0
    4    0.0
    6    NaN
    dtype: float64




```python
# 对应多重索引，可以单独选择索引级别
s_mi = pd.Series(np.arange(6),index=pd.MultiIndex.from_product([[0, 1], ['a', 'b', 'c']]))
s_mi
```




    0  a    0
       b    1
       c    2
    1  a    3
       b    4
       c    5
    dtype: int32




```python
s_mi.iloc[s_mi.index.isin([(1, 'a'), (2, 'b'), (0, 'c')])]
s_mi.iloc[s_mi.index.isin(['a', 'c', 'e'], level=1)]  # 指定索引级别，在第二级索引中选择
```




    0  c    2
    1  a    3
    dtype: int32






    0  a    0
       c    2
    1  a    3
       c    5
    dtype: int32




```python
# DataFrame
df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'],'ids2': ['a', 'n', 'c', 'n']})
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
      <th>ids</th>
      <th>ids2</th>
      <th>vals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>n</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>f</td>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>n</td>
      <td>n</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
values = ['a', 'b', 1, 3]
df.isin(values)  # 匹配所有的值
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
      <th>ids</th>
      <th>ids2</th>
      <th>vals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}
row_mask = df.isin(values)  # 对不用的列，分别匹配某些值
row_mask
# ?row_mask.all  # Return whether all elements are True over requested axis
row_mask = row_mask.all(1)
row_mask
df[row_mask]  # 选择全是True的行
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
      <th>ids</th>
      <th>ids2</th>
      <th>vals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>






    0     True
    1    False
    2    False
    3    False
    dtype: bool






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
      <th>ids</th>
      <th>ids2</th>
      <th>vals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The where() Method and Masking
# To guarantee that selection output has the same shape as the original data
# 保证选集输出与原数据有同样的shape形态

# series
s
s[s > 0]  # 只返回满足的项
s.where(s > 0)  # 全部返回，不满足的项，赋值nan
```




    4    0
    3    1
    2    2
    1    3
    0    4
    dtype: int64






    3    1
    2    2
    1    3
    0    4
    dtype: int64






    4    NaN
    3    1.0
    2    2.0
    1    3.0
    0    4.0
    dtype: float64




```python
# DataFrame 使用布尔值选择时，返回值保留原数据结构
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df < 0]
df.where(df < 0)  # 等价于上式
df.where(df < 0, -df)  # where 可以传入另一个参数，用于替换条件为 False 的项，返回copy数据拷贝，不修改原值
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>NaN</td>
      <td>-0.500453</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>NaN</td>
      <td>-0.295425</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>NaN</td>
      <td>-1.084442</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>NaN</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>NaN</td>
      <td>-0.500453</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>NaN</td>
      <td>-0.295425</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>NaN</td>
      <td>-1.084442</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>NaN</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.383691</td>
      <td>-0.500453</td>
      <td>-0.101632</td>
      <td>-0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>-0.856605</td>
      <td>-0.295425</td>
      <td>-1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>-0.278514</td>
      <td>-1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>-1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.656919</td>
      <td>-1.081810</td>
      <td>-1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>-0.533706</td>
      <td>-1.084442</td>
      <td>-1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>-0.565496</td>
      <td>-0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
    </tr>
  </tbody>
</table>
</div>




```python
# You may wish to set values based on some boolean criteria. This can be done intuitively like so:
# 设置基于布尔值的项值

s2 = s.copy()
s2
s2[s2 < 3] = 0
s2
df2 = df.copy()
df2
df2[df2 < 0] = 0
df2
```




    4    0
    3    1
    2    2
    1    3
    0    4
    dtype: int64






    4    0
    3    0
    2    0
    1    3
    0    4
    dtype: int64






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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>0.000000</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.000000</td>
      <td>0.856605</td>
      <td>0.000000</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.000000</td>
      <td>0.533706</td>
      <td>0.000000</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# where 默认返回修改后的数据拷贝，原值不变；可以设置inplace参数，直接修改原值，而不是创建拷贝

df_orig = df.copy()
df_orig.where(df > 0, -df, inplace=True)
df_orig
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>1.048619</td>
      <td>0.856605</td>
      <td>0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>0.214918</td>
      <td>1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>2.326385</td>
      <td>0.225754</td>
      <td>1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>1.041194</td>
      <td>0.533706</td>
      <td>1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.040706</td>
      <td>2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>0.075381</td>
      <td>0.951126</td>
      <td>0.347865</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 注意 ：pandas 和 numpy 的where方法不一样
# 一般的，df1.where(m, df2)  相当于 np.where(m, df1, df2)

df.where(df < 0, -df) == np.where(df < 0, df, -df)
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# alignment 定位，对齐
# where 可以选择局部（部分区域）的布尔条件  
# This is analogous to partial setting via .loc (but on the contents rather than the axis labels)

df2 = df.copy()
df2
df2[1:4]   # 行选择
df2.where(df2[1:4] > 0, 3)  # 对不符合项的值进行赋值！
df2[ df2[1:4] > 0 ] = 3  # 只定位部分区域，对符合项的值进行赋值
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>3.0</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>3.0</td>
      <td>0.856605</td>
      <td>3.000000</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>3.0</td>
      <td>3.000000</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>3.0</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>3.0</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>3.0</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>3.0</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>3.0</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>3.000000</td>
      <td>-0.295425</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Where can also accept axis and level parameters to align the input when performing the where.
# where 可以接受 轴参数axis 和 级别参数level 
df2 = df.copy()
df2
df2.where(df2>0,df2['A'],axis='index')  # 小于等于0的值，赋值为A列的值
df2
df2.apply(lambda x, y: x.where(x>0,y), y=df['A'])  # 相当于上式，但此式较慢，同样不改变原值，而是生成一个拷贝copy
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>0.383691</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-1.048619</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-0.214918</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-2.326385</td>
      <td>-2.326385</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>0.656919</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.041194</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-1.040706</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>0.166739</td>
      <td>0.166739</td>
      <td>0.166739</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>0.383691</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-1.048619</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-0.214918</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-2.326385</td>
      <td>-2.326385</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>0.656919</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.041194</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-1.040706</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>0.166739</td>
      <td>0.166739</td>
      <td>0.166739</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
    </tr>
  </tbody>
</table>
</div>




```python
# where 可以接受一个函数调用，此函数只能有一个参数，且返回有效的布尔条件
df3 = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6],'C': [7, 8, 9]})
df3
df3.where(lambda x: x > 4, lambda x: x + 10)  # x<=4 的值 赋值为  x+10
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
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
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11</td>
      <td>14</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# mask 遮罩 mask is the inverse boolean operation of where. 反向的布尔值操作
s
s.mask(s >= 0)  # 选择<0 的值， 不符合项 置为nan
df
df.mask(df >= 0)
```




    4    0
    3    1
    2    2
    1    3
    0    4
    dtype: int64






    4   NaN
    3   NaN
    2   NaN
    1   NaN
    0   NaN
    dtype: float64






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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.383691</td>
      <td>-0.500453</td>
      <td>0.101632</td>
      <td>0.848213</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>0.856605</td>
      <td>-0.295425</td>
      <td>1.060710</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>0.278514</td>
      <td>1.088771</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>1.457230</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.656919</td>
      <td>1.081810</td>
      <td>1.148303</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>0.533706</td>
      <td>-1.084442</td>
      <td>1.824709</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>0.565496</td>
      <td>0.269414</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.166739</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>NaN</td>
      <td>-0.500453</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.048619</td>
      <td>NaN</td>
      <td>-0.295425</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.214918</td>
      <td>-1.989228</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.326385</td>
      <td>-0.225754</td>
      <td>-1.331598</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.089382</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-1.041194</td>
      <td>NaN</td>
      <td>-1.084442</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-1.040706</td>
      <td>-2.336161</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>NaN</td>
      <td>-0.075381</td>
      <td>-0.951126</td>
      <td>-0.347865</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The query() Method (Experimental) 对 DataFrame对象 使用表达式进行选择

# 例如 ：选择b列中 在a列和c列两值中间的 行,a<b<c
n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.283094</td>
      <td>0.051807</td>
      <td>0.126487</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.020097</td>
      <td>0.373023</td>
      <td>0.147193</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.091921</td>
      <td>0.830956</td>
      <td>0.143214</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.340304</td>
      <td>0.527246</td>
      <td>0.709769</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.651722</td>
      <td>0.344524</td>
      <td>0.151233</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.396685</td>
      <td>0.524376</td>
      <td>0.540237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.502751</td>
      <td>0.627708</td>
      <td>0.708038</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.472338</td>
      <td>0.269770</td>
      <td>0.586165</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.937522</td>
      <td>0.239560</td>
      <td>0.861873</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.661879</td>
      <td>0.465536</td>
      <td>0.271580</td>
    </tr>
  </tbody>
</table>
</div>




```python
# pure python
df[(df.a < df.b) & (df.b < df.c)]

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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>0.340304</td>
      <td>0.527246</td>
      <td>0.709769</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.396685</td>
      <td>0.524376</td>
      <td>0.540237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.502751</td>
      <td>0.627708</td>
      <td>0.708038</td>
    </tr>
  </tbody>
</table>
</div>




```python
# query，传入的是str表达式
df.query('(a < b) & (b < c)')  # 比纯py慢？！
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>0.340304</td>
      <td>0.527246</td>
      <td>0.709769</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.396685</td>
      <td>0.524376</td>
      <td>0.540237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.502751</td>
      <td>0.627708</td>
      <td>0.708038</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 对于命名的index索引是低效的，比利用列名称
# 而且如果索引的名称和列名同名，列名优先
df = pd.DataFrame(np.random.randint(n / 2, size=(n, 2)), columns=list('bc'))
# df
df.index.name = "a"
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
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query('a <= b and b <= c')
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
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 可以不使用索引的名称，而是直接用index，这样同时可以避免与列名重名
df.query('index <= b <= c')
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
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# MultiIndex query() Syntax
# 对于多重索引

n = 10
colors = np.random.choice(['red', 'green'], size=n)
colors
foods = np.random.choice(['eggs', 'ham'], size=n)
foods
```




    array(['green', 'green', 'green', 'green', 'green', 'green', 'green',
           'red', 'green', 'green'], dtype='<U5')






    array(['ham', 'eggs', 'eggs', 'eggs', 'eggs', 'ham', 'eggs', 'eggs',
           'ham', 'ham'], dtype='<U4')




```python
index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])
index
df = pd.DataFrame(np.random.randn(n, 2), index=index)
df
```




    MultiIndex(levels=[['green', 'red'], ['eggs', 'ham']],
               labels=[[0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 1, 1]],
               names=['color', 'food'])






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
    <tr>
      <th>color</th>
      <th>food</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="7" valign="top">green</th>
      <th>ham</th>
      <td>-0.295761</td>
      <td>1.399719</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>1.807185</td>
      <td>0.498136</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>-0.119640</td>
      <td>2.279162</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>-0.238709</td>
      <td>-0.650418</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>2.235827</td>
      <td>1.066954</td>
    </tr>
    <tr>
      <th>ham</th>
      <td>1.156794</td>
      <td>1.694717</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>-0.037158</td>
      <td>-0.529213</td>
    </tr>
    <tr>
      <th>red</th>
      <th>eggs</th>
      <td>0.046799</td>
      <td>0.763592</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">green</th>
      <th>ham</th>
      <td>0.488240</td>
      <td>-0.455112</td>
    </tr>
    <tr>
      <th>ham</th>
      <td>-0.169486</td>
      <td>-0.646891</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query('color == "red"')
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
    <tr>
      <th>color</th>
      <th>food</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <th>eggs</th>
      <td>0.046799</td>
      <td>0.763592</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 如果多重索引没有命名 可以使用特殊的名字
df.index.names = [None, None]
df
df.query('ilevel_0 == "red"') # The convention is ilevel_0, which means “index level 0” for the 0th level of the index.
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
      <th rowspan="7" valign="top">green</th>
      <th>ham</th>
      <td>-0.295761</td>
      <td>1.399719</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>1.807185</td>
      <td>0.498136</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>-0.119640</td>
      <td>2.279162</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>-0.238709</td>
      <td>-0.650418</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>2.235827</td>
      <td>1.066954</td>
    </tr>
    <tr>
      <th>ham</th>
      <td>1.156794</td>
      <td>1.694717</td>
    </tr>
    <tr>
      <th>eggs</th>
      <td>-0.037158</td>
      <td>-0.529213</td>
    </tr>
    <tr>
      <th>red</th>
      <th>eggs</th>
      <td>0.046799</td>
      <td>0.763592</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">green</th>
      <th>ham</th>
      <td>0.488240</td>
      <td>-0.455112</td>
    </tr>
    <tr>
      <th>ham</th>
      <td>-0.169486</td>
      <td>-0.646891</td>
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
      <th>red</th>
      <th>eggs</th>
      <td>0.046799</td>
      <td>0.763592</td>
    </tr>
  </tbody>
</table>
</div>




```python
# query() Use Cases 使用示例
# A use case for query() is when you have a collection of DataFrame objects 
# that have a subset of column names (or index levels/names) in common.   ## 有公共列名称子集的df
# You can pass the same query to both frames 
# without having to specify which frame you’re interested in querying.  ## 传入同样的query
```


```python
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
df2 = pd.DataFrame(np.random.rand(n + 2, 3), columns=df.columns)
df
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.096087</td>
      <td>0.799309</td>
      <td>0.112070</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.083101</td>
      <td>0.505151</td>
      <td>0.830588</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.501472</td>
      <td>0.692792</td>
      <td>0.663570</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.872821</td>
      <td>0.442541</td>
      <td>0.904903</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.513651</td>
      <td>0.375617</td>
      <td>0.786898</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.184368</td>
      <td>0.285290</td>
      <td>0.055147</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.284951</td>
      <td>0.243556</td>
      <td>0.732871</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.431525</td>
      <td>0.676385</td>
      <td>0.458296</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.743057</td>
      <td>0.326079</td>
      <td>0.434655</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.610921</td>
      <td>0.717639</td>
      <td>0.580765</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.804932</td>
      <td>0.533058</td>
      <td>0.713190</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.305893</td>
      <td>0.460048</td>
      <td>0.879321</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.344438</td>
      <td>0.970870</td>
      <td>0.685098</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.348010</td>
      <td>0.839449</td>
      <td>0.799309</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.844713</td>
      <td>0.267562</td>
      <td>0.771202</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.403534</td>
      <td>0.088786</td>
      <td>0.950782</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.181616</td>
      <td>0.567118</td>
      <td>0.989711</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.363736</td>
      <td>0.852080</td>
      <td>0.140771</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.866127</td>
      <td>0.285365</td>
      <td>0.025491</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.329751</td>
      <td>0.121716</td>
      <td>0.782729</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.029253</td>
      <td>0.419409</td>
      <td>0.051255</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.057406</td>
      <td>0.106595</td>
      <td>0.559687</td>
    </tr>
  </tbody>
</table>
</div>




```python
expr = '0.0 <= a <= c <= 0.5'
mp = map(lambda frame: frame.query(expr), [df, df2])  # 同一个表达式，作用在有同样列名的多个df上
```


```python
for i in mp:
    print(i)
```

              a         b         c
    0  0.096087  0.799309  0.112070
    7  0.431525  0.676385  0.458296
               a         b         c
    10  0.029253  0.419409  0.051255
    


```python
# query() Python versus pandas Syntax Comparison


# Full numpy-like syntax
df = pd.DataFrame(np.random.randint(n, size=(n, 3)), columns=list('abc'))
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>8</td>
      <td>7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5</td>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>7</td>
      <td>1</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
 df.query('(a < b) & (b < c)')
 df[(df.a < df.b) & (df.b < df.c)]   
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>8</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 几种其他的不同的写法
df.query('a < b & b < c')  # 去掉括号
df.query('a < b and b < c')  # 使用英文and
df.query('a < b < c')  # 连写，优雅的表达
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>8</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>8</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The in and not in operators

# get all rows where columns "a" and "b" have overlapping values 
# 得到a列和b列有重叠值的行，a列中的值在 in b列的值中
df = pd.DataFrame({'a': list('aabbccddeeff'), 'b': list('aaaabbbbcccc'),
                       'c': np.random.randint(5, size=12),
                       'd': np.random.randint(9, size=12)})
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>a</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>d</td>
      <td>b</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>e</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>f</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>f</td>
      <td>c</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query('a in b')  # 第一次运行113ms 第二次明显加快 25ms
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>a</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df.a.isin(df.b)]   # How you'd do it in pure Python  仍然比query快 35ms
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>a</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[~df.a.isin(df.b)]
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>d</td>
      <td>b</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>e</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>f</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>f</td>
      <td>c</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query('a not in b')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>d</td>
      <td>b</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>e</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>f</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>f</td>
      <td>c</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# rows where cols a and b have overlapping values and col c's values are less than col d's
df.query('a in b and c < d')
df[df.a.isin(df.b) & (df.c < df.d)]
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 注意：？？？？？
# Note that in and not in are evaluated in Python, since numexpr has no equivalent of this operation. 
# However, only the in/not in expression itself is evaluated in vanilla Python. 
# For example, in the expression
df.query('a in b + c + d')
# (b + c + d) is evaluated by numexpr and then the in operation is evaluated in plain Python. In general, any operations that can be evaluated using numexpr will be.
```


```python
# Special use of the == operator with list objects
# 特别的用法，== 用于list
# Comparing a list of values to a column using ==/!= works similarly to in/not in
# 用==/!=比较列表的值与列的值，类似于in/not in
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>a</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>d</td>
      <td>b</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>e</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>f</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>f</td>
      <td>c</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query('b == ["a", "b", "c"]')  # b列中有列表中值的
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>a</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>a</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>d</td>
      <td>b</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>e</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>f</td>
      <td>c</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>f</td>
      <td>c</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query('c == [1, 2]')
df.query('[1, 2] in c')
df[df.c.isin([1, 2])]
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>b</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>b</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>e</td>
      <td>c</td>
      <td>2</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Boolean Operators 布尔操作符
# ~ 或 not
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
df
df['bools'] = np.random.rand(len(df)) > 0.5
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.528671</td>
      <td>0.265870</td>
      <td>0.932892</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.520069</td>
      <td>0.047895</td>
      <td>0.478818</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.648595</td>
      <td>0.180744</td>
      <td>0.838445</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.145614</td>
      <td>0.906190</td>
      <td>0.762163</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.612637</td>
      <td>0.027232</td>
      <td>0.778020</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.640565</td>
      <td>0.535538</td>
      <td>0.018280</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.633664</td>
      <td>0.124654</td>
      <td>0.185709</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.635088</td>
      <td>0.377300</td>
      <td>0.914968</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.702684</td>
      <td>0.504459</td>
      <td>0.107014</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.635757</td>
      <td>0.261144</td>
      <td>0.665611</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>bools</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.528671</td>
      <td>0.265870</td>
      <td>0.932892</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.520069</td>
      <td>0.047895</td>
      <td>0.478818</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.648595</td>
      <td>0.180744</td>
      <td>0.838445</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.145614</td>
      <td>0.906190</td>
      <td>0.762163</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.612637</td>
      <td>0.027232</td>
      <td>0.778020</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.640565</td>
      <td>0.535538</td>
      <td>0.018280</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.633664</td>
      <td>0.124654</td>
      <td>0.185709</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.635088</td>
      <td>0.377300</td>
      <td>0.914968</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.702684</td>
      <td>0.504459</td>
      <td>0.107014</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.635757</td>
      <td>0.261144</td>
      <td>0.665611</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query('~bools')
df.query('not bools')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>bools</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.528671</td>
      <td>0.265870</td>
      <td>0.932892</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.145614</td>
      <td>0.906190</td>
      <td>0.762163</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.702684</td>
      <td>0.504459</td>
      <td>0.107014</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.635757</td>
      <td>0.261144</td>
      <td>0.665611</td>
      <td>False</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>bools</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.528671</td>
      <td>0.265870</td>
      <td>0.932892</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.145614</td>
      <td>0.906190</td>
      <td>0.762163</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.702684</td>
      <td>0.504459</td>
      <td>0.107014</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.635757</td>
      <td>0.261144</td>
      <td>0.665611</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 任意组合布尔表达式
shorter = df.query('a < b < c and (not bools) or bools > 2')  # short query syntax
longer = df[(df.a < df.b) & (df.b < df.c) & (~df.bools) | (df.bools > 2)]  # equivalent in pure Python
shorter
longer
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>bools</th>
    </tr>
  </thead>
  <tbody>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>bools</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
# Performance of query()
# DataFrame.query() using numexpr is slightly faster than Python for large frames
# Note : You will only see the performance benefits of using the numexpr engine with DataFrame.query() 
# if your frame has more than approximately 200,000 rows

# query() 效能在大数据时高于数字表达式

```


```python
# Duplicate Data
# 识别和剔除重复数据，两个方法：duplicated and drop_duplicates，他们的参数都是列
# duplicated 返回布尔向量，标示重复的行
# drop_duplicates 删除重复列
# 默认保留第一个找到的值，但可以通过keep参数指定保留的值
# keep='first' (default): mark / drop duplicates except for the first occurrence. 只保留第一个
# keep='last': mark / drop duplicates except for the last occurrence. 只保留最后一个重复值
# keep=False: mark / drop all duplicates.  剔除所有重复值

```


```python
df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'two', 'two', 'three', 'four'],
                    'b': ['x', 'y', 'x', 'y', 'x', 'x', 'x'],
                    'c': np.random.randn(7)})
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>x</td>
      <td>2.206877</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>y</td>
      <td>-1.852209</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>x</td>
      <td>-0.706555</td>
    </tr>
    <tr>
      <th>3</th>
      <td>two</td>
      <td>y</td>
      <td>-1.007860</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>x</td>
      <td>-0.185356</td>
    </tr>
    <tr>
      <th>5</th>
      <td>three</td>
      <td>x</td>
      <td>-0.687592</td>
    </tr>
    <tr>
      <th>6</th>
      <td>four</td>
      <td>x</td>
      <td>-2.052029</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.duplicated('a')
df2.duplicated("a", keep="last")
df2.duplicated('a', keep=False)
```




    0    False
    1     True
    2    False
    3     True
    4     True
    5    False
    6    False
    dtype: bool






    0     True
    1    False
    2     True
    3     True
    4    False
    5    False
    6    False
    dtype: bool






    0     True
    1     True
    2     True
    3     True
    4     True
    5    False
    6    False
    dtype: bool




```python
df2.drop_duplicates('a')
df2.drop_duplicates('a', keep="last")
df2.drop_duplicates('a', keep=False)
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>x</td>
      <td>2.206877</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>x</td>
      <td>-0.706555</td>
    </tr>
    <tr>
      <th>5</th>
      <td>three</td>
      <td>x</td>
      <td>-0.687592</td>
    </tr>
    <tr>
      <th>6</th>
      <td>four</td>
      <td>x</td>
      <td>-2.052029</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>y</td>
      <td>-1.852209</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>x</td>
      <td>-0.185356</td>
    </tr>
    <tr>
      <th>5</th>
      <td>three</td>
      <td>x</td>
      <td>-0.687592</td>
    </tr>
    <tr>
      <th>6</th>
      <td>four</td>
      <td>x</td>
      <td>-2.052029</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>three</td>
      <td>x</td>
      <td>-0.687592</td>
    </tr>
    <tr>
      <th>6</th>
      <td>four</td>
      <td>x</td>
      <td>-2.052029</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 传入一个列表作为参数
df2.duplicated(['a', 'b'])  # a b 两列看做一个整体，标示重复值
df2.drop_duplicates(['a', 'b'])
```




    0    False
    1    False
    2    False
    3    False
    4     True
    5    False
    6    False
    dtype: bool






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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>x</td>
      <td>2.206877</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>y</td>
      <td>-1.852209</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>x</td>
      <td>-0.706555</td>
    </tr>
    <tr>
      <th>3</th>
      <td>two</td>
      <td>y</td>
      <td>-1.007860</td>
    </tr>
    <tr>
      <th>5</th>
      <td>three</td>
      <td>x</td>
      <td>-0.687592</td>
    </tr>
    <tr>
      <th>6</th>
      <td>four</td>
      <td>x</td>
      <td>-2.052029</td>
    </tr>
  </tbody>
</table>
</div>




```python
# index索引去重  index.duplicated
df3 = pd.DataFrame({'a': np.arange(6),'b': np.random.randn(6)},index=['a', 'a', 'b', 'c', 'b', 'a'])
df3
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1.446937</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1</td>
      <td>-1.740284</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
      <td>-0.604590</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>0.096239</td>
    </tr>
    <tr>
      <th>b</th>
      <td>4</td>
      <td>0.823314</td>
    </tr>
    <tr>
      <th>a</th>
      <td>5</td>
      <td>1.990803</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.index.duplicated()
df3[~df3.index.duplicated()]
df3[~df3.index.duplicated(keep='last')]
df3[~df3.index.duplicated(keep=False)]
```




    array([False,  True, False, False,  True,  True])






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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1.446937</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
      <td>-0.604590</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>0.096239</td>
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>0.096239</td>
    </tr>
    <tr>
      <th>b</th>
      <td>4</td>
      <td>0.823314</td>
    </tr>
    <tr>
      <th>a</th>
      <td>5</td>
      <td>1.990803</td>
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>0.096239</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Dictionary-like get() method get方法
# Each of Series, DataFrame, and Panel have a get method which can return a default value.
s = pd.Series([1,2,3], index=['a','b','c'])
s.get("a")  # 相当于s["a"]
s.get("x", default=-1)  # 可以对不存在的index赋值
```




    1






    -1




```python
# The lookup() Method
# 按一定的顺序取得行/列的值
dflookup = pd.DataFrame(np.random.rand(20,4), columns = ['A','B','C','D'])
dflookup
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.942679</td>
      <td>0.727316</td>
      <td>0.658345</td>
      <td>0.465770</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.437278</td>
      <td>0.225158</td>
      <td>0.436522</td>
      <td>0.164805</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.270947</td>
      <td>0.280223</td>
      <td>0.309800</td>
      <td>0.015967</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.559836</td>
      <td>0.630962</td>
      <td>0.673678</td>
      <td>0.712503</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.535372</td>
      <td>0.989887</td>
      <td>0.661567</td>
      <td>0.361962</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.726322</td>
      <td>0.601192</td>
      <td>0.547858</td>
      <td>0.477509</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.829411</td>
      <td>0.583613</td>
      <td>0.871647</td>
      <td>0.460966</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.365722</td>
      <td>0.563660</td>
      <td>0.164954</td>
      <td>0.134314</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.817334</td>
      <td>0.523003</td>
      <td>0.684492</td>
      <td>0.369386</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.710906</td>
      <td>0.693633</td>
      <td>0.618877</td>
      <td>0.888263</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.026953</td>
      <td>0.185217</td>
      <td>0.746235</td>
      <td>0.568846</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.192765</td>
      <td>0.927200</td>
      <td>0.431736</td>
      <td>0.084300</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.988460</td>
      <td>0.784320</td>
      <td>0.180145</td>
      <td>0.039405</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.233349</td>
      <td>0.148678</td>
      <td>0.888210</td>
      <td>0.004917</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.105130</td>
      <td>0.146724</td>
      <td>0.261370</td>
      <td>0.936558</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.701224</td>
      <td>0.791860</td>
      <td>0.420083</td>
      <td>0.391538</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.290186</td>
      <td>0.307993</td>
      <td>0.139429</td>
      <td>0.618879</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.182132</td>
      <td>0.174420</td>
      <td>0.845501</td>
      <td>0.647986</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.732009</td>
      <td>0.919950</td>
      <td>0.197361</td>
      <td>0.582814</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.568096</td>
      <td>0.539125</td>
      <td>0.269016</td>
      <td>0.537584</td>
    </tr>
  </tbody>
</table>
</div>




```python
list(range(0,10,2))
dflookup.lookup(list(range(0,10,2)), ['B','C','A','B','D'])
```




    [0, 2, 4, 6, 8]






    array([0.72731646, 0.30979986, 0.53537223, 0.58361289, 0.36938598])




```python
# index objets 索引对象

# 索引可以通过list或其他序列对象直接创建
index = pd.Index(['e', 'd', 'a', 'b'])
index

# 可以命名
index = pd.Index(['e', 'd', 'a', 'b'], name='something')
index.name
index
```




    Index(['e', 'd', 'a', 'b'], dtype='object')






    'something'






    Index(['e', 'd', 'a', 'b'], dtype='object', name='something')




```python
index = pd.Index(list(range(5)), name='rows')
index
columns = pd.Index(['A', 'B', 'C'], name='cols')
columns
```




    Int64Index([0, 1, 2, 3, 4], dtype='int64', name='rows')






    Index(['A', 'B', 'C'], dtype='object', name='cols')




```python
df = pd.DataFrame(np.random.randn(5, 3), index=index, columns=columns)  # 使用索引给列命名，列名是一个索引对象
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
      <th>cols</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>rows</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.868165</td>
      <td>0.704614</td>
      <td>-2.049472</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.878810</td>
      <td>0.706876</td>
      <td>-0.741121</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-2.649523</td>
      <td>-0.952211</td>
      <td>0.806387</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.369280</td>
      <td>-0.052788</td>
      <td>-0.995775</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.218246</td>
      <td>-0.034493</td>
      <td>-0.198815</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Setting metadata 设置元数据
# 索引“多半”是“不可变”，但是可以设置和改变其元数据，比如索引的名称，或者，多重索引的级别和标签
# 可以使用 rename, set_names, set_levels, and set_labels 设置这些属性。
# 默认返回一个拷贝（不修改原值），也可以就地修改in place
ind = pd.Index([1, 2, 3])
ind
```




    Int64Index([1, 2, 3], dtype='int64')




```python
ind.name = "ind"
ind
ind.rename("apple")
ind
ind.name = "apple"
ind
ind.set_names(["bob"], inplace=True)
ind
```




    Int64Index([1, 2, 3], dtype='int64', name='ind')






    Int64Index([1, 2, 3], dtype='int64', name='apple')






    Int64Index([1, 2, 3], dtype='int64', name='ind')






    Int64Index([1, 2, 3], dtype='int64', name='apple')






    Int64Index([1, 2, 3], dtype='int64', name='bob')




```python
# set_names, set_levels, and set_labels also take an optional level` argument
# df.query('ilevel_0 == "red"') 在query中使用 ilevel_0 ……
index = pd.MultiIndex.from_product([range(3), ['one', 'two']], names=['first', 'second'])
index
```




    MultiIndex(levels=[[0, 1, 2], ['one', 'two']],
               labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
               names=['first', 'second'])




```python
index.levels[1]
index.levels[0]
index.set_levels(["a", "b"], level=1)
```




    Index(['one', 'two'], dtype='object', name='second')






    Int64Index([0, 1, 2], dtype='int64', name='first')






    MultiIndex(levels=[[0, 1, 2], ['a', 'b']],
               labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
               names=['first', 'second'])




```python
# Set operations on Index objects 索引对象中的集合操作 
# Note: The resulting index from a set operation will be sorted in ascending order. 
# 注意： 索引的集合操作返回的是升序排序后的结果
a = pd.Index(['c', 'b', 'a'])
b = pd.Index(['c', 'e', 'd'])
a | b  # 并集
a & b  # 交集
# a - b  # 不支持
a.difference(b)  # 差集，非对称
a.symmetric_difference(b)  # 对称差集，相当于idx1.difference(idx2).union(idx2.difference(idx1))
a ^ b  # 对称差集
```




    Index(['a', 'b', 'c', 'd', 'e'], dtype='object')






    Index(['c'], dtype='object')






    Index(['a', 'b'], dtype='object')






    Index(['a', 'b', 'd', 'e'], dtype='object')






    Index(['a', 'b', 'd', 'e'], dtype='object')




```python
# Missing values 缺失值
# 注意：索引能够容纳缺失值，但是应该避免这样的情况。因为可能出现不可预料的结果，例如有些操作默认排除缺失值。

idx1 = pd.Index([1, np.nan, 3, 4])
idx1
```




    Float64Index([1.0, nan, 3.0, 4.0], dtype='float64')




```python
idx1.fillna(2)  # 缺失值赋值为2，nan的index赋值为2
```




    Float64Index([1.0, 2.0, 3.0, 4.0], dtype='float64')




```python
idx2 = pd.DatetimeIndex([pd.Timestamp('2011-01-01'), pd.NaT, pd.Timestamp('2011-01-03')])  # pd的缺失值是NaT，与np不同
idx2
```




    DatetimeIndex(['2011-01-01', 'NaT', '2011-01-03'], dtype='datetime64[ns]', freq=None)




```python
idx2.fillna(pd.Timestamp('2011-01-02'))
```




    DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='datetime64[ns]', freq=None)




```python
# Set / Reset Index 设置/重设索引


# DataFrame
data = pd.DataFrame({"a":["bar", "bar", "foo", "foo"],
                    "b":["one","two","one","two"],
                    "c":["z","y","x", "w"],
                    "d":range(1,5)})  # range 不用list
data
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bar</td>
      <td>one</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>foo</td>
      <td>two</td>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
indexed1 = data.set_index("c")  # 把df的某列设置为index索引
indexed1
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
      <th>a</th>
      <th>b</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <td>bar</td>
      <td>one</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <td>bar</td>
      <td>two</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <td>foo</td>
      <td>one</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <td>foo</td>
      <td>two</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
indexed2 = data.set_index(['a', 'b'])  # 把df的多列设置为多重索引
indexed2
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
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>a</th>
      <th>b</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>two</th>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>two</th>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame = data.set_index('c', drop=False)  # drop参数，可以设置索引时不删除列，默认为删除列
frame
frame = frame.set_index(['a', 'b'], append=True)  # append参数，在原有索引的基础上，增加索引，变成复合索引
frame
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <td>bar</td>
      <td>one</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <td>foo</td>
      <td>two</td>
      <td>w</td>
      <td>4</td>
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
      <th></th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th>a</th>
      <th>b</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <th>bar</th>
      <th>one</th>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <th>bar</th>
      <th>two</th>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <th>foo</th>
      <th>one</th>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <th>foo</th>
      <th>two</th>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.set_index('c', drop=False)  # 把某列设为索引，但不删除
data
data.set_index(['a', 'b'], inplace=True)  # 就地修改，而不是返回拷贝
data
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <td>bar</td>
      <td>one</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <td>foo</td>
      <td>two</td>
      <td>w</td>
      <td>4</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bar</td>
      <td>one</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>foo</td>
      <td>two</td>
      <td>w</td>
      <td>4</td>
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
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>a</th>
      <th>b</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>two</th>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>two</th>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reset the index 重置索引
# Note: The reset_index method used to be called delevel which is now deprecated. 不推荐使用delevel

data
data.index.name  # 无返回值？
data.index.names  # 索引列的名称
data.reset_index()  # 重置索引，原索引变为普通列，原索引名称变为列名
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
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>a</th>
      <th>b</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>two</th>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>two</th>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






    FrozenList(['a', 'b'])






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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bar</td>
      <td>one</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>foo</td>
      <td>two</td>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame
frame.reset_index(level=1)  # 对于多重索引，可以指定重置哪一级索引，而不是全部重置
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
      <th></th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th>a</th>
      <th>b</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <th>bar</th>
      <th>one</th>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <th>bar</th>
      <th>two</th>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <th>foo</th>
      <th>one</th>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <th>foo</th>
      <th>two</th>
      <td>w</td>
      <td>4</td>
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
      <th>a</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th>b</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <th>one</th>
      <td>bar</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <th>two</th>
      <td>bar</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <th>one</th>
      <td>foo</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <th>two</th>
      <td>foo</td>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reset_index方法可以使用drop参数，若其为true，则仅是把索引剔除，而不转换为df数据列
frame
frame.reset_index(level=2, drop=True) 
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
      <th></th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th>a</th>
      <th>b</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <th>bar</th>
      <th>one</th>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <th>bar</th>
      <th>two</th>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <th>foo</th>
      <th>one</th>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <th>foo</th>
      <th>two</th>
      <td>w</td>
      <td>4</td>
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
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <th>bar</th>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>y</th>
      <th>bar</th>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>x</th>
      <th>foo</th>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>w</th>
      <th>foo</th>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Adding an ad hoc index
# If you create an index yourself, you can just assign it to the index field
# 创建index对象，并赋值给df
index = pd.MultiIndex.from_product([range(2), ['one', 'two']], names=['first', 'second'])
index
data
data.index = index  # 注意：index的长度要与df向适应
data
```




    MultiIndex(levels=[[0, 1], ['one', 'two']],
               labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
               names=['first', 'second'])






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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bar</td>
      <td>one</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>foo</td>
      <td>two</td>
      <td>w</td>
      <td>4</td>
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">0</th>
      <th>one</th>
      <td>bar</td>
      <td>one</td>
      <td>z</td>
      <td>1</td>
    </tr>
    <tr>
      <th>two</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>one</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>3</td>
    </tr>
    <tr>
      <th>two</th>
      <td>foo</td>
      <td>two</td>
      <td>w</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Returning a view versus a copy 返回视图 对比 返回拷贝
# 避免链式操作，即多个连接的[]，具体见前面的说明

# Why does assignment fail when using chained indexing? 为什么链式索引赋值失败
# python解释器，对以下赋值的区别

# 第一种：非链式赋值
dfmi.loc[:,('one','second')] = value
# becomes， python解释为：
dfmi.loc.__setitem__((slice(None), ('one', 'second')), value)  # 直接set
# Of course, dfmi.loc.__getitem__(idx) may be a view or a copy of dfmi.

# 第二种：链式赋值
dfmi['one']['second'] = value  # pd会抛出异常SettingWithCopy，链式操作具有不确定性！
# becomes， python解释为：
dfmi.__getitem__('one').__setitem__('second', value)  # 先get，再set，前面的get返回的是一个copy

```


```python
# SettingWithCopy有时候会在没有明显的链式操作的情况下出现，例如：
def do_something(df):
   foo = df[['bar', 'baz']]  # Is foo a view? A copy? Nobody knows!
   # ... many lines here ...
   foo['quux'] = value       # We don't know whether this will modify df or not!  # “隐式”的链式操作
   return foo
```


```python
# Evaluation order matters 赋值命令事情
# 链式赋值操作引起的SettingWithCopyWarning，可以通过设置option mode取消或抑制。

dfb = pd.DataFrame({'a' : ['one', 'one', 'two','three', 'two', 'one', 'six'],'c' : np.arange(7)})
dfb
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
      <th>a</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>one</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>six</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# This will show the SettingWithCopyWarning
# but the frame values will be set
dfb['c'][dfb.a.str.startswith('o')] = 42
dfb
```

    d:\python\36-64\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    




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
      <th>a</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>42</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>42</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>one</td>
      <td>42</td>
    </tr>
    <tr>
      <th>6</th>
      <td>six</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# This however is operating on a copy and will not work.
# 把option的提示级别由warn改为raise ????
pd.set_option('mode.chained_assignment','warn')  # This however is operating on a copy and will not work. # ??

```


```python
# A chained assignment can also crop up in setting in a mixed dtype frame. 出现在
# Note ： These setting rules apply to all of .loc/.iloc 

# This is the correct access method 正确的存取方法
dfc = pd.DataFrame({'A':['aaa','bbb','ccc'],'B':[1,2,3]})
dfc
dfc.loc[0,'A'] = 11
dfc
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
      <td>aaa</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bbb</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ccc</td>
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
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bbb</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ccc</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfc = dfc.copy()
dfc
dfc['A'][0] = 111  # This can work at times, but is not guaranteed, and so should be avoided 有时可以工作，但不保证，应避免使用
dfc
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
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bbb</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ccc</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



    d:\python\36-64\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    




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
      <td>111</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bbb</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ccc</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option('mode.chained_assignment', 'raise')  # 链式赋值将不会执行
```


```python
# http://pandas.pydata.org/pandas-docs/stable/indexing.html 全文完
# 2018-02-19
```
