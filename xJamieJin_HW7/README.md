
# News Mood
### - Scores can shift dramatically based on current events, the general trend is that CNN and NYT are the closest to the neutral, Fox is generally more on the positive side (probably due to Trump and the conservative agenda being the majority), and CBS and BCC are more on the extreme side (positive or negative).
### - CBS had quite a few individual tweets that were above 0.75. On the otherhand, BBC had a quite a few individual tweets that were a below -0.75.
### - From the last 100 tweets, CBS is overwhelmingly positive, then Fox, and BBC. CNN and NYT were just below neutral in the negative zone.


```python
# Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import json
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
```


```python
# Twitter API Keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())
```


```python
# Target Account
target_user = ["@bbc","@cbs","@cnn","@foxnews","@nytimes"]

df = pd.DataFrame(columns = ['account_name','tweet','time_posted','compound_score','positive_score','neutral_score','negative_score'])
```


```python
count = 0
for user in target_user:
    
    for i in range(5):

        public_tweets = api.user_timeline(user)

        for ii in range(len(public_tweets)):
            try:
                df.set_value(count,'account_name',public_tweets[ii]["user"]["screen_name"])
                df.set_value(count,'tweet',public_tweets[ii]["text"])
                df.set_value(count,'time_posted',public_tweets[i]["created_at"])
                df.set_value(count,'compound_score',analyzer.polarity_scores(public_tweets[ii]["text"])["compound"])
                df.set_value(count,'positive_score',analyzer.polarity_scores(public_tweets[ii]["text"])["pos"])
                df.set_value(count,'neutral_score',analyzer.polarity_scores(public_tweets[ii]["text"])["neu"])
                df.set_value(count,'negative_score',analyzer.polarity_scores(public_tweets[ii]["text"])["neg"])
            except:
                print('tweet #{} failed'.format(count+1-(100*target_user.index(user))))
                break
            count += 1
            print('{} tweet #{} complete'.format(public_tweets[ii]['user']['screen_name'],(count-(100*target_user.index(user)))))
```

    BBC tweet #1 complete
    BBC tweet #2 complete
    BBC tweet #3 complete
    BBC tweet #4 complete
    BBC tweet #5 complete
    BBC tweet #6 complete
    BBC tweet #7 complete
    BBC tweet #8 complete
    BBC tweet #9 complete
    BBC tweet #10 complete
    BBC tweet #11 complete
    BBC tweet #12 complete
    BBC tweet #13 complete
    BBC tweet #14 complete
    BBC tweet #15 complete
    BBC tweet #16 complete
    BBC tweet #17 complete
    BBC tweet #18 complete
    BBC tweet #19 complete
    BBC tweet #20 complete
    BBC tweet #21 complete
    BBC tweet #22 complete
    BBC tweet #23 complete
    BBC tweet #24 complete
    BBC tweet #25 complete
    BBC tweet #26 complete
    BBC tweet #27 complete
    BBC tweet #28 complete
    BBC tweet #29 complete
    BBC tweet #30 complete
    BBC tweet #31 complete
    BBC tweet #32 complete
    BBC tweet #33 complete
    BBC tweet #34 complete
    BBC tweet #35 complete
    BBC tweet #36 complete
    BBC tweet #37 complete
    BBC tweet #38 complete
    BBC tweet #39 complete
    BBC tweet #40 complete
    BBC tweet #41 complete
    BBC tweet #42 complete
    BBC tweet #43 complete
    BBC tweet #44 complete
    BBC tweet #45 complete
    BBC tweet #46 complete
    BBC tweet #47 complete
    BBC tweet #48 complete
    BBC tweet #49 complete
    BBC tweet #50 complete
    BBC tweet #51 complete
    BBC tweet #52 complete
    BBC tweet #53 complete
    BBC tweet #54 complete
    BBC tweet #55 complete
    BBC tweet #56 complete
    BBC tweet #57 complete
    BBC tweet #58 complete
    BBC tweet #59 complete
    BBC tweet #60 complete
    BBC tweet #61 complete
    BBC tweet #62 complete
    BBC tweet #63 complete
    BBC tweet #64 complete
    BBC tweet #65 complete
    BBC tweet #66 complete
    BBC tweet #67 complete
    BBC tweet #68 complete
    BBC tweet #69 complete
    BBC tweet #70 complete
    BBC tweet #71 complete
    BBC tweet #72 complete
    BBC tweet #73 complete
    BBC tweet #74 complete
    BBC tweet #75 complete
    BBC tweet #76 complete
    BBC tweet #77 complete
    BBC tweet #78 complete
    BBC tweet #79 complete
    BBC tweet #80 complete
    BBC tweet #81 complete
    BBC tweet #82 complete
    BBC tweet #83 complete
    BBC tweet #84 complete
    BBC tweet #85 complete
    BBC tweet #86 complete
    BBC tweet #87 complete
    BBC tweet #88 complete
    BBC tweet #89 complete
    BBC tweet #90 complete
    BBC tweet #91 complete
    BBC tweet #92 complete
    BBC tweet #93 complete
    BBC tweet #94 complete
    BBC tweet #95 complete
    BBC tweet #96 complete
    BBC tweet #97 complete
    BBC tweet #98 complete
    BBC tweet #99 complete
    BBC tweet #100 complete
    CBS tweet #1 complete
    CBS tweet #2 complete
    CBS tweet #3 complete
    CBS tweet #4 complete
    CBS tweet #5 complete
    CBS tweet #6 complete
    CBS tweet #7 complete
    CBS tweet #8 complete
    CBS tweet #9 complete
    CBS tweet #10 complete
    CBS tweet #11 complete
    CBS tweet #12 complete
    CBS tweet #13 complete
    CBS tweet #14 complete
    CBS tweet #15 complete
    CBS tweet #16 complete
    CBS tweet #17 complete
    CBS tweet #18 complete
    CBS tweet #19 complete
    CBS tweet #20 complete
    CBS tweet #21 complete
    CBS tweet #22 complete
    CBS tweet #23 complete
    CBS tweet #24 complete
    CBS tweet #25 complete
    CBS tweet #26 complete
    CBS tweet #27 complete
    CBS tweet #28 complete
    CBS tweet #29 complete
    CBS tweet #30 complete
    CBS tweet #31 complete
    CBS tweet #32 complete
    CBS tweet #33 complete
    CBS tweet #34 complete
    CBS tweet #35 complete
    CBS tweet #36 complete
    CBS tweet #37 complete
    CBS tweet #38 complete
    CBS tweet #39 complete
    CBS tweet #40 complete
    CBS tweet #41 complete
    CBS tweet #42 complete
    CBS tweet #43 complete
    CBS tweet #44 complete
    CBS tweet #45 complete
    CBS tweet #46 complete
    CBS tweet #47 complete
    CBS tweet #48 complete
    CBS tweet #49 complete
    CBS tweet #50 complete
    CBS tweet #51 complete
    CBS tweet #52 complete
    CBS tweet #53 complete
    CBS tweet #54 complete
    CBS tweet #55 complete
    CBS tweet #56 complete
    CBS tweet #57 complete
    CBS tweet #58 complete
    CBS tweet #59 complete
    CBS tweet #60 complete
    CBS tweet #61 complete
    CBS tweet #62 complete
    CBS tweet #63 complete
    CBS tweet #64 complete
    CBS tweet #65 complete
    CBS tweet #66 complete
    CBS tweet #67 complete
    CBS tweet #68 complete
    CBS tweet #69 complete
    CBS tweet #70 complete
    CBS tweet #71 complete
    CBS tweet #72 complete
    CBS tweet #73 complete
    CBS tweet #74 complete
    CBS tweet #75 complete
    CBS tweet #76 complete
    CBS tweet #77 complete
    CBS tweet #78 complete
    CBS tweet #79 complete
    CBS tweet #80 complete
    CBS tweet #81 complete
    CBS tweet #82 complete
    CBS tweet #83 complete
    CBS tweet #84 complete
    CBS tweet #85 complete
    CBS tweet #86 complete
    CBS tweet #87 complete
    CBS tweet #88 complete
    CBS tweet #89 complete
    CBS tweet #90 complete
    CBS tweet #91 complete
    CBS tweet #92 complete
    CBS tweet #93 complete
    CBS tweet #94 complete
    CBS tweet #95 complete
    CBS tweet #96 complete
    CBS tweet #97 complete
    CBS tweet #98 complete
    CBS tweet #99 complete
    CBS tweet #100 complete
    CNN tweet #1 complete
    CNN tweet #2 complete
    CNN tweet #3 complete
    CNN tweet #4 complete
    CNN tweet #5 complete
    CNN tweet #6 complete
    CNN tweet #7 complete
    CNN tweet #8 complete
    CNN tweet #9 complete
    CNN tweet #10 complete
    CNN tweet #11 complete
    CNN tweet #12 complete
    CNN tweet #13 complete
    CNN tweet #14 complete
    CNN tweet #15 complete
    CNN tweet #16 complete
    CNN tweet #17 complete
    CNN tweet #18 complete
    CNN tweet #19 complete
    CNN tweet #20 complete
    CNN tweet #21 complete
    CNN tweet #22 complete
    CNN tweet #23 complete
    CNN tweet #24 complete
    CNN tweet #25 complete
    CNN tweet #26 complete
    CNN tweet #27 complete
    CNN tweet #28 complete
    CNN tweet #29 complete
    CNN tweet #30 complete
    CNN tweet #31 complete
    CNN tweet #32 complete
    CNN tweet #33 complete
    CNN tweet #34 complete
    CNN tweet #35 complete
    CNN tweet #36 complete
    CNN tweet #37 complete
    CNN tweet #38 complete
    CNN tweet #39 complete
    CNN tweet #40 complete
    CNN tweet #41 complete
    CNN tweet #42 complete
    CNN tweet #43 complete
    CNN tweet #44 complete
    CNN tweet #45 complete
    CNN tweet #46 complete
    CNN tweet #47 complete
    CNN tweet #48 complete
    CNN tweet #49 complete
    CNN tweet #50 complete
    CNN tweet #51 complete
    CNN tweet #52 complete
    CNN tweet #53 complete
    CNN tweet #54 complete
    CNN tweet #55 complete
    CNN tweet #56 complete
    CNN tweet #57 complete
    CNN tweet #58 complete
    CNN tweet #59 complete
    CNN tweet #60 complete
    CNN tweet #61 complete
    CNN tweet #62 complete
    CNN tweet #63 complete
    CNN tweet #64 complete
    CNN tweet #65 complete
    CNN tweet #66 complete
    CNN tweet #67 complete
    CNN tweet #68 complete
    CNN tweet #69 complete
    CNN tweet #70 complete
    CNN tweet #71 complete
    CNN tweet #72 complete
    CNN tweet #73 complete
    CNN tweet #74 complete
    CNN tweet #75 complete
    CNN tweet #76 complete
    CNN tweet #77 complete
    CNN tweet #78 complete
    CNN tweet #79 complete
    CNN tweet #80 complete
    CNN tweet #81 complete
    CNN tweet #82 complete
    CNN tweet #83 complete
    CNN tweet #84 complete
    CNN tweet #85 complete
    CNN tweet #86 complete
    CNN tweet #87 complete
    CNN tweet #88 complete
    CNN tweet #89 complete
    CNN tweet #90 complete
    CNN tweet #91 complete
    CNN tweet #92 complete
    CNN tweet #93 complete
    CNN tweet #94 complete
    CNN tweet #95 complete
    CNN tweet #96 complete
    CNN tweet #97 complete
    CNN tweet #98 complete
    CNN tweet #99 complete
    CNN tweet #100 complete
    FoxNews tweet #1 complete
    FoxNews tweet #2 complete
    FoxNews tweet #3 complete
    FoxNews tweet #4 complete
    FoxNews tweet #5 complete
    FoxNews tweet #6 complete
    FoxNews tweet #7 complete
    FoxNews tweet #8 complete
    FoxNews tweet #9 complete
    FoxNews tweet #10 complete
    FoxNews tweet #11 complete
    FoxNews tweet #12 complete
    FoxNews tweet #13 complete
    FoxNews tweet #14 complete
    FoxNews tweet #15 complete
    FoxNews tweet #16 complete
    FoxNews tweet #17 complete
    FoxNews tweet #18 complete
    FoxNews tweet #19 complete
    FoxNews tweet #20 complete
    FoxNews tweet #21 complete
    FoxNews tweet #22 complete
    FoxNews tweet #23 complete
    FoxNews tweet #24 complete
    FoxNews tweet #25 complete
    FoxNews tweet #26 complete
    FoxNews tweet #27 complete
    FoxNews tweet #28 complete
    FoxNews tweet #29 complete
    FoxNews tweet #30 complete
    FoxNews tweet #31 complete
    FoxNews tweet #32 complete
    FoxNews tweet #33 complete
    FoxNews tweet #34 complete
    FoxNews tweet #35 complete
    FoxNews tweet #36 complete
    FoxNews tweet #37 complete
    FoxNews tweet #38 complete
    FoxNews tweet #39 complete
    FoxNews tweet #40 complete
    FoxNews tweet #41 complete
    FoxNews tweet #42 complete
    FoxNews tweet #43 complete
    FoxNews tweet #44 complete
    FoxNews tweet #45 complete
    FoxNews tweet #46 complete
    FoxNews tweet #47 complete
    FoxNews tweet #48 complete
    FoxNews tweet #49 complete
    FoxNews tweet #50 complete
    FoxNews tweet #51 complete
    FoxNews tweet #52 complete
    FoxNews tweet #53 complete
    FoxNews tweet #54 complete
    FoxNews tweet #55 complete
    FoxNews tweet #56 complete
    FoxNews tweet #57 complete
    FoxNews tweet #58 complete
    FoxNews tweet #59 complete
    FoxNews tweet #60 complete
    FoxNews tweet #61 complete
    FoxNews tweet #62 complete
    FoxNews tweet #63 complete
    FoxNews tweet #64 complete
    FoxNews tweet #65 complete
    FoxNews tweet #66 complete
    FoxNews tweet #67 complete
    FoxNews tweet #68 complete
    FoxNews tweet #69 complete
    FoxNews tweet #70 complete
    FoxNews tweet #71 complete
    FoxNews tweet #72 complete
    FoxNews tweet #73 complete
    FoxNews tweet #74 complete
    FoxNews tweet #75 complete
    FoxNews tweet #76 complete
    FoxNews tweet #77 complete
    FoxNews tweet #78 complete
    FoxNews tweet #79 complete
    FoxNews tweet #80 complete
    FoxNews tweet #81 complete
    FoxNews tweet #82 complete
    FoxNews tweet #83 complete
    FoxNews tweet #84 complete
    FoxNews tweet #85 complete
    FoxNews tweet #86 complete
    FoxNews tweet #87 complete
    FoxNews tweet #88 complete
    FoxNews tweet #89 complete
    FoxNews tweet #90 complete
    FoxNews tweet #91 complete
    FoxNews tweet #92 complete
    FoxNews tweet #93 complete
    FoxNews tweet #94 complete
    FoxNews tweet #95 complete
    FoxNews tweet #96 complete
    FoxNews tweet #97 complete
    FoxNews tweet #98 complete
    FoxNews tweet #99 complete
    FoxNews tweet #100 complete
    nytimes tweet #1 complete
    nytimes tweet #2 complete
    nytimes tweet #3 complete
    nytimes tweet #4 complete
    nytimes tweet #5 complete
    nytimes tweet #6 complete
    nytimes tweet #7 complete
    nytimes tweet #8 complete
    nytimes tweet #9 complete
    nytimes tweet #10 complete
    nytimes tweet #11 complete
    nytimes tweet #12 complete
    nytimes tweet #13 complete
    nytimes tweet #14 complete
    nytimes tweet #15 complete
    nytimes tweet #16 complete
    nytimes tweet #17 complete
    nytimes tweet #18 complete
    nytimes tweet #19 complete
    nytimes tweet #20 complete
    nytimes tweet #21 complete
    nytimes tweet #22 complete
    nytimes tweet #23 complete
    nytimes tweet #24 complete
    nytimes tweet #25 complete
    nytimes tweet #26 complete
    nytimes tweet #27 complete
    nytimes tweet #28 complete
    nytimes tweet #29 complete
    nytimes tweet #30 complete
    nytimes tweet #31 complete
    nytimes tweet #32 complete
    nytimes tweet #33 complete
    nytimes tweet #34 complete
    nytimes tweet #35 complete
    nytimes tweet #36 complete
    nytimes tweet #37 complete
    nytimes tweet #38 complete
    nytimes tweet #39 complete
    nytimes tweet #40 complete
    nytimes tweet #41 complete
    nytimes tweet #42 complete
    nytimes tweet #43 complete
    nytimes tweet #44 complete
    nytimes tweet #45 complete
    nytimes tweet #46 complete
    nytimes tweet #47 complete
    nytimes tweet #48 complete
    nytimes tweet #49 complete
    nytimes tweet #50 complete
    nytimes tweet #51 complete
    nytimes tweet #52 complete
    nytimes tweet #53 complete
    nytimes tweet #54 complete
    nytimes tweet #55 complete
    nytimes tweet #56 complete
    nytimes tweet #57 complete
    nytimes tweet #58 complete
    nytimes tweet #59 complete
    nytimes tweet #60 complete
    nytimes tweet #61 complete
    nytimes tweet #62 complete
    nytimes tweet #63 complete
    nytimes tweet #64 complete
    nytimes tweet #65 complete
    nytimes tweet #66 complete
    nytimes tweet #67 complete
    nytimes tweet #68 complete
    nytimes tweet #69 complete
    nytimes tweet #70 complete
    nytimes tweet #71 complete
    nytimes tweet #72 complete
    nytimes tweet #73 complete
    nytimes tweet #74 complete
    nytimes tweet #75 complete
    nytimes tweet #76 complete
    nytimes tweet #77 complete
    nytimes tweet #78 complete
    nytimes tweet #79 complete
    nytimes tweet #80 complete
    nytimes tweet #81 complete
    nytimes tweet #82 complete
    nytimes tweet #83 complete
    nytimes tweet #84 complete
    nytimes tweet #85 complete
    nytimes tweet #86 complete
    nytimes tweet #87 complete
    nytimes tweet #88 complete
    nytimes tweet #89 complete
    nytimes tweet #90 complete
    nytimes tweet #91 complete
    nytimes tweet #92 complete
    nytimes tweet #93 complete
    nytimes tweet #94 complete
    nytimes tweet #95 complete
    nytimes tweet #96 complete
    nytimes tweet #97 complete
    nytimes tweet #98 complete
    nytimes tweet #99 complete
    nytimes tweet #100 complete
    


