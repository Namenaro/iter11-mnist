from clicker import *
from hypothesis import *
from sensors import *
from logger import *
from data import *
from plotter import *

def create_hypos_for_test(pic, sensor_field_radius, u_radius):
    hypos = []
    X, Y=select_coord_on_pic(pic)
    x0 = X[0]
    y0=Y[0]
    for i in range(1, len(X)):
        x=X[i]
        y=Y[i]
        dx = x-x0
        dy = y-y0
        etalon_mean = np.mean(get_sensory_array(pic,x,y,sensor_field_radius))
        hypo = Hypothesis(sensor_field_radius, etalon_mean,dx,dy,u_radius)
        hypos.append(hypo)
    return hypos

def make_exp1():
    logger = HtmlLogger("EX1")
    pic= etalons_of3()[0]
    sensor_field_radius = 1
    u_radius = 1
    hypos = create_hypos_for_test(pic, sensor_field_radius, u_radius)
    hypos_fields =[]
    for hypo in hypos:
        field = get_field_of_hypo_on_pic(hypo, pic)
        hypos_fields.append(field)
    fig = plot_several_pics_with_one_colorbar(hypos_fields)
    logger.add_fig(fig)
    logger.close()

if __name__ == "__main__":
    make_exp1()