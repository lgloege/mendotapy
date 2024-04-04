Quickstart Guide
====================================================

Installation
----------------------------------------------------

Install `mendotapy` using `pip`.

.. code-block:: bash

   # for latest release
   pip install mendotapy

   # for bleeding-edge up-to-date commit
   pip install -e git+https://github.com/lgloege/mendotapy.git

Once installed, use the `load()` function to load the data as a pandas dataframe.

.. code-block:: python

    import mendotapy
    df = mendotapy.load()

Now you can analyze the data using standard pandas methods.

Built in utilities
----------------------------------------------------
Once the data is loaded as dataframe, you can use some builtin ultities provided by `mendotapy`.
These will calculate the day of the year (DOY) and extract the start of the season for you.

.. code-block:: python

    list_of_iceondoy = df.utils.iceon_doy()
    list_of_iceoffdoy = df.utils.iceoff_doy()


Sometimes it is conventient to have the DOY wrap around the next the next or previous year.
For instance, DOYs greater than 365 correspond to the next year and negative values correspond to the previous year.
This can be useful when plotting trends in the ice-on or ice-off year.

.. code-block:: python

    list_of_iceondoy = df.utils.iceon_doy_wrapped()
    list_of_iceoffdoy = df.utils.iceoff_doy_wrapped()

Finally, when plotting you may want the start of the season the x-axis. Use the `season_start()` method.

.. code-block:: python

    season_start = df.utils.season_start()