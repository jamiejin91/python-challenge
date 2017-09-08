
## PyCity Schools Analysis
#### - The amount of money the school spends per student is inversely proportional to their performance in math and reading tests.
#### - Charter school students do much better than district school students.
#### - Schools with less than 2000 students do much better than schools with more than 2000 students.


```python
import pandas as pd
import numpy as np

df_students = pd.read_csv("students_complete.csv")
df_schools = pd.read_csv("schools_complete.csv")

# total math and reading passing grade added to school df
ayy = pd.DataFrame(df_students['school'].loc[df_students['math_score'] >= 70].value_counts())
lmao = pd.DataFrame(df_students['school'].loc[df_students['reading_score'] >= 70].value_counts())
ayy.reset_index(inplace=True)
lmao.reset_index(inplace=True)
ayylmao = pd.merge(ayy,lmao,on='index')
ayylmao.columns = ["name", "math_pass","reading_pass"]
ayylmao
df_schools = pd.merge(df_schools,ayylmao,on='name')
```

### Distric Summary


```python
math_path = df_students["math_score"].loc[df_students["math_score"] >= 70].count()/df_schools['size'].sum() * 100
read_path = df_students["reading_score"].loc[df_students["reading_score"] >= 70].count()/df_schools['size'].sum() * 100
dist_sum = pd.DataFrame(
        {"Total Schools": df_schools['name'].count(),
         "Total Students": "{:,}".format(df_schools['size'].sum()),
         "Total Budget": "${:,.2f}".format(df_schools['budget'].sum()),
         "Average Math Score": "{:.2f}".format(df_students['math_score'].mean()),
         "Average Reading Score": "{:.2f}".format(df_students ['reading_score'].mean()),
         "% Passing Math": "{:.2f}%".format(math_path),
         "% Passing Reading": "{:.2f}%".format(read_path),
         "% Overall Passing Rate": "{:.2f}%".format((math_path+read_path)/2)}, index = [0])
dist_sum = dist_sum[["Total Schools", "Total Students", "Total Budget", "Average Math Score",
                     "Average Reading Score","% Passing Math","% Passing Reading","% Overall Passing Rate"]]
dist_sum
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>74.98%</td>
      <td>85.81%</td>
      <td>80.39%</td>
    </tr>
  </tbody>
</table>
</div>



### School Summary


```python
sch_sum = df_schools.loc[:,['name','type','size','budget']]
sch_sum.columns = ['name','School Type','Total Students','Total School Budget']
sch_sum['Per Student Budget'] = df_schools['budget']/df_schools['size']
sch_sum['% Passing Math'] = df_schools['math_pass']/df_schools['size']*100
sch_sum['% Passing Reading'] = df_schools['reading_pass']/df_schools['size']*100
sch_sum['% Overall Passing Rate'] = (sch_sum['% Passing Math']+sch_sum['% Passing Reading'])/2
sch_sum = sch_sum.set_index('name')
sch_sum.index.name = None
sch_sum.sort_index(inplace=True)
sch_sum['Average Math Score'] = df_students.groupby('school')['math_score'].mean()
sch_sum['Average Reading Score'] = df_students.groupby('school')['reading_score'].mean()
sch_cols = sch_sum.columns.tolist()
sch_cols = sch_cols[:4] + sch_cols[7:] + sch_cols[4:7]
sch_sum = sch_sum[sch_cols]
sch_sum_final = sch_sum.style.format({"Total School Budget": "${:,.2f}", "Per Student Budget":"${:,.2f}", "Average Math Score":"{:.2f}", 
                      "Average Reading Score":"{:.2f}", "% Passing Math":"{:.2f}%", 
                      "% Passing Reading":"{:.2f}%", "% Overall Passing Rate":"{:.2f}%"})
