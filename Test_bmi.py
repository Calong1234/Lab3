import Lab2.bmi as bmi  

print("Test_Lab3")


def test_bmi_normal_weight():
    result=bmi.calculate_bmi(1.70, 55)
    print (result)
    assert (result == 0)
    
def test_bmi_over_weight():
    result=bmi.calculate_bmi(1.70, 555)

    assert (result == 1)

def test_bmi_under_weight():
    result=bmi.calculate_bmi(1.70, 5)

    assert (result == -1)