import pandas as pd
import numpy as np

fname = 'ATemp_2018.xlsx'

df = pd.read_excel(fname)

#print(df.columns)

AlabamaDF = df[df['State'] =='Alabama']
#AlbertaDF = df[df['State'] == 'Alberta']
ArizonaDF = df[df['State'] == 'Arizona']
ArkansasDF = df[df['State'] == 'Arkansas']
Baja_CaliforniaDF = df[df['State'] == 'Baja California']
British_ColumbiaDF = df[df['State'] == 'British Columbia']
CaliforniaDF = df[df['State'] == 'California']
ChihuahuaDF = df[df['State'] == 'Chihuahua']
Coahuila_de_ZaragozaDF = df[df['State'] == 'Coahuila de Zaragoza'] 
ColoradoDF = df[df['State'] == 'Colorado']
ConnecticutDF = df[df['State'] == 'Connecticut']
DelawareDF = df[df['State'] == 'Delaware']
FloridaDF = df[df['State'] == 'Florida']
GeorgiaDF = df[df['State'] == 'Georgia']
IdahoDF = df[df['State'] == 'Idaho']
IllinoisDF = df[df['State'] == 'Illinois']
IndianaDF = df[df['State'] == 'Indiana']
IowaDF = df[df['State'] == 'Iowa']
KansasDF = df[df['State'] == 'Kansas']
KentuckyDF = df[df['State'] == 'Kentucky']
LouisianaDF = df[df['State'] == 'Louisiana']
MaineDF = df[df['State'] == 'Maine']
ManitobaDF = df[df['State'] == 'Manitoba']
MarylandDF = df[df['State'] == 'Maryland']
MassachusettsDF = df[df['State'] == 'Massachusetts']
MichiganDF = df[df['State'] == 'Michigan']
MinnesotaDF = df[df['State'] == 'Minnesota']
MississippiDF = df[df['State'] == 'Mississippi']
MissouriDF = df[df['State'] == 'Missouri']
MontanaDF = df[df['State'] == 'Montana']
NebraskaDF = df[df['State'] == 'Nebraska']
NevadaDF = df[df['State'] == 'Nevada']
New_BrunswickDF = df[df['State'] == 'New Brunswick']
New_HampshireDF = df[df['State'] == 'New Hampshire']
New_JerseyDF = df[df['State'] == 'New Jersey']
New_MexicoDF = df[df['State'] == 'New Mexico']
New_YorkDF = df[df['State'] == 'New York']
North_CarolinaDF = df[df['State'] == 'North Carolina']
North_DakotaDF = df[df['State'] == 'North Dakota']
#Nuevo_LeónDF = df[df['State'] == 'Nuevo León']
OhioDF = df[df['State'] == 'Ohio']
OklahomaDF = df[df['State'] == 'Oklahoma']
OntarioDF = df[df['State'] == 'Ontario']
OregonDF = df[df['State'] == 'Oregon']
PennsylvaniaDF = df[df['State'] == 'Pennsylvania']
QuebecDF = df[df['State'] == 'Quebec']
QuébecDF = df[df['State'] == 'Québec']
Rhode_IslandDF = df[df['State'] == 'Rhode Island']
SaskatchewanDF = df[df['State'] == 'Saskatchewan']
SonoraDF = df[df['State'] == 'Sonora']
South_CarolinaDF = df[df['State'] == 'South Carolina']
South_DakotaDF = df[df['State'] == 'South Dakota']
TamaulipasDF = df[df['State'] == 'Tamaulipas']
TennesseeDF = df[df['State'] == 'Tennessee']
TexasDF = df[df['State'] == 'Texas']
UtahDF = df[df['State'] == 'Utah']
VermontDF = df[df['State'] == 'Vermont']
VirginiaDF = df[df['State'] == 'Virginia']
WashingtonDF = df[df['State'] == 'Washington']
West_VirginiaDF = df[df['State'] == 'West Virginia']
WisconsinDF = df[df['State'] == 'Wisconsin']
WyomingDF = df[df['State'] == 'Wyoming']


