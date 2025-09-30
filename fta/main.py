# To access Tulip indicators w/default values
# Only one of these may be necessary

from .pantulipy import *
from .pantulipy import _DEFAULTLESS_INDICATORS

import inspect
from typing import Callable, Dict, Iterable

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
        Get Technical Analysis indicator values based on a DataFrame
        with columns: 'open' 'high' 'low' 'close' 'volume'.

        The class automatically discovers indicators exposed by
        :mod:`pandas_ta` and ``pantulipy`` so that newly released
        metrics are immediately available without code changes.
    """

    pandas_ta_indicators: Dict[str, Callable] = {}
    unique_pandas_ta_indicators: Dict[str, Callable] = {}
    pantulipy_indicators: Dict[str, Callable] = {}
    unique_pantulipy_indicators: Dict[str, Callable] = {}
    _indicator_maps_ready = False

    def __init__(self) -> None:
        if not TA_Features._indicator_maps_ready:
            self._initialize_indicator_maps()

    @classmethod
    def _initialize_indicator_maps(cls) -> None:
        cls.pandas_ta_indicators = cls._discover_pandas_ta_indicators()
        cls.pantulipy_indicators = cls._discover_pantulipy_indicators()
        cls.unique_pandas_ta_indicators = {
            name: fn
            for name, fn in cls.pandas_ta_indicators.items()
            if name not in cls.pantulipy_indicators
        }
        cls.unique_pantulipy_indicators = {
            name: fn
            for name, fn in cls.pantulipy_indicators.items()
            if name not in cls.pandas_ta_indicators
        }
        cls._indicator_maps_ready = True

    @staticmethod
    def _discover_pandas_ta_indicators() -> Dict[str, Callable]:
        allowed_categories: Iterable[str] = (
            'candle', 'cycle', 'momentum', 'overlap', 'performance',
            'statistics', 'trend', 'volatility', 'volume'
        )
        excluded_indicators = {
            'candle', 'candle_all', 'candle_color', 'cdl_pattern', 'cdl_z'
        }
        indicators: Dict[str, Callable] = {}
        for category in allowed_categories:
            for indicator_name in ta.Category.get(category, []):
                if indicator_name in excluded_indicators:
                    continue
                fn = getattr(ta, indicator_name, None)
                if not callable(fn):
                    continue
                if indicator_name.startswith('_'):
                    continue
                indicators[indicator_name] = fn
        return indicators

    @staticmethod
    def _discover_pantulipy_indicators() -> Dict[str, Callable]:
        from . import pantulipy

        indicators: Dict[str, Callable] = {}
        for name in getattr(pantulipy, '__all__', []):
            if name in _DEFAULTLESS_INDICATORS:
                continue
            fn = getattr(pantulipy, name, None)
            if callable(fn):
                indicators[name] = fn
        return indicators

    @staticmethod
    def _build_indicator_kwargs(function: Callable, series_map: Dict[str, pd.Series]) -> Dict[str, pd.Series]:
        kwargs: Dict[str, pd.Series] = {}
        parameters = inspect.signature(function).parameters
        for name, parameter in parameters.items():
            if name in ('open_', 'open') and 'open' in series_map:
                kwargs[name] = series_map['open']
            elif name in ('high', 'low', 'close', 'volume') and name in series_map:
                kwargs[name] = series_map[name]
            elif parameter.default is inspect._empty and parameter.kind not in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            ):
                raise ValueError(f'Missing required argument: {name}')
        return kwargs

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
        series_map = {
            'open': open_,
            'high': high,
            'low': low,
            'close': close,
            'volume': volume,
        }

        for name, function in ind.items():
            try:
                kwargs = self._build_indicator_kwargs(function, series_map)
            except ValueError:
                continue

            try:
                indicator_data = function(**kwargs)
            except Exception:
                # Ignore indicators that cannot be computed for the provided dataset
                continue

            if indicator_data is None:
                continue

            if isinstance(indicator_data, tuple):
                for indicator_df in indicator_data:
                    if indicator_df is not None:
                        data = self._append_column(data, indicator_df)
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
        for function in ind.values():
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
