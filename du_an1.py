#Viết chương trình (dùng input()):
#Người dùng nhập nhiệt độ thấp nhất và nhiệt độ cao nhất trong ngày
#Dùng linspace tạo ra 24 điểm nhiệt độ chia đều từ thấp nhất đến cao nhất (giả lập nhiệt độ tăng dần suốt 24 giờ)
#Dùng reshape chuyển mảng 24 điểm đó thành 4 hàng, 6 cột (giả lập 4 buổi: sáng sớm, sáng, chiều, tối — mỗi buổi 6 giờ)
#In ra mảng sau khi reshape
#Dùng axis (đã học) để tính nhiệt độ trung bình của từng buổi (mỗi hàng là 1 buổi)
#Tìm xem buổi nào có nhiệt độ trung bình cao nhất (dùng argmax)
import numpy as np 
nguoi_dung=float(input('nhập nhiệt độ thấp nhất:   '))
nguoi_dung1=float(input('nhập nhiệt độ cao nhất:  '))
a=np.linspace(nguoi_dung,nguoi_dung1,num=24)
b=np.reshape(a,(4,6))
print(b)
trung_binh=np.mean(b,axis=1)
nhiet_do_cao_nhat=np.argmax(trung_binh)
print(trung_binh)
print(nhiet_do_cao_nhat)