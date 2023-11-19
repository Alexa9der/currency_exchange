import requests
import pandas as pd
import numpy as np
from tqdm import tqdm_notebook as t 
import yfinance as yf
from datetime import datetime
from math import ceil
import random
import json

import talib as tl
import MetaTrader5 as mt5

import matplotlib.pyplot as plt 
import seaborn as sns
from plotly import graph_objs as go
from plotly.offline import init_notebook_mode

import ipywidgets as widgets
from ipywidgets import interact, interact_manual

import warnings

from deap import base, creator, tools, algorithms

from tensorflow.keras.models import Model, clone_model
from tensorflow.keras.layers import Input, LSTM, Flatten, Dense
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
