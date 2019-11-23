from matplotlib import cm
from matplotlib import pyplot
from numpy import linalg
from numpy import random
from random import sample
from scipy import signal 
from scipy import stats
from shapely.geometry import Point, Polygon
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_samples
from sklearn.metrics import silhouette_score

import datetime
import foursquare
import geopandas
import math
import numpy
import pandas
import pickle
import pymongo
import time

bikemi_dataframe = pandas.DataFrame()
columns_filter = ['Data_prelievo'
                  , 'Gio_settimana_prelievo'
                  , 'Festivo_feriale_prelievo'
                  , 'Stazione_prelievo'
                  , 'Durata_sec'
                  , 'Data_arrivo'
                  , 'Gio_settimana_arrivo'
                  , 'Festivo_feriale_arrivo'
                  , 'Stazione_arrivo'
                 ]

#unione dei dataframe
for yy in range(2015, 2019): 
    for mm in range(1, 13):
        print(yy,mm)
        try:
            csv_uri = '/home/datasets/bikemi/{0}/{1:02d} {0}.csv'.format(yy,mm)
            next_df = pandas.read_csv(csv_uri,
                           lineterminator ='\r',
                           encoding = 'iso8859_2',
                           sep = ';',
                           parse_dates = ['Data_prelievo','Data_arrivo'],
                           date_parser = lambda x: datetime.datetime.strptime(x,'%d/%m/%y %H:%M'),
                           decimal = '.'
                          )
            
        except FileNotFoundError:
            pass
        else:
            #SAVE
            bikemi_dataframe = pandas.concat([bikemi_dataframe, next_df[columns_filter]])

pickle.dump(bikemi_dataframe, open( "archive/bikemi_dataframe.pkl", "wb" ) )