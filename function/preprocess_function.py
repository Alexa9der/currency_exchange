from import_libraries.libraries import  *

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
        self.open = self.df["open"]
        self.high = self.df["high"]
        self.low = self.df["low"]
        self.close = self.df["close"]
        self.volume = self.df["volume"]
        self.periods = periods if periods else [23,115,460]

    def add_indicators_pattern_recognition_functions(self):
        """
        Adds pattern recognition indicators to the dataframe.

        Returns:
            pd.DataFrame: Dataframe with added pattern recognition indicators.

        This function creates copies of the input data and adds pattern recognition indicators to the dataframe.
        """
        df = pd.DataFrame()
        df["open"] =  self.df["open"]
        df["high"] = self.df["high"]
        df["low"] = self.df["low"]
        df["close"] = self.df["close"]
        df["volume"] = self.df["volume"]

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
        df["open"] =  self.df["open"]
        df["high"] = self.df["high"]
        df["low"] = self.df["low"]
        df["close"] = self.df["close"]
        df["volume"] = self.df["volume"]
        
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
        df["open"] =  self.df["open"]
        df["high"] = self.df["high"]
        df["low"] = self.df["low"]
        df["close"] = self.df["close"]
        df["volume"] = self.df["volume"]
        
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
        df["open"] =  self.df["open"]
        df["high"] = self.df["high"]
        df["low"] = self.df["low"]
        df["close"] = self.df["close"]
        df["volume"] = self.df["volume"]
        
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
        df["open"] =  self.df["open"]
        df["high"] = self.df["high"]
        df["low"] = self.df["low"]
        df["close"] = self.df["close"]
        df["volume"] = self.df["volume"]
        
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
            df["median" + str(i)] = self.df["close"].rolling(window=i, min_periods=1).median()
            df["mode" + str(i)] = self.df["close"].rolling(window=i, min_periods=1).apply(lambda x: x.mode()[0])
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
        df["open"] =  self.df["open"]
        df["high"] = self.df["high"]
        df["low"] = self.df["low"]
        df["close"] = self.df["close"]
        df["volume"] = self.df["volume"]
        
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
    
    def all_methods(self):
        """
        Invokes all the preprocessing methods.
    
        Returns:
            pd.DataFrame: Dataframe with all the preprocessing methods applied.
    
        This function invokes all the preprocessing methods for the stock data.
        """
        
        all_methods = [getattr(self, method) for method in dir(self) if inspect.ismethod(getattr(self, method))]
        for method in all_methods:
            if method.__name__ != 'all_methods' and "__" not in  method.__name__ :
                method()
                
        return self.df
    
# Etap I. Określanie kierunku.
# 1. Wyznaczam cenę max i min dla różnych przedziałów od 1 do 60 dni wstecz.
# 2. Określam czy cena w bieżącym dniu przekroczyła wyznaczony poziom min lub max.
# 3. Określam czy cena w bieżącym dniu powróciła do określonego przedziału między min a max.
# 4. Wyznaczam bieżący kieru5.ek:
# - po przekroczeniu i powrocie do poziomu min ("wsparcie") kierunek to BUY;
# - po przekroczeniu i powrocie do poziomu max ("opór") kierunek to SELL;
# 5. Po zakończeniu sesji powtarzam punk
# 8. Sprawdzam w którym kierunku następnego dnia był większy ruch. W górę to cena max - otwarcie. W dół to cena otwarcie - min. ty 1-4 d
    
def define_level(data: pd.DataFrame, window_size: list = 14, bias: int = 1) -> pd.DataFrame:
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

def breakdown_analysis(data):
    """
    Przeprowadza analizę przełamania cen względem poziomów oporu i wsparcia.

    Funkcja określa, czy występuje przełamanie ceny względem poziomów oporu i wsparcia na podstawie danych wejściowych.
    Ustawia sygnały "buy" i "sell" w kolumnie "Signal" na podstawie wykrytych przełamań.

    Argumenty:
    data (pd.DataFrame): Dane wejściowe zawierające kolumny "RollingMax" i "RollingMin" oraz ceny otwarcia, zamknięcia, najwyższe i najniższe.

    Zwraca:
    pd.DataFrame: Dane wejściowe z dodanymi sygnałami "buy" i "sell" oraz kolumną "Signal" określającą rodzaj sygnału.

    Przykład użycia:
    >>> data = pd.DataFrame({'RollingMax': [50, 55, 60, 58, 52], 'RollingMin': [45, 40, 35, 38, 43], 'High': [52, 55, 58, 56, 51], 'Low': [48, 42, 36, 39, 45], 'Close': [50, 45, 40, 42, 48]})
    >>> analyzed_data = breakdown_analysis(data)
    >>> print(analyzed_data)
    """
    data['Buy'] = (
        (data["RollingMax"] < data["High"]) &  # maslo masliane
        (data["RollingMax"] < data["Close"])
    ).map({True: 1, False: 0})
    
    data['SELL'] = (
        (data["RollingMin"] > data["Low"]) &  # maslo masliane
        (data["RollingMin"] > data["Close"])
    ).map({True: 2, False: 0})
    
    data["Signal"] = data['Buy'] + data['SELL']
    data.loc[data["Signal"] == 1, "Signal"] = "buy"
    data.loc[data["Signal"] == 2, "Signal"] = "sell"

    data["Signal"] = data["Signal"].replace(0, np.nan).ffill()
    data = data.drop(["SELL", "Buy"], axis=1)

    data.dropna(axis=0, inplace=True)
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
    
    # resistance_indices = data[data['SELL'] == True].index + 1
    # data.loc[resistance_indices, 'Next_Resistance_Candle_Type'] = (
    #     data.loc[resistance_indices, 'Open'] - data.loc[resistance_indices, 'Low']
    # )

    # Analiza odbić cen od poziomów wsparcia
    data['Buy'] = (
        (data["RollingMin"] > data["Low"]) &
        (data["RollingMin"] < data["Close"])
    ).map({True: 2, False: 0})
    
    # support_indices = data[data['Buy'] == True].index + 1
    # data.loc[support_indices, 'Next_Support_Candle_Type'] = (
    #     data.loc[support_indices, 'High'] - data.loc[support_indices, 'Open']
    # )

    # Tworzenie sygnału na podstawie wykrytych odbić
    data["Signal"] = data['Buy'] + data['SELL']
    data.loc[data["Signal"] == 1, "Signal"] = "sell"
    data.loc[data["Signal"] == 2, "Signal"] = "buy"

    # Uzupełnianie pustych wartości sygnału zgodnie z poprzednimi wartościami
    data["Signal"] = data["Signal"].replace(0, np.nan).ffill()
    data = data.drop(["SELL","Buy"], axis=1)

    # Usunięcie wierszy zawierających wartości NaN
    data.dropna(axis=0, inplace=True)
    
    # Zresetowanie indeksu ramki danych
    data.reset_index(drop=True, inplace=True)

    return data

