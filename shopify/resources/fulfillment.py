from ..base import ShopifyResource
import json


class Fulfillment(ShopifyResource):
    @classmethod
    def _prefix(cls, options=None):
        if options is None:
            options = {}
        order_id = options.get("order_id")
        if order_id:
            return "%s/orders/%s" % (cls.site, order_id)
        else:
            return cls.site

    def cancel(self):
        self._load_attributes_from_response(self.post("cancel"))

    def complete(self):
        self._load_attributes_from_response(self.post("complete"))

    def open(self):
        self._load_attributes_from_response(self.post("open"))

    def update_tracking(self, tracking_info, notify_customer):
        body = {"fulfillment": {"tracking_info": tracking_info, "notify_customer": notify_customer}}
        return self.post("update_tracking", json.dumps(body).encode())


class FulfillmentOrders(ShopifyResource):
    @classmethod
    def _prefix(cls, options=None):
        if options is None:
            options = {}
        order_id = options.get("order_id")
        if order_id:
            return "%s/orders/%s" % (cls.site, order_id)
        else:
            return cls.site
