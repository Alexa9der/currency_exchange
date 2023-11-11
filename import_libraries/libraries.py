import requests
import pandas as pd
import numpy as np
from tqdm import tqdm_notebook as t 
import yfinance as yf
from datetime import datetime
from math import ceil
import random
# import talib as tl

import MetaTrader5 as mt5
import json

import matplotlib.pyplot as plt 
import seaborn as sns
from plotly import graph_objs as go
from plotly.offline import init_notebook_mode

import ipywidgets as widgets
from ipywidgets import interact, interact_manual

from deap import base, creator, tools, algorithms

import warnings