import pandas as pd

cities_df = pd.read_csv("data/uscities.csv")
cities_df['city_state'] = cities_df['city'] + "," + cities_df['state_id']

cities_df = cities_df[['city_state', 'county_name', 'population',
                'density', 'timezone', 'zips']]

cities_df = cities_df.drop_duplicates(['city_state'])

cities_df.to_csv("data/uscities_scrubbed.csv", index=False)