sch_sum_final
```




<style  type="text/css" >
</style>  
<table id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >School Type</th> 
        <th class="col_heading level0 col1" >Total Students</th> 
        <th class="col_heading level0 col2" >Total School Budget</th> 
        <th class="col_heading level0 col3" >Per Student Budget</th> 
        <th class="col_heading level0 col4" >Average Math Score</th> 
        <th class="col_heading level0 col5" >Average Reading Score</th> 
        <th class="col_heading level0 col6" >% Passing Math</th> 
        <th class="col_heading level0 col7" >% Passing Reading</th> 
        <th class="col_heading level0 col8" >% Overall Passing Rate</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row0" class="row_heading level0 row0" >Bailey High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col0" class="data row0 col0" >District</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col1" class="data row0 col1" >4976</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col2" class="data row0 col2" >$3,124,928.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col3" class="data row0 col3" >$628.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col4" class="data row0 col4" >77.05</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col5" class="data row0 col5" >81.03</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col6" class="data row0 col6" >66.68%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col7" class="data row0 col7" >81.93%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow0_col8" class="data row0 col8" >74.31%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row1" class="row_heading level0 row1" >Cabrera High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col0" class="data row1 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col1" class="data row1 col1" >1858</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col2" class="data row1 col2" >$1,081,356.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col3" class="data row1 col3" >$582.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col4" class="data row1 col4" >83.06</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col5" class="data row1 col5" >83.98</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col6" class="data row1 col6" >94.13%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col7" class="data row1 col7" >97.04%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow1_col8" class="data row1 col8" >95.59%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row2" class="row_heading level0 row2" >Figueroa High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col0" class="data row2 col0" >District</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col1" class="data row2 col1" >2949</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col2" class="data row2 col2" >$1,884,411.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col3" class="data row2 col3" >$639.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col4" class="data row2 col4" >76.71</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col5" class="data row2 col5" >81.16</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col6" class="data row2 col6" >65.99%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col7" class="data row2 col7" >80.74%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow2_col8" class="data row2 col8" >73.36%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row3" class="row_heading level0 row3" >Ford High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col0" class="data row3 col0" >District</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col1" class="data row3 col1" >2739</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col2" class="data row3 col2" >$1,763,916.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col3" class="data row3 col3" >$644.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col4" class="data row3 col4" >77.10</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col5" class="data row3 col5" >80.75</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col6" class="data row3 col6" >68.31%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col7" class="data row3 col7" >79.30%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow3_col8" class="data row3 col8" >73.80%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row4" class="row_heading level0 row4" >Griffin High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col0" class="data row4 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col1" class="data row4 col1" >1468</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col2" class="data row4 col2" >$917,500.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col3" class="data row4 col3" >$625.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col4" class="data row4 col4" >83.35</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col5" class="data row4 col5" >83.82</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col6" class="data row4 col6" >93.39%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col7" class="data row4 col7" >97.14%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow4_col8" class="data row4 col8" >95.27%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row5" class="row_heading level0 row5" >Hernandez High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col0" class="data row5 col0" >District</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col1" class="data row5 col1" >4635</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col2" class="data row5 col2" >$3,022,020.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col3" class="data row5 col3" >$652.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col4" class="data row5 col4" >77.29</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col5" class="data row5 col5" >80.93</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col6" class="data row5 col6" >66.75%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col7" class="data row5 col7" >80.86%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow5_col8" class="data row5 col8" >73.81%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row6" class="row_heading level0 row6" >Holden High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col0" class="data row6 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col1" class="data row6 col1" >427</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col2" class="data row6 col2" >$248,087.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col3" class="data row6 col3" >$581.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col4" class="data row6 col4" >83.80</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col5" class="data row6 col5" >83.81</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col6" class="data row6 col6" >92.51%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col7" class="data row6 col7" >96.25%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow6_col8" class="data row6 col8" >94.38%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row7" class="row_heading level0 row7" >Huang High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col0" class="data row7 col0" >District</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col1" class="data row7 col1" >2917</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col2" class="data row7 col2" >$1,910,635.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col3" class="data row7 col3" >$655.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col4" class="data row7 col4" >76.63</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col5" class="data row7 col5" >81.18</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col6" class="data row7 col6" >65.68%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col7" class="data row7 col7" >81.32%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow7_col8" class="data row7 col8" >73.50%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row8" class="row_heading level0 row8" >Johnson High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col0" class="data row8 col0" >District</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col1" class="data row8 col1" >4761</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col2" class="data row8 col2" >$3,094,650.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col3" class="data row8 col3" >$650.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col4" class="data row8 col4" >77.07</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col5" class="data row8 col5" >80.97</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col6" class="data row8 col6" >66.06%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col7" class="data row8 col7" >81.22%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow8_col8" class="data row8 col8" >73.64%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row9" class="row_heading level0 row9" >Pena High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col0" class="data row9 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col1" class="data row9 col1" >962</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col2" class="data row9 col2" >$585,858.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col3" class="data row9 col3" >$609.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col4" class="data row9 col4" >83.84</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col5" class="data row9 col5" >84.04</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col6" class="data row9 col6" >94.59%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col7" class="data row9 col7" >95.95%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow9_col8" class="data row9 col8" >95.27%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row10" class="row_heading level0 row10" >Rodriguez High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col0" class="data row10 col0" >District</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col1" class="data row10 col1" >3999</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col2" class="data row10 col2" >$2,547,363.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col3" class="data row10 col3" >$637.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col4" class="data row10 col4" >76.84</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col5" class="data row10 col5" >80.74</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col6" class="data row10 col6" >66.37%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col7" class="data row10 col7" >80.22%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow10_col8" class="data row10 col8" >73.29%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row11" class="row_heading level0 row11" >Shelton High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col0" class="data row11 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col1" class="data row11 col1" >1761</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col2" class="data row11 col2" >$1,056,600.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col3" class="data row11 col3" >$600.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col4" class="data row11 col4" >83.36</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col5" class="data row11 col5" >83.73</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col6" class="data row11 col6" >93.87%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col7" class="data row11 col7" >95.85%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow11_col8" class="data row11 col8" >94.86%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row12" class="row_heading level0 row12" >Thomas High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col0" class="data row12 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col1" class="data row12 col1" >1635</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col2" class="data row12 col2" >$1,043,130.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col3" class="data row12 col3" >$638.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col4" class="data row12 col4" >83.42</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col5" class="data row12 col5" >83.85</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col6" class="data row12 col6" >93.27%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col7" class="data row12 col7" >97.31%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow12_col8" class="data row12 col8" >95.29%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row13" class="row_heading level0 row13" >Wilson High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col0" class="data row13 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col1" class="data row13 col1" >2283</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col2" class="data row13 col2" >$1,319,574.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col3" class="data row13 col3" >$578.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col4" class="data row13 col4" >83.27</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col5" class="data row13 col5" >83.99</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col6" class="data row13 col6" >93.87%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col7" class="data row13 col7" >96.54%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow13_col8" class="data row13 col8" >95.20%</td> 
    </tr>    <tr> 
        <th id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52flevel0_row14" class="row_heading level0 row14" >Wright High School</th> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col0" class="data row14 col0" >Charter</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col1" class="data row14 col1" >1800</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col2" class="data row14 col2" >$1,049,400.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col3" class="data row14 col3" >$583.00</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col4" class="data row14 col4" >83.68</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col5" class="data row14 col5" >83.95</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col6" class="data row14 col6" >93.33%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col7" class="data row14 col7" >96.61%</td> 
        <td id="T_57ed4b42_942d_11e7_9f3b_f48c5097b52frow14_col8" class="data row14 col8" >94.97%</td> 
    </tr></tbody> 
</table> 



## Top Performing Schools (By Passing Rate)


```python
top_sch = sch_sum.sort_values(['% Overall Passing Rate'],ascending = False).head()
top_sch = top_sch.style.format({"Total School Budget": "${:,.2f}", "Per Student Budget":"${:,.2f}", "Average Math Score":"{:.2f}", 
                      "Average Reading Score":"{:.2f}", "% Passing Math":"{:.2f}%", 
                      "% Passing Reading":"{:.2f}%", "% Overall Passing Rate":"{:.2f}%"})
