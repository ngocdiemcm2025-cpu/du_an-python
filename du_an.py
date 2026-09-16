
import numpy as np 
while True:
    print("Tính năng 1 tạo danh sách")
    print("Tính năng 2 nhập giá trị vào danh sách")
    lua_chon=input("hãy nhập tính năng mà bạn muốn chọn:     ")

    if lua_chon == "1":
        print("bật tính năng 1")
        cot=int(input("nhập cột:    "))
        hang=int(input("nhập hàng:   "))
        danh_sach=np.zeros((hang,cot))
        print(danh_sach)
    elif lua_chon == "2":
        print("bật tính năng 2")
        cot1=int(input("nhập cột đi:  "))
        hang1=int(input("nhập hàng đi:   "))
        if hang1 < danh_sach.shape[0] and cot1 < danh_sach.shape[1]:
            hang2=int(input("nhập giá trị của hàng:   "))
            danh_sach[hang1,cot1]= hang2
            print(danh_sach)
    elif lua_chon == "0": 
        break