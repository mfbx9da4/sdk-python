"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from apideck.apideck_customers import ApideckCustomers
from apideck.orders import Orders
from apideck.products import Products
from apideck.stores import Stores


class Ecommerce(BaseSDK):
    orders: Orders
    products: Products
    customers: ApideckCustomers
    stores: Stores

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.orders = Orders(self.sdk_configuration)
        self.products = Products(self.sdk_configuration)
        self.customers = ApideckCustomers(self.sdk_configuration)
        self.stores = Stores(self.sdk_configuration)
