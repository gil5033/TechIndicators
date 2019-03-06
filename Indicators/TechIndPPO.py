from Indicators.TechIndicator import TechnicalIndicator
from talib import PPO
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorPPO(TechnicalIndicator):
    """
    Wrapper for the Percentage Price Oscillator Rating from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/PPO.htm
    """

    def __init__(self, fastperiod=12, slowperiod=26, matype=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorPPO, self).__init__()
        self.__fastperiod = fastperiod
        self.__slowperiod = slowperiod
        self.__matype = matype

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Percentage Price Oscillator technical indicator using a wrapper for the TA-lib

        Args:
            :param OHLCV_input:  the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas DataFrame

        Returns:
            DataFrame with the indicators values.
        """
        try:
            close = OHLCV_input['close'].values[:, 0]
        except IndexError:
            close = OHLCV_input['close'].values

        output = DataFrame(PPO(close, self.__fastperiod, self.__slowperiod, self.__matype))
        output.columns = ['PPO%d' % self.__slowperiod]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__fastperiod, self.__slowperiod, self.__matype))
