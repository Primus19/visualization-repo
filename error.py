primus.vekuh@sentinelone.com@C2W3596XDL reports % python3 age-by-days.py
Traceback (most recent call last):
  File "/Users/primus.vekuh@sentinelone.com/Documents/reports/age-by-days.py", line 35, in <module>
    df['age_in_days'] = (pd.to_datetime('today') - df['container_started_at']).dt.round('D').dt.days.astype(int)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/generic.py", line 6643, in astype
    new_data = self._mgr.astype(dtype=dtype, copy=copy, errors=errors)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/internals/managers.py", line 430, in astype
    return self.apply(
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/internals/managers.py", line 363, in apply
    applied = getattr(b, f)(**kwargs)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/internals/blocks.py", line 758, in astype
    new_values = astype_array_safe(values, dtype, copy=copy, errors=errors)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/dtypes/astype.py", line 237, in astype_array_safe
    new_values = astype_array(values, dtype, copy=copy)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/dtypes/astype.py", line 182, in astype_array
    values = _astype_nansafe(values, dtype, copy=copy)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/dtypes/astype.py", line 101, in _astype_nansafe
    return _astype_float_to_int_nansafe(arr, dtype, copy)
  File "/Users/primus.vekuh@sentinelone.com/Library/Python/3.9/lib/python/site-packages/pandas/core/dtypes/astype.py", line 145, in _astype_float_to_int_nansafe
    raise IntCastingNaNError(
pandas.errors.IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer
primus.vekuh@sentinelone.com@C2W3596XDL reports % 