top_sch
```




<style  type="text/css" >
</style>  
<table id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >School Type</th> 
        <th class="col_heading level0 col1" >Total Students</th> 
        <th class="col_heading level0 col2" >Total School Budget</th> 
        <th class="col_heading level0 col3" >Per Student Budget</th> 
        <th class="col_heading level0 col4" >Average Math Score</th> 
        <th class="col_heading level0 col5" >Average Reading Score</th> 
        <th class="col_heading level0 col6" >% Passing Math</th> 
        <th class="col_heading level0 col7" >% Passing Reading</th> 
        <th class="col_heading level0 col8" >% Overall Passing Rate</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52flevel0_row0" class="row_heading level0 row0" >Cabrera High School</th> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col0" class="data row0 col0" >Charter</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col1" class="data row0 col1" >1858</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col2" class="data row0 col2" >$1,081,356.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col3" class="data row0 col3" >$582.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col4" class="data row0 col4" >83.06</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col5" class="data row0 col5" >83.98</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col6" class="data row0 col6" >94.13%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col7" class="data row0 col7" >97.04%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow0_col8" class="data row0 col8" >95.59%</td> 
    </tr>    <tr> 
        <th id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52flevel0_row1" class="row_heading level0 row1" >Thomas High School</th> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col0" class="data row1 col0" >Charter</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col1" class="data row1 col1" >1635</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col2" class="data row1 col2" >$1,043,130.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col3" class="data row1 col3" >$638.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col4" class="data row1 col4" >83.42</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col5" class="data row1 col5" >83.85</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col6" class="data row1 col6" >93.27%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col7" class="data row1 col7" >97.31%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow1_col8" class="data row1 col8" >95.29%</td> 
    </tr>    <tr> 
        <th id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52flevel0_row2" class="row_heading level0 row2" >Pena High School</th> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col0" class="data row2 col0" >Charter</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col1" class="data row2 col1" >962</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col2" class="data row2 col2" >$585,858.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col3" class="data row2 col3" >$609.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col4" class="data row2 col4" >83.84</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col5" class="data row2 col5" >84.04</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col6" class="data row2 col6" >94.59%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col7" class="data row2 col7" >95.95%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow2_col8" class="data row2 col8" >95.27%</td> 
    </tr>    <tr> 
        <th id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52flevel0_row3" class="row_heading level0 row3" >Griffin High School</th> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col0" class="data row3 col0" >Charter</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col1" class="data row3 col1" >1468</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col2" class="data row3 col2" >$917,500.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col3" class="data row3 col3" >$625.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col4" class="data row3 col4" >83.35</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col5" class="data row3 col5" >83.82</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col6" class="data row3 col6" >93.39%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col7" class="data row3 col7" >97.14%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow3_col8" class="data row3 col8" >95.27%</td> 
    </tr>    <tr> 
        <th id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52flevel0_row4" class="row_heading level0 row4" >Wilson High School</th> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col0" class="data row4 col0" >Charter</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col1" class="data row4 col1" >2283</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col2" class="data row4 col2" >$1,319,574.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col3" class="data row4 col3" >$578.00</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col4" class="data row4 col4" >83.27</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col5" class="data row4 col5" >83.99</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col6" class="data row4 col6" >93.87%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col7" class="data row4 col7" >96.54%</td> 
        <td id="T_57f1b0e8_942d_11e7_b8d5_f48c5097b52frow4_col8" class="data row4 col8" >95.20%</td> 
    </tr></tbody> 
</table> 



## Bottom Performing Schools (By Passing Rate)


```python
bot_sch = sch_sum.sort_values(['% Overall Passing Rate'],ascending = True).head()
bot_sch = bot_sch.style.format({"Total School Budget": "${:,.2f}", "Per Student Budget":"${:,.2f}", "Average Math Score":"{:.2f}", 
                      "Average Reading Score":"{:.2f}", "% Passing Math":"{:.2f}%", 
                      "% Passing Reading":"{:.2f}%", "% Overall Passing Rate":"{:.2f}%"})
