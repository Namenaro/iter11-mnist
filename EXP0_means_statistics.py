from data import *
from logger import *
from sensors import *
from plotter import *

def get_means(radius, pics):
    ymax = pics[0].shape[0]
    xmax = pics[0].shape[1]
    means = []
    for pic in pics:
        for centery in range(0, ymax):
            for centerx in range(0, xmax):
                val = get_sensory_array(pic, centerx, centery, radius)
                means.append(np.mean(val))
    return means

def make_exp0():
    logger = HtmlLogger("EX0")
    sens_radiuses= [0,1, 2, 3, 5, 8, 12, 17]
    pics_for_stat = get_diverse_set_of_numbers(70)[0:56]

    for sens_radius in sens_radiuses:
        means = get_means(sens_radius, pics_for_stat)
        logger.add_text("radius:"+ str(sens_radius))
        fig = plot_hist(means, nbins=30)
        logger.add_fig(fig)
    logger.close()

if __name__ == "__main__":
    make_exp0()
