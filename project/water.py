import requests
import pandas as pd
import sys
import xmltodict

def tryAppendWater(dest_dict, dest_key, src_dict, src_keys):
    i = 1
    data = src_dict[src_keys[0]]
    while i < len(src_keys):
        if src_keys != None:
            try:
                data = data[src_keys[i]]
            except:
                data = 'na'
        i+=1

raw_water_df = pd.read_csv("data/adv_water_quality.csv")
site_ids = raw_water_df['MonitoringLocationIdentifier'].values
for i in range(len(site_ids)):
    site_ids[i] = site_ids[i]

# removes duplicate values by converting to dict and back to list,
# since dict keys only occur once
site_ids = list(dict.fromkeys(site_ids))

water_dict = {'usgs_id': [], 'city_state': [], 'hardness': [], 'ph': [], 'conductance': [],
            'ammonia': [], 'nitrites': [], 'fluoride': [], 'arsenic': [],
            'cobalt': [], 'copper': [], 'iron': [], 'lead': [], 'mercury': []}


for i in range(100):
    print(site_ids[i])
    r = requests.get(f"https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites={site_ids[i][5:]}&parameterCd=00060,00065&siteStatus=all")

    dict_data = xmltodict.parse(r.content)
    # XML format retrieved from url is messy
    try:
        usgs_id = dict_data['wml2:Collection']['gml:identifier']['#text']
        loc = dict_data['wml2:Collection']['gml:name']['#text'].upper()
        print(loc)
    except KeyError as exc:
        print(f"invalid location: {site_ids[i]}")
        water_dict['usgs_id'].append(site_ids[i])
        water_dict['city_state'].append('na')
        continue

    # get just the numbers of the usgs id (remove the 'usgs.')
    usgs_id = usgs_id.replace('.','-')
    # grab just the city,state text from the gml:name entry
    comma_separator = loc.rfind(", ")
    city_state_name_end = comma_separator + 4
    
    opt1 = loc.rfind("NEAR ") + 5
    opt2 = loc.rfind("AT ") + 3
    opt3 = loc.rfind("NR ") + 3
    opt4 = loc.rfind("A ") + 2
    city_state_name_start = max(opt1, opt2, opt3, opt4)

    city_state = loc[city_state_name_start:]
    # if space but no comma
    if city_state.find(' ') != len(city_state) -3 and city_state.find(',') == -1:
        # remove space, add comma
        city_state = city_state.replace(' ',',')
    # if space and comma
    if city_state.find(' ') != len(city_state) -3 and city_state.find(',') != -1:
        # remove space
        city_state = city_state.replace(' ','')
    
    city_state = city_state.replace('.','')
    print(f"{usgs_id}: {city_state}")

    # data to append to dict
    water_dict['usgs_id'].append(usgs_id)
    water_dict['city_state'].append(city_state)

hardness = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Hardness, Ca, Mg'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
harndess = hardness.rename(columns = {'ResultMeasureValue':'Hardness'}, inplace = True)
ph = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'pH'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
ph.rename(columns = {'ResultMeasureValue':'pH'}, inplace = True)
comb = hardness.merge(ph[['MonitoringLocationIdentifier','pH']], on = 'MonitoringLocationIdentifier')
print(comb.head())


# to fill missing dict values with 'None' in df, orient via index, and then take Transpose
clean_water_df = pd.DataFrame.from_dict(water_dict, orient='index').T
clean_water_df.to_csv("data/CLEANED_water_data.csv", index=False)
print(clean_water_df.head())