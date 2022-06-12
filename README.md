===============
korean_holiday_calendar
===============

This is a Korean-only version of python-holidays package (by dr-prodigy), which contains some new functions for calculating Korean holidays.

The usage is mostly the same as the existing python-holidays package, so please read its instruction manual for a complicated usage.

https://python-holidays.readthedocs.io/

Below is a brief instruction manual based on our package.


Quick Start
-----------

.. code-block:: python

    from datetime import date
    import holidays

    kr_holidays = holidays.KR()  # this is a dict
    # the below is the same, but takes a string:
    kr_holidays = holidays.country_holidays('KR')  # this is a dict

    date(2015, 1, 1) in kr_holidays  # True
    date(2015, 1, 2) in kr_holidays  # False
    kr_holidays.get('2014-01-01')  # "신정"
    
For English users, we added English options.

.. code-block:: python

    kr_holidays_en = holidays.KR(en_name = True)
    
    kr_holidays_en.get('2014-01-01')  # "New Year's Day"

The HolidayBase dict-like class will also recognize date strings and Unix
timestamps:

.. code-block:: python

    '2014-01-01' in kr_holidays  # True
    '1/1/2014' in kr_holidays    # True
    1388597445 in kr_holidays    # True


License
-------

.. __: LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