AlabamaDF = AlabamaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
#AlbertaDF = AlbertaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
ArizonaDF = ArizonaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
ArkansasDF = ArkansasDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
Baja_CaliforniaDF = Baja_CaliforniaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
British_ColumbiaDF = British_ColumbiaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
CaliforniaDF = CaliforniaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
ChihuahuaDF = ChihuahuaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
Coahuila_de_ZaragozaDF = Coahuila_de_ZaragozaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
ColoradoDF = ColoradoDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
ConnecticutDF = ConnecticutDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
DelawareDF = DelawareDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
FloridaDF = FloridaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
GeorgiaDF = GeorgiaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
IdahoDF = IdahoDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
IllinoisDF = IllinoisDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
IndianaDF = IndianaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
IowaDF = IowaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
KansasDF = KansasDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
KentuckyDF = KentuckyDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
LouisianaDF = LouisianaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MaineDF = MaineDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
ManitobaDF = ManitobaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MarylandDF = MarylandDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MassachusettsDF = MassachusettsDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MichiganDF = MichiganDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MinnesotaDF = MinnesotaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MississippiDF = MississippiDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MissouriDF = MissouriDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
MontanaDF = MontanaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
NebraskaDF = NebraskaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
NevadaDF = NevadaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
New_BrunswickDF = New_BrunswickDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
New_HampshireDF = New_HampshireDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
New_JerseyDF = New_JerseyDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
New_MexicoDF = New_MexicoDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
New_YorkDF = New_YorkDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
North_CarolinaDF = North_CarolinaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
North_DakotaDF = North_DakotaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
#Nuevo_LeónDF = Nuevo_LeónDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
OhioDF = OhioDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
OklahomaDF = OklahomaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
OntarioDF = OntarioDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
OregonDF = OregonDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
PennsylvaniaDF = PennsylvaniaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
QuebecDF = QuebecDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
QuébecDF = QuébecDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
Rhode_IslandDF = Rhode_IslandDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
SaskatchewanDF = SaskatchewanDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
SonoraDF = SonoraDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
South_CarolinaDF = South_CarolinaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
South_DakotaDF = South_DakotaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
TamaulipasDF = TamaulipasDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
TennesseeDF = TennesseeDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
TexasDF = TexasDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
UtahDF = UtahDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
VermontDF = VermontDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
VirginiaDF = VirginiaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
WashingtonDF = WashingtonDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
West_VirginiaDF = West_VirginiaDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
WisconsinDF = WisconsinDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]
WyomingDF = WyomingDF[['AREA,N,20,5', 'PERIMETER,N,20,5', 'FIRE_,N,11,0', 'FIRE_ID,N,11,0', 'LAT,N,13,3', 'LONG,N,13,3', 'DATE,D', 'JULIAN,N,3,0', 'GMT,N,4,0', 'TEMP,N,6,1', 'SPIX,N,6,1', 'TPIX,N,6,1', 'SRC,C,10', 'SAT_SRC,C,1', 'CONF,N,3,0']]