bot_sch
```




<style  type="text/css" >
</style>  
<table id="T_57f75a0a_942d_11e7_93d3_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >School Type</th> 
        <th class="col_heading level0 col1" >Total Students</th> 
        <th class="col_heading level0 col2" >Total School Budget</th> 
        <th class="col_heading level0 col3" >Per Student Budget</th> 
        <th class="col_heading level0 col4" >Average Math Score</th> 
        <th class="col_heading level0 col5" >Average Reading Score</th> 
        <th class="col_heading level0 col6" >% Passing Math</th> 
        <th class="col_heading level0 col7" >% Passing Reading</th> 
        <th class="col_heading level0 col8" >% Overall Passing Rate</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_57f75a0a_942d_11e7_93d3_f48c5097b52flevel0_row0" class="row_heading level0 row0" >Rodriguez High School</th> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col0" class="data row0 col0" >District</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col1" class="data row0 col1" >3999</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col2" class="data row0 col2" >$2,547,363.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col3" class="data row0 col3" >$637.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col4" class="data row0 col4" >76.84</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col5" class="data row0 col5" >80.74</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col6" class="data row0 col6" >66.37%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col7" class="data row0 col7" >80.22%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow0_col8" class="data row0 col8" >73.29%</td> 
    </tr>    <tr> 
        <th id="T_57f75a0a_942d_11e7_93d3_f48c5097b52flevel0_row1" class="row_heading level0 row1" >Figueroa High School</th> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col0" class="data row1 col0" >District</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col1" class="data row1 col1" >2949</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col2" class="data row1 col2" >$1,884,411.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col3" class="data row1 col3" >$639.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col4" class="data row1 col4" >76.71</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col5" class="data row1 col5" >81.16</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col6" class="data row1 col6" >65.99%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col7" class="data row1 col7" >80.74%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow1_col8" class="data row1 col8" >73.36%</td> 
    </tr>    <tr> 
        <th id="T_57f75a0a_942d_11e7_93d3_f48c5097b52flevel0_row2" class="row_heading level0 row2" >Huang High School</th> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col0" class="data row2 col0" >District</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col1" class="data row2 col1" >2917</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col2" class="data row2 col2" >$1,910,635.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col3" class="data row2 col3" >$655.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col4" class="data row2 col4" >76.63</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col5" class="data row2 col5" >81.18</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col6" class="data row2 col6" >65.68%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col7" class="data row2 col7" >81.32%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow2_col8" class="data row2 col8" >73.50%</td> 
    </tr>    <tr> 
        <th id="T_57f75a0a_942d_11e7_93d3_f48c5097b52flevel0_row3" class="row_heading level0 row3" >Johnson High School</th> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col0" class="data row3 col0" >District</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col1" class="data row3 col1" >4761</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col2" class="data row3 col2" >$3,094,650.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col3" class="data row3 col3" >$650.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col4" class="data row3 col4" >77.07</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col5" class="data row3 col5" >80.97</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col6" class="data row3 col6" >66.06%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col7" class="data row3 col7" >81.22%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow3_col8" class="data row3 col8" >73.64%</td> 
    </tr>    <tr> 
        <th id="T_57f75a0a_942d_11e7_93d3_f48c5097b52flevel0_row4" class="row_heading level0 row4" >Ford High School</th> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col0" class="data row4 col0" >District</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col1" class="data row4 col1" >2739</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col2" class="data row4 col2" >$1,763,916.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col3" class="data row4 col3" >$644.00</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col4" class="data row4 col4" >77.10</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col5" class="data row4 col5" >80.75</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col6" class="data row4 col6" >68.31%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col7" class="data row4 col7" >79.30%</td> 
        <td id="T_57f75a0a_942d_11e7_93d3_f48c5097b52frow4_col8" class="data row4 col8" >73.80%</td> 
    </tr></tbody> 
</table> 



## Math Scores by Grade


```python
math_temp = df_students.loc[:,['grade','school','math_score']]
math_gr_9 = math_temp.loc[math_temp['grade'] == "9th"].groupby(['school']).mean()
math_gr_9.reset_index(level=0, inplace=True)
math_gr_10 = math_temp.loc[math_temp['grade'] == "10th"].groupby(['school']).mean()
math_gr_10.reset_index(level=0, inplace=True)
math_gr_11 = math_temp.loc[math_temp['grade'] == "11th"].groupby(['school']).mean()
math_gr_11.reset_index(level=0, inplace=True)
math_gr_12 = math_temp.loc[math_temp['grade'] == "12th"].groupby(['school']).mean()
math_gr_12.reset_index(level=0, inplace=True)
math_gr = math_gr_9.merge(math_gr_10,on = 'school').merge(math_gr_11,on = 'school').merge(math_gr_12,on='school')
math_gr.columns = ['school','9th','10th','11th','12th']
math_gr = math_gr.set_index('school')
del math_gr.index.name
math_gr = math_gr.style.format({"9th": "{:.2f}", "10th":"{:.2f}", "11th":"{:.2f}","12th":"{:.2f}"})
math_gr
```




<style  type="text/css" >
</style>  
<table id="T_58097140_942d_11e7_9b5f_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >9th</th> 
        <th class="col_heading level0 col1" >10th</th> 
        <th class="col_heading level0 col2" >11th</th> 
        <th class="col_heading level0 col3" >12th</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row0" class="row_heading level0 row0" >Bailey High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow0_col0" class="data row0 col0" >77.08</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow0_col1" class="data row0 col1" >77.00</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow0_col2" class="data row0 col2" >77.52</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow0_col3" class="data row0 col3" >76.49</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row1" class="row_heading level0 row1" >Cabrera High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow1_col0" class="data row1 col0" >83.09</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow1_col1" class="data row1 col1" >83.15</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow1_col2" class="data row1 col2" >82.77</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow1_col3" class="data row1 col3" >83.28</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row2" class="row_heading level0 row2" >Figueroa High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow2_col0" class="data row2 col0" >76.40</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow2_col1" class="data row2 col1" >76.54</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow2_col2" class="data row2 col2" >76.88</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow2_col3" class="data row2 col3" >77.15</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row3" class="row_heading level0 row3" >Ford High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow3_col0" class="data row3 col0" >77.36</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow3_col1" class="data row3 col1" >77.67</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow3_col2" class="data row3 col2" >76.92</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow3_col3" class="data row3 col3" >76.18</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row4" class="row_heading level0 row4" >Griffin High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow4_col0" class="data row4 col0" >82.04</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow4_col1" class="data row4 col1" >84.23</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow4_col2" class="data row4 col2" >83.84</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow4_col3" class="data row4 col3" >83.36</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row5" class="row_heading level0 row5" >Hernandez High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow5_col0" class="data row5 col0" >77.44</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow5_col1" class="data row5 col1" >77.34</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow5_col2" class="data row5 col2" >77.14</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow5_col3" class="data row5 col3" >77.19</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row6" class="row_heading level0 row6" >Holden High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow6_col0" class="data row6 col0" >83.79</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow6_col1" class="data row6 col1" >83.43</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow6_col2" class="data row6 col2" >85.00</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow6_col3" class="data row6 col3" >82.86</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row7" class="row_heading level0 row7" >Huang High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow7_col0" class="data row7 col0" >77.03</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow7_col1" class="data row7 col1" >75.91</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow7_col2" class="data row7 col2" >76.45</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow7_col3" class="data row7 col3" >77.23</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row8" class="row_heading level0 row8" >Johnson High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow8_col0" class="data row8 col0" >77.19</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow8_col1" class="data row8 col1" >76.69</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow8_col2" class="data row8 col2" >77.49</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow8_col3" class="data row8 col3" >76.86</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row9" class="row_heading level0 row9" >Pena High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow9_col0" class="data row9 col0" >83.63</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow9_col1" class="data row9 col1" >83.37</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow9_col2" class="data row9 col2" >84.33</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow9_col3" class="data row9 col3" >84.12</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row10" class="row_heading level0 row10" >Rodriguez High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow10_col0" class="data row10 col0" >76.86</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow10_col1" class="data row10 col1" >76.61</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow10_col2" class="data row10 col2" >76.40</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow10_col3" class="data row10 col3" >77.69</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row11" class="row_heading level0 row11" >Shelton High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow11_col0" class="data row11 col0" >83.42</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow11_col1" class="data row11 col1" >82.92</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow11_col2" class="data row11 col2" >83.38</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow11_col3" class="data row11 col3" >83.78</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row12" class="row_heading level0 row12" >Thomas High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow12_col0" class="data row12 col0" >83.59</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow12_col1" class="data row12 col1" >83.09</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow12_col2" class="data row12 col2" >83.50</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow12_col3" class="data row12 col3" >83.50</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row13" class="row_heading level0 row13" >Wilson High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow13_col0" class="data row13 col0" >83.09</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow13_col1" class="data row13 col1" >83.72</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow13_col2" class="data row13 col2" >83.20</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow13_col3" class="data row13 col3" >83.04</td> 
    </tr>    <tr> 
        <th id="T_58097140_942d_11e7_9b5f_f48c5097b52flevel0_row14" class="row_heading level0 row14" >Wright High School</th> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow14_col0" class="data row14 col0" >83.26</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow14_col1" class="data row14 col1" >84.01</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow14_col2" class="data row14 col2" >83.84</td> 
        <td id="T_58097140_942d_11e7_9b5f_f48c5097b52frow14_col3" class="data row14 col3" >83.64</td> 
    </tr></tbody> 
</table> 



## Reading Score by Grade


```python
read_temp = df_students.loc[:,['grade','school','reading_score']]
read_gr_9 = read_temp.loc[read_temp['grade'] == "9th"].groupby(['school']).mean()
read_gr_9.reset_index(level=0, inplace=True)
read_gr_10 = read_temp.loc[read_temp['grade'] == "10th"].groupby(['school']).mean()
read_gr_10.reset_index(level=0, inplace=True)
read_gr_11 = read_temp.loc[read_temp['grade'] == "11th"].groupby(['school']).mean()
read_gr_11.reset_index(level=0, inplace=True)
read_gr_12 = read_temp.loc[read_temp['grade'] == "12th"].groupby(['school']).mean()
read_gr_12.reset_index(level=0, inplace=True)
read_gr = read_gr_9.merge(read_gr_10,on = 'school').merge(read_gr_11,on = 'school').merge(read_gr_12,on='school')
read_gr.columns = ['school','9th','10th','11th','12th']
read_gr = read_gr.set_index('school')
del read_gr.index.name
read_gr = read_gr.style.format({"9th": "{:.2f}", "10th":"{:.2f}", "11th":"{:.2f}","12th":"{:.2f}"})
read_gr
```




<style  type="text/css" >
</style>  
<table id="T_581a5d5a_942d_11e7_9093_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >9th</th> 
        <th class="col_heading level0 col1" >10th</th> 
        <th class="col_heading level0 col2" >11th</th> 
        <th class="col_heading level0 col3" >12th</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row0" class="row_heading level0 row0" >Bailey High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow0_col0" class="data row0 col0" >81.30</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow0_col1" class="data row0 col1" >80.91</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow0_col2" class="data row0 col2" >80.95</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow0_col3" class="data row0 col3" >80.91</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row1" class="row_heading level0 row1" >Cabrera High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow1_col0" class="data row1 col0" >83.68</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow1_col1" class="data row1 col1" >84.25</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow1_col2" class="data row1 col2" >83.79</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow1_col3" class="data row1 col3" >84.29</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row2" class="row_heading level0 row2" >Figueroa High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow2_col0" class="data row2 col0" >81.20</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow2_col1" class="data row2 col1" >81.41</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow2_col2" class="data row2 col2" >80.64</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow2_col3" class="data row2 col3" >81.38</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row3" class="row_heading level0 row3" >Ford High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow3_col0" class="data row3 col0" >80.63</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow3_col1" class="data row3 col1" >81.26</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow3_col2" class="data row3 col2" >80.40</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow3_col3" class="data row3 col3" >80.66</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row4" class="row_heading level0 row4" >Griffin High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow4_col0" class="data row4 col0" >83.37</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow4_col1" class="data row4 col1" >83.71</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow4_col2" class="data row4 col2" >84.29</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow4_col3" class="data row4 col3" >84.01</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row5" class="row_heading level0 row5" >Hernandez High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow5_col0" class="data row5 col0" >80.87</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow5_col1" class="data row5 col1" >80.66</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow5_col2" class="data row5 col2" >81.40</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow5_col3" class="data row5 col3" >80.86</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row6" class="row_heading level0 row6" >Holden High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow6_col0" class="data row6 col0" >83.68</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow6_col1" class="data row6 col1" >83.32</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow6_col2" class="data row6 col2" >83.82</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow6_col3" class="data row6 col3" >84.70</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row7" class="row_heading level0 row7" >Huang High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow7_col0" class="data row7 col0" >81.29</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow7_col1" class="data row7 col1" >81.51</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow7_col2" class="data row7 col2" >81.42</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow7_col3" class="data row7 col3" >80.31</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row8" class="row_heading level0 row8" >Johnson High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow8_col0" class="data row8 col0" >81.26</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow8_col1" class="data row8 col1" >80.77</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow8_col2" class="data row8 col2" >80.62</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow8_col3" class="data row8 col3" >81.23</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row9" class="row_heading level0 row9" >Pena High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow9_col0" class="data row9 col0" >83.81</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow9_col1" class="data row9 col1" >83.61</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow9_col2" class="data row9 col2" >84.34</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow9_col3" class="data row9 col3" >84.59</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row10" class="row_heading level0 row10" >Rodriguez High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow10_col0" class="data row10 col0" >80.99</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow10_col1" class="data row10 col1" >80.63</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow10_col2" class="data row10 col2" >80.86</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow10_col3" class="data row10 col3" >80.38</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row11" class="row_heading level0 row11" >Shelton High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow11_col0" class="data row11 col0" >84.12</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow11_col1" class="data row11 col1" >83.44</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow11_col2" class="data row11 col2" >84.37</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow11_col3" class="data row11 col3" >82.78</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row12" class="row_heading level0 row12" >Thomas High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow12_col0" class="data row12 col0" >83.73</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow12_col1" class="data row12 col1" >84.25</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow12_col2" class="data row12 col2" >83.59</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow12_col3" class="data row12 col3" >83.83</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row13" class="row_heading level0 row13" >Wilson High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow13_col0" class="data row13 col0" >83.94</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow13_col1" class="data row13 col1" >84.02</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow13_col2" class="data row13 col2" >83.76</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow13_col3" class="data row13 col3" >84.32</td> 
    </tr>    <tr> 
        <th id="T_581a5d5a_942d_11e7_9093_f48c5097b52flevel0_row14" class="row_heading level0 row14" >Wright High School</th> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow14_col0" class="data row14 col0" >83.83</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow14_col1" class="data row14 col1" >83.81</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow14_col2" class="data row14 col2" >84.16</td> 
        <td id="T_581a5d5a_942d_11e7_9093_f48c5097b52frow14_col3" class="data row14 col3" >84.07</td> 
    </tr></tbody> 
</table> 



## Scores by School Spending


```python
sss_temp = sch_sum.loc[:,['Per Student Budget','Average Math Score','Average Reading Score',
                          '% Passing Math','% Passing Reading']]
