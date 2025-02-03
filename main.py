from models.manageOrder import ManageOrder
from models.order import Order
from models.product import Product


def main():
    manager = ManageOrder()

    while True:
        print("\n1. Thêm mới đơn hàng")
        print("2. Sửa thông tin đơn hàng")
        print("3. Xóa đơn hàng")
        print("4. Tìm kiếm đơn hàng")
        print("5. Hiển thị danh sách đơn hàng theo trạng thái")
        print("6. Tính tổng doanh thu từ các đơn hàng đã giao")
        print("7. Hiển thị danh sách đơn hàng sắp xếp theo tổng tiền")
        print("8. Thống kê danh sách các đơn hàng chờ xử lý hoặc đang giao")
        print("9. Hiển thị danh sách sản phẩm bán chạy nhất")
        print("10. Thoát chương trình")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            order_id = input("Nhập mã đơn hàng: ")
            customer_name = input("Nhập tên khách hàng: ")
            phone = input("Nhập số điện thoại: ")
            address = input("Nhập địa chỉ giao hàng: ")
            products = []
            while True:
                name = input("Nhập tên sản phẩm (hoặc 'done' để kết thúc): ")
                if name == "done":
                    break
                quantity = int(input("Nhập số lượng: "))
                price = float(input("Nhập đơn giá: "))
                products.append(Product(name, quantity, price))
            order = Order(order_id, customer_name, phone, address, products)
            manager.add_order(order)
            print("Đơn hàng đã được thêm thành công!")

        elif choice == "2":
            order_id = input("Nhập mã đơn hàng cần sửa: ")
            new_customer_name = input("Nhập tên khách hàng mới (hoặc bỏ qua): ")
            new_phone = input("Nhập số điện thoại mới (hoặc bỏ qua): ")
            new_address = input("Nhập địa chỉ giao hàng mới (hoặc bỏ qua): ")
            new_status = input("Nhập trạng thái mới (hoặc bỏ qua): ")
            manager.edit_order(
                order_id, new_customer_name, new_phone, new_address, None, new_status
            )
            print("Đơn hàng đã được cập nhật thành công!")

        elif choice == "3":
            order_id = input("Nhập mã đơn hàng cần xóa: ")
            manager.delete_order(order_id)
            print("Đơn hàng đã được xóa thành công!")

        elif choice == "4":
            search_by = input(
                "Tìm kiếm theo mã đơn hàng (id) hoặc số điện thoại (phone): "
            )
            if search_by == "id":
                order_id = input("Nhập mã đơn hàng: ")
                order = manager.find_order_by_id(order_id)
                if order:
                    print(order)
                else:
                    print("Không tìm thấy đơn hàng!")
            elif search_by == "phone":
                phone = input("Nhập số điện thoại: ")
                orders = manager.find_order_by_phone(phone)
                for order in orders:
                    print(order)
            else:
                print("Lựa chọn không hợp lệ!")

        elif choice == "5":
            status = input("Nhập trạng thái đơn hàng (Chờ xử lý, Đang giao, Đã giao): ")
            orders = manager.display_orders_by_status(status)
            for order in orders:
                print(order)

        elif choice == "6":
            revenue = manager.calculate_total_revenue()
            print(f"Tổng doanh thu từ các đơn hàng đã giao: {revenue}")

        elif choice == "7":
            ascending = input("Sắp xếp từ thấp lên cao? (y/n): ").lower() == "y"
            sorted_orders = manager.sort_orders_by_total_amount(ascending)
            for order in sorted_orders:
                print(order)

        elif choice == "8":
            pending_orders = manager.get_pending_orders()
            for order in pending_orders:
                print(order)

        elif choice == "9":
            top_products = manager.get_top_selling_products()
            for product, quantity in top_products:
                print(f"{product}: {quantity}")

        elif choice == "10":
            print("Thoát chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")


if __name__ == "__main__":
    main()
