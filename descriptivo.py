#Ciencia de datos en el conjunto de datos de alquiler de bicicletas
#Procesar datos, analizar y visualizar, encontrar insights, aplicar técnicas
#predictivas y razonar al respecto.

import pandas as pd
import matplotlib.pyplot as plt
import math
from numpy import mean
from numpy import std

import numpy as np
from pylab import rcParams
import seaborn as sns


#Parte 1: Carga de datos

#Cargue los datos del repositorio UCI y colóquelos en la misma carpeta
#que el cuaderno.
#El enlace es https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset.

#Lea los datos del archivo .csv usando pandas.

hour_basis = pd.read_csv("bike+sharing+dataset/hour.csv")
day_basis = pd.read_csv("bike+sharing+dataset/day.csv")


