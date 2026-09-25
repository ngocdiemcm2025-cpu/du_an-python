def tu_xuat_hien_nhieu_nhat(doan_van):
    tach = doan_van.split()
    dem_tu = {}   # dictionary rỗng để lưu số lần đếm
    for tu in tach:
        if tu in dem_tu:
              dem_tu[tu]+=1
        else:
            dem_tu[tu]=1
    tu_nhieu_nhat = max(dem_tu, key=dem_tu.get)
    return tu_nhieu_nhat
