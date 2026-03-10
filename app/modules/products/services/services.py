from app.modules.utils.json_loader import load_products


def get_all_products():
    return load_products()


def get_product_by_id(product_id: int):
    products = load_products()

    for product in products:
        if product["product_id"] == product_id:
            return product

    return None