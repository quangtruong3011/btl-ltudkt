class Product:
    #Khởi tạo đối tượng sản phẩm.
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name         #Tên sản phẩm
        self.quantity = quantity #Số lượng sản phẩm
        self.price = price       #Đơn giá sản phẩm
    #Tính tổng giá trị sản phẩm (số lượng * giá).
    def get_total_price(self):
        return self.quantity * self.price
    #Chỉnh sửa thông tin sản phẩm.
    def edit_product(self, new_name = None, new_quantity = None, new_price = None):
        if new_name:
            self.name = new_name
        if new_quantity:
            self.quantity = int(new_quantity)
        if new_price:
            self.price = float(new_price)
    #Trả về chuỗi biểu diễn của sản phẩm.
    def __str__(self):
        return (
            f"{self.name} - {self.quantity} x  {self.price} = {self.get_total_price()}"
        )
