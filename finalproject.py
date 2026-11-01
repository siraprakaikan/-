# เมนูอาหารและราคา
menu = {
    "1": {"name": "ข้าวผัดกะเพรา", "price": 50},
    "2": {"name": "ข้าวไข่เจียว", "price": 35},
    "3": {"name": "ก๋วยเตี๋ยว", "price": 45},
    "4": {"name": "ชามะนาว", "price": 20}
}

# ฟังก์ชันที่ 1: แสดงเมนูอาหาร
def display_menu(menu_data):
    print("=== เมนูอาหาร ===")
    for key, item in menu_data.items():
        print(f"{key}. {item['name']} - {item['price']} บาท")
    print("==================")
    print("พิมพ์ 'exit' เพื่อจบการสั่งซื้อ\n")

# ฟังก์ชันที่ 2: รับค่าและตรวจสอบจำนวนจาน (จัดการ ValueError)
def get_quantity(item_name):
    quantity_input = input(f"ต้องการสั่ง '{item_name}' กี่จาน: ")
    # หากผู้ใช้กรอกข้อความแทนตัวเลข int() จะเกิด ValueError
    quantity = int(quantity_input)

    if quantity <= 0:
        print("จำนวนต้องมากกว่า 0 จาน\n")
        return 0
    return quantity

# ฟังก์ชันที่ 3: รับออเดอร์จากผู้ใช้ (จัดการ KeyError)
def process_order(menu_data, choice):
    # หากเลือกเลขเมนูไม่มีใน dict จะเกิด KeyError
    if choice not in menu_data:
        raise KeyError("ไม่มีหมายเลขเมนูนี้ในรายการ")

    item_name = menu_data[choice]["name"]
    price = menu_data[choice]["price"]

    # เรียกใช้ฟังก์ชันรับจำนวน
    quantity = get_quantity(item_name)
    if quantity > 0:
        subtotal = price * quantity
        print(f"เพิ่ม {item_name} จำนวน {quantity} รายการ เรียบร้อยแล้ว!\n")
        return item_name, quantity, subtotal

    return None

# ฟังก์ชันที่ 4: สรุปรายการสั่งซื้อและราคารวม
def print_receipt(cart):
    print("\n==============================")
    print("สรุปรายการสั่งซื้อของคุณ:")
    total_price = 0

    if cart:
        for name, qty, price in cart:
            print(f"- {name} x{qty} = {price} บาท")
            total_price += price
        print(f"\nราคารวมทั้งหมด: {total_price} บาท")
    else:
        print("ไม่มีรายการสั่งซื้อ")
    print("==============================")

# --- โครงสร้างหลักของโปรแกรม (Main Loop) ---
def main():
    cart = []
    display_menu(menu)

    while True:
        choice = input("เลือกหมายเลขเมนูที่ต้องการสั่ง: ")

        if choice.lower() == "exit":
            break

        try:
            order = process_order(menu, choice)
            if order:
                cart.append(order)

        except KeyError:
            print("ข้อผิดพลาด: เลือกหมายเลขเมนูไม่ถูกต้อง กรุณาเลือกตามเลขที่มีในเมนู\n")

        except ValueError:
            print("ข้อผิดพลาด: กรุณากรอกจำนวนเป็นตัวเลขปรกติเท่านั้น (เช่น 1, 2, 3)\n")

    print_receipt(cart)

main()