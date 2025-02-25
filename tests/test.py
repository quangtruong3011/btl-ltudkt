import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.product import Product
from models.order import Order
from models.manageOrder import ManageOrder


class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        p = Product(
            "Laptop Lenovo LOQ 15ARP9",
            1,
            16790000,
        )
        self.assertEqual(p.name, "Laptop Lenovo LOQ 15ARP9")
        self.assertEqual(p.quantity, 1)
        self.assertEqual(p.price, 16790000)

    def test_product_str(self):
        p = Product("Laptop Lenovo LOQ 15ARP9", 1, 16790000)
        self.assertEqual(
            str(p),
            "Laptop Lenovo LOQ 15ARP9 - 1 x  16790000 = 16790000",
        )


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.products = [
            Product("Laptop Lenovo LOQ 15ARP9", 1, 16790000),
            Product("Chuột không dây Lenovo ThinkPad", 1, 290000),
        ]
        self.order = Order(1, "Vương Hữu Lộc", "0123456789", "Hà Nội", self.products)

    def test_order_initialization(self):
        self.assertEqual(self.order.order_id, 1)
        self.assertEqual(self.order.customer_name, "Vương Hữu Lộc")
        self.assertEqual(self.order.phone, "0123456789")
        self.assertEqual(self.order.address, "Hà Nội")
        self.assertEqual(self.order.products, self.products)
        self.assertEqual(self.order.status, Order.STATUS_PENDING)
        self.assertEqual(self.order.total_amount, 17080000)

    def test_order_str(self):
        expected_str = (
            "Order ID: 1\n"
            "Customer Name: Vương Hữu Lộc\n"
            "Phone: 0123456789\n"
            "Address: Hà Nội\n"
            "Products:\n"
            "Laptop Lenovo LOQ 15ARP9 - 1 x  16790000 = 16790000\n"
            "Chuột không dây Lenovo ThinkPad - 1 x  290000 = 290000\n"
            "Status: Pending\n"
            "Total Amount: 17080000"
        )
        self.assertEqual(str(self.order), expected_str)

    def test_order_update_status(self):
        self.order.update_status(Order.STATUS_DELIVERING)
        self.assertEqual(self.order.status, Order.STATUS_DELIVERING)
        with self.assertRaises(ValueError):
            self.order.update_status("Invalid status")


class TestManageOrder(unittest.TestCase):
    def setUp(self):
        self.manager = ManageOrder()
        self.products = [
            Product("Laptop Lenovo LOQ 15ARP9", 1, 16790000),
            Product("Chuột không dây Lenovo ThinkPad", 1, 290000),
        ]
        self.order = Order(1, "Vương Hữu Lộc", "0123456789", "Hà Nội", self.products)
        self.manager.add_order(self.order)

    def test_add_order(self):
        self.assertEqual(len(self.manager.orders), 1)
        self.assertEqual(self.manager.orders[0].order_id, 1)

    def test_edit_order(self):
        self.manager.edit_order(1, new_customer_name="Vương Hữu Lộc 2")
        self.assertEqual(self.manager.orders[0].customer_name, "Vương Hữu Lộc 2")

    def test_delete_order(self):
        self.manager.delete_order(1)
        self.assertEqual(len(self.manager.orders), 0)

    def test_find_order_by_id(self):
        order = self.manager.find_order_by_id(1)
        self.assertEqual(order, self.order)

    def test_find_order_by_phone(self):
        orders = self.manager.find_order_by_phone("0123456789")
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].customer_name, "Vương Hữu Lộc")

    def test_display_orders_by_status(self):
        orders = self.manager.display_orders_by_status(Order.STATUS_PENDING)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].status, self.order.status)

    def test_caculate_total_revenue(self):
        self.assertEqual(
            self.manager.caculate_total_revenue(), 0
        )  # No "Delivered" orders yet
        self.order.update_status(Order.STATUS_DELIVERED)
        self.assertEqual(self.manager.caculate_total_revenue(), 17080000)

    def test_sort_orders_by_total_amount(self):
        new_order = Order(2, "Vương Hữu Lộc", "0123456789", "Hà Nội", self.products)
        self.manager.add_order(new_order)
        sorted_orders = self.manager.sort_orders_by_total_amount(ascending=True)
        self.assertEqual(sorted_orders[0].order_id, 1)
        self.assertEqual(sorted_orders[1].order_id, 2)

    def test_get_pending_orders(self):
        pending_orders = self.manager.get_pending_orders()
        self.assertEqual(len(pending_orders), 1)
        self.assertEqual(pending_orders[0].status, Order.STATUS_PENDING)

    def test_get_top_selling_products(self):
        self.order.update_status(Order.STATUS_DELIVERED)
        top_selling_products = self.manager.get_top_selling_products(top_n=1)
        self.assertEqual(top_selling_products[0][0], "Laptop Lenovo LOQ 15ARP9")
        self.assertEqual(top_selling_products[0][1], 1)


if __name__ == "__main__":
    unittest.main()
