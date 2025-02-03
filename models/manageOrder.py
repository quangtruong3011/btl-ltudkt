from models.order import Order


class ManageOrder:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

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
            if new_phone:
                order.phone = new_phone
            if new_address:
                order.address = new_address
            if new_products:
                order.products = new_products
                order.total_amount = order.caculate_total_amount()
            if new_status:
                order.update_status(new_status)
        else:
            raise ValueError("Order not found")  # Đơn hàng không tồn tại

    def delete_order(self, order_id):
        order = self.find_order_by_id(order_id)
        if order:
            self.orders.remove(order)
        else:
            raise ValueError("Order not found")  # Đơn hàng không tồn tại

    def find_order_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def find_order_by_phone(self, phone):
        return [order for order in self.orders if order.phone == phone]

    def display_orders_by_status(self, status):
        return [order for order in self.orders if order.status == status]

    def caculate_total_revenue(self):
        return sum(
            [
                order.total_amount
                for order in self.orders
                if order.status == Order.STASTUS_DELIVERED
            ]
        )

    def sort_orders_by_total_amount(self, ascending=True):
        return sorted(
            self.orders, key=lambda order: order.total_amount, reverse=not ascending
        )

    def get_pending_orders(self):
        return self.display_orders_by_status(
            Order.STASTUS_PENDING
        ) + self.display_orders_by_status(Order.STASTUS_DELIVERING)

    def get_top_selling_products(self, top_n=5):
        products_sales = {}
        for order in self.orders:
            if order.status == Order.STASTUS_DELIVERED:
                for product in order.products:
                    if product.name in products_sales:
                        products_sales[product.name] += product.quantity
                    else:
                        products_sales[product.name] = product.quantity
                    sorted_products = sorted(
                        products_sales.items(), key=lambda x: x[1], reverse=True
                    )
        return sorted_products[:top_n]
