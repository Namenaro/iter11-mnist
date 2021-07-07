
from sensors import *

import numpy as np
import math
import operator

class Hypothesis:
    def __init__(self, sensor_field_radius, etalon_mean, dx, dy, u_radius):
        self.sensor_field_radius = sensor_field_radius
        self.etalon_mean = etalon_mean

        self.dx = dx
        self.dy = dy
        self.u_radius = u_radius

    def _apply_to_point_no_u(self, pic, x, y):
        sensory_array = get_sensory_array(pic, x, y, self.sensor_field_radius)
        current_mean = np.mean(sensory_array)
        deviation_from_etalon = math.pow((self.etalon_mean - current_mean),2)
        return deviation_from_etalon

    def apply_to_point(self, pic, x, y):
        expected_x = x + self.dx
        expected_y = y + self.dy

        X, Y = get_coords_less_or_eq_raduis(expected_x, expected_y, self.u_radius)
        temporary_hypotheses = {}
        for i in range(len(X)):
            deviation_from_etalon = self._apply_to_point_no_u(pic, X[i], Y[i])
            ddx = X[i] - expected_x
            ddy = Y[i] - expected_y

            temporary_hypotheses[(ddx, ddy)] = deviation_from_etalon

        deviation_from_etalon, ddx, ddy = find_best_hypothesys(temporary_hypotheses)
        return deviation_from_etalon, ddx, ddy

def find_best_hypothesys(dict_hypotheses): #ищем ту что с самым маленьким значением
    sorted_hypos = sorted(dict_hypotheses.items(), key=operator.itemgetter(1),reverse=False)
    best_hypo = sorted_hypos[0]
    dxdy= best_hypo[0]
    val = best_hypo[1]
    return val, dxdy[0], dxdy[1]

def get_field_of_hypo_on_pic(hypo, pic):
    ymax = pic.shape[0]
    xmax = pic.shape[1]

    res = np.zeros((ymax, xmax))
    for centery in range(0, ymax):
        for centerx in range(0, xmax):
            deviation_from_etalon, ddx, ddy = hypo.apply_to_point(pic, centerx, centery)
            res[centery, centerx] = deviation_from_etalon
    return res


