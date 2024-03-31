from dbVisualisatorApp.models import Product


def get_all_products():
    return list(Product.objects.all().values())