```python
df.to_csv("0_tweetsdf.csv", encoding="utf-8", index=False)
df.head()
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
      <th>account_name</th>
      <th>tweet</th>
      <th>time_posted</th>
      <th>compound_score</th>
      <th>positive_score</th>
      <th>neutral_score</th>
      <th>negative_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC</td>
      <td>👽🌍 Welcome back to Earth! Six people 'living o...</td>
      <td>Fri Sep 22 18:00:10 +0000 2017</td>
      <td>0.5093</td>
      <td>0.162</td>
      <td>0.838</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BBC</td>
      <td>Criminal networks smuggling rhino horn from Af...</td>
      <td>Fri Sep 22 18:00:10 +0000 2017</td>
      <td>-0.7579</td>
      <td>0</td>
      <td>0.683</td>
      <td>0.317</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BBC</td>
      <td>Tonight, the #LiveLounge Show features music f...</td>
      <td>Fri Sep 22 18:00:10 +0000 2017</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BBC</td>
      <td>👀 'I can see their eyes glowing in the dark &amp;a...</td>
      <td>Fri Sep 22 18:00:10 +0000 2017</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BBC</td>
      <td>Monochrome sportswear. Kebab. Techno. Repeat. ...</td>
      <td>Fri Sep 22 18:00:10 +0000 2017</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbc_comp = list(df.loc[df['account_name'] == 'BBC']['compound_score'])[::-1]
cbs_comp = list(df.loc[df['account_name'] == 'CBS']['compound_score'])[::-1]
cnn_comp = list(df.loc[df['account_name'] == 'CNN']['compound_score'])[::-1]
fox_comp = list(df.loc[df['account_name'] == 'FoxNews']['compound_score'])[::-1]
nyt_comp = list(df.loc[df['account_name'] == 'nytimes']['compound_score'])[::-1]

x_axis = list(range(100))
```


