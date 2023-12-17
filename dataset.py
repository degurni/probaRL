import datetime

import pandas as pd
from binance import Client  # pip install python-binance


client = Client('', '')

class Dataset:
    def __init__(self) -> None:
        self.time_frames = [
            '1m',
            '2m',
            '3m',
            '5m',
            '15m',
            '30m',
            '1h',
            '2h',
            '4h',
            '6h',
            '8h',
            '12h',
            '1d',
            '3d',
            '1w',
            '1M'
        ]

    def get_data(self, days: int, symbol: str, tf: str) -> pd.DataFrame:
        return self._download_data(days=days, symbol=symbol, tf=tf)

    def _download_data(self, days: int=10, symbol: str='BTCUSDT', tf: str='1h') -> pd.DataFrame:
        '''
        https://python-binance.readthedocs.io/en/latest/binance.html
        '''
        if tf not in self.time_frames:
            raise ValueError(f'Поддерживаются таймфреймы: {self.time_frames}')
        from_day = self._get_start_day(days=days)
        klines = client.get_historical_klines(symbol=symbol, interval=tf, start_str=from_day)
        data = self._convert_to_dataframe(klines=klines)
        data['symbol'] = symbol
        return data

    def _convert_to_dataframe(self, klines: list) -> pd.DataFrame:
        data = pd.DataFrame(data=[row[1:7] for row in klines],
                            columns=['open', 'high', 'low', 'close', 'volume', 'time']
                            ).set_index('time')
        data.index = pd.to_datetime(data.index + 1, unit='ms')
        data = data.sort_index()
        data = data.apply(pd.to_numeric, axis=1)
        return data

    def _get_start_day(self, days: int) -> str:
        end = datetime.datetime.now()
        end = end - datetime.timedelta(days=0)
        start = end - datetime.timedelta(days=days)
        end = end.strftime('%d %b, %Y')
        start = start.strftime('%d %b, %Y')
        return start