def ham_so_bac_nhat():
    
    import numpy as np
    import matplotlib.pyplot as plt

    print(f"y = ax + b (a!=0)")
    while True:
        a = float(input("Nhập vào hệ số (a): "))
        if a == 0:
            print("Hệ số a bắt buộc phải != 0!")
        else:
            break
    print(f"y = {a}x + b")
    b = float(input("Nhập vào hằng số (b): "))
    print(f"y = {a}x + {b}")

    # Xác định tính đồng biến, nghịch biến
    if a > 0:
        print("Hàm số trên đồng biến (hướng dốc lên trên).")
    elif a < 0:
        print("Hàm số trên nghịch biến (hướng dốc xuống dưới).")
    
    # Xác định giao điểm với trục tọa độ
    if b == 0:
        print("Đường thẳng trên đi qua gốc toạ độ.")
    print(f"Hàm số trên giao với trục tung tại điểm có toạ độ (0 , {b})")

    # Xác định tập giá trị x và tính y
    x_values = np.linspace(-10, 10, 100)  # Giá trị x từ -10 đến 10
    y_values = a * x_values + b

    # Vẽ đồ thị
    plt.figure(figsize=(4, 3))
    plt.plot(x_values, y_values, label=f'y = {a}x + {b}', color='green')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Trục Ox
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Trục Oy
    plt.title('Đồ thị hàm số bậc nhất', fontsize=12)
    plt.xlabel('x', fontsize=11)
    plt.ylabel('y', fontsize=11)
    plt.legend(fontsize=11)
    plt.grid(alpha=0.4)
    plt.show()

    print("------")
    
    def tinh_ham_bac_nhat(x):
        return a * x + b
    
    x = int(input("Nhập vào x: "))
    y = tinh_ham_bac_nhat(x)
    print(f"Kết quả y cho ra là: {y}")
    
    print("------")
    
    # Tính tập nghiệm cho các giá trị mẫu
    x_values = [-(x), -(x / 2), 0, x / 2, x]
    y_values = [tinh_ham_bac_nhat(val) for val in x_values]
    
    print(f"Tập biến độc lập: {x_values}")
    print(f"Tập biến phụ thuộc: {y_values}")


def ham_so_bac_hai():
    
    import numpy as np
    import matplotlib.pyplot as plt

    print ( f"y = ax^2 + bx + c (a!=0)")
    while True:
        a = float(input("Nhập vào hệ số (a): "))
        if a == 0:
            print("Hệ số a bắt buộc phải != 0!")
        else:
            break
    print ( f"y = {a}x^2 + bx + c")
    b = float (input("Nhập vào hằng số b: "))
    print ( f"y = {a}x^2 + {b}x + c")
    c = float (input("Nhập vào hằng số c: "))
    print ( f"y = {a}x^2 + {b}x + {c}")

    Delta = b**2 - 4*a*c
    print ( f"Delta = {Delta}")
    if Delta > 0:
        print ("Phương trình có 2 nghiệm phân biệt (cắt trục x tại 2 điểm)")
    elif Delta == 0:
        print ("Phương trình có 1 nghiệm kép (tiếp xúc với trục x)")
    else:
        print ("Phương trình vô nghiệm (không cắt trục x)")
    if a > 0:
        print ("Hàm số cực tiểu tại đỉnh")
        print ( f"Hàm số trên đồng biến trên khoảng ({-b/(2*a)} , +++)")
        print ( f"Nghịch biến trên khoảng (-++ , {-b/(2*a)})")
        print ( f"Tập giá trị = [{-(Delta/(4*a))} , +++)")
    if a < 0:
        print ("Hàm số cực đại tại đỉnh ")
        print ( f"Hàm số trên đồng biến trên khoảng (-++ , {-b/(2*a)})")
        print ( f"Nghịch biến trên khoảng ({-b/(2*a)} , +++)")
        print ( f"Tập giá trị = (-++ , {-(Delta/(4*a))}]")
    
    print ( f"Toạ độ đỉnh parabol: ({-(b/(2*a))} , {-(Delta/(4*a))})")
    print ( f"Giao với trục tung tại (0 , {c})")

    # Xác định tập giá trị x và tính y
    x_values = np.linspace(-10, 10, 100)  # Giá trị x từ -10 đến 10
    y_values = a * x_values**2 + b * x_values + c

    # Vẽ đồ thị
    plt.figure(figsize=(4, 3))
    plt.plot(x_values, y_values, label=f'y = {a}x^2 + {b}x + {c}', color='blue')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Trục Ox
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Trục Oy
    plt.title('Đồ thị hàm số bậc hai', fontsize=12)
    plt.xlabel('x', fontsize=11)
    plt.ylabel('y', fontsize=11)
    plt.legend(fontsize=11)
    plt.grid(alpha=0.4)
    plt.show()

    print ("------")

    def tinh_ham_bac_hai(x):
        return a*x**2 + b*x + c

    x = int(input("Nhập vào x: "))
    y = tinh_ham_bac_hai(x)
    print( f"Kết quả y cho ra là: {y}")
    if x < -(b/(2*a)):
        print ("Hàm số đồng biến")
    elif x > -(b/(2*a)):
        print ("Hàm số nghịch biến")

    x_values = [-(x), -(x / 2), 0, x / 2, x]
    y_values = [tinh_ham_bac_hai(val) for val in x_values]

