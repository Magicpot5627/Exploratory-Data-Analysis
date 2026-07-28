''' Merging database-style dataframes
Now, consider another use case where you are teaching two courses: Software Engineering and Introduction to Machine Learning. You will get two dataframes from each subject:

Two for the Software Engineering course
Another two for the Introduction to Machine Learning course.
There are important details you need to note in the preceding dataframes:

There are some students who are not taking the software engineering exam.
There are some students who are not taking the machine learning exam.
There are students who appeared in both courses.
Now, assume your head of department walked up to your desk and started bombarding you with a series of questions:

How many students appeared for the exams in total?
How many students only appeared for the Software Engineering course?
How many students only appeared for the Machine Learning course?  '''


import pandas as pd

df1SE =  pd.DataFrame({ 'StudentID': [9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],
                       'ScoreSE' : [22, 66, 31, 51, 71, 91, 56, 32, 52, 73, 92]})
df2SE =  pd.DataFrame({'StudentID': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
                       'ScoreSE': [98, 93, 44, 77, 69, 56, 31, 53, 78, 93, 56, 77, 33, 56, 27]})

df1ML =  pd.DataFrame({ 'StudentID': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],
                       'ScoreML' : [39, 49, 55, 77, 52, 86, 41, 77, 73, 51, 86, 82, 92, 23, 49]})
df2ML =  pd.DataFrame({'StudentID': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                       'ScoreML': [93, 44, 78, 97, 87, 89, 39, 43, 88, 78]})

# Option 1
dfSE = pd.concat([df1SE, df2SE], ignore_index=True)
dfML = pd.concat([df1ML, df2ML], ignore_index=True)
df = pd.concat([dfML, dfSE], axis=1)
df

# # Option 2
# df = dfSE.merge(dfML, how='inner')  # Here we will perform inner join with each dataframe.
# df

# # Option 3
# dfSE = pd.concat([df1SE, df2SE], ignore_index=True)
# dfML = pd.concat([df1ML, df2ML], ignore_index=True)
# df = dfSE.merge(dfML, how='left')
# df

# # Option 4
# dfSE = pd.concat([df1SE, df2SE], ignore_index=True)
# dfML = pd.concat([df1ML, df2ML], ignore_index=True)
# df = dfSE.merge(dfML, how='right')
# df
# df = pd.read_csv('https://raw.githubusercontent.com/rameshc70707/EDA/main/Data/sales.csv')
# df.head(10)