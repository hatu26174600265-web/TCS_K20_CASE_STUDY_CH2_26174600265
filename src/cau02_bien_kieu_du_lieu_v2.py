# Khai báo các biến lưu trữ thông tin phiên sử dụng theo quy tắc snake_case và đúng kiểu dữ liệu
ma_phien = "LAB026"          # Kiểu str
ma_may = "PC12"               # Kiểu str
cong_suat = 250.0             # Kiểu float
thoi_gian = 90                # Kiểu int
trang_thai_hoat_dong = True   # Kiểu bool
ghi_chu = None                # Kiểu NoneType (chưa có)

# In từng giá trị và dùng type() để kiểm tra kiểu dữ liệu
print("Mã phiên:", ma_phien, "-", type(ma_phien))
print("Mã máy:", ma_may, "-", type(ma_may))
print("Công suất:", cong_suat, "-", type(cong_suat))
print("Thời gian:", thoi_gian, "-", type(thoi_gian))
print("Trạng thái hoạt động:", trang_thai_hoat_dong, "-", type(trang_thai_hoat_dong))
print("Ghi chú:", ghi_chu, "-", type(ghi_chu))

# Thay đổi thời gian sử dụng từ 90 thành 120 bằng phép gán lại và in giá trị mới
thoi_gian = 120
print("Thời gian sử dụng mới:", thoi_gian)
# Cập nhật phiên bản v2: Đã hoàn thiện và kiểm thử toàn bộ mã nguồn của chương trình.
