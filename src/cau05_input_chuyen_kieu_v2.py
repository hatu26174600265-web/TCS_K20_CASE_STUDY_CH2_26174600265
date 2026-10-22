# 17. Dùng input() để nhận bốn giá trị và in type() ngay sau khi nhập
ma_may = input("Nhập mã máy: ")
cong_suat_nhap = input("Nhập công suất W: ")
so_phut_nhap = input("Nhập số phút sử dụng: ")
don_gia_nhap = input("Nhập đơn giá điện/kWh: ")

print("\n--- Kiểu dữ liệu gốc từ input() ---")
print("Mã máy:", type(ma_may))
print("Công suất W:", type(cong_suat_nhap))
print("Số phút:", type(so_phut_nhap))
print("Đơn giá:", type(don_gia_nhap))

# 18. Chuyển công suất sang float, số phút sang int và đơn giá sang float
cong_suat_w = float(cong_suat_nhap)
so_phut = int(so_phut_nhap)
don_gia_kwh = float(don_gia_nhap)

# 19. Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Kết quả tính toán sau khi chuyển kiểu ---")
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí điện (VNĐ):", chi_phi, "| Kiểu:", type(chi_phi))
# Cập nhật phiên bản v2: Đã hoàn thiện và kiểm thử toàn bộ mã nguồn của chương trình.
