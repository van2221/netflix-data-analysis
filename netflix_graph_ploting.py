import numpy as np # linear algebra
import pandas as pd # for data preparation
import plotly.express as px # for data visualization


dff=pd.read_csv('netflix_titles.csv')
dff.shape
##### Distribution of Rating #####
z = dff.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='rating', 
                  title='Distribution of Content Ratings on Netflix',
                  color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()

##### TOP 5 Directors ##### 
dff['director']=dff['director'].fillna('No Director Specified')
filtered_directors=pd.DataFrame()
filtered_directors=dff['director'].str.split(',',expand=True).stack()
filtered_directors=filtered_directors.to_frame()
filtered_directors.columns=['Director']
directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content')
directors=directors[directors.Director !='No Director Specified']
directors=directors.sort_values(by=['Total Content'],ascending=False)
directorsTop5=directors.head()
directorsTop5=directorsTop5.sort_values(by=['Total Content'])
fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix')
fig1.show()

##### TOP 5 Cast #####
dff['cast']=dff['cast'].fillna('No Cast Specified')
filtered_cast=pd.DataFrame()
filtered_cast=dff['cast'].str.split(',',expand=True).stack()
filtered_cast=filtered_cast.to_frame()
filtered_cast.columns=['Actor']
actors=filtered_cast.groupby(['Actor']).size().reset_index(name='Total Content')
actors=actors[actors.Actor !='No Cast Specified']
actors=actors.sort_values(by=['Total Content'],ascending=False)
actorsTop5=actors.head()
actorsTop5=actorsTop5.sort_values(by=['Total Content'])
fig2=px.bar(actorsTop5,x='Total Content',y='Actor', title='Top 5 Actors on Netflix')
fig2.show()

##### TOP 10 Countries #####
dff['country']=dff['country'].fillna('No country Specified')
filtered_country=pd.DataFrame()
filtered_country=dff['country'].str.split(',',expand=True).stack()
filtered_country=filtered_country.to_frame()
filtered_country.columns=['Country']
countries=filtered_country.groupby(['Country']).size().reset_index(name='Total Content')
countries=countries[countries.Actor !='No Cast Specified']
countries=countries.sort_values(by=['Total Content'],ascending=False)
countriesTop10=countries.head(10)
countriesTop10=countriesTop10.sort_values(by=['Total Content'])
fig2=px.bar(countriesTop10,x='Total Content',y='Country', title='Top 10 Countries on Netflix')
fig2.show()


##### Trend of production over the years on Netflix #####
df1=dff[['type','release_year']]
df1=df1.rename(columns={"release_year": "Release Year"})
df2=df1.groupby(['Release Year','type']).size().reset_index(name='Total Content')
df2=df2[df2['Release Year']>=2010]
fig3 = px.line(df2, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the years on Netflix')
fig3.show()



