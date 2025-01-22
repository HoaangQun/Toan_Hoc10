import numpy as np
import matplotlib.pyplot as plt


def nhap_so_thuc(mo_ta):
    while True:
        try:
            return float(input(mo_ta))
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")


def ve_do_thi(x_values, y_values, title, label, color):
    plt.figure(figsize=(6, 4))
    plt.plot(x_values, y_values, label=label, color=color)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Trục Ox
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Trục Oy
    plt.title(title, fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.4)
    plt.show()


def ham_so_bac_nhat():
    print("Hàm số bậc nhất: y = ax + b (a != 0)")
    a = nhap_so_thuc("Nhập hệ số a (a != 0): ")
    while a == 0:
        print("Hệ số a không được bằng 0!")
        a = nhap_so_thuc("Nhập lại hệ số a: ")
    b = nhap_so_thuc("Nhập hằng số b: ")

    print(f"Hàm số: y = {a}x + {b}")
    if a > 0:
        print("Hàm số đồng biến.")
    else:
        print("Hàm số nghịch biến.")

    print(f"Giao với trục tung tại: (0, {b})")

    x_values = np.linspace(-10, 10, 100)
    y_values = a * x_values + b
    ve_do_thi(x_values, y_values, "Đồ thị hàm số bậc nhất", f"y = {a}x + {b}", "green")

    x = nhap_so_thuc("Nhập giá trị x để tính y: ")
    y = a * x + b
    print(f"Với x = {x}, y = {y}")


def ham_so_bac_hai():
    print("Hàm số bậc hai: y = ax^2 + bx + c (a != 0)")
    a = nhap_so_thuc("Nhập hệ số a (a != 0): ")
    while a == 0:
        print("Hệ số a không được bằng 0!")
        a = nhap_so_thuc("Nhập lại hệ số a: ")
    b = nhap_so_thuc("Nhập hệ số b: ")
    c = nhap_so_thuc("Nhập hằng số c: ")

    print(f"Hàm số: y = {a}x^2 + {b}x + {c}")

    delta = b**2 - 4 * a * c
    print(f"Delta = {delta}")
    if delta > 0:
        print("Phương trình có 2 nghiệm phân biệt.")
    elif delta == 0:
        print("Phương trình có 1 nghiệm kép.")
    else:
        print("Phương trình vô nghiệm.")

    dinh_x = -b / (2 * a)
    dinh_y = -delta / (4 * a)
    print(f"Đỉnh parabol: ({dinh_x}, {dinh_y})")
    print(f"Giao với trục tung tại: (0, {c})")

    x_values = np.linspace(dinh_x - 5, dinh_x + 5, 200)
    y_values = a * x_values**2 + b * x_values + c
    ve_do_thi(x_values, y_values, "Đồ thị hàm số bậc hai", f"y = {a}x^2 + {b}x + {c}", "blue")

    x = nhap_so_thuc("Nhập giá trị x để tính y: ")
    y = a * x**2 + b * x + c
    print(f"Với x = {x}, y = {y}")


def menu():
    while True:
        print("\n1. Hàm số bậc nhất")
        print("2. Hàm số bậc hai")
        print("3. Thoát")
        lua_chon = input("Lựa chọn: ")
        if lua_chon == '1':
            ham_so_bac_nhat()
        elif lua_chon == '2':
            ham_so_bac_hai()
        elif lua_chon == '3':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


menu()

