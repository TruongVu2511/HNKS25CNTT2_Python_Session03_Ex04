print("\n --- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI --- \n")
while True :
    human_resources = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    if human_resources > 0 :
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {human_resources} nhân sự mới !")
        break
    else :
        print(f"[LỖI] Số lượng không hợp lệ ! Vui lòng nhập một con số lớn hơn 0")
    
print("\n --- CHƯƠNG TRÌNH KẾT THÚC --- \n")


