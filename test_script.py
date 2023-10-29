import source as src
import pytest

sc = src.ShoppingCart()

def test_add_item():
    sc.add_item('apple', 2)
    assert sc.items == [{'product': 'apple', 'quantity': 2}]
    sc.add_item('apple')
    assert sc.items == [{'product': 'apple', 'quantity': 3}]
    sc.add_item('orange', 2)
    assert sc.items == [{'product': 'apple', 'quantity': 3},
                        {'product': 'orange', 'quantity': 2}]

def test_validate_quantity_add():
    with pytest.raises(ValueError) as err:
        output = sc.add_item('apple', 0)
    assert str(err.value) == "Quantity must be greater than 0"

def test_validate_quantity_remove():
    with pytest.raises(ValueError) as err:
        sc.remove_item('', 0)
    assert str(err.value) == "Quantity must be greater than 0"

    with pytest.raises(ValueError) as err:
        sc.remove_item('grapes')
    assert str(err.value) == "Product not found in the shopping cart"   

def test_item_removed():
    sc.remove_item('apple',3)
    assert sc.items == [{'product': 'orange', 'quantity': 2}]
    sc.remove_item('orange')
    assert sc.items ==  [{'product': 'orange', 'quantity': 1}]
    
#p = src.Product('orange', 10)

def test_calculate():
    total = sc.calculate_total()
    assert  total == 10







    







    

