Datetime Time Deltas
====================


Timedelta object
----------------
Shifting datetime objects:

.. code-block:: python

    from datetime import datetime


    gagarin = datetime(1961, 4, 12, 6, 7)
    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    between_dates = armstrong - gagarin

    str(between_dates)                  # '3021 days, 20:49:15'
    between_dates                       # datetime.timedelta(days=3021, seconds=74955)
    between_dates.days                  # 3021
    between_dates.seconds               # 74955
    between_dates.total_seconds()       # 261089355.0 (days * seconds per day + seconds)


Time Shift
----------

Simple Shifts
-------------
Simple ``timedelta`` shifts:

.. code-block:: python

    from datetime import timedelta, datetime


    gagarin = datetime(1961, 4, 12)

    gagarin - timedelta(minutes=15)
    # datetime.datetime(1961, 4, 11, 23, 45)

    gagarin + timedelta(minutes=10)
    # datetime.datetime(1961, 4, 12, 0, 10)


Simple ``timedelta`` shifts:

.. code-block:: python

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    armstrong - timedelta(hours=21)
    # datetime.datetime(1969, 7, 20, 5, 56, 15)

    armstrong + timedelta(hours=5)
    # datetime.datetime(1969, 7, 21, 7, 56, 15)

Simple ``timedelta`` shifts:

.. code-block:: python

    from datetime import timedelta, date


    sputnik = date(1957, 10, 4)

    sputnik + timedelta(days=5)
    # datetime.date(1957, 10, 9)

    sputnik - timedelta(days=3)
    # datetime.date(1957, 10, 1)

Simple ``timedelta`` shifts:

.. code-block:: python

    from datetime import datetime, timedelta


    gagarin = datetime(1961, 4, 12)

    gagarin + timedelta(weeks=2)
    # datetime.datetime(1961, 4, 26, 0, 0)

    gagarin - timedelta(weeks=3)
    # datetime.datetime(1961, 3, 22, 0, 0)

Complex Shifts
--------------
Complex ``timedelta`` shifts:

.. code-block:: python

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    armstrong - timedelta(days=2, hours=21)
    # datetime.datetime(1969, 7, 18, 5, 56, 15)

Complex ``timedelta`` shifts:

.. code-block:: python

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    duration = timedelta(
        weeks=3,
        days=2,
        hours=21,
        minutes=5,
        seconds=12,
        milliseconds=10,
        microseconds=55)
    # datetime.timedelta(days=23, seconds=75912, microseconds=10055)

    between_dates = armstrong - duration
    # datetime.datetime(1969, 6, 27, 5, 51, 2, 989945)

Month Shifts
------------
Subtract month from ``datetime``:

.. code-block:: python

    from datetime import timedelta, date


    MONTH = timedelta(days=30.436875)

    gagarin = date(1961, 4, 12)
    gagarin - MONTH
    # datetime.date(1961, 3, 13)

Subtract month from ``datetime``:

.. code-block:: python

    from calendar import monthlen
    from datetime import timedelta, date


    def month_before(dt):
        MONTH = monthlen(dt.year, dt.month)
        return dt - timedelta(days=MONTH)


    gagarin = date(1961, 4, 12)
    month_before(gagarin)
    # datetime.date(1961, 3, 13)


Duration
--------
Duration between two datetimes:

.. code-block:: python

    from datetime import datetime

    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    MONTH = 30.436875 * DAY  # Average days a month in solar calendar
    YEAR = 365.2425 * DAY  # Solar calendar

    def duration(dt):
        years, seconds = divmod(dt.total_seconds(), YEAR)
        months, seconds = divmod(seconds, MONTH)
        days, seconds = divmod(seconds, DAY)
        hours, seconds = divmod(dt.seconds, HOUR)
        minutes, seconds = divmod(seconds, MINUTE)

        return {
            'years': int(years),
            'months': int(months),
            'days': int(days),
            'hours': int(hours),
            'minutes': int(minutes),
            'seconds': int(seconds),
        }


    gagarin = datetime(1961, 4, 12, 6, 7)
    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    dt = armstrong - gagarin
    # datetime.timedelta(days=3021, seconds=74955)

    duration(dt)
    # {'years': 8, 'months': 3, 'days': 8, 'hours': 20, 'minutes': 49, 'seconds': 15}


Assignments
-----------
.. literalinclude:: assignments/datetime_timedelta_period.py
    :caption: :download:`Solution <assignments/datetime_timedelta_period.py>`
    :end-before: # Solution
