from Indicators.TechIndicator import TechnicalIndicator
from talib import SAREXT
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorSAREXT(TechnicalIndicator):
    """
    Wrapper for the SAR - Parabolic SAR Extended period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/SAR.htm
    """

    def __init__(self, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0,
                 accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorSAREXT, self).__init__()
        self.__starvalue = startvalue
        self.__offsetonreverse = offsetonreverse
        self.__accelerationinilong = accelerationinitlong
        self.__accelerationlong = accelerationlong
        self.__accelerationmaxlong = accelerationmaxlong
        self.__accelerationinitshort = accelerationinitshort
        self.__accelerationshort = accelerationshort
        self.__accelerationmaxshort = accelerationmaxshort

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the SAR - Parabolic SAR Extended technical indicator using a wrapper for the TA-lib

        Args:
            :param OHLCV_input:  the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas DataFrame

        Returns:
            DataFrame with the indicators values.
        """
        try:
            high = OHLCV_input['high'].values[:, 0]
        except IndexError:
            high = OHLCV_input['high'].values

        try:
            low = OHLCV_input['low'].values[:, 0]
        except IndexError:
            low = OHLCV_input['low'].values

        output = DataFrame(SAREXT(high, low, self.__startvalue, self.__offsetonreverse,
                                  self.__accelerationinitlong, self.__accelerationlong,
                                  self.__accelerationmaxlong, self.__accelerationinitshort,
                                  self.__accelerationshort, self.__accelerationmaxshort))
        output.columns = ['SAREXT%d' % self.__starvalue]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__startvalue, self.__offsetonreverse, self.__accelerationinitlong, self.__accelerationlong,
                       self.__accelerationmaxlong, self.__accelerationinitshort, self.__accelerationshort,
                       self.__accelerationmaxshort))
