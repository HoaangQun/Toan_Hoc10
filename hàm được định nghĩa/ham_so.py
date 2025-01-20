def ham_so_bac_nhat():
    print(f"y = ax + b (a!=0)")
    while True:
        a = int(input("Nhập vào hệ số (a): "))
        if a == 0:
            print("Hệ số a bắt buộc phải != 0!")
        else:
            break
    print(f"y = {a}x + b")
    b = int(input("Nhập vào hằng số (b): "))
    print(f"y = {a}x + {b}")
    print("------")
    
    def tinh_ham_bac_nhat(x):
        return a * x + b
    
    x = int(input("Nhập vào x: "))
    y = tinh_ham_bac_nhat(x)
    print(f"Kết quả y cho ra là: {y}")
    
    # Xác định tính đồng biến, nghịch biến
    if a > 0:
        print("Hàm số trên đồng biến (hướng dốc lên trên).")
    elif a < 0:
        print("Hàm số trên nghịch biến (hướng dốc xuống dưới).")
    
    # Xác định giao điểm với trục tọa độ
    if b == 0:
        print("Đường thẳng trên đi qua gốc toạ độ.")
    print(f"Hàm số trên giao với trục tung tại điểm có toạ độ (0 , {b})")
    print("------")
    
    # Tính tập nghiệm cho các giá trị mẫu
    x_values = [-(x), -(x / 2), 0, x / 2, x]
    y_values = [tinh_ham_bac_nhat(val) for val in x_values]
    
    print(f"Tập biến độc lập: {x_values}")
    print(f"Tập biến phụ thuộc: {y_values}")


def ham_so_bac_hai():
    print ( f"y = ax^2 + bx + c (a!=0)")
    while True:
        a = int(input("Nhập vào hệ số (a): "))
        if a == 0:
            print("Hệ số a bắt buộc phải != 0!")
        else:
            break
    print ( f"y = {a}x^2 + bx + c")
    b,c = map (int, input ("Nhập vào 2 hằng số (b,c): "))
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
    print ("Giao với trục tung tại (0 , {c})")

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


