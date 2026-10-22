from datetime import datetime

# 1. Nhập dữ liệu từ người dùng thông qua hàm input()
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_nhap = input("Nhập công suất thiết bị (W): ")
so_phut_nhap = input("Nhập thời gian sử dụng (phút): ")
don_gia_nhap = input("Nhập đơn giá điện (VND/kWh): ")

# 2. Chuyển đổi kiểu dữ liệu phù hợp
cong_suat_w = float(cong_suat_nhap)
so_phut = int(so_phut_nhap)
don_gia_kwh = float(don_gia_nhap)

# 3. Tính toán điện năng, chi phí và kiểm tra điều kiện thời gian bằng toán tử
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
su_dung_tren_60_phut = so_phut > 60

# 4. Lấy thời điểm ghi nhận hiện tại và định dạng chuỗi bằng strftime()
thoi_diem_hien_tai = datetime.now()
thoi_diem_text = thoi_diem_hien_tai.strftime("%Y-%m-%d %H:%M:%S")

# 5. Xuất kết quả định dạng bằng f-string
print("\n--- BÁO CÁO PHIÊN SỬ DỤNG THIẾT BỊ ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {su_dung_tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_text}")