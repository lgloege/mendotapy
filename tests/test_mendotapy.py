import pandas as pd
import mendotapy

# import pytest


def test_load():
    assert isinstance(mendotapy.load(), pd.DataFrame), "load should return a Pandas dataframe"
