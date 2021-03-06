from Indicators.TechIndicator import TechnicalIndicator
from talib import ROCR100
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorROC100(TechnicalIndicator):
    """
    Wrapper for the Rate of change ratio 100 scale: (price/prevPrice)*100 Rating from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/ROC.htm
    """

    def __init__(self, timeperiod=10):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorROC100, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Rate of change ratio 100 scale: (price/prevPrice)*100 technical indicator using a wrapper for the TA-lib

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

        output = DataFrame(ROCR100(close, self.__timeperiod))
        output.columns = ['ROC100%d' % self.__timeperiod]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