AlabamaDF.to_excel('ATemp_2018_Alabama.xlsx', index = False)
#AlbertaDF.to_excel('ATemp_2018_Alberta.xlsx', index = False)
ArizonaDF.to_excel('ATemp_2018_Arizona.xlsx', index = False)
ArkansasDF.to_excel('ATemp_2018_Arkansas.xlsx', index = False)
Baja_CaliforniaDF.to_excel('ATemp_2018_BajaCalifornia.xlsx', index = False)
British_ColumbiaDF.to_excel('ATemp_2018_BritishColumbia.xlsx', index = False)
CaliforniaDF.to_excel('ATemp_2018_California.xlsx', index = False)
ChihuahuaDF.to_excel('ATemp_2018_Chihuahua.xlsx', index = False)
Coahuila_de_ZaragozaDF.to_excel('ATemp_2018_CoahuilaDeZaragoza.xlsx', index = False)
ColoradoDF.to_excel('ATemp_2018_Colorado.xlsx', index = False)
ConnecticutDF.to_excel('ATemp_2018_Connecticut.xlsx', index = False)
DelawareDF.to_excel('ATemp_2018_Delaware.xlsx', index = False)
FloridaDF.to_excel('ATemp_2018_Florida.xlsx', index = False)
GeorgiaDF.to_excel('ATemp_2018_Georgia.xlsx', index = False)
IdahoDF.to_excel('ATemp_2018_Idaho.xlsx', index = False)
IllinoisDF.to_excel('ATemp_2018_Illinois.xlsx', index = False)
IndianaDF.to_excel('ATemp_2018_Indiana.xlsx', index = False)
IowaDF.to_excel('ATemp_2018_Iowa.xlsx', index = False)
KansasDF.to_excel('ATemp_2018_Kansas.xlsx', index = False)
KentuckyDF.to_excel('ATemp_2018_Kentucky.xlsx', index = False)
LouisianaDF.to_excel('ATemp_2018_Louisiana.xlsx', index = False)
MaineDF.to_excel('ATemp_2018_Maine.xlsx', index = False)
ManitobaDF.to_excel('ATemp_2018_Manitoba.xlsx', index = False)
MarylandDF.to_excel('ATemp_2018_Maryland.xlsx', index = False)
MassachusettsDF.to_excel('ATemp_2018_Massachusetts.xlsx', index = False)
MichiganDF.to_excel('ATemp_2018_Michigan.xlsx', index = False)
MinnesotaDF.to_excel('ATemp_2018_Minnesota.xlsx', index = False)
MississippiDF.to_excel('ATemp_2018_Mississippi.xlsx', index = False)
MissouriDF.to_excel('ATemp_2018_Missouri.xlsx', index = False)
MontanaDF.to_excel('ATemp_2018_Montana.xlsx', index = False)
NebraskaDF.to_excel('ATemp_2018_Nebraska.xlsx', index = False)
NevadaDF.to_excel('ATemp_2018_Nevada.xlsx', index = False)
New_BrunswickDF.to_excel('ATemp_2018_NewBrunswick.xlsx', index = False)
New_HampshireDF.to_excel('ATemp_2018_NewHampshire.xlsx', index = False)
New_JerseyDF.to_excel('ATemp_2018_NewJersey.xlsx', index = False)
New_MexicoDF.to_excel('ATemp_2018_NewMexico.xlsx', index = False)
New_YorkDF.to_excel('ATemp_2018_NewYork.xlsx', index = False)
North_CarolinaDF.to_excel('ATemp_2018_NorthCarolina.xlsx', index = False)
North_DakotaDF.to_excel('ATemp_2018_NorthDakota.xlsx', index = False)
#Nuevo_LeónDF.to_excel('ATemp_2018_NuevoLeon.xlsx', index = False)
OhioDF.to_excel('ATemp_2018_Ohio.xlsx', index = False)
OklahomaDF.to_excel('ATemp_2018_Oklahoma.xlsx', index = False)
OntarioDF.to_excel('ATemp_2018_Ontario.xlsx', index = False)
OregonDF.to_excel('ATemp_2018_Oregon.xlsx', index = False)
PennsylvaniaDF.to_excel('ATemp_2018_Pennsylvania.xlsx', index = False)
QuebecDF.to_excel('ATemp_2018_Quebec.xlsx', index = False)
QuébecDF.to_excel('ATemp_2018_Québec.xlsx', index = False)
Rhode_IslandDF.to_excel('ATemp_2018_RhodeIsland.xlsx', index = False)
SaskatchewanDF.to_excel('ATemp_2018_Saskatchewan.xlsx', index = False)
SonoraDF.to_excel('ATemp_2018_Sonora.xlsx', index = False)
South_CarolinaDF.to_excel('ATemp_2018_SouthCarolina.xlsx', index = False)
South_DakotaDF.to_excel('ATemp_2018_SouthDakota.xlsx', index = False)
TamaulipasDF.to_excel('ATemp_2018_Tamaulipas.xlsx', index = False)
TennesseeDF.to_excel('ATemp_2018_Tennessee.xlsx', index = False)
TexasDF.to_excel('ATemp_2018_Texas.xlsx', index = False)
UtahDF.to_excel('ATemp_2018_Utah.xlsx', index = False)
VermontDF.to_excel('ATemp_2018_Vermont.xlsx', index = False)
VirginiaDF.to_excel('ATemp_2018_Virginia.xlsx', index = False)
WashingtonDF.to_excel('ATemp_2018_Washington.xlsx', index = False)
West_VirginiaDF.to_excel('ATemp_2018_WestVirginia.xlsx', index = False)
WisconsinDF.to_excel('ATemp_2018_Wisconsin.xlsx', index = False)
WyomingDF.to_excel('ATemp_2018_Whyoming.xlsx', index = False)