# calc
def calculate_percentage(data, return_count=False):
    """
    Calculates the score based on the provided data, which includes buy and sell signals.

    Args:
    data (pd.DataFrame): Input data containing columns such as 'Signal', 'PriceChange', 'Close', and 'Open'.
    return_count (bool): Indicates whether to return the percentage of buy and sell price changes separately.

    Returns:
    float or tuple: The calculated percentage score. If return_count is True, it returns a tuple containing the percentage of buy and sell price changes.

    Example:
    >>> import pandas as pd
    >>> data = pd.DataFrame({'Signal': ['sell', 'buy', 'buy', 'sell'], 'PriceChange': [0.1, 0.2, -0.1, -0.2], 'Close': [10, 11, 12, 13], 'Open': [9, 10, 11, 12]})
    >>> calculate_score(data)
    37.5
    """

    df = data.copy()

    sell_count = 0
    buy_count = 0
    sell_price_changes = np.array([])
    buy_price_changes = np.array([])
    oll_sell_price_changes = np.array([])
    oll_buy_price_changes = np.array([])

    for i in range(len(df)):
        if df['Signal'].iloc[i] == 'sell':
            oll_sell_price_changes = np.append(oll_sell_price_changes, df["PriceChange"].iloc[i])
            if df['Close'].iloc[i] < df['Open'].iloc[i]:
                sell_price_changes = np.append(sell_price_changes, df["PriceChange"].iloc[i])
                sell_count += 1
                if buy_count > 0:
                    buy_price_changes = np.append(buy_price_changes, df["PriceChange"].iloc[i])
                    oll_buy_price_changes = np.append(oll_buy_price_changes, df["PriceChange"].iloc[i])
                    buy_count = 0
        elif df['Signal'].iloc[i] == 'buy':
            oll_buy_price_changes = np.append(oll_buy_price_changes, df["PriceChange"].iloc[i])
            if df['Close'].iloc[i] > df['Open'].iloc[i]:
                buy_price_changes = np.append(buy_price_changes, df["PriceChange"].iloc[i])
                buy_count += 1
                if sell_count > 0:
                    sell_price_changes = np.append(sell_price_changes, df["PriceChange"].iloc[i])
                    oll_sell_price_changes = np.append(oll_sell_price_changes, df["PriceChange"].iloc[i])
                    sell_count = 0

    if sell_count > 0:
        sell_price_changes = np.append(sell_price_changes, df["PriceChange"].iloc[i])
        oll_sell_price_changes = np.append(oll_sell_price_changes, df["PriceChange"].iloc[i])
        
    if buy_count > 0:
        buy_price_changes = np.append(buy_price_changes, df["PriceChange"].iloc[i])
        oll_buy_price_changes = np.append(oll_buy_price_changes, df["PriceChange"].iloc[i])

    percentage_buy = (buy_price_changes.sum() / oll_buy_price_changes.sum()) * 100
    percentage_sell = (sell_price_changes.sum() / oll_sell_price_changes.sum()) * 100
    percentage = (percentage_sell + percentage_buy) / 2

    if return_count:
        return percentage_buy, percentage_sell

    return percentage


def calculate_accumulated_price_changes(df, princ=False):    
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
        return all_buy, all_sell
    else:
        return all_buy + all_sell


# optimizer
def optimize_parameters(data, analysis, calculate, windows_size, bias = [1]):
    """
    Optimizes the parameters of a given analysis by testing different window sizes and bias values.

    Args:
        data (pd.DataFrame): The input DataFrame.
        analysis (function): The analysis function to be optimized.
        calculate (function): The function to calculate the score.
        windows_size (list): List of window sizes to be tested.
        bias (list, optional): List of bias values to be tested. Defaults to [1].

    Returns:
        dict: The best parameters found during optimization.

    This function iterates through the provided window sizes and bias values, applies the analysis and calculates 
    the score for each combination. It then returns the parameters that yield the best score.
    """
    best_score = 0
    best_params = None

    for window_size in t(windows_size):
        for b in bias:
            current_data = define_level(data, window_size, b)
            rebound_data = analysis(current_data)
            current_score = calculate(rebound_data)  

            if current_score > best_score:
                best_score = current_score
                best_params = {'window_size': window_size, 'bias': b}

    return best_params


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













