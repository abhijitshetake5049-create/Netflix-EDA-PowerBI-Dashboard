import numpy  as np
import pandas as pd
df=pd.read_csv("netflix_titles.csv")

#understanding of the data
print(df.shape)
print(df.head())
print(df.tail())
print(df.columns)

#see the null values in the data
print(df.isnull().sum())
df.drop_duplicates(inplace=True)

#cleaning process 

df.replace([-np.inf,np.inf],np.nan,inplace=True)

df["director"]=df["director"].fillna("Info_unavaible")
df['cast']=df['cast'].fillna('Cast_members_inf0_unavaible')
df['rating']=df['rating'].fillna("NO_rating_given")
df['country']=df['country'].fillna("unkonwn_country")

#this making the date into actually datetime right 
df["date_added"]=pd.to_datetime(df['date_added'],errors="coerce")
print("do cleaniiinggg")
print(df["date_added"].isna().sum())

df["duration"]=df["duration"].fillna("No_duration is the avaible bro ")

#this great thinking ot the cleaninng bro what i am going use see herer
df["Movie_durations"]=df["duration"].str.extract(r"(\d+)")
df["Movie_durations"]=df["Movie_durations"].astype(float)
df.loc[df["type"] != "Movie", "Movie_durations"] = None

#this make the new clounm using the tv shows time right for the spearte and which hleps actually the data cleaning right 
df["TV_Show_durqtions"]=df["duration"].str.extract(r"(\d+)")
df["TV_Show_durqtions"]=df["TV_Show_durqtions"].astype(float)
df.loc[df["type"]!="TV Show","TV_Show_durqtions"]=None
print(df.isnull().sum())

#this problem of the rating where contains duration is corrected right 
print(df[df["rating"].str.contains("min", na=False)][["title", "rating", "duration"]])
df.loc[df["rating"].str.contains("min",na=False),"rating"]="unkown"

print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df=pd.read_csv("netflix_cleaned.csv")
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
#this little analyis part bro 
print(" this tellss how much movie and the tv show avaible bro")
print(df["type"].value_counts())

#this rating anlayis 
print(df["rating"].value_counts())
#total count of the particular type movie or show as based on rating means catgorie

#this new dataframe for the rating of the particular movie or 
print("sperat tble for anlayis ")
rating_anlayis=df[["title","rating"]]
print(rating_anlayis)
print(rating_anlayis.head())
print(rating_anlayis.value_counts())
df.to_csv("netflix_cleaned.csv", index=False)

#small anlayis of the tile or the movies or show relqse on this platform right 
print("titles added at specific year counts ")
print(df["date_added"].dt.year.value_counts().sort_index())
#this how it works bro using the count we have done lot of thinks right 

print(df.columns)
#this analayis of the realse of the movie and comapre the title added on this plafrom right 
print(" relaed year ")
print(df["release_year"].value_counts().sort_index())
print(df["release_year"].value_counts().head(10))

#this new clounm of years taken to add the movie right 
df["year_taken_add"]=df["date_added"].dt.year - df["release_year"]
print(df[["release_year","date_added","year_taken_add"]])
print("avg time take for add movie is ")
print(df["year_taken_add"].mean())

#for the movie duration bro anlayis of the
print("movie durations insights ")
print(df["Movie_durations"].describe())
print(df["Movie_durations"].value_counts().sort_index())

#movie rnages catgories right on top 
print(" moivie ranges using the ")
df["movies_catgories_based_on_durations"]=pd.cut(df["Movie_durations"],bins=(0,60,120,float("inf")),labels=("short","medium","long"))
print(df[["title","Movie_durations","movies_catgories_based_on_durations"]])


#tv show anlyis right on shown below 
print(" TV shows anlayis ")
print(df["TV_Show_durqtions"].describe())
print(df["TV_Show_durqtions"].value_counts().sort_index())
df["TV_shows_catgories_on_sessons"]=pd.cut(df["TV_Show_durqtions"],bins=(0,2,5,float("inf")),labels=("short","Medium","long"))
print(df[["title","TV_Show_durqtions","TV_shows_catgories_on_sessons"]])

#thlisted_ins the genera anlayis bro
print(df["listed_in"].head())
print("this listed anlyis of the genera ")
print(df['listed_in'].value_counts().sort_index())

print(df["listed_in"].describe())
print(df["listed_in"].str.split(",").explode().value_counts().sort_index())
print("frist ten ")
print(df["listed_in"].str.split(",").explode().value_counts().head(10))
print("last ten")
print(df["listed_in"].str.split(",").explode().value_counts().tail(10))


#country anlyis 
print(df['country'].head(10))
print(df["country"].tail(10))
print("new table extracted ")

country_analysis = df[["country", "type", "title"]]

print(country_analysis)
print("top ten movies ")
print(df["country"].str.split(",").explode().value_counts().head(10))
print("least countryiess")
print(df["country"].str.split(",").explode().value_counts().tail(10))


#next task is the grouping the tv shows and movies based on the ratings right 
print(df.groupby("type")["rating"].value_counts())


#this anlyis used too catgories the dtaa also perform the work on the catgories data at time usin gthe lambda function using the apply function right 
print(df.groupby("type")["listed_in"].apply(
    lambda x: x.str.split(", ").explode().value_counts()
))

#country vs type anlyis 
print("country vs type an;layis ")
print(df.groupby("type")["country"].apply(
    lambda x: x.str.split(", ").explode().value_counts()
))

#movie vs tv show as per year added per year
print(df.groupby(df["date_added"].dt.year)["type"].value_counts())

#this groouping byvusing the groupby and the lamada
print("movie vs tv show groping with country")
print(df.groupby("type")['country'].apply(
    lambda x:x.str.split(",").explode().value_counts().head(10)
))


#this filtered ablayis 
director_new=df[df["director"] != "Info_unavaible"]
print(director_new["director"].value_counts().head(10))
print(director_new.groupby("type")['director'].apply(
    lambda x:x.str.split(",").explode().value_counts().head(10)
))

#movie driectors 
print("moivies dricetor bro")
movie_direcotors=director_new[director_new["type"]=="Movie"]
print(movie_direcotors["director"].value_counts().head(10))
#tv show driector 
print(" tv show dricetors bro")
tvshow_direcotors=director_new[director_new["type"]=="TV Show"]
print(tvshow_direcotors["director"].value_counts().head(10))


#final EDA

print("final Eda insights ")


#most common content 
print("most common content ")
print(df["type"].value_counts().idxmax())

#most common rating
print("most common ratings")
print(df["rating"].value_counts().idxmax())

#avg movie durtions 
print("avg moive durations is ")
print(df["Movie_durations"].mean())

#Most coommon number of tv show seasons 
print("most common number of the tv shows seassons ")
print(df["TV_Show_durqtions"].value_counts().idxmax())

#most common genere right 
print(" most common gener")
print(df["listed_in"].str.split(",").explode().value_counts().idxmax())

#most common country 
print("most common countries ")
print(" most watching the netflix ")
print(df["country"].str.split(",").explode().value_counts().idxmax())

#avg years taken to add the title or moies or shows on the netflix
print(" avg time taken to add movies or show in years  ")
print(df["year_taken_add"].mean())

#years with most tiles added right 
print(" years with most tiles added ")
print(df["date_added"].dt.year.value_counts().idxmax())

#most common realeasd at any year 
print("most common relased year ")
print(df["release_year"].value_counts().idxmax())

#most common director 
print(" most common director ")
print(director_new["director"].value_counts().idxmax())


df.to_csv("netflix_cleaned_v2.csv", index=False)




