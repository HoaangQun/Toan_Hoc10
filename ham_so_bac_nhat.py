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
        return a * x + b  # Phép biến đổi
    
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