```python
plt.figure(figsize=(15,10))
bbc_scatter = plt.scatter(x_axis, bbc_comp, edgecolor="black", linewidths=1, marker="o", alpha=0.8, label="BBC", c='red')
cbs_scatter = plt.scatter(x_axis, cbs_comp, edgecolor="black", linewidths=1, marker="o", alpha=0.8, label="CBS", c='green')
cnn_scatter = plt.scatter(x_axis, cnn_comp, edgecolor="black", linewidths=1, marker="o", alpha=0.8, label="CNN", c='blue')
fox_scatter = plt.scatter(x_axis, fox_comp, edgecolor="black", linewidths=1, marker="o", alpha=0.8, label="FOX", c='yellow')
nyt_scatter = plt.scatter(x_axis, nyt_comp, edgecolor="black", linewidths=1, marker="o", alpha=0.8, label="NYT", c='magenta')

plt.xticks(range(0,101,20),range(100,-1,-20))
plt.title("Sentiment Analysis of Media Tweets ({})".format(time.strftime("%x")))
plt.ylabel("Tweet Polarity")
plt.xlabel("Tweets Ago")
plt.grid(True)
plt.ylim([-1,1])
plt.legend(loc='best')

plt.savefig("1_vaderscatter.png")
plt.show()
```


![png](output_7_0.png)



```python
plt.figure(figsize=(15,10))
vader_mean = [np.mean(bbc_comp),np.mean(cbs_comp),np.mean(cnn_comp),np.mean(fox_comp),np.mean(nyt_comp)]
plt.bar(range(len(vader_mean)),vader_mean,1,align='center',edgecolor='black',color=['red','green','blue','yellow','magenta'],
       tick_label=['BBC','CBS','CNN','FOX','NYT'])

for i in range(len(vader_mean)):
    if vader_mean[i] > 0:
        plt.text(i-0.1,vader_mean[i]+0.005,np.around(vader_mean[i],decimals=2),color='black',fontsize=15)
    else:
        plt.text(i-0.1,vader_mean[i]-0.015,np.around(vader_mean[i],decimals=2),color='black',fontsize=15)

plt.title("Overall Media Sentiment Based On Twitter ({})".format(time.strftime("%x")))
plt.ylabel("Tweet Polarity")
plt.savefig("2_vaderbar.png")
plt.show()
```


![png](output_8_0.png)



```python

```
