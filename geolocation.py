import pandas as pd
import numpy as np
import geocoder

states = []
df = pd.read_csv('Alison_2018.csv')
for i in df.index:
	g=geocoder.arcgis([df.loc[i, 'LAT,N,13,3'], df.loc[i, 'LONG,N,13,3']], method='reverse')
	states.append(g.state)
	#print(g.state)
	#print(g)

df['State']=states
df.to_excel('MODIS_Terra_STATES_2018.xlsx')	

