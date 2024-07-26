"""
Test the Flux equations in comparison with the POC Flux R Package found here:

https://rdrr.io/github/chihlinwei/OceanData/src/R/lutz_p_flux.R

Note that at time of writing, the above package contained an error for the equation for rld
and an issue has been raised here:

https://github.com/chihlinwei/OceanData/issues/1

The error in the rld equation is rectified in the include R script and these values
test against the rectified version of the equation. Monitor the issue in case this
is wrong.
"""

import json
from pytest import approx
from lutzpocflux.equations import (
    prd,
    rld,
    prr,
    pratioze,
)

RESULTS_FILE = "tests/R_Project/lutz/test_values.json"
with open(RESULTS_FILE, "r", encoding='utf8') as f:
    RESULTS = json.load(f)


def test_equations():
    for d in RESULTS:
        assert prd(d["svi"]) == approx(d["prd"])
        assert rld(d["svi"]) == approx(d["rld"])
        assert prr(d["svi"]) == approx(d["prr"])


def test_pratio_flux():
    for d in RESULTS:
        pratio = pratioze(prd(d["svi"]), d["ze"], rld(d["svi"]), prr(d["svi"]))
        assert pratio == approx(d["pratio"])
        assert pratio * d["npp"] == approx(d["flux"])
