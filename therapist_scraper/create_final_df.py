import pandas as pd


df_97005 = pd.read_csv('therapist_scraper/data/97005_data.csv')
df_97006 = pd.read_csv('therapist_scraper/data/97006_data.csv')
df_97007 = pd.read_csv('therapist_scraper/data/97007_data.csv')
df_97008 = pd.read_csv('therapist_scraper/data/97008_data.csv')
df_97034 = pd.read_csv('therapist_scraper/data/97034_data.csv')
df_97035 = pd.read_csv('therapist_scraper/data/97035_data.csv')
df_97080 = pd.read_csv('therapist_scraper/data/97080_data.csv')
df_97086 = pd.read_csv('therapist_scraper/data/97086_data.csv')
df_97201 = pd.read_csv('therapist_scraper/data/97201_data.csv')
df_97202 = pd.read_csv('therapist_scraper/data/97202_data.csv')
df_97203 = pd.read_csv('therapist_scraper/data/97203_data.csv')
df_97204 = pd.read_csv('therapist_scraper/data/97204_data.csv')
df_97205 = pd.read_csv('therapist_scraper/data/97205_data.csv')
df_97206 = pd.read_csv('therapist_scraper/data/97206_data.csv')
df_97209 = pd.read_csv('therapist_scraper/data/97209_data.csv')
df_97210 = pd.read_csv('therapist_scraper/data/97210_data.csv')
df_97211 = pd.read_csv('therapist_scraper/data/97211_data.csv')
df_97212 = pd.read_csv('therapist_scraper/data/97212_data.csv')
df_97213 = pd.read_csv('therapist_scraper/data/97213_data.csv')
df_97214 = pd.read_csv('therapist_scraper/data/97214_data.csv')
df_97215 = pd.read_csv('therapist_scraper/data/97215_data.csv')
df_97216 = pd.read_csv('therapist_scraper/data/97216_data.csv')
df_97217 = pd.read_csv('therapist_scraper/data/97217_data.csv')
df_97218 = pd.read_csv('therapist_scraper/data/97218_data.csv')
df_97219 = pd.read_csv('therapist_scraper/data/97219_data.csv')
df_97220 = pd.read_csv('therapist_scraper/data/97220_data.csv')
df_97221 = pd.read_csv('therapist_scraper/data/97221_data.csv')
df_97222 = pd.read_csv('therapist_scraper/data/97222_data.csv')
df_97223 = pd.read_csv('therapist_scraper/data/97223_data.csv')
df_97225 = pd.read_csv('therapist_scraper/data/97225_data.csv')
df_97227 = pd.read_csv('therapist_scraper/data/97227_data.csv')
df_97229 = pd.read_csv('therapist_scraper/data/97229_data.csv')
df_97230 = pd.read_csv('therapist_scraper/data/97230_data.csv')
df_97231 = pd.read_csv('therapist_scraper/data/97231_data.csv')
df_97232 = pd.read_csv('therapist_scraper/data/97232_data.csv')
df_97233 = pd.read_csv('therapist_scraper/data/97233_data.csv')
df_97236 = pd.read_csv('therapist_scraper/data/97236_data.csv')
df_97239 = pd.read_csv('therapist_scraper/data/97239_data.csv')
df_97266 = pd.read_csv('therapist_scraper/data/97266_data.csv')




df_running = [df_97005,df_97006,df_97007,df_97008,df_97034,df_97035,df_97080,df_97086,df_97201,df_97202,df_97203,df_97204,df_97205,df_97206,df_97209,df_97210,df_97211,df_97212,df_97213,df_97214,df_97215,df_97216,df_97217,df_97218,df_97219,df_97220,df_97221,df_97222,df_97223,df_97225,df_97227,df_97229,df_97230,df_97231,df_97232,df_97233,df_97236,df_97239,df_97266]

df_final = pd.concat(df_running)
df_final = df_final.set_index("name").drop(columns="Unnamed: 0").drop_duplicates()
#df_final = df_final.drop(columns="Unnamed: 0")
#df_final = df_final.drop_duplicates()

df_final.to_csv('therapist_data.csv')