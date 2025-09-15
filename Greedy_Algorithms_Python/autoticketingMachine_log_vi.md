# Máy Bán Vé Tự Động - Nhật Ký Chương Trình

## Tổng Quan Chương Trình
**Tệp:** `autoticketingMachine.py`  
**Mục đích:** Hệ thống mua vé tàu tự động cho tuyến Hà Nội - Sài Gòn (Tàu SE7)  
**Thuật toán sử dụng:** Thuật toán tham lam để tính tiền thừa  
**Ngày:** 14 tháng 9, 2025  

## Cấu Trúc và Luồng Chương Trình

### 1. Hiển Thị Bảng Giá Vé
```
Hiển thị các loại vé có sẵn với giá:
- Loại 1: Nằm khoang 4 điều hoà T2 - 1,609,000 VNĐ
- Loại 2: Nằm khoang 6 điều hoà T1 - 1,444,000 VNĐ  
- Loại 3: Nằm khoang 6 điều hoà T3 - 1,146,000 VNĐ
- Loại 4: Ngồi mềm điều hoà - 966,000 VNĐ
- Loại 5: Ngồi cứng điều hoà - 744,000 VNĐ
- Loại 6: Ghế phụ - 524,000 VNĐ
```

### 2. Quy Trình Xác Thực Đầu Vào

#### Chọn Loại Vé
- **Phạm vi nhập:** 1-6 (số nguyên)
- **Xác thực:** Lặp cho đến khi nhập hợp lệ (1 ≤ userChoice ≤ 6)
- **Xử lý lỗi:** Nhắc người dùng nhập lại nếu không hợp lệ

#### Chọn Số Lượng Vé  
- **Phạm vi nhập:** Chỉ số nguyên dương
- **Xác thực:** Lặp cho đến khi numberOfTicket > 0
- **Xử lý lỗi:** Hiển thị "Số vé phải lớn hơn 0!"

### 3. Logic Tính Giá
Sử dụng câu lệnh `match-case` của Python (Python 3.10+):
```python
Ánh xạ giá:
- Trường hợp 1 → 1609K VNĐ
- Trường hợp 2 → 1444K VNĐ  
- Trường hợp 3 → 1146K VNĐ
- Trường hợp 4 → 966K VNĐ
- Trường hợp 5 → 744K VNĐ
- Mặc định → 524K VNĐ
```

**Công thức tổng chi phí:** `cost = ticketPrice × numberOfTicket`

### 4. Xử Lý Thanh Toán

#### Nhập Số Tiền Thanh Toán
- **Yêu cầu:** paid ≥ cost
- **Xác thực:** Lặp cho đến khi nhận đủ tiền thanh toán
- **Xử lý lỗi:** "Số tiền chưa đủ, vui lòng nhập lại!"

#### Tính Tiền Thừa
- **Công thức:** `change = paid - cost`
- **Thuật toán:** Phương pháp tham lam sử dụng mệnh giá lớn nhất trước

### 5. Triển Khai Thuật Toán Tham Lam Đổi Tiền

#### Mảng Mệnh Giá
```python
denoms = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # đơn vị nghìn VNĐ
```

#### Các Bước Thuật Toán
1. **Khởi tạo:** Danh sách phân tích rỗng, bộ đếm = 0
2. **Với mỗi mệnh giá:**
   - Tính: `temp = change // denomination`
   - Cập nhật: `change %= denomination`
   - Tăng: `counter += temp`
   - Ghi lại: Nếu temp > 0, thêm vào danh sách phân tích
3. **Đầu ra:** Tổng số tờ và phân tích chi tiết

### 6. Định Dạng Đầu Ra

#### Hiển Thị Hóa Đơn
```
Định dạng: "Hóa đơn của bạn: [giá] x [số lượng] = [tổng] K"
Ví dụ: "Hóa đơn của bạn: 1609 x 2 = 3218 K"
```

#### Phân Tích Tiền Thừa
```
Định dạng: "Số tờ cần trả lại cho khách: [số lượng] tờ"
Định dạng chi tiết: "- [số lượng] x [mệnh giá]K"
Ví dụ: 
- 3 x 500K
- 1 x 200K
- 1 x 50K
```

## Tính Năng Chính

### 1. Xác Thực Đầu Vào
- **Xử lý lỗi mạnh mẽ:** Tất cả đầu vào của người dùng được xác thực với thông báo lỗi phù hợp
- **An toàn kiểu:** Chuyển đổi số nguyên với xử lý ngoại lệ thích hợp được mong đợi
- **Kiểm tra phạm vi:** Đảm bảo phạm vi đầu vào logic cho tất cả tham số

