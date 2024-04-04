[![pypi](https://badgen.net/pypi/v/mendotapy)](https://pypi.org/project/mendotapy/)
[![Documentation Status](https://readthedocs.org/projects/mendotapy/badge/?version=latest)](https:/mendotapy.readthedocs.io/en/latest/?badge=latest)
[![Formatted with black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/lgloege/mendotapy/issues)


# mendotapy

A Python 3.6+ package for analysis-ready [Lake Mendota ice phenology](https://climatology.nelson.wisc.edu/first-order-station-climate-data/madison-climate/lake-ice/history-of-ice-freezing-and-thawing-on-lake-mendota/) data

Installing
----------

### PyPi
```sh
pip install mendotapy==1.0.0
```

### GitHub
```sh
pip install -e git+https://github.com/lgloege/mendotapy.git#egg=mendotapy
```

Using the Package
----------
**Read data into a dataframe**
```python
import mendotapy
df = mendotapy.load()
```