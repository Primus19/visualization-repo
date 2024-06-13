[80 rows x 6 columns]
/Users/primus.vekuh@sentinelone.com/Documents/reports/save_formatted_version.py:51: FutureWarning: 'M' is deprecated and will be removed in a future version, please use 'ME' instead.
  df.set_index('instance_create_time').resample('M').size().plot(color='coral')
Traceback (most recent call last):
  File "/Users/primus.vekuh@sentinelone.com/Documents/reports/save_formatted_version.py", line 51, in <module>
    df.set_index('instance_create_time').resample('M').size().plot(color='coral')
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/generic.py", line 9771, in resample
    return get_resampler(
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/resample.py", line 2050, in get_resampler
    return tg._get_resampler(obj, kind=kind)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/resample.py", line 2272, in _get_resampler
    raise TypeError(
TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'Index'
