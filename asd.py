
def display_menu(menu_dict):
    print("---------- MENU ----------")
    for key, (name, price) in menu_dict.items():
        print(f"{key}. {name} - {price} บาท")
    print("--------------------------")

def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("กรุณากรอกเฉพาะตัวเลขเท่านั้น!")

def calculate_total(price, quantity):
    return price * quantity

def process_payment(total_amount):
    while True:
        try:
            money = int(input("\nรับเงิน: "))
            change = money - total_amount
            if change >= 0:
                print(f"เงินทอน: {change} บาท")
                break
            else:
                print(f"เงินไม่พอ ขาดอีก {-change} บาท กรุณาลองใหม่")
        except ValueError:
            print("กรุณากรอกจำนวนเงินเป็นตัวเลขเท่านั้น!")

menu = {
    1: ("ข้าวกะเพรา", 50),
    2: ("ข้าวผัด", 45),
    3: ("ผัดไทย", 50),
    4: ("ก๋วยเตี๋ยว", 40)
}

display_menu(menu)
menu_id = get_number_input("เลือกเมนู (1-4): ")

if menu_id in menu:
    quantity = get_number_input("จำนวน: ")
    name, price = menu[menu_id]
    
    total = calculate_total(price, quantity)

    print("\n--- รายการอาหาร ---")
    print(f"เมนู: {name}")
    print(f"ราคาต่อจาน: {price} บาท")
    print(f"จำนวน: {quantity}")
    print(f"ราคารวม: {total} บาท")

    process_payment(total)
else:
    print("ไม่พบเมนูที่เลือก")