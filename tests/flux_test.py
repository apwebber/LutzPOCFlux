import numpy as np

import pytest

from lutzpocflux import MakeFlux


def test_flux_maker():
    """
    Test basic functionality of the MakeFlux class
    """

    npp = [np.random.randint(0, 10, (10, 10)) for _ in range(6)]

    mf = MakeFlux(ze=4000.0, annual_npp=npp)
    f = mf.get_flux()
    assert f.shape == (10, 10)

    npp = [np.random.randint(0, 10, (1, 10)) for _ in range(6)]
    mf = MakeFlux(ze=4000.0, annual_npp=npp)
    f = mf.get_flux()
    assert f.shape == (1, 10)

    npp = [np.random.randint(0, 10, (10, 10)) for _ in range(1)]
    with pytest.raises(ValueError):
        mf = MakeFlux(ze=4000.0, annual_npp=npp)
