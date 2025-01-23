require 'gnuplot'

def nhap_so_thuc(mo_ta)
  loop do
    print mo_ta
    begin
      return Float(gets.chomp)
    rescue ArgumentError
      puts "Vui lòng nhập một số hợp lệ!"
    end
  end
end

def ve_do_thi(x_values, y_values, title, label, color)
  Gnuplot.open do |gp|
    Gnuplot::Plot.new(gp) do |plot|
      plot.title title
      plot.xlabel 'x'
      plot.ylabel 'y'
      plot.grid
      plot.style 'data lines'
      plot.data << Gnuplot::DataSet.new([x_values, y_values]) do |ds|
        ds.with = "lines lc rgb '#{color}'"
        ds.title = label
      end
    end
  end
end

def ham_so_bac_nhat
  puts "Hàm số bậc nhất: y = ax + b (a != 0)"
  a = nhap_so_thuc("Nhập hệ số a (a != 0): ")
  while a == 0
    puts "Hệ số a không được bằng 0!"
    a = nhap_so_thuc("Nhập lại hệ số a: ")
  end
  b = nhap_so_thuc("Nhập hằng số b: ")

  puts "Hàm số: y = #{a}x + #{b}"
  if a > 0
    puts "Hàm số đồng biến."
  else
    puts "Hàm số nghịch biến."
  end

  puts "Giao với trục tung tại: (0, #{b})"

  x_values = (-10..10).step(0.1).to_a
  y_values = x_values.map { |x| a * x + b }
  ve_do_thi(x_values, y_values, "Đồ thị hàm số bậc nhất", "y = #{a}x + #{b}", "green")

  x = nhap_so_thuc("Nhập giá trị x để tính y: ")
  y = a * x + b
  puts "Với x = #{x}, y = #{y}"
end

def ham_so_bac_hai
  puts "Hàm số bậc hai: y = ax^2 + bx + c (a != 0)"
  a = nhap_so_thuc("Nhập hệ số a (a != 0): ")
  while a == 0
    puts "Hệ số a không được bằng 0!"
    a = nhap_so_thuc("Nhập lại hệ số a: ")
  end
  b = nhap_so_thuc("Nhập hệ số b: ")
  c = nhap_so_thuc("Nhập hằng số c: ")

  puts "Hàm số: y = #{a}x^2 + #{b}x + #{c}"

  delta = b**2 - 4 * a * c
  puts "Delta = #{delta}"
  if delta > 0
    puts "Phương trình có 2 nghiệm phân biệt."
  elsif delta == 0
    puts "Phương trình có 1 nghiệm kép."
  else
    puts "Phương trình vô nghiệm."
  end

  dinh_x = -b / (2.0 * a)
  dinh_y = -delta / (4.0 * a)
  puts "Đỉnh parabol: (#{dinh_x}, #{dinh_y})"
  puts "Giao với trục tung tại: (0, #{c})"

  x_values = (dinh_x - 5..dinh_x + 5).step(0.1).to_a
  y_values = x_values.map { |x| a * x**2 + b * x + c }
  ve_do_thi(x_values, y_values, "Đồ thị hàm số bậc hai", "y = #{a}x^2 + #{b}x + #{c}", "blue")

  x = nhap_so_thuc("Nhập giá trị x để tính y: ")
  y = a * x**2 + b * x + c
  puts "Với x = #{x}, y = #{y}"
end

def menu
  loop do
    puts "\n1. Hàm số bậc nhất"
    puts "2. Hàm số bậc hai"
    puts "3. Thoát"
    print "Lựa chọn: "
    lua_chon = gets.chomp
    case lua_chon
    when '1'
      ham_so_bac_nhat
    when '2'
      ham_so_bac_hai
    when '3'
      puts "Tạm biệt!"
      break
    else
      puts "Lựa chọn không hợp lệ!"
    end
  end
end

menu

