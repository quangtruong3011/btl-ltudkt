import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.product import Product


class Order:
    #Các trạng thái của đơn hàng.
    STATUS_PENDING = "Chờ xử lý"
    STATUS_DELIVERING = "Đang giao"
    STATUS_DELIVERED = "Đã giao"
    #Khởi tạo đối tượng đơn hàng.
    def __init__(
        self,
        order_id: int,                #Mã đơn hàng
        customer_name: str,           #Tên khách hàng
        phone: str,                   #Số điện thoại khách hàng
        address: str,                 #Địa chỉ gia hàng
        products: list,               #Danh sách sản phẩm trong đơn hàng
        status: str = STATUS_PENDING, #Trạng thái đơn hàng (Mặc định là "Chờ xử lý")
    ):
        self.order_id = order_id
        self.customer_name = customer_name
        self.phone = phone
        self.address = address
        self.products = products
        self.status = status
        self.total_amount = self.calculate_total_amount()
    #Tính tổng tiền của đơn hàng.
    def calculate_total_amount(self):
        return sum([product.get_total_price() for product in self.products]) #Tổng giá trị các sản phẩm trong đơn hàng
    #Cập nhập trạng thái đơn hàng.
    def update_status(self, new_status: str):
        if new_status not in [
            Order.STATUS_PENDING,
            Order.STATUS_DELIVERING,
            Order.STATUS_DELIVERED,
        ]:
            print ("Trạng thái không hợp lệ.")
        self.status = new_status
    #Trả về chuỗi biểu diễn của đơn hàng.
    def __str__(self):
        products_str = "\n".join([str(product) for product in self.products])
        return f"Order ID: {self.order_id}\nCustomer Name: {self.customer_name}\nPhone: {self.phone}\nAddress: {self.address}\nProducts:\n{products_str}\nStatus: {self.status}\nTotal Amount: {self.total_amount}"
