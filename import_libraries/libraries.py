import requests
import pandas as pd
import numpy as np
from tqdm.notebook import tqdm
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

import tensorflow as tf
from tensorflow.keras.models import Model, clone_model
from tensorflow.keras.layers import Input, LSTM, Flatten, Dense, Attention
from keras_tuner.tuners import Hyperband
from keras_tuner.engine.hyperparameters import HyperParameters
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.models import load_model


from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