sss = sss_temp.groupby(['Per Student Budget'],as_index=False).mean()
sss1 = sss.loc[sss['Per Student Budget'] < 585].mean()
sss2 = sss.loc[(sss['Per Student Budget'] >= 585) & (sss['Per Student Budget'] < 615)].mean()
sss3 = sss.loc[(sss['Per Student Budget'] >= 615) & (sss['Per Student Budget'] < 645)].mean()
sss4 = sss.loc[(sss['Per Student Budget'] >= 645) & (sss['Per Student Budget'] < 675)].mean()
sss_new = pd.DataFrame([sss1,sss2,sss3,sss4])
sss_new['% Overall Passing Rate'] = (sss_new['% Passing Math'] + sss_new['% Passing Reading'])/2
del sss_new['Per Student Budget']
sss_new['Spending Ranges (Per Student)'] = ['<$585','$585-615','$615-645','$645-675']
sss_new.set_index(['Spending Ranges (Per Student)'],inplace = True)
sss_new = sss_new.style.format({"Average Math Score": "{:.2f}", "Average Reading Score":"{:.2f}", 
                                "% Passing Math":"{:.2f}%","% Passing Reading":"{:.2f}%",
                               "% Overall Passing Rate":"{:.2f}%"})
sss_new
```




<style  type="text/css" >
</style>  
<table id="T_5822796e_942d_11e7_940f_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >% Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Spending Ranges (Per Student)</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5822796e_942d_11e7_940f_f48c5097b52flevel0_row0" class="row_heading level0 row0" ><$585</th> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow0_col0" class="data row0 col0" >83.46</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow0_col1" class="data row0 col1" >83.93</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow0_col2" class="data row0 col2" >93.46%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow0_col3" class="data row0 col3" >96.61%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow0_col4" class="data row0 col4" >95.04%</td> 
    </tr>    <tr> 
        <th id="T_5822796e_942d_11e7_940f_f48c5097b52flevel0_row1" class="row_heading level0 row1" >$585-615</th> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow1_col0" class="data row1 col0" >83.60</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow1_col1" class="data row1 col1" >83.89</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow1_col2" class="data row1 col2" >94.23%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow1_col3" class="data row1 col3" >95.90%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow1_col4" class="data row1 col4" >95.07%</td> 
    </tr>    <tr> 
        <th id="T_5822796e_942d_11e7_940f_f48c5097b52flevel0_row2" class="row_heading level0 row2" >$615-645</th> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow2_col0" class="data row2 col0" >79.08</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow2_col1" class="data row2 col1" >81.89</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow2_col2" class="data row2 col2" >75.67%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow2_col3" class="data row2 col3" >86.11%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow2_col4" class="data row2 col4" >80.89%</td> 
    </tr>    <tr> 
        <th id="T_5822796e_942d_11e7_940f_f48c5097b52flevel0_row3" class="row_heading level0 row3" >$645-675</th> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow3_col0" class="data row3 col0" >77.00</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow3_col1" class="data row3 col1" >81.03</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow3_col2" class="data row3 col2" >66.16%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow3_col3" class="data row3 col3" >81.13%</td> 
        <td id="T_5822796e_942d_11e7_940f_f48c5097b52frow3_col4" class="data row3 col4" >73.65%</td> 
    </tr></tbody> 
</table> 



## Scores by School Size


```python
ssz_temp = sch_sum.loc[:,['Total Students','Average Math Score','Average Reading Score',
                          '% Passing Math','% Passing Reading']]
