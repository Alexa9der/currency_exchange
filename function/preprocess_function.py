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

if __name__ == "__main__":
    preprocessor = Preprocessing_stock_data(data)
    all_data = preprocessor.all_methods()