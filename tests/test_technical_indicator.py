"""
Created on May 2 th 2016

@author: pveroneziesa

"""
import numpy as np
import pandas as pd
from Indicators import *
from TechIndFACTORY import TechnicalIndicatorFACTORY
__author__ = 'Pedro Henrique Veronezi e Sa'


class InterfaceRequirements(object):
    """

    """
    # Initializing parameters
    n_observation = 300
    OHLCV_df = pd.DataFrame(np.random.randn(n_observation, 5), columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    factory_instance = None
    max_timeperiod = 0
    list_talib = []
    n_cols_talib = len(list_talib)

    def test_calc_len(self):
        """
        This method aims to test the length of the results calculated by the ta-lib indicators
        Returns:

        """
        output_df = self.factory_instance.calc_TechIndicators(self.OHLCV_df)
        self.max_timeperiod = self.factory_instance.get_max_timeperiod()

        assert len(output_df.index) == (self.n_observation - self.max_timeperiod)

    def test_calc_type(self):
        """
        This method test the type for the ta-lib wrappers
        Returns:

        """
        output_df = self.factory_instance.calc_TechIndicators(self.OHLCV_df)
        assert isinstance(output_df, pd.DataFrame)

    def test_navalues(self):
        """
        Check if there is any NaN values in the output
        Returns:

        """
        output_df = self.factory_instance.calc_TechIndicators(self.OHLCV_df)
        assert output_df.notnull().values.any() == True


class TestTALIB(InterfaceRequirements):
    """
    Test for the whole TALIB at once
    """
    def setup_method(self, method):
        self.list_talib = ['ACOS',
                           'ADD',
                           'ADX',
                           'ADXR',
                           'APO',
                           'AROON',
                           'AROONOSC',
                           'ATAN',
                           'AVERAGEPRICE',
                           'BBANDS',
                           'BOP',
                           'CCI',
                           'CDL3BLACKCROW',
                           'CDL3INSIDE',
                           'CDL3LINESTRIKE',
                           'CDL3OUTSIDE',
                           'CDLCROWS',
                           'CEIL',
                           'CMO',
                           'COS',
                           'COSH',
                           'DEMA',
                           'DIV',
                           'DX',
                           'EMA',
                           'EXP',
                           'FLOOR',
                           'HTDCPERIOD',
                           'HTDCPHASE',
                           'HTPHASOR',
                           'HTSINE',
                           'HTTRENDLINE',
                           'HTTRENDMODE',
                           'KAMA',
                           'MA',
                           'MACD',
                           'MACDEXT',
                           'MACDFIX',
                           'MAX',
                           'MAXINDEX',
                           'MFI',
                           'MIDPOINT',
                           'MIDPRICE',
                           'MIN',
                           'MININDEX',
                           'MINMAX',
                           'MINUSDI',
                           'MINUSDM',
                           'MOM',
                           'MULTI',
                           'PLUSDI',
                           'PLUSDM',
                           'PPO',
                           'ROC',
                           'ROC100',
                           'ROCP',
                           'ROCR',
                           'RSI',
                           'SAR',
                           'SIN',
                           'SINH',
                           'SMA',
                           'SQRT',
                           'STOCH',
                           'STOCHF',
                           'SUB',
                           'SUM',
                           'T3',
                           'TAN',
                           'TEMA',
                           'TRIMA',
                           'TRIX',
                           'ULTOSC',
                           'WILLR',
                           'WMA']

        self.factory_instance = TechnicalIndicatorFACTORY(self.list_talib)


class TestHAclose(InterfaceRequirements):
    """
    Tests for HEIKENASHICLOSE techinical indicator
    """
    def setup_method(self, method):
        self.list_talib = ['HA_close']
        self.factory_instance = TechnicalIndicatorFACTORY(self.list_talib)


class TestHAopen(InterfaceRequirements):
    """
    Tests for HEIKENASHIOPEN techinical indicator
    """
    def setup_method(self, method):
        self.list_talib = ['HA_open']
        self.factory_instance = TechnicalIndicatorFACTORY(self.list_talib)


class TestHAhigh(InterfaceRequirements):
    """
    Tests for HEIKENASHIHIGH techinical indicator
    """
    def setup_method(self, method):
        self.list_talib = ['HA_high']
        self.factory_instance = TechnicalIndicatorFACTORY(self.list_talib)


class TestHAlow(InterfaceRequirements):
    """
    Tests for HEIKENASHIHIGH techinical indicator
    """
    def setup_method(self, method):
        self.list_talib = ['HA_low']
        self.factory_instance = TechnicalIndicatorFACTORY(self.list_talib)


class TestACCUMDIST(InterfaceRequirements):
    def setup_method(self, method):
        self.list_talib = ['AccDist']
        self.factory_instance = TechnicalIndicatorFACTORY(self.list_talib)
