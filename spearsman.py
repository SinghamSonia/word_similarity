import pandas as pd



df=pd.read_csv("Similarity 2 - Sheet1.csv")
n=len(df.index)
list1=(df.values.tolist())
list1.sort(key=lambda r:r[2])
df1=pd.DataFrame(list1,columns=list(df.columns.values))
df1['human_index'] = n-(df1.index)

list1=(df1.values.tolist())
list1.sort(key=lambda r:r[3])
df2=pd.DataFrame(list1,columns=list(df1.columns.values))
df2['deg_cen_index'] = n - df2.index 

list1=(df2.values.tolist())
list1.sort(key=lambda r:r[6])
df3=pd.DataFrame(list1,columns=list(df2.columns.values))
df3['cosine_index'] = n - df3.index 

list1=(df3.values.tolist())
list1.sort(key=lambda r:r[8])
df4=pd.DataFrame(list1,columns=list(df3.columns.values))
df4['pearson_index'] = n - df4.index 
print (df4)

df4.to_csv("ranked.csv", sep='\t')

df4['dif_degcen'] = (df4['human_index'] - df4['deg_cen_index'])**2
df4['dif_cos'] = (df4['human_index'] - df4['cosine_index'])**2
df4['dif_pear'] = (df4['human_index'] - df4['pearson_index'])**2
# df4['dif_cos']=df4.apply(lambda x: (x['human_index'] - x['cosine_index']))
# df4['dif_pear']=df4.apply(lambda x: (x['human_index'] - x['pearson_index']))

spear_cos=1-(6*df4['dif_cos'].sum())/(n**3-n)
print ("sum = " , df4['dif_cos'].sum())
spear_pear=1-(6*df4['dif_pear'].sum())/(n**3-n)
print ("sum = " , df4['dif_pear'].sum())
spear_degcen=1-(6*df4['dif_degcen'].sum())/(n**3-n)
print ("sum = " , df4['dif_degcen'].sum())
print(spear_degcen,spear_pear,spear_cos)
