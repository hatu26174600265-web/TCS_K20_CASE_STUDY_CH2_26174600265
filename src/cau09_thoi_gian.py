from datetime import datetime

# Phần 1: Lấy thời điểm hiện tại và định dạng chuỗi
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Phần 2: Tính toán khoảng thời gian (thời lượng) giữa 2 mốc
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
# Giải thích sự khác nhau giữa datetime, str và timedelta:
# 1. datetime (<class 'datetime.datetime'>): Đại diện cho một mốc thời gian cụ thể (bao gồm năm, tháng, ngày, giờ, phút, giây). Hỗ trợ các phép toán so sánh hoặc tính toán thời gian.
# 2. str (<class 'str'>): Là chuỗi ký tự văn bản thông thường (được tạo ra từ phương thức strftime), dùng để hiển thị trực quan hoặc lưu trữ chứ không thể thực hiện các phép toán trừ thời gian trực tiếp.
# 3. timedelta (<class 'datetime.timedelta'>): Đại diện cho một khoảng thời gian (khoảng cách chênh lệch giữa hai mốc thời gian), được sinh ra tự động khi lấy kết quả của phép trừ hai đối tượng datetime.