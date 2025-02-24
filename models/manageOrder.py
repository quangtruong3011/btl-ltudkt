from models.order import Order


class ManageOrder:
    #Khởi tạo đối tượng quản lý đơn hàng.
    def __init__(self):
        self.orders = []
    #Thêm một đơn hàng mới vào danh sách.
    def add_order(self, order):
        self.orders.append(order) #validate trên main.py
    #Chỉnh sửa thông tin đơn hàng dựa trên mã đơn hàng.
    def edit_order(
        self,
        order_id,
        new_customer_name=None,
        new_phone=None,
        new_address=None,
        new_products=None,
        new_status=None,
    ):
        order = self.find_order_by_id(order_id)
        if order:
            if new_customer_name:
                order.customer_name = new_customer_name
            if new_phone and (new_phone.isdigit()):
                order.phone = new_phone
            else:
                print ("Số điện thoại không hợp lệ.")
            if new_address:
                order.address = new_address
            if new_products:
                for product_data in new_products:
                    product_name, new_name, new_quantity, new_price = product_data
                    for product in order.products:
                        if product.name == product_name:
                            product.edit_product(new_name or None, new_quantity or None, new_price or None)
                            break
                        else:
                            print ("Sản phẩm không tồn tại.")
                order.total_amount = order.calculate_total_amount()
            if new_status and new_status in [Order.STATUS_PENDING, Order.STATUS_DELIVERING, Order.STATUS_DELIVERED]:
                order.update_status(new_status)
            else:
                print ("Trạng thái không hợp lệ.")
        else:
            print ("Đơn hàng không tồn tại.")
    #Xoá đơn hàng khỏi danh sách.
    def delete_order(self, order_id):
        order = self.find_order_by_id(order_id)
        if order:
            self.orders.remove(order)
        else:
            print ("Đơn hàng không tồn tại.")
    #Tìm đơn hàng theo mã đơn hàng.
    def find_order_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None
    #Tìm đơn hàng theo số điện thoại.
    def find_order_by_phone(self, phone):
        return [order for order in self.orders if order.phone == phone]
    #Danh sách các đơn hàng theo trạng thái đơn hàng.
    def display_orders_by_status(self, status):
        return [order for order in self.orders if order.status == status]
    #Tính tổng doanh thu các đơn hàng đã giao.
    def calculate_total_revenue(self):
        return sum(
            [
                order.total_amount
                for order in self.orders
                if order.status == Order.STATUS_DELIVERED
            ]
        )
    #Sắp xếp danh sách đơn hàng theo tổng tiền.
    def sort_orders_by_total_amount(self, ascending=True):
        return sorted(
            self.orders,
            key=lambda order: (order.total_amount, order.order_id),
            reverse=not ascending,
        )
    #Danh sách các đơn hàng ở trạng thái "Chờ xử lý" và "Đang giao".
    def get_pending_orders(self):
        return self.display_orders_by_status(
            Order.STATUS_PENDING
        ) + self.display_orders_by_status(Order.STATUS_DELIVERING)
    #Danh sách các sản phẩm bán chạy nhất
    def get_top_selling_products(self, top_n=5):
        products_sales = {}
        for order in self.orders:
            if order.status == Order.STATUS_DELIVERED:
                for product in order.products:
                    if product.name in products_sales:
                        products_sales[product.name] += product.quantity
                    else:
                        products_sales[product.name] = product.quantity
                    sorted_products = sorted(
                        products_sales.items(), key=lambda x: x[1], reverse=True
                    )
        return sorted_products[:top_n]
