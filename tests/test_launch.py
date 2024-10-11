
from airtest.core.api import *


def test_begin(driver):
    print('!!!!!!!!!!!1')
    print(G.BASEDIR)
    ernie_coord = wait(Template('Ernie.png'))
    touch(ernie_coord)
    field_coord = wait(Template('empty_field.png'))
    touch(field_coord)
    wheat_coord = wait(Template('wheat.png'))
    swipe(wheat_coord, field_coord)
    sown_field_coord = wait(Template('sown_field.png'), timeout=5)
    assert sown_field_coord, 'Wheat has not planted'