### 2. Hiệu Quả Thuật Toán Tham Lam
- **Độ phức tạp thời gian:** O(n) với n = số lượng mệnh giá (9)
- **Độ phức tạp không gian:** O(n) để lưu trữ phân tích
- **Tối ưu:** Cung cấp số lượng tờ tiền tối thiểu để trả lại

### 3. Trải Nghiệm Người Dùng
- **Hướng dẫn rõ ràng:** Giao diện tiếng Việt cho người dùng địa phương
- **Phản hồi tức thì:** Xác thực thời gian thực và thông báo lỗi
- **Đầu ra chi tiết:** Tóm tắt giao dịch hoàn chỉnh với phân tích tiền thừa

## Sơ Đồ Luồng Thực Thi Chương Trình
```
BẮT ĐẦU
  ↓
Hiển thị Bảng Giá Vé
  ↓
Nhận Loại Vé (1-6) [Lặp cho đến khi hợp lệ]
  ↓
Nhận Số Lượng Vé [Lặp cho đến khi > 0]
  ↓
Tính Tổng Chi Phí
  ↓
Nhận Số Tiền Thanh Toán [Lặp cho đến khi >= chi phí]
  ↓
Tính Tiền Thừa
  ↓
Áp dụng Thuật Toán Tham Lam để Phân Tích Tiền Thừa
  ↓
Hiển thị Kết Quả (Số tờ + phân tích)
  ↓
KẾT THÚC
```

## Ghi Chú Triển Khai Kỹ Thuật

### Tính Năng Ngôn Ngữ Được Sử Dụng
- **Câu lệnh Match-Case:** Cú pháp Python hiện đại (3.10+)
- **Định dạng F-string:** Để hiển thị đầu ra sạch sẽ
- **List Comprehension:** Để thu thập phân tích
- **Phép chia nguyên:** Toán tử `//` để đếm tờ chính xác
- **Phép chia lấy dư:** Toán tử `%` để tính tiền thừa còn lại

### Khía Cạnh Chất Lượng Code
- **Trách nhiệm đơn lẻ:** Mỗi phần xử lý một nhiệm vụ cụ thể
- **Xác thực đầu vào:** Kiểm tra lỗi toàn diện
- **Tên biến rõ ràng:** Cấu trúc code tự giải thích
- **Định dạng nhất quán:** Bố cục code được tổ chức tốt

## Cải Tiến Tiềm Năng
1. **Xử lý ngoại lệ:** Thêm try-catch cho đầu vào không phải số nguyên
2. **Cấu hình:** Tệp cấu hình giá bên ngoài
3. **Ghi log:** Thêm ghi log giao dịch vào tệp
4. **Quốc tế hóa:** Hỗ trợ đa ngôn ngữ
5. **Giao diện GUI:** Tùy chọn giao diện đồ họa

## Phân Tích Thuật Toán
Phương pháp tham lam hoạt động tối ưu cho hệ thống tiền tệ Việt Nam này vì:
- Các mệnh giá tuân theo một mẫu trong đó các mệnh giá lớn hơn là bội số hoặc gần bội số của các mệnh giá nhỏ hơn
- Không có sự kết hợp mệnh giá nào có thể tạo ra giải pháp hiệu quả hơn việc sử dụng mệnh giá lớn nhất có thể trước
- Thiết kế tiền tệ tiêu chuẩn đảm bảo tính tối ưu của thuật toán tham lam

## So Sánh Với Phiên Bản Java
Để tham khảo, có thể so sánh với tệp `autoTicketingMachine.java` trong thư mục `Greedy_Algorithms_Java/`:

### Điểm Khác Biệt Chính:
- **Cú pháp:** Python đơn giản hơn, ít dài dòng hơn
- **Nhập liệu:** Python sử dụng `input()`, Java sử dụng `Scanner`
- **Switch/Match:** Python có match-case hiện đại, Java có switch truyền thống
- **Kiểu dữ liệu:** Python linh hoạt hơn với kiểu dữ liệu động

### Điểm Tương Đồng:
- **Logic thuật toán:** Cùng thuật toán tham lam
- **Luồng chương trình:** Cùng cấu trúc điều khiển
- **Mục đích:** Cùng chức năng bán vé tự động

---
**Nhật ký được tạo:** 14 tháng 9, 2025  
**Phiên bản chương trình:** Python 3.10+  
**Trạng thái:** Hoạt động và Hoàn chỉnh