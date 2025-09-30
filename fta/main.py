# To access Tulip indicators w/default values
# Only one of these may be necessary

from .pantulipy import *
from .pantulipy import _DEFAULTLESS_INDICATORS

import pandas_ta as ta

import pandas as pd


def GetDayOfWeek(datetimes,
                 dataframe=None):
    """
        Convert DateTime Objects to Day of Week
        Inputting a DataFrame will append the new data column

        Example:
            # Return a pd.Series with datetime index
            series = GetDayOfWeek(datetimes)

            # Return your dataframe
            # with the new data column appended
            dataframe = GetDayOfWeek(
                datetimes = dataframe.index,
                dataframe = dataframe
            )
    """

    def _get_day_of_week(date):
        """Converts 0-6 to a day string"""
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[date.weekday()]

    # Convert datetimes to int 0-6 then to a day string
    days_of_week = pd.Series(datetimes,
                             index=datetimes
                             ).apply(_get_day_of_week)
    # Attach day strings
    if dataframe is not None:
        dataframe = dataframe.assign(day_of_week=days_of_week)
        return dataframe

    return days_of_week


class TA_Features:
    """
        Get 144 Unique Indicator Values based on a DataFrame,
        with columns: 'open' 'high' 'low' 'close' 'volume'.
        Using Tulip indicators and Pandas_TA Indicators.
    """

    unique_pandas_ta_indicators = {
        'accbands': ta.accbands, 'amat': ta.amat, 'aobv': ta.aobv,
        'cg': ta.cg, 'coppock': ta.coppock, 'decreasing': ta.decreasing,
        'donchian': ta.donchian, 'efi': ta.efi, 'eom': ta.eom, 'fwma': ta.fwma,
        'increasing': ta.increasing, 'kc': ta.kc,
        'kst': ta.kst, 'kurtosis': ta.kurtosis, 'linear_decay': ta.decay,
        'log_return': ta.log_return, 'mad': ta.mad, 'median': ta.median,
        'midpoint': ta.midpoint, 'midprice': ta.midprice,
        'percent_return': ta.percent_return, 'pvol': ta.pvol, 'pvt': ta.pvt,
        'pwma': ta.pwma, 'quantile': ta.quantile, 'rma': ta.rma, 'rvi': ta.rvi,
        'sinwma': ta.sinwma, 'skew': ta.skew, 'slope': ta.slope, 'swma': ta.swma,
        't3': ta.t3, 'tsi': ta.tsi, 'uo': ta.uo, 'variance': ta.variance,
        'vortex': ta.vortex, 'zscore': ta.zscore
    }
    pandas_ta_indicators = {
        'accbands': ta.accbands, 'ad': ta.ad, 'adosc': ta.adosc, 'adx': ta.adx,
        'amat': ta.amat, 'ao': ta.ao, 'aobv': ta.aobv, 'apo': ta.apo,
        'aroon': ta.aroon, 'atr': ta.atr, 'bbands': ta.bbands, 'bop': ta.bop,
        'cci': ta.cci, 'cg': ta.cg, 'cmo': ta.cmo,
        'coppock': ta.coppock, 'decreasing': ta.decreasing, 'dema': ta.dema,
        'donchian': ta.donchian, 'dpo': ta.dpo, 'efi': ta.efi, 'ema': ta.ema,
        'eom': ta.eom, 'fisher': ta.fisher, 'fwma': ta.fwma, 'hma': ta.hma,
        'increasing': ta.increasing, 'kama': ta.kama,
        'kc': ta.kc, 'kst': ta.kst, 'kurtosis': ta.kurtosis,
        'log_return': ta.log_return, 'mad': ta.mad, 'massi': ta.massi, 'median': ta.median,
        'midpoint': ta.midpoint, 'midprice': ta.midprice,
        'mom': ta.mom, 'natr': ta.natr, 'obv': ta.obv, 'ppo': ta.ppo,
        'pvol': ta.pvol, 'pvt': ta.pvt, 'pwma': ta.pwma, 'qstick': ta.qstick,
        'quantile': ta.quantile, 'rma': ta.rma, 'roc': ta.roc, 'rsi': ta.rsi,
        'rvi': ta.rvi, 'sinwma': ta.sinwma, 'skew': ta.skew, 'slope': ta.slope,
        'sma': ta.sma, 'stdev': ta.stdev, 'swma': ta.swma,
        't3': ta.t3, 'tema': ta.tema, 'trima': ta.trima, 'trix': ta.trix,
        'true_range': ta.true_range, 'tsi': ta.tsi, 'uo': ta.uo,
        'variance': ta.variance, 'vortex': ta.vortex,
        'vwma': ta.vwma, 'willr': ta.willr, 'wma': ta.wma,
        'zlma': ta.zlma, 'zscore': ta.zscore
    }
    unique_pantulipy_indicators = {
        'adxr': adxr, 'aroonosc': aroonosc, 'avgprice': avgprice,
        'cvi': cvi, 'decay': decay, 'di': di, 'dm': dm, 'dx': dx,
        'edecay': edecay, 'emv': emv, 'fosc': fosc, 'kvo': kvo,
        'lag': lag, 'linreg': linreg, 'linregintercept': linregintercept,
        'linregslope': linregslope, 'marketfi': marketfi,
        'md': md, 'msw': msw, 'psar': psar, 'rocr': rocr, 'stderr': stderr,
        'tr': tr, 'tsf': tsf, 'typprice': typprice, 'vhf': vhf,
        'vidya': vidya, 'volatility': volatility,  'wad': wad,
        'wcprice': wcprice
    }
    pantulipy_indicators = {
        'ad': ad, 'adosc': adosc, 'adx': adx, 'adxr': adxr, 'ao': ao,
        'apo': apo, 'aroon': aroon, 'aroonosc': aroonosc, 'atr': atr,
        'avgprice': avgprice, 'bbands': bbands, 'bop': bop, 'cci': cci,
        'cmo': cmo, 'cvi': cvi, 'decay': decay, 'dema': dema, 'di': di,
        'dm': dm, 'dpo': dpo, 'dx': dx, 'edecay': edecay, 'ema': ema,
        'emv': emv, 'fisher': fisher, 'fosc': fosc, 'hma': hma,
        'kama': kama, 'kvo': kvo, 'lag': lag, 'linreg': linreg,
        'linregintercept': linregintercept, 'linregslope': linregslope,
        'macd': macd, 'marketfi': marketfi, 'mass': mass, 'md': md,
        'mfi': mfi, 'mom': mom, 'msw': msw, 'natr': natr, 'nvi': nvi,
        'obv': obv, 'ppo': ppo, 'psar': psar, 'pvi': pvi, 'qstick': qstick,
        'roc': roc, 'rocr': rocr, 'rsi': rsi, 'sma': sma, 'stderr': stderr,
        'stoch': stoch, 'tema': tema, 'tr': tr, 'trima': trima, 'trix': trix,
        'tsf': tsf, 'typprice': typprice, 'ultosc': ultosc, 'vhf': vhf,
        'vidya': vidya, 'volatility': volatility, 'vwma': vwma,
        'wad': wad, 'wcprice': wcprice, 'wilders': wilders, 'willr': willr,
        'wma': wma, 'zlema': zlema
    }

    def _remove_duplicate_columns(self, df: pd.DataFrame):
        """Rename all duplicate columns appending _2 or _3 or _4 etc"""
        cols = pd.Series(df.columns)
        for dup in cols[cols.duplicated()].unique():
            cols[cols[cols == dup].index.values.tolist()] = [dup + '_' + str(i + 1) if i != 0 else dup for i in
                                                             range(sum(cols == dup))]
        df.columns = cols  # Rename columns
        return df

    def _append_column(cls, orig, new):
        if isinstance(new, pd.DataFrame):
            new.columns = [c.lower() for c in new.columns]
            orig = pd.concat([orig, new], axis=1)
        else:
            orig = pd.concat([orig, new.rename(new.name.lower()).to_frame()], axis=1)
        return orig

    def get_all_pandas_ta_indicators(self, data=None, unique=False, **kwargs):
        """
            Get all Pandas_TA indicators
            :param: data - DataFrame with columns: 'open' 'high' 'low' 'close' 'volume'
            :param: unique - True would exclude all indicators that Tulip also has
        """
        data.columns = map(str.lower, data.columns)
        data['open'] = pd.to_numeric(data['open'], errors='coerce')
        data['high'] = pd.to_numeric(data['high'], errors='coerce')
        data['low'] = pd.to_numeric(data['low'], errors='coerce')
        data['close'] = pd.to_numeric(data['close'], errors='coerce')
        data['volume'] = pd.to_numeric(data['volume'], errors='coerce')
        open_ = data['open']
        high = data['high']
        low = data['low']
        close = data['close']
        volume = data['volume']

        ind = self.unique_pandas_ta_indicators if unique else self.pandas_ta_indicators

        for name, function in ind.items():
            if name == 'massi':  # Can't handle being sent a close= kwarg
                indicator_data = function(high=high,
                                          low=low)
            else:
                indicator_data = function(open_=open_,
                                          high=high,
                                          low=low,
                                          close=close,
                                          volume=volume)
            if type(indicator_data) == tuple:  # tuple of dataframes
                for i in range(0, len(indicator_data)):
                    data = self._append_column(data, indicator_data.iloc[i])
            else:
                data = self._append_column(data, indicator_data)
        return self._remove_duplicate_columns(data)

    def get_all_pantulipy_indicators(self, data=None, unique=False, **kwargs):
        """
            Get all Tulip Indicators
            :param: data - DataFrame with columns: 'open' 'high' 'low' 'close' 'volume'
            :param: unique - True would exclude all indicators that Pandas_TA has also
        """
        data.columns = map(str.lower, data.columns)
        data['open'] = pd.to_numeric(data['open'], errors='coerce')
        data['high'] = pd.to_numeric(data['high'], errors='coerce')
        data['low'] = pd.to_numeric(data['low'], errors='coerce')
        data['close'] = pd.to_numeric(data['close'], errors='coerce')
        data['volume'] = pd.to_numeric(data['volume'], errors='coerce')
        ind = self.unique_pantulipy_indicators if unique else self.pantulipy_indicators
        for name, function in ind.items():
            if name not in _DEFAULTLESS_INDICATORS:
                data = pd.concat([data, function(data)], axis=1)
        return self._remove_duplicate_columns(data)

    def get_all_indicators(self, data=None, **kwargs):
        """
            Get all Tulipy and Pandas_TA indicators
            :param: data = DataFrame with columns: 'open' 'high' 'low' 'close' 'volume'
        """
        if len(data) > 500:
            data.columns = map(str.lower, data.columns)
            data = self.get_all_pandas_ta_indicators(data, unique=True)
            data = self.get_all_pantulipy_indicators(data, unique=False)
        else:
            print("Num of data should larger then 500.")
        return data
