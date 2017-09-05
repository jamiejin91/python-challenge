
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

        <table id="T_603655d2_8f4b_11e7_877b_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  School Type
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  Total Students
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  Total School Budget
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  Per Student Budget
                
                
                
                <th class="col_heading level0 col4" colspan=1>
                  Average Math Score
                
                
                
                <th class="col_heading level0 col5" colspan=1>
                  Average Reading Score
                
                
                
                <th class="col_heading level0 col6" colspan=1>
                  % Passing Math
                
                
                
                <th class="col_heading level0 col7" colspan=1>
                  % Passing Reading
                
                
                
                <th class="col_heading level0 col8" colspan=1>
                  % Overall Passing Rate
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    Bailey High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    District
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    4976
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    $3,124,928.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    $628.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col4"
                 class="data row0 col4" >
                    77.05
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col5"
                 class="data row0 col5" >
                    81.03
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col6"
                 class="data row0 col6" >
                    66.68%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col7"
                 class="data row0 col7" >
                    81.93%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row0_col8"
                 class="data row0 col8" >
                    74.31%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    Cabrera High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    1858
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    $1,081,356.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    $582.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col4"
                 class="data row1 col4" >
                    83.06
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col5"
                 class="data row1 col5" >
                    83.98
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col6"
                 class="data row1 col6" >
                    94.13%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col7"
                 class="data row1 col7" >
                    97.04%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row1_col8"
                 class="data row1 col8" >
                    95.59%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row2" rowspan=1>
                    Figueroa High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col0"
                 class="data row2 col0" >
                    District
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col1"
                 class="data row2 col1" >
                    2949
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col2"
                 class="data row2 col2" >
                    $1,884,411.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col3"
                 class="data row2 col3" >
                    $639.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col4"
                 class="data row2 col4" >
                    76.71
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col5"
                 class="data row2 col5" >
                    81.16
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col6"
                 class="data row2 col6" >
                    65.99%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col7"
                 class="data row2 col7" >
                    80.74%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row2_col8"
                 class="data row2 col8" >
                    73.36%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row3" rowspan=1>
                    Ford High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col0"
                 class="data row3 col0" >
                    District
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col1"
                 class="data row3 col1" >
                    2739
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col2"
                 class="data row3 col2" >
                    $1,763,916.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col3"
                 class="data row3 col3" >
                    $644.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col4"
                 class="data row3 col4" >
                    77.10
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col5"
                 class="data row3 col5" >
                    80.75
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col6"
                 class="data row3 col6" >
                    68.31%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col7"
                 class="data row3 col7" >
                    79.30%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row3_col8"
                 class="data row3 col8" >
                    73.80%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row4" rowspan=1>
                    Griffin High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col0"
                 class="data row4 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col1"
                 class="data row4 col1" >
                    1468
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col2"
                 class="data row4 col2" >
                    $917,500.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col3"
                 class="data row4 col3" >
                    $625.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col4"
                 class="data row4 col4" >
                    83.35
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col5"
                 class="data row4 col5" >
                    83.82
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col6"
                 class="data row4 col6" >
                    93.39%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col7"
                 class="data row4 col7" >
                    97.14%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row4_col8"
                 class="data row4 col8" >
                    95.27%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row5" rowspan=1>
                    Hernandez High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col0"
                 class="data row5 col0" >
                    District
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col1"
                 class="data row5 col1" >
                    4635
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col2"
                 class="data row5 col2" >
                    $3,022,020.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col3"
                 class="data row5 col3" >
                    $652.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col4"
                 class="data row5 col4" >
                    77.29
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col5"
                 class="data row5 col5" >
                    80.93
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col6"
                 class="data row5 col6" >
                    66.75%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col7"
                 class="data row5 col7" >
                    80.86%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row5_col8"
                 class="data row5 col8" >
                    73.81%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row6" rowspan=1>
                    Holden High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col0"
                 class="data row6 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col1"
                 class="data row6 col1" >
                    427
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col2"
                 class="data row6 col2" >
                    $248,087.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col3"
                 class="data row6 col3" >
                    $581.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col4"
                 class="data row6 col4" >
                    83.80
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col5"
                 class="data row6 col5" >
                    83.81
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col6"
                 class="data row6 col6" >
                    92.51%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col7"
                 class="data row6 col7" >
                    96.25%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row6_col8"
                 class="data row6 col8" >
                    94.38%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row7" rowspan=1>
                    Huang High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col0"
                 class="data row7 col0" >
                    District
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col1"
                 class="data row7 col1" >
                    2917
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col2"
                 class="data row7 col2" >
                    $1,910,635.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col3"
                 class="data row7 col3" >
                    $655.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col4"
                 class="data row7 col4" >
                    76.63
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col5"
                 class="data row7 col5" >
                    81.18
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col6"
                 class="data row7 col6" >
                    65.68%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col7"
                 class="data row7 col7" >
                    81.32%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row7_col8"
                 class="data row7 col8" >
                    73.50%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row8" rowspan=1>
                    Johnson High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col0"
                 class="data row8 col0" >
                    District
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col1"
                 class="data row8 col1" >
                    4761
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col2"
                 class="data row8 col2" >
                    $3,094,650.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col3"
                 class="data row8 col3" >
                    $650.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col4"
                 class="data row8 col4" >
                    77.07
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col5"
                 class="data row8 col5" >
                    80.97
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col6"
                 class="data row8 col6" >
                    66.06%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col7"
                 class="data row8 col7" >
                    81.22%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row8_col8"
                 class="data row8 col8" >
                    73.64%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row9" rowspan=1>
                    Pena High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col0"
                 class="data row9 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col1"
                 class="data row9 col1" >
                    962
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col2"
                 class="data row9 col2" >
                    $585,858.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col3"
                 class="data row9 col3" >
                    $609.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col4"
                 class="data row9 col4" >
                    83.84
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col5"
                 class="data row9 col5" >
                    84.04
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col6"
                 class="data row9 col6" >
                    94.59%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col7"
                 class="data row9 col7" >
                    95.95%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row9_col8"
                 class="data row9 col8" >
                    95.27%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row10" rowspan=1>
                    Rodriguez High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col0"
                 class="data row10 col0" >
                    District
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col1"
                 class="data row10 col1" >
                    3999
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col2"
                 class="data row10 col2" >
                    $2,547,363.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col3"
                 class="data row10 col3" >
                    $637.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col4"
                 class="data row10 col4" >
                    76.84
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col5"
                 class="data row10 col5" >
                    80.74
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col6"
                 class="data row10 col6" >
                    66.37%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col7"
                 class="data row10 col7" >
                    80.22%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row10_col8"
                 class="data row10 col8" >
                    73.29%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row11" rowspan=1>
                    Shelton High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col0"
                 class="data row11 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col1"
                 class="data row11 col1" >
                    1761
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col2"
                 class="data row11 col2" >
                    $1,056,600.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col3"
                 class="data row11 col3" >
                    $600.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col4"
                 class="data row11 col4" >
                    83.36
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col5"
                 class="data row11 col5" >
                    83.73
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col6"
                 class="data row11 col6" >
                    93.87%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col7"
                 class="data row11 col7" >
                    95.85%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row11_col8"
                 class="data row11 col8" >
                    94.86%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row12" rowspan=1>
                    Thomas High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col0"
                 class="data row12 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col1"
                 class="data row12 col1" >
                    1635
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col2"
                 class="data row12 col2" >
                    $1,043,130.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col3"
                 class="data row12 col3" >
                    $638.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col4"
                 class="data row12 col4" >
                    83.42
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col5"
                 class="data row12 col5" >
                    83.85
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col6"
                 class="data row12 col6" >
                    93.27%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col7"
                 class="data row12 col7" >
                    97.31%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row12_col8"
                 class="data row12 col8" >
                    95.29%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row13" rowspan=1>
                    Wilson High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col0"
                 class="data row13 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col1"
                 class="data row13 col1" >
                    2283
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col2"
                 class="data row13 col2" >
                    $1,319,574.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col3"
                 class="data row13 col3" >
                    $578.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col4"
                 class="data row13 col4" >
                    83.27
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col5"
                 class="data row13 col5" >
                    83.99
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col6"
                 class="data row13 col6" >
                    93.87%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col7"
                 class="data row13 col7" >
                    96.54%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row13_col8"
                 class="data row13 col8" >
                    95.20%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_603655d2_8f4b_11e7_877b_b4b6765f9203"
                 class="row_heading level0 row14" rowspan=1>
                    Wright High School
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col0"
                 class="data row14 col0" >
                    Charter
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col1"
                 class="data row14 col1" >
                    1800
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col2"
                 class="data row14 col2" >
                    $1,049,400.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col3"
                 class="data row14 col3" >
                    $583.00
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col4"
                 class="data row14 col4" >
                    83.68
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col5"
                 class="data row14 col5" >
                    83.95
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col6"
                 class="data row14 col6" >
                    93.33%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col7"
                 class="data row14 col7" >
                    96.61%
                
                
                
                <td id="T_603655d2_8f4b_11e7_877b_b4b6765f9203row14_col8"
                 class="data row14 col8" >
                    94.97%
                
                
            </tr>
            
        </tbody>
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

        <table id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  School Type
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  Total Students
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  Total School Budget
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  Per Student Budget
                
                
                
                <th class="col_heading level0 col4" colspan=1>
                  Average Math Score
                
                
                
                <th class="col_heading level0 col5" colspan=1>
                  Average Reading Score
                
                
                
                <th class="col_heading level0 col6" colspan=1>
                  % Passing Math
                
                
                
                <th class="col_heading level0 col7" colspan=1>
                  % Passing Reading
                
                
                
                <th class="col_heading level0 col8" colspan=1>
                  % Overall Passing Rate
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    Cabrera High School
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    Charter
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    1858
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    $1,081,356.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    $582.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col4"
                 class="data row0 col4" >
                    83.06
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col5"
                 class="data row0 col5" >
                    83.98
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col6"
                 class="data row0 col6" >
                    94.13%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col7"
                 class="data row0 col7" >
                    97.04%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row0_col8"
                 class="data row0 col8" >
                    95.59%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    Thomas High School
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    Charter
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    1635
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    $1,043,130.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    $638.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col4"
                 class="data row1 col4" >
                    83.42
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col5"
                 class="data row1 col5" >
                    83.85
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col6"
                 class="data row1 col6" >
                    93.27%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col7"
                 class="data row1 col7" >
                    97.31%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row1_col8"
                 class="data row1 col8" >
                    95.29%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203"
                 class="row_heading level0 row2" rowspan=1>
                    Pena High School
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col0"
                 class="data row2 col0" >
                    Charter
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col1"
                 class="data row2 col1" >
                    962
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col2"
                 class="data row2 col2" >
                    $585,858.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col3"
                 class="data row2 col3" >
                    $609.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col4"
                 class="data row2 col4" >
                    83.84
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col5"
                 class="data row2 col5" >
                    84.04
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col6"
                 class="data row2 col6" >
                    94.59%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col7"
                 class="data row2 col7" >
                    95.95%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row2_col8"
                 class="data row2 col8" >
                    95.27%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203"
                 class="row_heading level0 row3" rowspan=1>
                    Griffin High School
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col0"
                 class="data row3 col0" >
                    Charter
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col1"
                 class="data row3 col1" >
                    1468
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col2"
                 class="data row3 col2" >
                    $917,500.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col3"
                 class="data row3 col3" >
                    $625.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col4"
                 class="data row3 col4" >
                    83.35
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col5"
                 class="data row3 col5" >
                    83.82
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col6"
                 class="data row3 col6" >
                    93.39%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col7"
                 class="data row3 col7" >
                    97.14%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row3_col8"
                 class="data row3 col8" >
                    95.27%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203"
                 class="row_heading level0 row4" rowspan=1>
                    Wilson High School
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col0"
                 class="data row4 col0" >
                    Charter
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col1"
                 class="data row4 col1" >
                    2283
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col2"
                 class="data row4 col2" >
                    $1,319,574.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col3"
                 class="data row4 col3" >
                    $578.00
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col4"
                 class="data row4 col4" >
                    83.27
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col5"
                 class="data row4 col5" >
                    83.99
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col6"
                 class="data row4 col6" >
                    93.87%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col7"
                 class="data row4 col7" >
                    96.54%
                
                
                
                <td id="T_604179a8_8f4b_11e7_95c9_b4b6765f9203row4_col8"
                 class="data row4 col8" >
                    95.20%
                
                
            </tr>
            
        </tbody>
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

        <table id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  School Type
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  Total Students
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  Total School Budget
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  Per Student Budget
                
                
                
                <th class="col_heading level0 col4" colspan=1>
                  Average Math Score
                
                
                
                <th class="col_heading level0 col5" colspan=1>
                  Average Reading Score
                
                
                
                <th class="col_heading level0 col6" colspan=1>
                  % Passing Math
                
                
                
                <th class="col_heading level0 col7" colspan=1>
                  % Passing Reading
                
                
                
                <th class="col_heading level0 col8" colspan=1>
                  % Overall Passing Rate
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    Rodriguez High School
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    District
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    3999
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    $2,547,363.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    $637.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col4"
                 class="data row0 col4" >
                    76.84
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col5"
                 class="data row0 col5" >
                    80.74
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col6"
                 class="data row0 col6" >
                    66.37%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col7"
                 class="data row0 col7" >
                    80.22%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row0_col8"
                 class="data row0 col8" >
                    73.29%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    Figueroa High School
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    District
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    2949
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    $1,884,411.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    $639.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col4"
                 class="data row1 col4" >
                    76.71
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col5"
                 class="data row1 col5" >
                    81.16
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col6"
                 class="data row1 col6" >
                    65.99%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col7"
                 class="data row1 col7" >
                    80.74%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row1_col8"
                 class="data row1 col8" >
                    73.36%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203"
                 class="row_heading level0 row2" rowspan=1>
                    Huang High School
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col0"
                 class="data row2 col0" >
                    District
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col1"
                 class="data row2 col1" >
                    2917
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col2"
                 class="data row2 col2" >
                    $1,910,635.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col3"
                 class="data row2 col3" >
                    $655.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col4"
                 class="data row2 col4" >
                    76.63
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col5"
                 class="data row2 col5" >
                    81.18
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col6"
                 class="data row2 col6" >
                    65.68%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col7"
                 class="data row2 col7" >
                    81.32%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row2_col8"
                 class="data row2 col8" >
                    73.50%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203"
                 class="row_heading level0 row3" rowspan=1>
                    Johnson High School
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col0"
                 class="data row3 col0" >
                    District
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col1"
                 class="data row3 col1" >
                    4761
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col2"
                 class="data row3 col2" >
                    $3,094,650.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col3"
                 class="data row3 col3" >
                    $650.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col4"
                 class="data row3 col4" >
                    77.07
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col5"
                 class="data row3 col5" >
                    80.97
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col6"
                 class="data row3 col6" >
                    66.06%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col7"
                 class="data row3 col7" >
                    81.22%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row3_col8"
                 class="data row3 col8" >
                    73.64%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203"
                 class="row_heading level0 row4" rowspan=1>
                    Ford High School
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col0"
                 class="data row4 col0" >
                    District
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col1"
                 class="data row4 col1" >
                    2739
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col2"
                 class="data row4 col2" >
                    $1,763,916.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col3"
                 class="data row4 col3" >
                    $644.00
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col4"
                 class="data row4 col4" >
                    77.10
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col5"
                 class="data row4 col5" >
                    80.75
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col6"
                 class="data row4 col6" >
                    68.31%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col7"
                 class="data row4 col7" >
                    79.30%
                
                
                
                <td id="T_60480986_8f4b_11e7_ae2e_b4b6765f9203row4_col8"
                 class="data row4 col8" >
                    73.80%
                
                
            </tr>
            
        </tbody>
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

        <table id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  9th
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  10th
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  11th
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  12th
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    Bailey High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    77.08
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    77.00
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    77.52
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    76.49
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    Cabrera High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    83.09
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    83.15
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    82.77
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    83.28
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row2" rowspan=1>
                    Figueroa High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row2_col0"
                 class="data row2 col0" >
                    76.40
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row2_col1"
                 class="data row2 col1" >
                    76.54
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row2_col2"
                 class="data row2 col2" >
                    76.88
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row2_col3"
                 class="data row2 col3" >
                    77.15
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row3" rowspan=1>
                    Ford High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row3_col0"
                 class="data row3 col0" >
                    77.36
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row3_col1"
                 class="data row3 col1" >
                    77.67
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row3_col2"
                 class="data row3 col2" >
                    76.92
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row3_col3"
                 class="data row3 col3" >
                    76.18
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row4" rowspan=1>
                    Griffin High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row4_col0"
                 class="data row4 col0" >
                    82.04
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row4_col1"
                 class="data row4 col1" >
                    84.23
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row4_col2"
                 class="data row4 col2" >
                    83.84
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row4_col3"
                 class="data row4 col3" >
                    83.36
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row5" rowspan=1>
                    Hernandez High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row5_col0"
                 class="data row5 col0" >
                    77.44
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row5_col1"
                 class="data row5 col1" >
                    77.34
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row5_col2"
                 class="data row5 col2" >
                    77.14
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row5_col3"
                 class="data row5 col3" >
                    77.19
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row6" rowspan=1>
                    Holden High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row6_col0"
                 class="data row6 col0" >
                    83.79
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row6_col1"
                 class="data row6 col1" >
                    83.43
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row6_col2"
                 class="data row6 col2" >
                    85.00
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row6_col3"
                 class="data row6 col3" >
                    82.86
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row7" rowspan=1>
                    Huang High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row7_col0"
                 class="data row7 col0" >
                    77.03
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row7_col1"
                 class="data row7 col1" >
                    75.91
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row7_col2"
                 class="data row7 col2" >
                    76.45
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row7_col3"
                 class="data row7 col3" >
                    77.23
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row8" rowspan=1>
                    Johnson High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row8_col0"
                 class="data row8 col0" >
                    77.19
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row8_col1"
                 class="data row8 col1" >
                    76.69
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row8_col2"
                 class="data row8 col2" >
                    77.49
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row8_col3"
                 class="data row8 col3" >
                    76.86
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row9" rowspan=1>
                    Pena High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row9_col0"
                 class="data row9 col0" >
                    83.63
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row9_col1"
                 class="data row9 col1" >
                    83.37
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row9_col2"
                 class="data row9 col2" >
                    84.33
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row9_col3"
                 class="data row9 col3" >
                    84.12
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row10" rowspan=1>
                    Rodriguez High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row10_col0"
                 class="data row10 col0" >
                    76.86
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row10_col1"
                 class="data row10 col1" >
                    76.61
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row10_col2"
                 class="data row10 col2" >
                    76.40
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row10_col3"
                 class="data row10 col3" >
                    77.69
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row11" rowspan=1>
                    Shelton High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row11_col0"
                 class="data row11 col0" >
                    83.42
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row11_col1"
                 class="data row11 col1" >
                    82.92
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row11_col2"
                 class="data row11 col2" >
                    83.38
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row11_col3"
                 class="data row11 col3" >
                    83.78
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row12" rowspan=1>
                    Thomas High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row12_col0"
                 class="data row12 col0" >
                    83.59
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row12_col1"
                 class="data row12 col1" >
                    83.09
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row12_col2"
                 class="data row12 col2" >
                    83.50
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row12_col3"
                 class="data row12 col3" >
                    83.50
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row13" rowspan=1>
                    Wilson High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row13_col0"
                 class="data row13 col0" >
                    83.09
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row13_col1"
                 class="data row13 col1" >
                    83.72
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row13_col2"
                 class="data row13 col2" >
                    83.20
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row13_col3"
                 class="data row13 col3" >
                    83.04
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203"
                 class="row_heading level0 row14" rowspan=1>
                    Wright High School
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row14_col0"
                 class="data row14 col0" >
                    83.26
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row14_col1"
                 class="data row14 col1" >
                    84.01
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row14_col2"
                 class="data row14 col2" >
                    83.84
                
                
                
                <td id="T_605cf19e_8f4b_11e7_a768_b4b6765f9203row14_col3"
                 class="data row14 col3" >
                    83.64
                
                
            </tr>
            
        </tbody>
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

        <table id="T_607227da_8f4b_11e7_994d_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  9th
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  10th
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  11th
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  12th
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    Bailey High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    81.30
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    80.91
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    80.95
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    80.91
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    Cabrera High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    83.68
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    84.25
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    83.79
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    84.29
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row2" rowspan=1>
                    Figueroa High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row2_col0"
                 class="data row2 col0" >
                    81.20
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row2_col1"
                 class="data row2 col1" >
                    81.41
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row2_col2"
                 class="data row2 col2" >
                    80.64
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row2_col3"
                 class="data row2 col3" >
                    81.38
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row3" rowspan=1>
                    Ford High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row3_col0"
                 class="data row3 col0" >
                    80.63
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row3_col1"
                 class="data row3 col1" >
                    81.26
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row3_col2"
                 class="data row3 col2" >
                    80.40
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row3_col3"
                 class="data row3 col3" >
                    80.66
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row4" rowspan=1>
                    Griffin High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row4_col0"
                 class="data row4 col0" >
                    83.37
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row4_col1"
                 class="data row4 col1" >
                    83.71
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row4_col2"
                 class="data row4 col2" >
                    84.29
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row4_col3"
                 class="data row4 col3" >
                    84.01
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row5" rowspan=1>
                    Hernandez High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row5_col0"
                 class="data row5 col0" >
                    80.87
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row5_col1"
                 class="data row5 col1" >
                    80.66
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row5_col2"
                 class="data row5 col2" >
                    81.40
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row5_col3"
                 class="data row5 col3" >
                    80.86
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row6" rowspan=1>
                    Holden High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row6_col0"
                 class="data row6 col0" >
                    83.68
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row6_col1"
                 class="data row6 col1" >
                    83.32
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row6_col2"
                 class="data row6 col2" >
                    83.82
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row6_col3"
                 class="data row6 col3" >
                    84.70
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row7" rowspan=1>
                    Huang High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row7_col0"
                 class="data row7 col0" >
                    81.29
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row7_col1"
                 class="data row7 col1" >
                    81.51
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row7_col2"
                 class="data row7 col2" >
                    81.42
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row7_col3"
                 class="data row7 col3" >
                    80.31
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row8" rowspan=1>
                    Johnson High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row8_col0"
                 class="data row8 col0" >
                    81.26
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row8_col1"
                 class="data row8 col1" >
                    80.77
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row8_col2"
                 class="data row8 col2" >
                    80.62
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row8_col3"
                 class="data row8 col3" >
                    81.23
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row9" rowspan=1>
                    Pena High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row9_col0"
                 class="data row9 col0" >
                    83.81
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row9_col1"
                 class="data row9 col1" >
                    83.61
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row9_col2"
                 class="data row9 col2" >
                    84.34
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row9_col3"
                 class="data row9 col3" >
                    84.59
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row10" rowspan=1>
                    Rodriguez High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row10_col0"
                 class="data row10 col0" >
                    80.99
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row10_col1"
                 class="data row10 col1" >
                    80.63
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row10_col2"
                 class="data row10 col2" >
                    80.86
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row10_col3"
                 class="data row10 col3" >
                    80.38
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row11" rowspan=1>
                    Shelton High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row11_col0"
                 class="data row11 col0" >
                    84.12
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row11_col1"
                 class="data row11 col1" >
                    83.44
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row11_col2"
                 class="data row11 col2" >
                    84.37
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row11_col3"
                 class="data row11 col3" >
                    82.78
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row12" rowspan=1>
                    Thomas High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row12_col0"
                 class="data row12 col0" >
                    83.73
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row12_col1"
                 class="data row12 col1" >
                    84.25
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row12_col2"
                 class="data row12 col2" >
                    83.59
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row12_col3"
                 class="data row12 col3" >
                    83.83
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row13" rowspan=1>
                    Wilson High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row13_col0"
                 class="data row13 col0" >
                    83.94
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row13_col1"
                 class="data row13 col1" >
                    84.02
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row13_col2"
                 class="data row13 col2" >
                    83.76
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row13_col3"
                 class="data row13 col3" >
                    84.32
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607227da_8f4b_11e7_994d_b4b6765f9203"
                 class="row_heading level0 row14" rowspan=1>
                    Wright High School
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row14_col0"
                 class="data row14 col0" >
                    83.83
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row14_col1"
                 class="data row14 col1" >
                    83.81
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row14_col2"
                 class="data row14 col2" >
                    84.16
                
                
                
                <td id="T_607227da_8f4b_11e7_994d_b4b6765f9203row14_col3"
                 class="data row14 col3" >
                    84.07
                
                
            </tr>
            
        </tbody>
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

        <table id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  Average Math Score
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  Average Reading Score
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  % Passing Math
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  % Passing Reading
                
                
                
                <th class="col_heading level0 col4" colspan=1>
                  % Overall Passing Rate
                
                
            </tr>
            
            <tr>
                
                
                <th class="index_name level0" >
                  Spending Ranges (Per Student)
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    <$585
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    83.46
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    83.93
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    93.46%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    96.61%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row0_col4"
                 class="data row0 col4" >
                    95.04%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    $585-615
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    83.60
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    83.89
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    94.23%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    95.90%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row1_col4"
                 class="data row1 col4" >
                    95.07%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203"
                 class="row_heading level0 row2" rowspan=1>
                    $615-645
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row2_col0"
                 class="data row2 col0" >
                    79.08
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row2_col1"
                 class="data row2 col1" >
                    81.89
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row2_col2"
                 class="data row2 col2" >
                    75.67%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row2_col3"
                 class="data row2 col3" >
                    86.11%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row2_col4"
                 class="data row2 col4" >
                    80.89%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203"
                 class="row_heading level0 row3" rowspan=1>
                    $645-675
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row3_col0"
                 class="data row3 col0" >
                    77.00
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row3_col1"
                 class="data row3 col1" >
                    81.03
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row3_col2"
                 class="data row3 col2" >
                    66.16%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row3_col3"
                 class="data row3 col3" >
                    81.13%
                
                
                
                <td id="T_607fe3d2_8f4b_11e7_a43a_b4b6765f9203row3_col4"
                 class="data row3 col4" >
                    73.65%
                
                
            </tr>
            
        </tbody>
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

        <table id="T_60898102_8f4b_11e7_827b_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  Average Math Score
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  Average Reading Score
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  % Passing Math
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  % Passing Reading
                
                
                
                <th class="col_heading level0 col4" colspan=1>
                  % Overall Passing Rate
                
                
            </tr>
            
            <tr>
                
                
                <th class="index_name level0" >
                  School Size
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_60898102_8f4b_11e7_827b_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    Small (<1000)
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    83.82
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    83.93
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    93.55%
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    96.10%
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row0_col4"
                 class="data row0 col4" >
                    94.82%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_60898102_8f4b_11e7_827b_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    Medium (1000-2000)
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    83.37
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    83.86
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    93.60%
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    96.79%
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row1_col4"
                 class="data row1 col4" >
                    95.20%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_60898102_8f4b_11e7_827b_b4b6765f9203"
                 class="row_heading level0 row2" rowspan=1>
                    Large (2000-5000)
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row2_col0"
                 class="data row2 col0" >
                    77.75
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row2_col1"
                 class="data row2 col1" >
                    81.34
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row2_col2"
                 class="data row2 col2" >
                    69.96%
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row2_col3"
                 class="data row2 col3" >
                    82.77%
                
                
                
                <td id="T_60898102_8f4b_11e7_827b_b4b6765f9203row2_col4"
                 class="data row2 col4" >
                    76.36%
                
                
            </tr>
            
        </tbody>
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

        <table id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203" None>
        

        <thead>
            
            <tr>
                
                
                <th class="blank level0" >
                  
                
                
                
                <th class="col_heading level0 col0" colspan=1>
                  Average Math Score
                
                
                
                <th class="col_heading level0 col1" colspan=1>
                  Average Reading Score
                
                
                
                <th class="col_heading level0 col2" colspan=1>
                  % Passing Math
                
                
                
                <th class="col_heading level0 col3" colspan=1>
                  % Passing Reading
                
                
                
                <th class="col_heading level0 col4" colspan=1>
                  % Overall Passing Rate
                
                
            </tr>
            
            <tr>
                
                
                <th class="index_name level0" >
                  School Type
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
                
                <th class="blank" >
                  
                
                
            </tr>
            
        </thead>
        <tbody>
            
            <tr>
                
                
                <th id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203"
                 class="row_heading level0 row0" rowspan=1>
                    Charter
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row0_col0"
                 class="data row0 col0" >
                    83.47
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row0_col1"
                 class="data row0 col1" >
                    83.90
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row0_col2"
                 class="data row0 col2" >
                    93.62%
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row0_col3"
                 class="data row0 col3" >
                    96.5865
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row0_col4"
                 class="data row0 col4" >
                    95.10%
                
                
            </tr>
            
            <tr>
                
                
                <th id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203"
                 class="row_heading level0 row1" rowspan=1>
                    District
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row1_col0"
                 class="data row1 col0" >
                    76.96
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row1_col1"
                 class="data row1 col1" >
                    80.97
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row1_col2"
                 class="data row1 col2" >
                    66.55%
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row1_col3"
                 class="data row1 col3" >
                    80.7991
                
                
                
                <td id="T_608e3c12_8f4b_11e7_bb13_b4b6765f9203row1_col4"
                 class="data row1 col4" >
                    73.67%
                
                
            </tr>
            
        </tbody>
        </table>
        




```python

```
