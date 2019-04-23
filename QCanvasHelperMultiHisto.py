from QCanvasHelperBase import *
import numpy as np
from QSettings import *

class QCanvasHelperMultiHisto(QCanvasHelperBase):
    def add_result_file(self, file):
        dta = np.loadtxt(file, dtype=QSettings.results_dtype, delimiter=',', skiprows=2)

        self.idx_data = QSettings.PLOTITEMS
        self.hist_data = {'$[N_T]$ (ppm)': dta['[NT]'],
            '$[N_A]$ (ppm)': dta['[NA]'],
            '$[N_B]$ (ppm)': dta['[NB]'],
            '$[N_B]/[N_T]$': (dta['[NB]']/dta['[NT]']),
            '$T (^{\circ}C)$': dta['T'],
            'platelet peak position $(cm^{-1})$': dta['p_x0'],
            'platelet peak area $(cm^{-2})$': dta['p_area_ana'],
            'platelet peak width $(cm^{-1})$': (dta['p_HWHM_l'] + dta['p_HWHM_r']),
            'platelet peak symmetry $(cm^{-1})$': (dta['p_x0'] - dta['avg']),
            'I(3107) $(cm^{-2})$': dta['H_area_ana']}

        self.maxidx = len(self.hist_data)

    def display_current(self):
        self.clear_plot()

        key = self.idx_data[self.current]
        data = self.hist_data[key]
        fig = self.canv.figure
        sp = fig.add_subplot(111)

        sp.hist(data[~np.isnan(data)], bins='auto')
        fig.suptitle(key)

        self.canv.draw()