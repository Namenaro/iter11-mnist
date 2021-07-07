from clicker import *
from hypothesis import *
from sensors import *

def create_hypos_same_radiuses(pic, sensor_field_radius, u_radius):
    hypos = []
    X, Y = select_coord_on_pic(pic)
    x0 = X[0]
    y0 = Y[0]
    for i in range(1, len(X)):
        x=X[i]
        y=Y[i]
        dx = x-x0
        dy = y-y0
        etalon_mean = np.mean(get_sensory_array(pic,x,y,sensor_field_radius))
        hypo = Hypothesis(sensor_field_radius, etalon_mean,dx,dy,u_radius)
        hypos.append(hypo)
    return hypos