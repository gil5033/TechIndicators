"""
Created on April 13th  2016

@author: pedroveronezi

"""
from abc import abstractmethod
from abc import ABCMeta
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicator(object):
    """
    TechnicalIndicator is a base class to wrap algorithms that calculates different technical indicators for the data

    Methods:


    Abstract Methods:

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Constructor of the TechnicalIndicator interface.

        Returns:
            self
        """
        self._calculated = False
        self._max_periodNaN = 0
        self._columns_to_replace = {}

    def calc_indicator(self, OHLCV_input):
        """
        calculates the indicator
        Args:
            :param OHLCV_input: the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas Dataframe

        Returns:

        """
        # classify the instance as calculated
        self._calculated = True

        # Transform the input data into Pandas DataFrame, if it is already, nothings is done
        if isinstance(OHLCV_input, DataFrame) is not True:
            OHLCV_input = DataFrame(OHLCV_input)

        # Checks each columns in the dataframe to guarantee that is according to the TA-LIB package
        for col in OHLCV_input.columns:
            if "LONG_Close" in col:
                self._columns_to_replace['LONG_Close'] = col
                OHLCV_input.rename(index=str, columns={col: "close"}, inplace=True)
            elif "LONG_Open" in col:
                self._columns_to_replace['LONG_Open'] = col
                OHLCV_input.rename(index=str, columns={col: "open"}, inplace=True)
            elif "LONG_High" in col:
                self._columns_to_replace['LONG_High'] = col
                OHLCV_input.rename(index=str, columns={col: "high"}, inplace=True)
            elif "LONG_Low" in col:
                self._columns_to_replace['LONG_Low'] = col
                OHLCV_input.rename(index=str, columns={col: "low"}, inplace=True)
            elif "LONG_Volume" in col:
                self._columns_to_replace['LONG_Volume'] = col
                OHLCV_input.rename(index=str, columns={col: "volume"}, inplace=True)
            elif "LONG_TickVolume" in col:
                self._columns_to_replace['LONG_Volume'] = col
                OHLCV_input.rename(index=str, columns={col: "volume"}, inplace=True)
            else:
                # Renames the columns to calculate the indicators
                OHLCV_input.rename(index=str, columns={"Close": "close", "Open": "open", "High": "high", "Low": "low",
                                                       "TickVolume": "volume", "Volume": "volume"}, inplace=True)

        # Transform the input data into Pandas DataFrame, if it is already, nothings is done
        if isinstance(OHLCV_input, DataFrame) is not True:
            OHLCV_input = DataFrame(OHLCV_input)

        # Drops the duplicated columns, leaving only the first one
        reviewed_df = OHLCV_input.T.drop_duplicates(keep='first').T

        # Changes the data type to float for the columns colume
        reviewed_df[['volume']] = reviewed_df[['volume']].astype('float')

        return self._calc_indicator(reviewed_df)

    @abstractmethod
    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the technical indicator using a wrapper for the TA-lib

        Args:
            :param OHLCV_input:  the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas DataFrame

        Returns:
            DataFrame with the Indicator values.
        """
        raise NotImplementedError("Should implement calc_indicator()")

    def get_max_periodNaN(self):
        """
        Function to get the number od bars to be gathered in order to guarantee that the nbars for training is being
        respected
        Returns:

        """
        return self._get_max_periodNaN()

    @abstractmethod
    def _get_max_periodNaN(self):
        """
        Calculates the number of bars to be gathered in addition in order to guarantee the nbars for training is being
        respected
        Returns:

        """
        raise NotImplementedError("Should implement calc_indicator()")

    def get_columns_to_replace(self):
        return self._columns_to_replace
