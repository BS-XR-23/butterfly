from pydantic import BaseModel
from typing import List


class Metadata(BaseModel):
    url: str


class Product3DModel(BaseModel):
    url: str
    available_colour: List[str]
    metadata: Metadata


class Product(BaseModel):
    product_id: int
    product_name: str
    product_3D_model: Product3DModel