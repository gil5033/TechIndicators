"""
Created on April 15th  2016

@author: pedroveronezi

"""
from Indicators import *
import pandas as pd
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorFACTORY(object):
    """
    This class is used to create instances of each Technical indicator required, it has only one method
    """

    def __init__(self, techind_list):
        """
        Constructor for the Factory class
        """
        if isinstance(techind_list, list):
            self.__techind_list = techind_list
        elif techind_list == 'default':
            self.__techind_list = ['HA_close',
                                   'EMA6',
                                   'EMA6',
                                   'Momentum',
                                   'ATR',
                                   'STOCHF5D5S3',
                                   'STOCHF9D3S5',
                                   'RSI12',
                                   'AccDist',
                                   'CCI7',
                                   'SAR02',
                                   'MACD',
                                   'BBANDS20',
                                   'TRIX14']
        elif techind_list == 'all':
            self.__techind_list = 'all'
        else:
            print "Invalid value for technical analysis to be calculated, should be 'default', 'all' or a dict object"
            raise TypeError

        self.__max_timeperiod = 0

        #creates the dict
        self.__available_techind = {'ACOS': (TechnicalIndicatorACOS()),
                                    'ADD': (TechnicalIndicatorADD()),
                                    'ADX': (TechnicalIndicatorADX()),
                                    'ADXR': (TechnicalIndicatorADXR()),
                                    'APO': (TechnicalIndicatorAPO()),
                                    'AROON': (TechnicalIndicatorAROON()),
                                    'AROONOSC': (TechnicalIndicatorAROONOSC()),
                                    'ATAN': (TechnicalIndicatorATAN()),
                                    'AVERAGEPRICE': TechnicalIndicatorAVERAGEPRICE(),
                                    'BBANDS': (TechnicalIndicatorBBANDS()),
                                    'BOP': (TechnicalIndicatorBOP()),
                                    'CCI': (TechnicalIndicatorCCI()),
                                    'CDL3BLACKCROW': (TechnicalIndicatorCDL3BLACKCROWS()),
                                    'CDL3INSIDE': (TechnicalIndicatorCDL3INSIDE()),
                                    'CDL3LINESTRIKE': (TechnicalIndicatorCDL3LINESTRIKE()),
                                    'CDL3OUTSIDE': (TechnicalIndicatorCDL3OUTSIDE()),
                                    'CDLCROWS': (TechnicalIndicatorCDLCROWS()),
                                    'CEIL': (TechnicalIndicatorCEIL()),
                                    'CMO': (TechnicalIndicatorCMO()),
                                    'COS': (TechnicalIndicatorCOS()),
                                    'COSH': (TechnicalIndicatorCOSH()),
                                    'DIV': (TechnicalIndicatorDIV()),
                                    'DX': (TechnicalIndicatorDX()),
                                    'EMA': (TechnicalIndicatorEMA()),
                                    'EXP': (TechnicalIndicatorEXP()),
                                    'FLOOR': (TechnicalIndicatorFLOOR()),
                                    'HTDCPERIOD': (TechnicalIndicatorHTDCPERIOD()),
                                    'HTDCPHASE': (TechnicalIndicatorHTDCPHASE()),
                                    'HTPHASOR': (TechnicalIndicatorHTPHASOR()),
                                    'HTSINE': (TechnicalIndicatorHTSINE()),
                                    'HTTRENDLINE': (TechnicalIndicatorHTTRENDLINE()),
                                    'HTTRENDMODE': (TechnicalIndicatorHTTRENDMODE()),
                                    'KAMA': (TechnicalIndicatorKAMA()),
                                    'MA': (TechnicalIndicatorMA()),
                                    'MACD': (TechnicalIndicatorMACD()),
                                    'MACDEXT': (TechnicalIndicatorMACDEXT()),
                                    'MACDFIX': (TechnicalIndicatorMACDFIX()),
                                    'MAX': (TechnicalIndicatorMAX()),
                                    'MAXINDEX': (TechnicalIndicatorMAXINDEX()),
                                    'MFI': (TechnicalIndicatorMFI()),
                                    'MIDPOINT': (TechnicalIndicatorMIDPOINT()),
                                    'MIDPRICE': (TechnicalIndicatorMIDPRICE()),
                                    'MININDEX': (TechnicalIndicatorMININDEX()),
                                    'MINMAX': (TechnicalIndicatorMINMAX()),
                                    'MINUSDI': (TechnicalIndicatorMINUSDI()),
                                    'MINUSDM': (TechnicalIndicatorMINUSDM()),
                                    'MOM': (TechnicalIndicatorMOM()),
                                    'MULTI': (TechnicalIndicatorMULTI()),
                                    'PLUSDI': (TechnicalIndicatorPLUSDI()),
                                    'PLUSDM': (TechnicalIndicatorPLUSDM()),
                                    'PPO': (TechnicalIndicatorPPO()),
                                    'ROC': (TechnicalIndicatorROC()),
                                    'ROC100': (TechnicalIndicatorROC100()),
                                    'ROCR': (TechnicalIndicatorROCR()),
                                    'ROCP': TechnicalIndicatorROCP(),
                                    'RSI': (TechnicalIndicatorRSI()),
                                    'SAR': (TechnicalIndicatorSAR()),
                                    'SIN': (TechnicalIndicatorSIN()),
                                    'SINH': (TechnicalIndicatorSINH()),
                                    'SMA': (TechnicalIndicatorSMA()),
                                    'SQRT': (TechnicalIndicatorSQRT()),
                                    'STOCH': (TechnicalIndicatorSTOCH()),
                                    'STOCHF': (TechnicalIndicatorSTOCHF()),
                                    'SUB': TechnicalIndicatorSUB(),
                                    'SUM': TechnicalIndicatorSUM(),
                                    'T3': TechnicalIndicatorT3(),
                                    'TAN': TechnicalIndicatorTAN(),
                                    'TANH': TechnicalIndicatorTANH(),
                                    'TEMA': TechnicalIndicatorTEMA(),
                                    'TRIMA': TechnicalIndicatorTRIMA(),
                                    'TRIX': TechnicalIndicatorTRIX(),
                                    'ULTOSC': TechnicalIndicatorULTOSC(),
                                    'WILLR': TechnicalIndicatorWILLR(),
                                    'WMA': TechnicalIndicatorWMA(),
                                    'MA6': (TechnicalIndicatorMA(timeperiod=6)),
                                    'MA20': (TechnicalIndicatorMA(timeperiod=20)),
                                    'HA_close': (TechnicalIndicatorHEIKENASHICLOSE()),
                                    'HA_low': (TechnicalIndicatorHEIKENASHILOW()),
                                    'HA_high': (TechnicalIndicatorHEIKENASHIHIGH()),
                                    'HA_open': (TechnicalIndicatorHEIKENASHIOPEN()),
                                    'EMA6': (TechnicalIndicatorEMA(timeperiod=6)),
                                    'EMA20': (TechnicalIndicatorEMA(timeperiod=20)),
                                    'Momentum': (TechnicalIndicatorMOM(timeperiod=7)),
                                    'ATR': (TechnicalIndicatorATR()),
                                    'RSI12': (TechnicalIndicatorRSI(timeperiod=12)),
                                    'AccDist': (TechnicalIndicatorACUMULATIONDISTRIBUTION()),
                                    'CCI7': (TechnicalIndicatorCCI(timeperiod=7)),
                                    'SAR02': (TechnicalIndicatorSAR(acceleration=0.2, maximum=0.2)),
                                    'BBANDS20': (TechnicalIndicatorBBANDS(timeperiod=20)),
                                    'TRIX14': (TechnicalIndicatorTRIX(timeperiod=14)),
                                    'STOCHF5D5S3': (TechnicalIndicatorSTOCH(fastk_period=5, slowk_period=3,
                                                                            slowd_period=3)),
                                    'STOCHF9D3S5': (TechnicalIndicatorSTOCH(fastk_period=9, slowk_period=5,
                                                                            slowd_period=3))}

        # Store the list of instances
        self.__list_instances = []

        # Creates the instances
        self.__create_instances_technical_indicators()

        # Creates a variable to store the columns which had the name changed
        self._columns_to_replace = self.__list_instances[0].get_columns_to_replace()

    def __create_instances_technical_indicators(self):
        """
        This method creates all instances necessaries for the calculations. It receives a dict python object and for
        each entry creates a respective instance
        Returns:
            Returns a dict with the called name, and the instance of the technical indicator
        """

        if self.__techind_list == 'all':
            self.__techind_list = self.__available_techind.keys()

        for i in self.__techind_list:
            # Iterates to get the correct instance for the Technical indicator to be calculated
            self.__list_instances.append(self.__available_techind[i])

        return self

    def get_max_timeperiod(self):
        """

        Returns:

        """
        for ti in self.__list_instances:
            self.__max_timeperiod = int(max(self.__max_timeperiod, ti.get_max_periodNaN()))

        return int(self.__max_timeperiod)

    def get_list_techind(self):
        """
        Getter for the dict with all instances and its attributes
        Returns:

        """
        return self.__list_instances

    def get_list_columns_name(self):
        """
        Getter for the list of char representing the columns name
        Returns:

        """
        return self.__techind_list

    def calc_TechIndicators(self, training_data):
        """
        This function is responsible to calculate the technical indicators
        Returns:

        """

        list_instances = self.get_list_techind()

        training_data_techind = pd.DataFrame()

        # sets teh counter to 0
        ite = 0

        # Loops through the instances to calculate the indicators
        for ti in list_instances:
            if self.__techind_list[ite] not in training_data.columns:
                print self.__techind_list[ite]
                training_data_techind = concat([training_data_techind, ti.calc_indicator(training_data)], axis=1,
                                               ignore_index=True)
                print len(training_data_techind.index)
            # Sums 1 to the iteratorS
            ite += 1

        # Deletes the iterator
        del ite

        tech_ind_results = DataFrame(index=training_data.index, columns=training_data_techind.columns, data=training_data_techind.values)

        # Concatenates the training_data with the technical indicators
        output = concat([training_data, tech_ind_results], axis=1)

        # Delete teh training_techind
        del training_data_techind

        # Renames the columns to go back to default values
        for col in output.columns:
            if len(self._columns_to_replace) > 0:
                if len(self._columns_to_replace['LONG_Close']) > 0:
                    if "close" in str(col):
                        output.rename(index=str, columns={col: self._columns_to_replace['LONG_Close']}, inplace=True)
                    elif "open" in str(col):
                        output.rename(index=str, columns={col: self._columns_to_replace['LONG_Open']}, inplace=True)
                    elif "high" in str(col):
                        output.rename(index=str, columns={col: self._columns_to_replace['LONG_High']}, inplace=True)
                    elif "low" in str(col):
                        output.rename(index=str, columns={col: self._columns_to_replace['LONG_Low']}, inplace=True)
                    elif "volume" in str(col):
                        output.rename(index=str, columns={col: self._columns_to_replace['LONG_Volume']}, inplace=True)
                else:
                    # Renames the columns to calculate the indicators
                    output.rename(index=str, columns={"close": "Close", "open": "Open", "high": "High", "low": "Low",
                                                           "volume": "Volume"}, inplace=True)
            else:
                # Renames the columns to calculate the indicators
                output.rename(index=str, columns={"close": "Close", "open": "Open", "high": "High", "low": "Low",
                                                  "volume": "Volume"}, inplace=True)

        # Cleaning the NA columns (dropping columsn that oinly contain NA values)
        output.dropna(axis=1, how='all', inplace=True)

        # Drops the first max_number of rows that were just support for the calculations and return a DataFrame
        return output.tail(len(output.index) - self.get_max_timeperiod())
