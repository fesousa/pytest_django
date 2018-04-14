from lms_app.utils.utils import calculaMediaFinal

def test_calculaMediaFinal():
    assert calculaMediaFinal(10,10) == 10
    assert calculaMediaFinal(10,0) == 6
    assert calculaMediaFinal(6,10) == 7.6
    assert calculaMediaFinal(10,6) == 8.4
    assert calculaMediaFinal(0,10) == 4
    assert calculaMediaFinal(8,4) == 6.4
    assert calculaMediaFinal(5,5) == 5
    assert calculaMediaFinal(5,9) == 6.6
    assert calculaMediaFinal(3,7) == 4.6
    assert calculaMediaFinal(3,10) == 5.8


