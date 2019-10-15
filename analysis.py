import pandas as pd

df = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')


df_sub = df[['Mortality rate, infant (per 1,000 live births)',
            'GDP per capita (constant 2010 US$)',
            'Country Name']]

import plotnine as p9
from plotnine import aes
from plotnine import geom_point

(p9.ggplot(df_sub, aes(x = 'Mortality rate, infant (per 1,000 live births)', y = 'GDP per capita (constant 2010 US$)')) +
     geom_point()
)