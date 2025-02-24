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
            while (not order_id) or (
                order_id in [order.order_id for order in manager.orders]
            ):
                order_id = input("Mã đơn hàng không hợp lệ hoặc đã tồn tại. Nhập lại: ")
            customer_name = input("Nhập tên khách hàng: ")
            while not customer_name:
                customer_name = input("Tên khách hàng không được để trống. Nhập lại: ")
            phone = input("Nhập số điện thoại: ")
            while (not phone) or (not phone.isdigit()):
                phone = input("Số điện thoại không hợp lệ. Nhập lại: ")
            address = input("Nhập địa chỉ giao hàng: ")
            while not address:
                address = input("Địa chỉ giao hàng không được để trống. Nhập lại: ")
            products = []
            while True:
                name = input("Nhập tên sản phẩm (hoặc 'done' để kết thúc): ")
                if name == "done":
                    break
                quantity = input("Nhập số lượng: ")
                while (not quantity.isdigit()) or (int(quantity) <= 0):
                    quantity = input("Số lượng không hợp lệ. Nhập lại: ")
                quantity = int(quantity)
                while True:
                    price = input("Nhập đơn giá: ")
                    try:
                        price = float(price)
                        if price > 0:
                            break
                        else:
                            print("Đơn giá phải lớn hơn 0.")
                    except:
                        print("Đơn giá không hợp lệ.")
                products.append(Product(name, quantity, price))
            order = Order(order_id, customer_name, phone, address, products)
            manager.add_order(order)
            print("Đơn hàng đã được thêm thành công!")

        elif choice == "2":
            order_id = input("Nhập mã đơn hàng cần sửa: ")
            while (not order_id) or (manager.find_order_by_id(order_id) == None):
                order_id = input(
                    "Mã đơn hàng không hợp lệ hoặc không tồn tại. Nhập lại: "
                )
            new_customer_name = input("Nhập tên khách hàng mới (Ấn enter để bỏ qua): ")
            new_phone = input("Nhập số điện thoại mới (Ấn enter để bỏ qua): ")
            while new_phone and (not new_phone.isdigit()):
                new_phone = input("Số điện thoại không hợp lệ. Nhập lại: ")
            new_address = input("Nhập địa chỉ giao hàng mới (Ấn enter để bỏ qua): ")
            new_status = input("Nhập trạng thái mới (Ấn enter để bỏ qua): ")
            while new_status not in [
                Order.STATUS_PENDING,
                Order.STATUS_DELIVERING,
                Order.STATUS_DELIVERED,
                "",
            ]:
                new_status = input("Trạng thái không hợp lệ. Nhập lại: ")

            edit_products = []
            edit_choice = input("Có muốn sửa thông tin sản phẩm không? (y/n): ")
            if edit_choice.lower() == "y":
                while True:
                    product_name = input(
                        "Nhập tên sản phẩm cần sửa (hoặc 'done' để kết thúc): "
                    )
                    if product_name.lower() == "done":
                        break
                    new_name = input("Nhập tên sản phẩm mới (Ấn enter để bỏ qua): ")
                    new_quantity = input("Nhập số lượng mới (Ấn enter để bỏ qua): ")
                    new_price = input("Nhập đơn giá mới (Ấn enter để bỏ qua): ")
                    edit_products.append(
                        (product_name, new_name, new_quantity, new_price)
                    )

            manager.edit_order(
                order_id,
                new_customer_name,
                new_phone,
                new_address,
                edit_products,
                new_status,
            )
            print("Đơn hàng đã được cập nhật thành công!")

        elif choice == "3":
            order_id = input("Nhập mã đơn hàng cần xóa: ")
            while (not order_id) or (manager.find_order_by_id(order_id) == None):
                order_id = input(
                    "Mã đơn hàng không hợp lệ hoặc không tồn tại. Nhập lại: "
                )
            manager.delete_order(order_id)
            print("Đơn hàng đã được xóa thành công!")

        elif choice == "4":
            search_by = input(
                "Tìm kiếm theo mã đơn hàng (id) hoặc số điện thoại (phone): "
            )
            if search_by == "id":
                order_id = input("Nhập mã đơn hàng: ")
                while not order_id:
                    order_id = input("Mã đơn hàng không hợp lệ. Nhập lại: ")
                order = manager.find_order_by_id(order_id)
                if order:
                    print(order)
                else:
                    print("Không tìm thấy đơn hàng!")
            elif search_by == "phone":
                phone = input("Nhập số điện thoại: ")
                while (not phone) or (not phone.isdigit()):
                    phone = input("Số điện thoại không hợp lệ. Nhập lại: ")
                orders = manager.find_order_by_phone(phone)
                if orders:
                    for order in orders:
                        print(order)
                else:
                    print("Không tìm thấy đơn hàng!")
            else:
                print("Lựa chọn không hợp lệ!")

        elif choice == "5":
            status = input("Nhập trạng thái đơn hàng (Chờ xử lý, Đang giao, Đã giao): ")
            orders = manager.display_orders_by_status(status)
            if orders:
                for order in orders:
                    print(order)
            else:
                print("Không có đơn hàng nào!")

        elif choice == "6":
            revenue = manager.calculate_total_revenue()
            print(f"Tổng doanh thu từ các đơn hàng đã giao: {revenue}")

        elif choice == "7":
            ascending = (
                input(
                    "Nhập y để xếp theo từ bé đến lớn/Nhập n để xếp từ lớn đến bé (Mặc định là n): "
                ).lower()
                == "n"
            )
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
