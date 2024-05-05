import price_info as price

print("Test_price_info")

def test_total_cost_shopping():
    result = price.total_cost_shopping()

    assert(result == 46.75)

def test_cost_of_fruit():
    result = price.cost_of_fruits('apple', 10)

    assert(result == 12.0)