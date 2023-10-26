import requests
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import talib as tl
# import MetaTrader5 as mt5 # treiding platforms

import matplotlib.pyplot as plt 
import seaborn as sns
from plotly import graph_objs as go
from plotly.offline import init_notebook_mode

from datetime import datetime, timedelta
import time

# интерактивные виджеты
# @interact
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

# Jupyter Notebook progressbar decorator
# from tqdm import tqdm_notebook as tqdm

import inspect