ssz = ssz_temp.groupby(['Total Students'],as_index=False).mean()
ssz1 = ssz.loc[ssz['Total Students'] < 1000].mean()
ssz2 = ssz.loc[(ssz['Total Students'] >= 1000) & (ssz['Total Students'] < 2000)].mean()
ssz3 = ssz.loc[(ssz['Total Students'] >= 2000) & (ssz['Total Students'] < 5000)].mean()
ssz_new = pd.DataFrame([ssz1,ssz2,ssz3])
ssz_new['% Overall Passing Rate'] = (ssz_new['% Passing Math']+ssz_new['% Passing Reading'])/2
del ssz_new['Total Students']
ssz_new['School Size'] = ['Small (<1000)','Medium (1000-2000)','Large (2000-5000)']
ssz_new.set_index(['School Size'],inplace = True)
ssz_new = ssz_new.style.format({"Average Math Score": "{:.2f}", "Average Reading Score":"{:.2f}", 
                                "% Passing Math":"{:.2f}%","% Passing Reading":"{:.2f}%",
                               "% Overall Passing Rate":"{:.2f}%"})
ssz_new
```




<style  type="text/css" >
</style>  
<table id="T_582b8106_942d_11e7_8ba3_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >% Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >School Size</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_582b8106_942d_11e7_8ba3_f48c5097b52flevel0_row0" class="row_heading level0 row0" >Small (<1000)</th> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow0_col0" class="data row0 col0" >83.82</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow0_col1" class="data row0 col1" >83.93</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow0_col2" class="data row0 col2" >93.55%</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow0_col3" class="data row0 col3" >96.10%</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow0_col4" class="data row0 col4" >94.82%</td> 
    </tr>    <tr> 
        <th id="T_582b8106_942d_11e7_8ba3_f48c5097b52flevel0_row1" class="row_heading level0 row1" >Medium (1000-2000)</th> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow1_col0" class="data row1 col0" >83.37</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow1_col1" class="data row1 col1" >83.86</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow1_col2" class="data row1 col2" >93.60%</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow1_col3" class="data row1 col3" >96.79%</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow1_col4" class="data row1 col4" >95.20%</td> 
    </tr>    <tr> 
        <th id="T_582b8106_942d_11e7_8ba3_f48c5097b52flevel0_row2" class="row_heading level0 row2" >Large (2000-5000)</th> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow2_col0" class="data row2 col0" >77.75</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow2_col1" class="data row2 col1" >81.34</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow2_col2" class="data row2 col2" >69.96%</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow2_col3" class="data row2 col3" >82.77%</td> 
        <td id="T_582b8106_942d_11e7_8ba3_f48c5097b52frow2_col4" class="data row2 col4" >76.36%</td> 
    </tr></tbody> 
</table> 



## Scores by School Type


```python
sst_temp = sch_sum.loc[:,['School Type','Average Math Score','Average Reading Score',
                         '% Passing Math','% Passing Reading']]
