from clicker import *
from hypothesis import *
from sensors import *
from logger import *
from data import *
from plotter import *
from creator import *


def make_exp1():
    logger = HtmlLogger("EX1")
    pic= etalons_of3()[0]
    sensor_field_radius = 1
    u_radius = 1
    hypos = create_hypos_same_radiuses(pic, sensor_field_radius, u_radius)
    hypos_fields =[]
    for hypo in hypos:
        field = get_field_of_hypo_on_pic(hypo, pic)
        hypos_fields.append(field)
    fig = plot_several_pics_with_one_colorbar(hypos_fields)
    logger.add_fig(fig)
    logger.close()

if __name__ == "__main__":
    make_exp1()