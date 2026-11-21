# from pydantic import validate_call

# @validate_call #decorator used to check specific pydantic function inputs.
# def calculate_total(price: int, quantity: int):
#     total = price * quantity
#     return total

# result = calculate_total("10", 2) #benefit of pydantic: 10 and "10" gives same output
# print(result)

from pydantic import BaseModel

class Product(BaseModel):
    product_name: str
    price: int
    in_stock: bool = True

product_details = Product(product_name = "Cashew", price = "3500", in_stock= False) 
print(product_details)
print(product_details.model_dump_json())