from TechIndicator import TechnicalIndicator
from abc import abstractmethod
from abc import ABCMeta
from talib import abstract
from talib.abstract import *
from pandas import concat
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorHEIKENASHICLOSE(TechnicalIndicator):
    """
    Calculates the Heiken-Ashi tehcnical indicator for the candle stick
    Ref: http://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:heikin_ashi
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHEIKENASHICLOSE, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        CAlcualtes the Heiken_ashi tech Indicator
        Args:
            OHLCV_input: DataFrame with Open, High, Low, CLose and Volume

        Returns:

        """
        output = (OHLCV_input['open'] + OHLCV_input['high'] + OHLCV_input['low'] + OHLCV_input['close']) / float(4)
        output = DataFrame(index=range(0, len(OHLCV_input.index), 1), columns=['HA_Close'], data=output.values)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod


class TechnicalIndicatorHEIKENASHIOPEN(TechnicalIndicator):
    """
    Calculates the Heiken-Ashi tehcnical indicator for the candle stick
    Ref: http://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:heikin_ashi
    """

    def __init__(self, timeperiod=1):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHEIKENASHIOPEN, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        CAlcualtes the Heiken_ashi tech Indicator
        Args:
            OHLCV_input: DataFrame with Open, High, Low, CLose and Volume

        Returns:

        """
        output = (OHLCV_input.open.shift(self.__timeperiod) + OHLCV_input.close.shift(self.__timeperiod)) / float(2)
        output = DataFrame(index=range(0, len(OHLCV_input.index), 1), columns=['HA_Open'], data=output.values)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod


class TechnicalIndicatorHEIKENASHIHIGH(TechnicalIndicator):
    """
    Calculates the Heiken-Ashi tehcnical indicator for the candle stick
    Ref: http://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:heikin_ashi
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHEIKENASHIHIGH, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        CAlcualtes the Heiken_ashi tech Indicator
        Args:
            OHLCV_input: DataFrame with Open, High, Low, CLose and Volume

        Returns:

        """
        output = OHLCV_input[['high', 'open', 'close']].max(axis=1)
        output = DataFrame(index=range(0, len(OHLCV_input.index), 1), columns=['HA_High'], data=output.values)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod


class TechnicalIndicatorHEIKENASHILOW(TechnicalIndicator):
    """
    Calculates the Heiken-Ashi tehcnical indicator for the candle stick
    Ref: http://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:heikin_ashi
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHEIKENASHILOW, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        CAlcualtes the Heiken_ashi tech Indicator
        Args:
            OHLCV_input: DataFrame with Open, High, Low, CLose and Volume

        Returns:

        """
        output = OHLCV_input[['high', 'open', 'close']].min(axis=1)
        output = DataFrame(index=range(0, len(OHLCV_input.index), 1), columns=['HA_Low'], data=output.values)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod


class TechnicalIndicatorACUMULATIONDISTRIBUTION(TechnicalIndicator):
    """
    Calculates the Accumulation distribution indicator for the candle stick
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorACUMULATIONDISTRIBUTION, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        CAlcualtes the Acumulation / Distribution tech Indicator
        Ref: http://www.investopedia.com/terms/a/accumulationdistribution.asp
        Args:
            OHLCV_input: DataFrame with Open, High, Low, CLose and Volume

        Returns:

        """
        output = ((OHLCV_input['close'] - OHLCV_input['low']) - (OHLCV_input['high'] - OHLCV_input['close'])) / \
                 (OHLCV_input['high'] - OHLCV_input['low']) * OHLCV_input['volume']
        output = DataFrame(index=range(0, len(OHLCV_input.index), 1), columns=['AccDist'], data=output.values)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod