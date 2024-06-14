
None
/Users/primus.vekuh@sentinelone.com/Documents/reports/save_formatted_version.py:42: FutureWarning: 'M' is deprecated and will be removed in a future version, please use 'ME' instead.
  instances_over_time = df.set_index('instance_create_time').resample('M').size().reset_index()
Traceback (most recent call last):
  File "/Users/primus.vekuh@sentinelone.com/Documents/reports/save_formatted_version.py", line 42, in <module>
    instances_over_time = df.set_index('instance_create_time').resample('M').size().reset_index()
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/generic.py", line 9771, in resample
    return get_resampler(
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/resample.py", line 2050, in get_resampler
    return tg._get_resampler(obj, kind=kind)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/resample.py", line 2272, in _get_resampler
    raise TypeError(
TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'Index'
