import pandas as pd
df=pd.read_csv('input/main.csv')
filteredCountry=pd.DataFrame(columns=df.columns)
i=0
for index,row in df.iterrows():
    if 'usa' in str(row['COUNTRY']).lower():
        filteredCountry.loc[i]=row
        i=i+1
filteredCountry.to_csv('output/filteredCountry.csv', index=False)