sst = sst_temp.groupby('School Type')['Average Math Score', "Average Reading Score","% Passing Math",
                               '% Passing Reading'].mean()
sst['% Overall Passing Rate'] = (sst['% Passing Math']+sst['% Passing Reading'])/2
sst_new = sst.style.format({'Average Math Score': "{:.2f}", "Average Reading Score":"{:.2f}", 
                        "% Passing Math":"{:.2f}%","% Reading Math":"{:.2f}%","% Overall Passing Rate":"{:.2f}%"})
sst_new
```




<style  type="text/css" >
</style>  
<table id="T_5830b3e4_942d_11e7_8710_f48c5097b52f" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >% Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >School Type</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5830b3e4_942d_11e7_8710_f48c5097b52flevel0_row0" class="row_heading level0 row0" >Charter</th> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow0_col0" class="data row0 col0" >83.47</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow0_col1" class="data row0 col1" >83.90</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow0_col2" class="data row0 col2" >93.62%</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow0_col3" class="data row0 col3" >96.5865</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow0_col4" class="data row0 col4" >95.10%</td> 
    </tr>    <tr> 
        <th id="T_5830b3e4_942d_11e7_8710_f48c5097b52flevel0_row1" class="row_heading level0 row1" >District</th> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow1_col0" class="data row1 col0" >76.96</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow1_col1" class="data row1 col1" >80.97</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow1_col2" class="data row1 col2" >66.55%</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow1_col3" class="data row1 col3" >80.7991</td> 
        <td id="T_5830b3e4_942d_11e7_8710_f48c5097b52frow1_col4" class="data row1 col4" >73.67%</td> 
    </tr></tbody> 
</table> 




```python

```
