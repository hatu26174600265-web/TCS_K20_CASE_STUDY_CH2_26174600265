# Chương trình tương tác hoàn chỉnh: Nhập thông tin phiên sử dụng, tính toán và in kết quả

# Nhập các giá trị từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_nhap = input("Nhập công suất (W): ")
so_phut_nhap = input("Nhập số phút sử dụng: ")
don_gia_nhap = input("Nhập đơn giá điện/kWh: ")

# Chuyển đổi kiểu dữ liệu phù hợp để tính toán
cong_suat_w = float(cong_suat_nhap)
so_phut = int(so_phut_nhap)
don_gia_kwh = float(don_gia_nhap)

# Tính toán điện năng (kWh) và chi phí (VNĐ)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In đầu ra theo đúng định dạng yêu cầu
print("\n--- THÔNG TIN KẾT QUẢ PHIÊN SỬ DỤNG ---")
print("Mã phiên:", ma_phien)
print("Máy:", ma_may)
print("Điện năng:", dien_nang_kwh)
print("Chi phí:", chi_phi)
# Cập nhật phiên bản v2: Đã hoàn thiện và kiểm thử toàn bộ mã nguồn của chương trình.
