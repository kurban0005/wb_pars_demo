from pydantic import BaseModel, field_validator
from typing import List, Optional

class Price(BaseModel):
    basic: int
    product: int
    total: int

    @field_validator('basic','product','total')
    def convert_price(cls, price: int) -> float:
        if price is not None:
            return price / 100

class SizeItem(BaseModel):
    price: Price


class Product(BaseModel):
    id: int
    brand: str
    rating: Optional[int] = None
    volume: int
    sizes: List[SizeItem]
    name: str

class Products(BaseModel):
    products: List[Product]


