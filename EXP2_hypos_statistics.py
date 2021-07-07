from clicker import *
from hypothesis import *
from sensors import *
from logger import *
from data import *
from plotter import *

def get_hist_for_hypo(hypo, pics):
    activations = np.array([])
    for pic in pics:
        field = get_field_of_hypo_on_pic(hypo, pic).flatten()
        activations = np.concatenate([activations, field])
    fig = plot_hist(activations, nbins=15)
    return fig

def make_exp2(logger,X, Y ,sensor_field_radius,u_radius):


    logger.add_text("sensor_field_radius = " + str(sensor_field_radius))
    logger.add_text("u_radius = " + str(u_radius))
    x0 = X[0]
    y0 = Y[0]
    pics_for_stat = etalons_of3()[0:5]
    for i in range(1, len(X)):
        x = X[i]
        y = Y[i]
        dx = x - x0
        dy = y - y0

        etalon_mean = np.mean(get_sensory_array(pic, x, y, sensor_field_radius))
        hypo = Hypothesis(sensor_field_radius, etalon_mean, dx, dy, u_radius)
        fig = plot_points_on_pic(pic,[x0,x],[y0,y])
        logger.add_text("----")
        logger.add_fig(fig)
        fig = get_hist_for_hypo(hypo, pics_for_stat)
        logger.add_fig(fig)


if __name__ == "__main__":
    pic = etalons_of3()[0]
    X, Y = select_coord_on_pic(pic)
    logger = HtmlLogger("EX2")

    sensor_field_radius = 1
    u_radius = 2
    make_exp2(logger,X, Y, sensor_field_radius, u_radius)

    sensor_field_radius = 1
    u_radius = 5
    make_exp2(logger, X, Y, sensor_field_radius, u_radius)

    sensor_field_radius = 1
    u_radius = 8
    make_exp2(logger, X, Y, sensor_field_radius, u_radius)

    logger.close()