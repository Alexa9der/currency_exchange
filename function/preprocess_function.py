from import_libraries.libraries import  *
from function.NN import * 

# Ta-Lib
class Preprocessing_stock_data:
    """
    A class to preprocess stock data by applying various technical indicators and mathematical transformations.
    """
    def __init__ (self, data: pd.DataFrame, periods: list[int] = None):
        """
        Initializes the Preprocessing_stock_data class.

        Args:
            data (pd.DataFrame): Input data to be processed.
            periods (list, optional): List of periods for calculations. Defaults to None.

        This function initializes the Preprocessing_stock_data class and sets the dataframe, columns, and periods to be used for processing.
        """
        self.df = data.copy()
        self.open = data["Open"].copy()
        self.high = data["High"].copy()
        self.low = data["Low"].copy()
        self.close = data["Close"].copy()
        self.volume = data["Volume"].copy()
        self.date = data["Date"].copy()
        
        self.periods = periods if periods else [23,115,220]

    def add_indicators_pattern_recognition_functions(self):
        """
        Adds pattern recognition indicators to the dataframe.

        Returns:
            pd.DataFrame: Dataframe with added pattern recognition indicators.

        This function creates copies of the input data and adds pattern recognition indicators to the dataframe.
        """
        df = pd.DataFrame()
        df["Open"] =  self.open
        df["High"] = self.high
        df["Low"] = self.low
        df["Close"] = self.close
        df["Volume"] = self.volume
        df["Date"] = self.date
        

        df["CDL2CROWS"] = tl.CDL2CROWS(self.open, self.high, self.low, self.close)
        df["CDL3BLACKCROWS"] = tl.CDL3BLACKCROWS(self.open, self.high, self.low, self.close)
        df["CDL3INSIDE"] = tl.CDL3INSIDE(self.open, self.high, self.low, self.close)
        df["CDL3LINESTRIKE"] = tl.CDL3LINESTRIKE(self.open, self.high, self.low, self.close)
        df["CDL3OUTSIDE"] = tl.CDL3OUTSIDE(self.open, self.high, self.low, self.close)
        df["CDL3STARSINSOUTH"] = tl.CDL3STARSINSOUTH(self.open, self.high, self.low, self.close)
        df["CDL3WHITESOLDIERS"] = tl.CDL3WHITESOLDIERS(self.open, self.high, self.low, self.close)
        df["CDLABANDONEDBABY"] = tl.CDLABANDONEDBABY(self.open, self.high, self.low, self.close)
        df["CDLADVANCEBLOCK"] = tl.CDLADVANCEBLOCK(self.open, self.high, self.low, self.close)
        df["CDLBELTHOLD"] = tl.CDLBELTHOLD(self.open, self.high, self.low, self.close)
        df["CDLBREAKAWAY"] = tl.CDLBREAKAWAY(self.open, self.high, self.low, self.close)
        df["CDLCLOSINGMARUBOZU"] = tl.CDLCLOSINGMARUBOZU(self.open, self.high, self.low, self.close)
        df["CDLCONCEALBABYSWALL"] = tl.CDLCONCEALBABYSWALL(self.open, self.high, self.low, self.close)
        df["CDLCOUNTERATTACK"] = tl.CDLCOUNTERATTACK(self.open, self.high, self.low, self.close)
        df["CDLDARKCLOUDCOVER"] = tl.CDLDARKCLOUDCOVER(self.open, self.high, self.low, self.close)
        df["CDLDOJI"] = tl.CDLDOJI(self.open, self.high, self.low, self.close)
        df["CDLDOJISTAR"] = tl.CDLDOJISTAR(self.open, self.high, self.low, self.close)
        df["CDLDRAGONFLYDOJI"] = tl.CDLDRAGONFLYDOJI(self.open, self.high, self.low, self.close)
        df["CDLENGULFING"] = tl.CDLENGULFING(self.open, self.high, self.low, self.close)
        df["CDLEVENINGDOJISTAR"] = tl.CDLEVENINGDOJISTAR(self.open, self.high, self.low, self.close, penetration=0)
        df["CDLEVENINGSTAR"] = tl.CDLEVENINGSTAR(self.open, self.high, self.low, self.close, penetration=0)
        df["CDLGAPSIDESIDEWHITE"] = tl.CDLGAPSIDESIDEWHITE(self.open, self.high, self.low, self.close)
        df["CDLGRAVESTONEDOJI"] = tl.CDLGRAVESTONEDOJI(self.open, self.high, self.low, self.close)
        df["CDLHAMMER"] = tl.CDLHAMMER(self.open, self.high, self.low, self.close)
        df["CDLHANGINGMAN"] = tl.CDLHANGINGMAN(self.open, self.high, self.low, self.close)
        df["CDLHARAMI"] = tl.CDLHARAMI(self.open, self.high, self.low, self.close)
        df["CDLHARAMICROSS"] = tl.CDLHARAMICROSS(self.open, self.high, self.low, self.close)
        df["CDLHIGHWAVE"] = tl.CDLHIGHWAVE(self.open, self.high, self.low, self.close)
        df["CDLHIKKAKE"] = tl.CDLHIKKAKE(self.open, self.high, self.low, self.close)
        df["CDLHIKKAKEMOD"] = tl.CDLHIKKAKEMOD(self.open, self.high, self.low, self.close)
        df["CDLHOMINGPIGEON"] = tl.CDLHOMINGPIGEON(self.open, self.high, self.low, self.close)
        df["CDLIDENTICAL3CROWS"] = tl.CDLIDENTICAL3CROWS(self.open, self.high, self.low, self.close)
        df["CDLINNECK"] = tl.CDLINNECK(self.open, self.high, self.low, self.close)
        df["CDLINVERTEDHAMMER"] = tl.CDLINVERTEDHAMMER(self.open, self.high, self.low, self.close)
        df["CDLKICKING"] = tl.CDLKICKING(self.open, self.high, self.low, self.close)
        df["CDLKICKINGBYLENGTH"] = tl.CDLKICKINGBYLENGTH(self.open, self.high, self.low, self.close)
        df["CDLLADDERBOTTOM"] = tl.CDLLADDERBOTTOM(self.open, self.high, self.low, self.close)
        df["CDLLONGLEGGEDDOJI"] = tl.CDLLONGLEGGEDDOJI(self.open, self.high, self.low, self.close)
        df["CDLLONGLINE"] = tl.CDLLONGLINE(self.open, self.high, self.low, self.close)
        df["CDLMARUBOZU"] = tl.CDLMARUBOZU(self.open, self.high, self.low, self.close)
        df["CDLMATCHINGLOW"] = tl.CDLMATCHINGLOW(self.open, self.high, self.low, self.close)
        df["CDLMATHOLD"] = tl.CDLMATHOLD(self.open, self.high, self.low, self.close, penetration=0)
        df["CDLMORNINGDOJISTAR"] = tl.CDLMORNINGDOJISTAR(self.open, self.high, self.low, self.close, penetration=0)
        df["CDLMORNINGSTAR"] = tl.CDLMORNINGSTAR(self.open, self.high, self.low, self.close, penetration=0)
        df["CDLONNECK"] = tl.CDLONNECK(self.open, self.high, self.low, self.close)
        df["CDLPIERCING"] = tl.CDLPIERCING(self.open, self.high, self.low, self.close)
        df["CDLRICKSHAWMAN"] = tl.CDLRICKSHAWMAN(self.open, self.high, self.low, self.close)
        df["CDLRISEFALL3METHODS"] = tl.CDLRISEFALL3METHODS(self.open, self.high, self.low, self.close)
        df["CDLSEPARATINGLINES"] = tl.CDLSEPARATINGLINES(self.open, self.high, self.low, self.close)
        df["CDLSHOOTINGSTAR"] = tl.CDLSHOOTINGSTAR(self.open, self.high, self.low, self.close)
        df["CDLSHORTLINE"] = tl.CDLSHORTLINE(self.open, self.high, self.low, self.close)
        df["CDLSPINNINGTOP"] = tl.CDLSPINNINGTOP(self.open, self.high, self.low, self.close)
        df["CDLSTALLEDPATTERN"] = tl.CDLSTALLEDPATTERN(self.open, self.high, self.low, self.close)
        df["CDLSTICKSANDWICH"] = tl.CDLSTICKSANDWICH(self.open, self.high, self.low, self.close)
        df["CDLTAKURI"] = tl.CDLTAKURI(self.open, self.high, self.low, self.close)
        df["CDLTASUKIGAP"] = tl.CDLTASUKIGAP(self.open, self.high, self.low, self.close)
        df["CDLTHRUSTING"] = tl.CDLTHRUSTING(self.open, self.high, self.low, self.close)
        df["CDLTRISTAR"] = tl.CDLTRISTAR(self.open, self.high, self.low, self.close)
        df["CDLUNIQUE3RIVER"] = tl.CDLUNIQUE3RIVER(self.open, self.high, self.low, self.close)
        df["CDLUPSIDEGAP2CROWS"] = tl.CDLUPSIDEGAP2CROWS(self.open, self.high, self.low, self.close)
        df["CDLXSIDEGAP3METHODS"] = tl.CDLXSIDEGAP3METHODS(self.open, self.high, self.low, self.close)

        return df.fillna(0)
    
    def calculate_overlap_studies(self):
        """
        Calculates various overlap studies for the input data.

        Returns:
            pd.DataFrame: Dataframe with calculated overlap studies.

        This function calculates various overlap studies based on the provided periods.
        """
        df = pd.DataFrame()
        df["Open"] =  self.open
        df["High"] = self.high
        df["Low"] = self.low
        df["Close"] = self.close
        df["Volume"] = self.volume
        df["Date"] = self.date
        
        for i in self.periods: 
            df["DEMA"+str(i)] = tl.DEMA(self.close, timeperiod=i)
            df["EMA"+str(i)] = tl.EMA(self.close, timeperiod=i)
            df["KAMA"+str(i)] = tl.KAMA(self.close, timeperiod=i)
            df["MIDPOINT"+str(i)] = tl.MIDPOINT(self.close, timeperiod=i)
            df["SMA"+str(i)] = tl.SMA(self.close, timeperiod=i)
            df["TRIMA"+str(i)] = tl.TRIMA(self.close, timeperiod=i)
            df["WMA"+str(i)] = tl.WMA(self.close, timeperiod=i)
            df["T3"+str(i)] = tl.T3(self.close, timeperiod=i, vfactor=0)
            df["TEMA"+str(i)] = tl.TEMA(self.close, timeperiod=i)
            df["MA"+str(i)] = tl.MA(self.close, timeperiod=i, matype=0)
            df["HT_TRENDLINE"+str(i)] = tl.HT_TRENDLINE(self.close)
    
        return df.fillna(0)
        
    def math_transform_functions(self):
        """
        Applies various mathematical transformation functions to the input data.

        Returns:
            pd.DataFrame: Dataframe with applied mathematical transformation functions.

        This function applies various mathematical transformation functions to the 'close' column.
        """
        df = pd.DataFrame()
        df["Open"] =  self.open
        df["High"] = self.high
        df["Low"] = self.low
        df["Close"] = self.close
        df["Volume"] = self.volume
        df["Date"] = self.date
        
        df["ACOS"] = tl.ACOS(self.close)
        df["ASIN"] = tl.ASIN(self.close)
        df["ATAN"] = tl.ATAN(self.close)
        df["CEIL"] = tl.CEIL(self.close)
        df["COS"] = tl.COS(self.close)
        # df["COSH"] = tl.COSH(self.close)
        # df["EXP"] = tl.EXP(self.close)
        df["FLOOR"] = tl.FLOOR(self.close)
        df["LN"] = tl.LN(self.close)
        df["LOG10"] = tl.LOG10(self.close)
        df["SIN"] = tl.SIN(self.close)
        # df["SINH"] = tl.SINH(self.close)
        df["SQRT"] = tl.SQRT(self.close)
        df["TAN"] = tl.TAN(self.close)
        df["TANH"] = tl.TANH(self.close)
    
        return df.fillna(0)
    
    def momentum_indicator_functions(self):
        """
        Applies various momentum indicator functions to the input data.

        Returns:
            pd.DataFrame: Dataframe with applied momentum indicator functions.

        This function applies various momentum indicator functions to the columns such as 'open', 'high', 'low', 'close', and 'real_volume'.
        """
        df = pd.DataFrame()
        df["Open"] =  self.open
        df["High"] = self.high
        df["Low"] = self.low
        df["Close"] = self.close
        df["Volume"] = self.volume
        df["Date"] = self.date
        
        for i in self.periods:
            df["ADX" + str(i)] = tl.ADX(self.high, self.low, self.close, timeperiod=i)
            df["ADXR" + str(i)] = tl.ADXR(self.high, self.low, self.close, timeperiod=i)
            df["AROONOSC" + str(i)] = tl.AROONOSC(self.high, self.low, timeperiod=i)
            df["CCI" + str(i)] = tl.CCI(self.high, self.low, self.close, timeperiod=i)
            df["CMO" + str(i)] = tl.CMO(self.close, timeperiod=i)
            df["DX" + str(i)] = tl.DX(self.high, self.low, self.close, timeperiod=i)
            df["MFI" + str(i)] = tl.MFI(self.high, self.low, self.close, self.volume, timeperiod=i)
            df["MINUS_DI" + str(i)] = tl.MINUS_DI(self.high, self.low, self.close, timeperiod=i)
            df["MINUS_DM" + str(i)] = tl.MINUS_DM(self.high, self.low, timeperiod=i)
            df["MOM" + str(i)] = tl.MOM(self.close, timeperiod=i)
            df["PLUS_DI" + str(i)] = tl.PLUS_DI(self.high, self.low, self.close, timeperiod=i)
            df["PLUS_DM" + str(i)] = tl.PLUS_DM(self.high, self.low, timeperiod=i)
            df["ROC" + str(i)] = tl.ROC(self.close, timeperiod=i)
            df["ROCP" + str(i)] = tl.ROCP(self.close, timeperiod=i)
            df["ROCR" + str(i)] = tl.ROCR(self.close, timeperiod=i)
            df["ROCR100" + str(i)] = tl.ROCR100(self.close, timeperiod=i)
            df["RSI" + str(i)] = tl.RSI(self.close, timeperiod=i)
            df["WILLR" + str(i)] = tl.WILLR(self.high, self.low, self.close, timeperiod=i)
            df["TRIX" + str(i)] = tl.TRIX(self.close, timeperiod=i)

        df["APO"] = tl.APO(self.close, fastperiod=12, slowperiod=26, matype=0)
        df["PPO"] = tl.PPO(self.close, fastperiod=12, slowperiod=26, matype=0)
        df["real"] = tl.ULTOSC(self.high, self.low, self.close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
        df["real"] = tl.ULTOSC(self.high, self.low, self.close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
        
        return df.fillna(0)
     
    def statistic_functions(self):
        """
        Applies various statistical functions to the input data.

        Returns:
            pd.DataFrame: Dataframe with applied statistical functions.

        This function applies various statistical functions to the columns such as 'high', 'low', and 'close'.
        """
        df = pd.DataFrame()
        df["Open"] =  self.open
        df["High"] = self.high
        df["Low"] = self.low
        df["Close"] = self.close
        df["Volume"] = self.volume
        df["Date"] = self.date
        
        for i in self.periods:
            df["BETA" + str(i)] = tl.BETA(self.high, self.low, timeperiod=i)
            df["CORREL" + str(i)] = tl.CORREL(self.high, self.low, timeperiod=i)
            df["LINEARREG" + str(i)] = tl.LINEARREG(self.close, timeperiod=i)
            df["LINEARREG_ANGLE" + str(i)] = tl.LINEARREG_ANGLE(self.close, timeperiod=i)
            df["LINEARREG_INTERCEPT" + str(i)] = tl.LINEARREG_INTERCEPT(self.close, timeperiod=i)
            df["LINEARREG_SLOPE" + str(i)] = tl.LINEARREG_SLOPE(self.close, timeperiod=i)
            df["STDDEV" + str(i)] = tl.STDDEV(self.close, timeperiod=i, nbdev=1)
            df["TSF" + str(i)] = tl.TSF(self.close, timeperiod=i)
            df["VAR" + str(i)] = tl.VAR(self.close, timeperiod=i, nbdev=1)
            df["median" + str(i)] = self.close.rolling(window=i, min_periods=1).median()
            df["mode" + str(i)] = self.close.rolling(window=i, min_periods=1).apply(lambda x: x.mode()[0])
            df["std" + str(i)] = df["median" + str(i)].rolling(window=i, min_periods=1).std()
        
        return df.fillna(0)
    
    def math_operator_functions(self):
        """
        Applies various mathematical operator functions to the input data.
    
        Returns:
            pd.DataFrame: Dataframe with applied mathematical operator functions.
    
        This function creates copies of the input data and applies various mathematical operator functions to the columns such as 'high', 'low', and 'close'.
        """
        
        df = pd.DataFrame()
        df["Open"] =  self.open
        df["High"] = self.high
        df["Low"] = self.low
        df["Close"] = self.close
        df["Volume"] = self.volume
        df["Date"] = self.date
        
        for i in self.periods:
            df["MAX"+str(i)] = tl.MAX(self.close, timeperiod=i)
            df["MAXINDEX"+str(i)] = tl.MAXINDEX(self.close, timeperiod=i)
            df["MIN"+str(i)] = tl.MIN(self.close, timeperiod=i)
            df["MININDEX"+str(i)] = tl.MININDEX(self.close, timeperiod=i)
            df["SUM"+str(i)] = tl.SUM(self.close, timeperiod=i)

        # min, max = MINMAX(close, timeperiod=30)
        # minidx, maxidx = MINMAXINDEX(close, timeperiod=30)
    
        df["ADD"] = tl.ADD(self.high, self.low)
        df["DIV"] = tl.DIV(self.high, self.low)
        df["SUB"] = tl.SUB(self.high, self.low)
    
        return df.fillna(0)

    def all_ (self):

        data_indicators_pattern  =  self.add_indicators_pattern_recognition_functions()
        data_calculate_overlap_studies  =  self.calculate_overlap_studies()
        data_math_operator_functions  =  self.math_operator_functions()
        data_math_transform_functions  =  self.math_transform_functions()
        data_momentum_indicator_functions  =  self.momentum_indicator_functions()
        data_statistic =  self.statistic_functions()
        
        dataframes = {
            'indicators_pattern': data_indicators_pattern,
            'calculate_overlap_studies': data_calculate_overlap_studies,
            'math_operator_functions': data_math_operator_functions,
            'math_transform_functions': data_math_transform_functions,
            'momentum_indicator_functions': data_momentum_indicator_functions,
            'statistic': data_statistic
        }

        merged_data = None  # Создаем пустой датафрейм для объединенных данных

        for key, df in dataframes.items():
            if merged_data is None:
                merged_data = df.copy()  # Копируем первый датафрейм, если merged_data пустой
            else:
                # Объединяем по общим колонкам
                merged_data = pd.merge(merged_data, df, on=['Date', 'Close', 'High', 'Low', 
                                                            'Open',"Volume"], how='inner')

        return merged_data
    


    
# manual strategy    
def define_level(data: pd.DataFrame, window_size: int = 14, bias: int = 1) -> pd.DataFrame:
    """
    Dodaje wartości maksimum i minimum przesuwające się do ramki danych na podstawie określonych parametrów.

    Argumenty:
    data (pd.DataFrame): Ramka danych wejściowych.
    window_size (list): Rozmiar okna używany do obliczania wartości maksimum i minimum. Domyślnie ustawiony na 14.
    bias (int): Wartość przesunięcia dla obliczeń. Domyślnie ustawiony na 1.

    Zwraca:
    pd.DataFrame: Zaktualizowana ramka danych zawierająca wartości maksimum i minimum.
    """
    data = data.copy()
    
    if not isinstance(window_size, int) or not isinstance(bias, int) or window_size <= 0 or bias < 0:
        window_size = ceil(abs(window_size))
        bias = ceil(abs(bias))
        
        # raise ValueError("window_size должно быть целым положительным числом, а bias - целым неотрицательным числом.")

    
    # Obliczenie wartości maksimum i minimum za pomocą przesuwającego się okna
    data.loc[:, f'RollingMax'] = data['High'].rolling(window=window_size).max().shift(bias)
    data.loc[:, f'RollingMin'] = data['Low'].rolling(window=window_size).min().shift(bias)

    # Usunięcie wierszy zawierających wartości NaN
    data.dropna(axis=0, inplace=True)
    
    # Zresetowanie indeksu ramki danych
    data.reset_index(drop=True, inplace=True)
    
    return data

    
def rebound_analysis(data):
    """
    Przeprowadza analizę odbić cen od poziomów wsparcia i oporu w ramce danych.

    Argumenty:
    data (pd.DataFrame): Ramka danych wejściowych.

    Zwraca:
    pd.DataFrame: Zaktualizowana ramka danych zawierająca analizę odbić.
    """
    # Analiza odbić cen od poziomów oporu
    data['SELL'] = (
        (data["RollingMax"] < data["High"]) &
        (data["RollingMax"] > data["Close"])
    ).map({True: 1, False: 0}) 

    # Analiza odbić cen od poziomów wsparcia
    data['Buy'] = (
        (data["RollingMin"] > data["Low"]) &
        (data["RollingMin"] < data["Close"])
    ).map({True: 2, False: 0})
    

    # Tworzenie sygnału na podstawie wykrytych odbić
    data["Signal"] = data['Buy'] + data['SELL']
    data["Signal"] = data["Signal"].astype(str)
    data.loc[data["Signal"] == '1', "Signal"] = "sell"
    data.loc[data["Signal"] == '2', "Signal"] = "buy"

    # Uzupełnianie pustych wartości sygnału zgodnie z poprzednimi wartościami
    data["Signal"] = data["Signal"].replace("0", np.nan).ffill()
    data = data.drop(["SELL","Buy"], axis=1)

    # Usunięcie wierszy zawierających wartości NaN
    data.dropna(axis=0, inplace=True)
    
    # Zresetowanie indeksu ramki danych
    data.reset_index(drop=True, inplace=True)

    return data

    
# calc
def calculate_accumulated_price_changes(data, princ=False):    
    """
    Calculates the accumulated price changes based on buy and sell signals in the given data.

    Args:
        data (pd.DataFrame): The input DataFrame.
        princ (bool, optional): A boolean value indicating whether to return separate accumulated changes for buy and sell. Defaults to False.

    Returns:
        float or tuple: The accumulated price changes. If princ is True, the function returns separate changes for buy and sell.

    This function calculates the accumulated price changes based on buy and sell signals in the provided DataFrame.
    It returns the total accumulated changes. If princ is True, the function returns separate changes for buy and sell.
    """
    df = data.copy()
    signal_changes = df['Signal'].ne(df['Signal'].shift())
    
    indices = df.index[signal_changes].tolist()
    
    df['AccumulatedPriceChange'] = 0.0
    
    
    for i in range(0, len(indices) - 1):
        accumulated_change = 0.0
        if df.loc[indices[i], 'Signal'] == 'sell' and df.loc[indices[i + 1], 'Signal'] == 'buy':
            start_sell_index = indices[i]
            end_buy_index = indices[i + 1]
    
            start_sell_price = df.loc[start_sell_index, 'Close']
            end_buy_price = df.loc[end_buy_index, 'Close']
    
            price_change_sell_to_buy = start_sell_price - end_buy_price
    
            accumulated_change += price_change_sell_to_buy
            df.loc[indices[i + 1], 'AccumulatedPriceChange'] = accumulated_change
    
        elif df.loc[indices[i], 'Signal'] == 'buy' and df.loc[indices[i + 1], 'Signal'] == 'sell':
            start_buy_index = indices[i]
            end_sell_index = indices[i + 1]
    
            start_buy_price = df.loc[start_buy_index, 'Close']
            end_sell_price = df.loc[end_sell_index, 'Close']
    
            price_change_buy_to_sell = end_sell_price - start_buy_price
    
            accumulated_change += price_change_buy_to_sell
            df.loc[indices[i + 1], 'AccumulatedPriceChange'] = accumulated_change
    
    df["AccumulatedPriceChange"] = df["AccumulatedPriceChange"].shift(-1).fillna(0)
    all_sell = df.loc[df["Signal"] == "sell", "AccumulatedPriceChange"].sum()
    all_buy = df.loc[df["Signal"] == "buy", "AccumulatedPriceChange"].sum()

    if princ:
        return all_buy + all_sell
    else:
        return df

    
# optimizer
def optimize_parameters(data, analysis, calculate, window_size_range, 
                        bias_range , return_param = False):
    # или валидация (учим на первых трех а смотрим на 4 ) и так до конца 
    """
    Optimizes the parameters of a given analysis by testing different window sizes and bias values.

    Args:
        data (pd.DataFrame): The input DataFrame.
        analysis (function): The analysis function to be optimized.
        calculate (function): The function to calculate the score.
        windows_size (list): List of window sizes to be tested.
        bias (list, optional): List of bias values to be tested. Defaults to [1].

    Returns:
            pd.DataFrame(): The best data found during optimization.

    This function iterates through the provided window sizes and bias values, applies the analysis and calculates 
    the score for each combination. It then returns the parameters that yield the best score.
    """
    best_score = float('-inf')
    best_params = None
    return_data = None
    for window_size in tqdm(range(*window_size_range)):
        for bias in range(*bias_range):
            current_data = define_level(data, window_size, bias)
            rebound_data = analysis(current_data)
            current_score = calculate(rebound_data, princ=True)

            if current_score > best_score:
                best_score = current_score
                best_params = {'window_size': window_size, 'bias': bias}
                return_data = rebound_data
                
    print(best_params)
    
    if return_param:
        return best_params
        
    return return_data

    
def cross_validate_on_periods(data, analysis, calculate, window_size_range, 
                              bias_range, n_splits=5, return_param = False):
    
    """
    Cross-validates the analysis on different periods of the given data using TimeSeriesSplit.

    Args:
        data (pd.DataFrame): The input DataFrame with a time series.
        analysis (function): The analysis function to be optimized.
        calculate (function): The function to calculate the score.
        window_size_range (tuple): Range of window sizes to be tested.
        bias_range (tuple): Range of bias values to be tested.
        n_splits (int): Number of splits for TimeSeriesSplit. Defaults to 5.
        return_param (bool): If True, returns the best parameters. If False, returns the best data.

    Returns:
        pd.DataFrame or dict: The best data found during optimization or the best parameters.

    This function iterates through the provided window sizes and bias values, applies the analysis, 
    and calculates the score for each combination. It then returns the parameters that yield the best score
    or the best data, based on the value of 'return_param'.

    Note: The function uses tqdm to display a progress bar during the optimization process.
    """

    # Calculate the step size for splitting the data into time periods
    step = len(data) // n_splits
    start = 0
    best_score = float('-inf')
    best_params = None

    # Iterate through the range of window sizes using tqdm for progress visualization
    for window_size in tqdm(range(*window_size_range)):
        for bias in range(*bias_range):
            score = []

            # Reset start and step for each combination of window size and bias
            # start = 0
            # step = len(data) // n_splits

            # Iterate through each time period for cross-validation
            for _ in range(n_splits):
                # Select the current time period for training
                train_data = data.iloc[start : start + step]
                # print(start, start + step)
                
                # Transform the training data based on the current window size and bias
                current_train_data = define_level(train_data, window_size, bias)
                
                # Apply the analysis function to the transformed training data
                rebound_train_data = analysis(current_train_data)
                
                # Calculate the score using the provided calculate function
                current_score = calculate(rebound_train_data, princ=True) # 10 test 8
                
                # Append the current score to the list
                score.append(current_score)

                # Update start and step for the next time period
                start += step

            # Calculate the average score for the current combination of window size and bias
            average_score = sum(score) / len(score)

            # Update the best score and parameters if the current combination is better
            if average_score > best_score:
                best_score = average_score
                best_params = {'window_size': window_size, 'bias': bias}
                # Calculate the best data using the provided analysis and define_level functions
                best_data = calculate(analysis(define_level(data, window_size, bias)))

    # Print the best parameters and return the best data
    print(best_params)
    
    if return_param:
        return best_params
    else :
        return best_data

    
# Genetic algorithm strategy
class GeneticAlgorithm:
    """
    A class representing a Genetic Algorithm for parameter optimization in trading strategies.

    Attributes:
        data (pd.DataFrame): The financial data used for analysis.
        analysis (callable): The analysis function to process the data.
        calculate (callable): The scoring function to evaluate the performance of parameter combinations.
        window_sizes (list): Possible values for the window size parameter.
        biases (list): Possible values for the bias parameter.
        best_individual (list): The best parameter combination found by the genetic algorithm.

    Methods:
        init_individual(individual_class): Initializes an individual for the genetic algorithm.
        evaluate(individual): Evaluates the fitness of an individual based on the provided scoring function.
        mutate(individual): Performs mutation on an individual to introduce diversity in the population.
        calculate_parameters(params): Calculates the score for a given set of parameters.
        run_genetic_algorithm(population_size, offspring_size, cx_probability, mut_probability, n_generations):
            Runs the genetic algorithm to find the best parameter combination.
        get_best_individual(): Returns the best parameter combination found by the genetic algorithm.
    """
    
    def __init__(self, data, analysis, calculate, window_sizes, biases=[1]):
        """Initializes the GeneticAlgorithm instance.

        Args:
            data (pd.DataFrame): The financial data used for analysis.
            analysis (callable): The analysis function to process the data.
            calculate (callable): The scoring function to evaluate the performance of parameter combinations.
            window_sizes (list): Possible values for the window size parameter.
            biases (list, optional): Possible values for the bias parameter. Defaults to [1].
        """
        # Initialize the GeneticAlgorithm instance with the provided parameters
        # Attribute Initialization:
        self.data = data
        self.analysis = analysis
        self.calculate = calculate
        self.window_sizes = window_sizes
        self.biases = biases
        self.best_individual = None

        # Problem Definition
        # Define the problem as a maximization problem
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        # Toolbox Initialization
        # Create a toolbox with the necessary components
        self.toolbox = base.Toolbox()

        # Registering Functions in the Toolbox
        # Register an initialization method for individuals
        self.toolbox.register("individual", self.init_individual, creator.Individual)
        
        # Register a method to initialize a population of individuals
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        
        # Register the evaluation method for individuals
        self.toolbox.register("evaluate", self.evaluate)
        
        # Register the crossover method using Blend Crossover with a specified alpha value
        self.toolbox.register("mate", tools.cxBlend, alpha=0.5)
        
        # Register the mutation method
        self.toolbox.register("mutate", self.mutate)
        
        # Register the selection method using Tournament Selection with a tournament size of 3
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    
    def init_individual(self, individual_class):
        """
        Initializes an individual for the genetic algorithm.

        Args:
            individual_class: The class representing an individual in the genetic algorithm.

        Returns:
            list: The initialized individual.
        """
        
        return individual_class([random.choice(self.window_sizes), random.choice(self.biases)])

    
    def evaluate(self, individual):
        """
        Evaluates the fitness of an individual based on the provided scoring function.

        Args:
            individual (list): The individual representing a parameter combination.

        Returns:
            tuple: The fitness score of the individual.
        """
        
        window_size, bias = map(int, individual)
        params = {'window_size': window_size, 'bias': bias}
        score = self.calculate_parameters(params)
        return (score,)

    
    def mutate(self, individual):
        """
        Performs mutation on an individual to introduce diversity in the population.

        Args:
            individual (list): The individual to be mutated.

        Returns:
            tuple: The mutated individual.
        """
        
        if random.random() < 0.5:
            individual[0] = int(abs(individual[0] + random.randint(-5, 5)))
        else:
            individual[1] = random.choice(self.biases)
        return individual,

    
    def calculate_parameters(self, params):
        """
        Calculates the score for a given set of parameters.

        Args:
            params (dict): The parameter values.

        Returns:
            float: The calculated score.
        """
        
        current_data = define_level(self.data, params['window_size'], params['bias'])
        rebound_data = self.analysis(current_data)
        return self.calculate(rebound_data)

        
    def run_genetic_algorithm(self, population_size=10, offspring_size=50, cx_probability=0.7, mut_probability=0.2, n_generations=10):
        """
        Runs the genetic algorithm to find the best parameter combination.

        Args:
            population_size (int, optional): The size of the initial population. Defaults to 10.
            offspring_size (int, optional): The size of the offspring population. Defaults to 50.
            cx_probability (float, optional): The crossover probability. Defaults to 0.7.
            mut_probability (float, optional): The mutation probability. Defaults to 0.2.
            n_generations (int, optional): The number of generations. Defaults to 10.

        Returns:
            list: The best parameter combination found by the genetic algorithm.
        """
        # Create an initial population
        population = self.toolbox.population(n=population_size)

        # Run the genetic algorithm
        algorithms.eaMuPlusLambda(population, self.toolbox, mu=population_size, lambda_=offspring_size,
                                  cxpb=cx_probability, mutpb=mut_probability, ngen=n_generations, stats=None, halloffame=None)

        # Get the best individual
        self.best_individual = tools.selBest(population, k=1)[0]
        print("Best Parameters:", self.best_individual)

        return self.best_individual

    
    def get_best_individual(self):
        """
        Returns the best parameter combination found by the genetic algorithm.

        Returns:
            list: The best parameter combination.
        """
        return self.best_individual

    
# network strategy
# preparing data for a neural network

    
def cleaned_data(df: pd.DataFrame, variance_threshold: float = 0.1) ->  pd.DataFrame :
    """
    Perform data cleaning on a collection of DataFrames.

    Parameters:
    - data (dict): A dictionary where keys are names (strings) and values are DataFrames to be cleaned.

    Returns:
    - dict: A dictionary containing cleaned DataFrames, where keys are names and values are corresponding cleaned DataFrames.

    The function performs the following steps for each DataFrame in the input dictionary:
    1. Separates datetime columns and non-datetime columns.
    2. Handles non-datetime columns by removing rows with missing values and keeping columns with more than one unique value.
    3. Drops duplicate columns in the cleaned DataFrame.
    4. Adds a 'Date' column to the cleaned DataFrame containing datetime values.

    Example:
    ```
    data_dict = {'df1': pd.DataFrame(...), 'df2': pd.DataFrame(...)}
    cleaned_data_dict = cleaned_data(data_dict)
    ```

    Note:
    - The function uses the tqdm library to display a progress bar during the cleaning process.
    """

    # Separate datetime columns
    datetime_columns = df.select_dtypes(include=['datetime64']).columns
    
    other_columns = df.columns.difference(datetime_columns)

    # Handle non-datetime columns
    df_cleaned = df[other_columns].dropna()
    df_cleaned = df_cleaned.loc[:, df_cleaned.nunique() > 1]

    # Drop duplicate columns
    duplicate_columns = df_cleaned.columns[df_cleaned.T.duplicated()].tolist()
    df_cleaned = df_cleaned.drop(columns=duplicate_columns, axis=1)

    # Calculate variance and remove columns with low variance
    variances = df_cleaned.var()
    df_cleaned = df_cleaned.loc[:, variances >= variance_threshold]

    df_cleaned["Date"] = df[datetime_columns]
    
    return df_cleaned


    
def create_lagged_features_and_target(df: {pd.DataFrame}) -> {str: pd.DataFrame}:
    """
    Creates lagged features and a target variable for each DataFrame in the provided dictionary.

    Parameters:
    - data (dict): A dictionary where keys are names and values are DataFrames.

    Returns:
    - dict: A dictionary with DataFrames containing lagged features and a target variable.

    Example:
    ```
    lagged_data_dict = create_lagged_features_and_target({'df1': df1, 'df2': df2})
    ```

    This function iterates through the provided dictionary of DataFrames and creates lagged features
    and a target variable for each DataFrame.

    The target variable ('Close_diff') is calculated as the difference between the current and next 'Close' values.

    The resulting DataFrames are cleaned by removing rows with missing values.

    The function returns a dictionary with DataFrames containing lagged features and a target variable.
    """


    # Creating target
    df['Close_diff'] = df['Close'] - df['Close'].shift(-1)

    # Drop rows with missing values
    df = df.dropna()


    return df

    
# parameter optimization
def get_best_data_frame_parameters_for_LSTM(data: {str, pd.DataFrame}) ->  {str, pd.DataFrame}:
    """
    Process a dictionary of DataFrames using GradientRFE and return the best parameters for each DataFrame.

    Parameters:
    - data (Dict[str, pd.DataFrame]): A dictionary where keys are DataFrame names and values are DataFrames.

    Returns:
    - best_parameters (Dict[str, dict]): A dictionary where keys are DataFrame names and values are
      the best parameters obtained from GradientRFE for each DataFrame.
    """

    best_parameters = {}  # Initialize an empty dictionary to store the best parameters


    # Remove columns with a single unique value, as they do not contribute to the model
    df = df.drop("Date", axis=1)

    # Create an instance of GradientRFE for the current DataFrame
    grfe = GradientRFE(df)
    
    # Fit GradientRFE to the data and obtain the best parameters
    grfe.fit() 
    
    # Store the best parameters in the dictionary with the DataFrame name as the key
    best_parameters[name] = grfe.best_parameters

    return best_parameters










