import pandas as pd


"""
   native-country salary  unique-values
0               ?  <=50K      74.957118
1               ?   >50K      25.042882
2        Cambodia  <=50K      63.157895
3        Cambodia   >50K      36.842105
"""


df = pd.DataFrame([['?', '<=50K', 74.957118],
                   ['?', '>50K', 25.042882],
                   ['Cambodia', '<=50K', 63.157895],
                   ['Cambodia', '>50K', 36.842105]],
     index=[0, 1, 2, 3],
     columns=['native-country', 'salary', 'unique-values'])

print(df)
print('------------')
test = df.loc[df['salary'] == '>50K']
print(test)
