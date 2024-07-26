import numpy as np
from lutzpocflux.equations import rld_f, prd_f, prr_f, pratioze_f


class MakeFlux:
    def __init__(
        self,
        ze: np.ndarray | float,
        annual_npp: list[np.ndarray],
        svi: np.ndarray | None = None,
    ):
        self.ze = ze
        self.all_years_average = np.nanmean(np.array(annual_npp), axis=0)

        if svi is None:
            self.svi = self._make_svi(annual_npp)
        else:
            self.svi = svi

    def _make_svi(self, layers: list[np.ndarray]) -> np.ndarray:
        all_years_std = np.nanstd(np.array(layers), axis=0)

        return all_years_std / self.all_years_average

    def get_flux(self):
        prdl = prd_f(self.svi)
        rldl = rld_f(self.svi)
        prrl = prr_f(self.svi)

        pratioze_res = pratioze_f(prdl, self.ze, rldl, prrl)
        return self.all_years_average * pratioze_res
