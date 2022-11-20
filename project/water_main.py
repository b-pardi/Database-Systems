import requests
import pandas as pd
import sys
import xmltodict
from functools import reduce

# pull information from csv's
raw_water_df = pd.read_csv("old data/adv_water_quality.csv")
site_ids = raw_water_df['MonitoringLocationIdentifier'].values
print(len(site_ids))

# removes duplicate values by converting to dict and back to list,
# since dict keys only occur once
site_ids = list(dict.fromkeys(site_ids))
# dict for us geoligical survey site ids, to cross reference API and spreadsheet
usgs_dict = {'usgs_key': [i for i in range(len(site_ids))], 'MonitoringLocationIdentifier': [], 'city_state': []}

'''
GRAB LOCATION OF SITE ID'S 
take site ids from the water quality data sheet, and send them to the api to find the location of the site    
'''

for i in range(len(site_ids)):
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
        usgs_dict['MonitoringLocationIdentifier'].append(site_ids[i])
        usgs_dict['city_state'].append('na')
        continue

    # get just the numbers of the usgs id (remove the 'usgs.')
    usgs_id = usgs_id.replace('.','-')

    # grab just the city,state text from the gml:name entry   
    opt1 = loc.rfind("NEAR ") + 5
    opt2 = loc.rfind("AT ") + 3
    opt3 = loc.rfind("NR ") + 3
    opt4 = loc.rfind(" A ") + 3
    opt5 = loc.rfind("ABOVE ") + 6
    opt6 = loc.rfind(" @ ") + 3
    city_state_name_start = max(opt1, opt2, opt3, opt4, opt5, opt6)
    city_state = loc[city_state_name_start:]
    
    # remove dot for abbrev
    city_state = city_state.replace('.','')

    # if space but no comma
    if city_state.rfind(' ') == len(city_state) -3 and city_state.find(',') == -1:
        # add comma
        city_state = city_state[:len(city_state)-3] + ',' + city_state[len(city_state)-2:]
    # if space and comma
    if city_state.rfind(' ') == len(city_state) -3 and city_state.find(',') != -1:
        # remove space
        city_state = city_state[:len(city_state)-3] + city_state[len(city_state)-2:]

    # some states listed as 4 letter abbreviations
    city_state = city_state[:city_state.rfind(',')+3]
    # sometimes multiples of cities or locs with commas
    while city_state.count(',') > 1:
        city_state = city_state[city_state.find(',')+1:]

    # outliar cases can't algorithmically be accounted for
    if city_state == 'SACRAMENTO R DEEP WATER SHIP CHANNEL MARKER 51,CA':
        city_state = 'SOLANO,CA'
    
    if city_state =='SLC,UT':
        city_state = 'SALT LAKE CITY,UT'

    print(f"{usgs_id}: {city_state}")

    # data to append to dict
    usgs_dict['MonitoringLocationIdentifier'].append(usgs_id)
    usgs_dict['city_state'].append(city_state)


'''
ORGANIZE DATA FROM WATER QUALITY SPREADSHEET
data for water quality is formatted differently than our sql table design,
grab all individual measurements into their own df, and then merge
'''
hardness = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Hardness, Ca, Mg'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
hardness = hardness.reset_index(drop=True)
hardness.rename(columns = {'ResultMeasureValue':'Hardness mg/l CaCO3'}, inplace = True)

ph = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'pH'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
ph = ph.reset_index(drop=True)
ph.rename(columns = {'ResultMeasureValue':'pH std units'}, inplace = True)

conductance = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Specific conductance'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
conductance = conductance.reset_index(drop=True)
conductance.rename(columns={'ResultMeasureValue':'Conductance uS/cm @25C'}, inplace = True)

ammonia = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Ammonia and ammonium'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
ammonia = ammonia.reset_index(drop=True)
ammonia.rename(columns={'ResultMeasureValue':'Ammonia mg/l as N'}, inplace = True)

nitrites = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Inorganic nitrogen (nitrate and nitrite)'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
nitrites = nitrites.reset_index(drop=True)
nitrites.rename(columns={'ResultMeasureValue':'Nitrites mg/l as N'}, inplace = True)

fluoride = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Fluoride'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
fluoride = fluoride.reset_index(drop=True)
fluoride.rename(columns={'ResultMeasureValue':'Fluoride mg/l'}, inplace = True)

cobalt = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Cobalt'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
cobalt = cobalt.reset_index(drop=True)
cobalt.rename(columns={'ResultMeasureValue':'Cobalt ug/l'}, inplace = True)

copper = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Copper'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
copper = copper.reset_index(drop=True)
copper.rename(columns={'ResultMeasureValue':'Copper ug/l'}, inplace = True)

iron = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Iron'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
iron = iron.reset_index(drop=True)
iron.rename(columns={'ResultMeasureValue':'Iron ug/l'}, inplace = True)

arsenic = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Arsenic'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
arsenic = arsenic.reset_index(drop=True)
arsenic.rename(columns={'ResultMeasureValue':'Arsenic ug/l'}, inplace = True)

mercury = raw_water_df.loc[raw_water_df['CharacteristicName'] == 'Mercury'][['MonitoringLocationIdentifier', 'ResultMeasureValue']]
mercury = mercury.reset_index(drop=True)
mercury.rename(columns={'ResultMeasureValue':'Mercury ug/l'}, inplace = True)

water_prop_dfs = [hardness, ph, conductance, ammonia, nitrites, fluoride,
                cobalt, copper, iron, arsenic, mercury]

selected_water_df = reduce(lambda left,right: pd.merge(left,right,on=['MonitoringLocationIdentifier'], how='outer'), water_prop_dfs)

selected_water_df = selected_water_df.drop_duplicates(subset=['MonitoringLocationIdentifier'], keep='first')
print(selected_water_df.head())

# to fill missing dict values with 'None' in df, orient via index, and then take Transpose
usgs_ids_df = pd.DataFrame.from_dict(usgs_dict, orient='index').T
usgs_ids_df.to_csv("data/usgs_ids.csv", index=False)
print(usgs_ids_df.head())

'''
MERGE FORMATTED WATER QUALITY AND USGS ID LOCATIONS
'''
org_water_df = pd.merge(usgs_ids_df, selected_water_df, on = "MonitoringLocationIdentifier", how = "inner")
mercury.rename(columns={'MonitoringLocationIdentifier':'usgs_id'}, inplace = True)

selected_water_df.to_csv("data/selected_water.csv", index=False)
org_water_df.to_csv("data/org_water.csv", index=False)

