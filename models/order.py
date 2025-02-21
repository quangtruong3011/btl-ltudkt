import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.product import Product


class Order:
    STATUS_PENDING = "Pending"  # Chờ xử lý
    STATUS_DELIVERING = "Delivering"  # Đang giao
    STATUS_DELIVERED = "Delivered"  # Đã giao

    def __init__(
        self,
        order_id: int,
        customer_name: str,
        phone: str,
        address: str,
        products: list,
        status: str = STATUS_PENDING,  # Default value for status
    ):
        self.order_id = order_id
        self.customer_name = customer_name
        self.phone = phone
        self.address = address
        self.products = products
        self.status = status
        self.total_amount = self.caculate_total_amount()

    def caculate_total_amount(self):
        return sum([product.get_total_price() for product in self.products])

    def update_status(self, new_status: str):
        if new_status not in [
            Order.STATUS_PENDING,
            Order.STATUS_DELIVERING,
            Order.STATUS_DELIVERED,
        ]:
            raise ValueError("Invalid status")  # Trạng thái không hợp lệ
        self.status = new_status

    def __str__(self):
        products_str = "\n".join([str(product) for product in self.products])
        return f"Order ID: {self.order_id}\nCustomer Name: {self.customer_name}\nPhone: {self.phone}\nAddress: {self.address}\nProducts:\n{products_str}\nStatus: {self.status}\nTotal Amount: {self.total_amount}"
