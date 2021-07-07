from clicker import *
from hypothesis import *
from sensors import *
from logger import *
from data import *
from plotter import *

def make_exp2():
    logger = HtmlLogger("EX2")
    pic = etalons_of3()[0]
    X, Y=select_coord_on_pic(pic)

