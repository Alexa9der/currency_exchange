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


    def support_resistance_line(self, support_columns: str = 'high', resistance_columns: str = 'low',
                                timeperiods_start: int = 100, timeperiods_finish: int = 250, timeperiods_step: int = 50):
        """
        Calculate support and resistance lines for the given data.

        Args:
            support_columns (str, optional): Name of the column for calculating support. Defaults to 'high'.
            resistance_columns (str, optional): Name of the column for calculating resistance. Defaults to 'low'.
            timeperiods_start (int, optional): Starting value for the time period. Defaults to 100.
            timeperiods_finish (int, optional): Ending value for the time period. Defaults to 250.
            timeperiods_step (int, optional): Step size for the time period. Defaults to 50.

        Returns:
            pd.DataFrame: DataFrame with support and resistance lines for different time periods.

        This function calculates support and resistance lines for the given data based on the specified time periods and columns.
        """


        support = tl.MIN(self.df[support_columns], timeperiod=100)
        resistance = tl.MAX(self.df[resistance_columns], timeperiod=100)

        for timeperiod in range(timeperiods_start, timeperiods_finish, timeperiods_step):
            self.df.loc[:, f'support_{timeperiod}'] = tl.MIN(self.df[support_columns], timeperiod=timeperiod)
            self.df.loc[:, f'resistance_{timeperiod}'] = tl.MAX(self.df[resistance_columns], timeperiod=timeperiod)

        return self.df
    

    def add_indicators_pattern_recognition_functions(self):
        """
        Adds pattern recognition indicators to the dataframe.

        Returns:
            pd.DataFrame: Dataframe with added pattern recognition indicators.

        This function creates copies of the input data and adds pattern recognition indicators to the dataframe.
        """
        
        self.df["CDL2CROWS"] = tl.CDL2CROWS(self.open, self.high, self.low, self.close)
        self.df["CDL3BLACKCROWS"] = tl.CDL3BLACKCROWS(self.open, self.high, self.low, self.close)
        self.df["CDL3INSIDE"] = tl.CDL3INSIDE(self.open, self.high, self.low, self.close)
        self.df["CDL3LINESTRIKE"] = tl.CDL3LINESTRIKE(self.open, self.high, self.low, self.close)
        self.df["CDL3OUTSIDE"] = tl.CDL3OUTSIDE(self.open, self.high, self.low, self.close)
        self.df["CDL3STARSINSOUTH"] = tl.CDL3STARSINSOUTH(self.open, self.high, self.low, self.close)
        self.df["CDL3WHITESOLDIERS"] = tl.CDL3WHITESOLDIERS(self.open, self.high, self.low, self.close)
        self.df["CDLABANDONEDBABY"] = tl.CDLABANDONEDBABY(self.open, self.high, self.low, self.close)
        self.df["CDLADVANCEBLOCK"] = tl.CDLADVANCEBLOCK(self.open, self.high, self.low, self.close)
        self.df["CDLBELTHOLD"] = tl.CDLBELTHOLD(self.open, self.high, self.low, self.close)
        self.df["CDLBREAKAWAY"] = tl.CDLBREAKAWAY(self.open, self.high, self.low, self.close)
        self.df["CDLCLOSINGMARUBOZU"] = tl.CDLCLOSINGMARUBOZU(self.open, self.high, self.low, self.close)
        self.df["CDLCONCEALBABYSWALL"] = tl.CDLCONCEALBABYSWALL(self.open, self.high, self.low, self.close)
        self.df["CDLCOUNTERATTACK"] = tl.CDLCOUNTERATTACK(self.open, self.high, self.low, self.close)
        self.df["CDLDARKCLOUDCOVER"] = tl.CDLDARKCLOUDCOVER(self.open, self.high, self.low, self.close)
        self.df["CDLDOJI"] = tl.CDLDOJI(self.open, self.high, self.low, self.close)
        self.df["CDLDOJISTAR"] = tl.CDLDOJISTAR(self.open, self.high, self.low, self.close)
        self.df["CDLDRAGONFLYDOJI"] = tl.CDLDRAGONFLYDOJI(self.open, self.high, self.low, self.close)
        self.df["CDLENGULFING"] = tl.CDLENGULFING(self.open, self.high, self.low, self.close)
        self.df["CDLEVENINGDOJISTAR"] = tl.CDLEVENINGDOJISTAR(self.open, self.high, self.low, self.close, penetration=0)
        self.df["CDLEVENINGSTAR"] = tl.CDLEVENINGSTAR(self.open, self.high, self.low, self.close, penetration=0)
        self.df["CDLGAPSIDESIDEWHITE"] = tl.CDLGAPSIDESIDEWHITE(self.open, self.high, self.low, self.close)
        self.df["CDLGRAVESTONEDOJI"] = tl.CDLGRAVESTONEDOJI(self.open, self.high, self.low, self.close)
        self.df["CDLHAMMER"] = tl.CDLHAMMER(self.open, self.high, self.low, self.close)
        self.df["CDLHANGINGMAN"] = tl.CDLHANGINGMAN(self.open, self.high, self.low, self.close)
        self.df["CDLHARAMI"] = tl.CDLHARAMI(self.open, self.high, self.low, self.close)
        self.df["CDLHARAMICROSS"] = tl.CDLHARAMICROSS(self.open, self.high, self.low, self.close)
        self.df["CDLHIGHWAVE"] = tl.CDLHIGHWAVE(self.open, self.high, self.low, self.close)
        self.df["CDLHIKKAKE"] = tl.CDLHIKKAKE(self.open, self.high, self.low, self.close)
        self.df["CDLHIKKAKEMOD"] = tl.CDLHIKKAKEMOD(self.open, self.high, self.low, self.close)
        self.df["CDLHOMINGPIGEON"] = tl.CDLHOMINGPIGEON(self.open, self.high, self.low, self.close)
        self.df["CDLIDENTICAL3CROWS"] = tl.CDLIDENTICAL3CROWS(self.open, self.high, self.low, self.close)
        self.df["CDLINNECK"] = tl.CDLINNECK(self.open, self.high, self.low, self.close)
        self.df["CDLINVERTEDHAMMER"] = tl.CDLINVERTEDHAMMER(self.open, self.high, self.low, self.close)
        self.df["CDLKICKING"] = tl.CDLKICKING(self.open, self.high, self.low, self.close)
        self.df["CDLKICKINGBYLENGTH"] = tl.CDLKICKINGBYLENGTH(self.open, self.high, self.low, self.close)
        self.df["CDLLADDERBOTTOM"] = tl.CDLLADDERBOTTOM(self.open, self.high, self.low, self.close)
        self.df["CDLLONGLEGGEDDOJI"] = tl.CDLLONGLEGGEDDOJI(self.open, self.high, self.low, self.close)
        self.df["CDLLONGLINE"] = tl.CDLLONGLINE(self.open, self.high, self.low, self.close)
        self.df["CDLMARUBOZU"] = tl.CDLMARUBOZU(self.open, self.high, self.low, self.close)
        self.df["CDLMATCHINGLOW"] = tl.CDLMATCHINGLOW(self.open, self.high, self.low, self.close)
        self.df["CDLMATHOLD"] = tl.CDLMATHOLD(self.open, self.high, self.low, self.close, penetration=0)
        self.df["CDLMORNINGDOJISTAR"] = tl.CDLMORNINGDOJISTAR(self.open, self.high, self.low, self.close, penetration=0)
        self.df["CDLMORNINGSTAR"] = tl.CDLMORNINGSTAR(self.open, self.high, self.low, self.close, penetration=0)
        self.df["CDLONNECK"] = tl.CDLONNECK(self.open, self.high, self.low, self.close)
        self.df["CDLPIERCING"] = tl.CDLPIERCING(self.open, self.high, self.low, self.close)
        self.df["CDLRICKSHAWMAN"] = tl.CDLRICKSHAWMAN(self.open, self.high, self.low, self.close)
        self.df["CDLRISEFALL3METHODS"] = tl.CDLRISEFALL3METHODS(self.open, self.high, self.low, self.close)
        self.df["CDLSEPARATINGLINES"] = tl.CDLSEPARATINGLINES(self.open, self.high, self.low, self.close)
        self.df["CDLSHOOTINGSTAR"] = tl.CDLSHOOTINGSTAR(self.open, self.high, self.low, self.close)
        self.df["CDLSHORTLINE"] = tl.CDLSHORTLINE(self.open, self.high, self.low, self.close)
        self.df["CDLSPINNINGTOP"] = tl.CDLSPINNINGTOP(self.open, self.high, self.low, self.close)
        self.df["CDLSTALLEDPATTERN"] = tl.CDLSTALLEDPATTERN(self.open, self.high, self.low, self.close)
        self.df["CDLSTICKSANDWICH"] = tl.CDLSTICKSANDWICH(self.open, self.high, self.low, self.close)
        self.df["CDLTAKURI"] = tl.CDLTAKURI(self.open, self.high, self.low, self.close)
        self.df["CDLTASUKIGAP"] = tl.CDLTASUKIGAP(self.open, self.high, self.low, self.close)
        self.df["CDLTHRUSTING"] = tl.CDLTHRUSTING(self.open, self.high, self.low, self.close)
        self.df["CDLTRISTAR"] = tl.CDLTRISTAR(self.open, self.high, self.low, self.close)
        self.df["CDLUNIQUE3RIVER"] = tl.CDLUNIQUE3RIVER(self.open, self.high, self.low, self.close)
        self.df["CDLUPSIDEGAP2CROWS"] = tl.CDLUPSIDEGAP2CROWS(self.open, self.high, self.low, self.close)
        self.df["CDLXSIDEGAP3METHODS"] = tl.CDLXSIDEGAP3METHODS(self.open, self.high, self.low, self.close)
        
        return self.df.fillna(0)


    def calculate_overlap_studies(self):
        """
        Calculates various overlap studies for the input data.

        Returns:
            pd.DataFrame: Dataframe with calculated overlap studies.

        This function calculates various overlap studies based on the provided periods.
        """
        for i in self.periods: 
            self.df["DEMA"+str(i)] = tl.DEMA(self.close, timeperiod=i)
            self.df["EMA"+str(i)] = tl.EMA(self.close, timeperiod=i)
            self.df["KAMA"+str(i)] = tl.KAMA(self.close, timeperiod=i)
            self.df["MIDPOINT"+str(i)] = tl.MIDPOINT(self.close, timeperiod=i)
            self.df["SMA"+str(i)] = tl.SMA(self.close, timeperiod=i)
            self.df["TRIMA"+str(i)] = tl.TRIMA(self.close, timeperiod=i)
            self.df["WMA"+str(i)] = tl.WMA(self.close, timeperiod=i)
            self.df["T3"+str(i)] = tl.T3(self.close, timeperiod=i, vfactor=0)
            self.df["TEMA"+str(i)] = tl.TEMA(self.close, timeperiod=i)
            self.df["MA"+str(i)] = tl.MA(self.close, timeperiod=i, matype=0)
        
        self.df["HT_TRENDLINE"+str(i)] = tl.HT_TRENDLINE(self.close)
    
        return self.df.fillna(0)

        
    def math_transform_functions(self):
        """
        Applies various mathematical transformation functions to the input data.

        Returns:
            pd.DataFrame: Dataframe with applied mathematical transformation functions.

        This function applies various mathematical transformation functions to the 'close' column.
        """
    
        self.df["ACOS"] = tl.ACOS(self.close)
        self.df["ASIN"] = tl.ASIN(self.close)
        self.df["ATAN"] = tl.ATAN(self.close)
        self.df["CEIL"] = tl.CEIL(self.close)
        self.df["COS"] = tl.COS(self.close)
        self.df["COSH"] = tl.COSH(self.close)
        self.df["EXP"] = tl.EXP(self.close)
        self.df["FLOOR"] = tl.FLOOR(self.close)
        self.df["LN"] = tl.LN(self.close)
        self.df["LOG10"] = tl.LOG10(self.close)
        self.df["SIN"] = tl.SIN(self.close)
        self.df["SINH"] = tl.SINH(self.close)
        self.df["SQRT"] = tl.SQRT(self.close)
        self.df["TAN"] = tl.TAN(self.close)
        self.df["TANH"] = tl.TANH(self.close)
    
        return self.df.fillna(0)


    def momentum_indicator_functions(self):
        """
        Applies various momentum indicator functions to the input data.

        Returns:
            pd.DataFrame: Dataframe with applied momentum indicator functions.

        This function applies various momentum indicator functions to the columns such as 'open', 'high', 'low', 'close', and 'real_volume'.
        """
    
        for i in self.periods:
            self.df["ADX" + str(i)] = tl.ADX(self.high, self.low, self.close, timeperiod=i)
            self.df["ADXR" + str(i)] = tl.ADXR(self.high, self.low, self.close, timeperiod=i)
            self.df["AROONOSC" + str(i)] = tl.AROONOSC(self.high, self.low, timeperiod=i)
            self.df["CCI" + str(i)] = tl.CCI(self.high, self.low, self.close, timeperiod=i)
            self.df["CMO" + str(i)] = tl.CMO(self.close, timeperiod=i)
            self.df["DX" + str(i)] = tl.DX(self.high, self.low, self.close, timeperiod=i)
            self.df["MFI" + str(i)] = tl.MFI(self.high, self.low, self.close, self.volume, timeperiod=i)
            self.df["MINUS_DI" + str(i)] = tl.MINUS_DI(self.high, self.low, self.close, timeperiod=i)
            self.df["MINUS_DM" + str(i)] = tl.MINUS_DM(self.high, self.low, timeperiod=i)
            self.df["MOM" + str(i)] = tl.MOM(self.close, timeperiod=i)
            self.df["PLUS_DI" + str(i)] = tl.PLUS_DI(self.high, self.low, self.close, timeperiod=i)
            self.df["PLUS_DM" + str(i)] = tl.PLUS_DM(self.high, self.low, timeperiod=i)
            self.df["ROC" + str(i)] = tl.ROC(self.close, timeperiod=i)
            self.df["ROCP" + str(i)] = tl.ROCP(self.close, timeperiod=i)
            self.df["ROCR" + str(i)] = tl.ROCR(self.close, timeperiod=i)
            self.df["ROCR100" + str(i)] = tl.ROCR100(self.close, timeperiod=i)
            self.df["RSI" + str(i)] = tl.RSI(self.close, timeperiod=i)
            self.df["WILLR" + str(i)] = tl.WILLR(self.high, self.low, self.close, timeperiod=i)
            self.df["TRIX" + str(i)] = tl.TRIX(self.close, timeperiod=i)
    
        self.df["APO"] = tl.APO(self.close, fastperiod=12, slowperiod=26, matype=0)
        self.df["PPO"] = tl.PPO(self.close, fastperiod=12, slowperiod=26, matype=0)
        self.df["real"] = tl.ULTOSC(self.high, self.low, self.close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
        self.df["real"] = tl.ULTOSC(self.high, self.low, self.close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    

    #     df["macd","macdsignal","macdhistdf"]  = tl.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    #     df["MACDEXT","MACDEXTsignal","MACDEXThist"]  = tl.MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
    #     df["MACDFIX","MACDFIXsignal","MACDFIXhist"] = tl.MACDFIX(close, signalperiod=9)
    #     df["STOCHRSIfastk","STOCHRSIfastd"] = tl.STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    #     df["STOCHslowk","STOCHslowd"] = tl.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    #     df["STOCHFfastk","STOCHFfastd"] = tl.STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
        
        return self.df.fillna(0)
     
    def statistic_functions(self):
        """
        Applies various statistical functions to the input data.

        Returns:
            pd.DataFrame: Dataframe with applied statistical functions.

        This function applies various statistical functions to the columns such as 'high', 'low', and 'close'.
        """
    
        for i in self.periods:
            self.df["BETA" + str(i)] = tl.BETA(self.high, self.low, timeperiod=i)
            self.df["CORREL" + str(i)] = tl.CORREL(self.high, self.low, timeperiod=i)
            self.df["LINEARREG" + str(i)] = tl.LINEARREG(self.close, timeperiod=i)
            self.df["LINEARREG_ANGLE" + str(i)] = tl.LINEARREG_ANGLE(self.close, timeperiod=i)
            self.df["LINEARREG_INTERCEPT" + str(i)] = tl.LINEARREG_INTERCEPT(self.close, timeperiod=i)
            self.df["LINEARREG_SLOPE" + str(i)] = tl.LINEARREG_SLOPE(self.close, timeperiod=i)
            self.df["STDDEV" + str(i)] = tl.STDDEV(self.close, timeperiod=i, nbdev=1)
            self.df["TSF" + str(i)] = tl.TSF(self.close, timeperiod=i)
            self.df["VAR" + str(i)] = tl.VAR(self.close, timeperiod=i, nbdev=1)
            self.df["median" + str(i)] = self.df["close"].rolling(window=i, min_periods=1).median()
            self.df["mode" + str(i)] = self.df["close"].rolling(window=i, min_periods=1).apply(lambda x: x.mode()[0])
            self.df["std" + str(i)] = self.df["median" + str(i)].rolling(window=i, min_periods=1).std()
    
        return self.df.fillna(0)

  
    def math_operator_functions(self):
        """
        Applies various mathematical operator functions to the input data.
    
        Returns:
            pd.DataFrame: Dataframe with applied mathematical operator functions.
    
        This function creates copies of the input data and applies various mathematical operator functions to the columns such as 'high', 'low', and 'close'.
        """
        
        
        for i in self.periods:
            self.df["MAX"+str(i)] = tl.MAX(self.close, timeperiod=i)
            self.df["MAXINDEX"+str(i)] = tl.MAXINDEX(self.close, timeperiod=i)
            self.df["MIN"+str(i)] = tl.MIN(self.close, timeperiod=i)
            self.df["MININDEX"+str(i)] = tl.MININDEX(self.close, timeperiod=i)
            self.df["SUM"+str(i)] = tl.SUM(self.close, timeperiod=i)
    
        # min, max = MINMAX(close, timeperiod=30)
        # minidx, maxidx = MINMAXINDEX(close, timeperiod=30)
    
        self.df["ADD"] = tl.ADD(self.high, self.low)
        self.df["DIV"] = tl.DIV(self.high, self.low)
        self.df["SUB"] = tl.SUB(self.high, self.low)
        
        return self.df.fillna(0)

    
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

def calculate_score(data, return_count=False):
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
    sell_counts = np.array([])
    buy_counts = np.array([])
    sell_price_changes = np.array([])
    buy_price_changes = np.array([])
    oll_sell_price_changes = np.array([])
    oll_buy_price_changes = np.array([])

    for i in range(len(df)):
        # Checking the conditions to determine buy and sell signals
        if df['Signal'].iloc[i] == 'sell':
            oll_sell_price_changes = np.append(oll_sell_price_changes, df["PriceChange"].iloc[i])
            if df['Close'].iloc[i] < df['Open'].iloc[i]:
                sell_price_changes = np.append(sell_price_changes, df["PriceChange"].iloc[i])
                sell_count += 1
                if buy_count > 0:
                    buy_counts = np.append(buy_counts, buy_count)
                    buy_price_changes = np.append(buy_price_changes, df["PriceChange"].iloc[i])
                    oll_buy_price_changes = np.append(oll_buy_price_changes, df["PriceChange"].iloc[i])
                    buy_count = 0
        elif df['Signal'].iloc[i] == 'buy':
            oll_buy_price_changes = np.append(oll_buy_price_changes, df["PriceChange"].iloc[i])
            if df['Close'].iloc[i] > df['Open'].iloc[i]:
                buy_price_changes = np.append(buy_price_changes, df["PriceChange"].iloc[i])
                buy_count += 1
                if sell_count > 0:
                    sell_counts = np.append(sell_counts, sell_count)
                    sell_price_changes = np.append(sell_price_changes, df["PriceChange"].iloc[i])
                    oll_sell_price_changes = np.append(oll_sell_price_changes, df["PriceChange"].iloc[i])
                    sell_count = 0

    # Handling the remaining values
    if sell_count > 0:
        sell_counts = np.append(sell_counts, sell_count)
        sell_price_changes = np.append(sell_price_changes, df["PriceChange"].iloc[i])
        oll_sell_price_changes = np.append(oll_sell_price_changes, df["PriceChange"].iloc[i])
        
    if buy_count > 0:
        buy_counts = np.append(buy_counts, buy_count)
        buy_price_changes = np.append(buy_price_changes, df["PriceChange"].iloc[i])
        oll_buy_price_changes = np.append(oll_buy_price_changes, df["PriceChange"].iloc[i])

    percentage_buy = (buy_price_changes.sum() / oll_buy_price_changes.sum()) * 100
    percentage_sell = (sell_price_changes.sum() / oll_sell_price_changes.sum()) * 100
    percentage = (percentage_sell + percentage_buy) / 2

    if return_count:
        return percentage_buy, percentage_sell

    return percentage

def optimize_parameters(data, analysis, windows_size, bias = [1]):
    """
    Optymalizuje parametry modelu na podstawie wyników analizy.

    Funkcja iteruje po zestawach parametrów określonych przez wielkość okna i przesunięcie (bias), 
    wywołuje funkcje define_level, rebound_analysis oraz calculate_score, aby obliczyć wyniki dla każdego zestawu parametrów 
    i zwraca zestaw parametrów, który osiąga najwyższy wynik.

    Argumenty:
    data (pd.DataFrame): Ramka danych wejściowych.
    windows_size (list): Lista zawierająca różne wartości dla wielkości okna.
    bias (list): Lista zawierająca różne wartości dla przesunięcia (bias).

    Zwraca:
    dict: Zestaw parametrów, który osiąga najwyższy wynik.

    Przykład użycia:
    >>> data = pd.DataFrame({'Close': [1, 2, 3, 4, 5], 'High': [2, 3, 4, 5, 6], 'Low': [0, 1, 2, 3, 4]})
    >>> windows_size = [5, 10, 15]
    >>> bias = [1, 2]
    >>> best_params = optimize_parameters(data, windows_size, bias)
    >>> print(best_params)
    {'window_size': 10, 'bias': 2}
    """
    best_score = 0
    best_params = None

    for window_size in t(windows_size):
        for b in bias:
            current_data = define_level(data, window_size, b)
            rebound_data = analysis(current_data)
            current_score = calculate_score(rebound_data)  

            if current_score > best_score:
                best_score = current_score
                best_params = {'window_size': window_size, 'bias': b}

    return best_params