ticket = """
Bảng giá vé Hà Nội - Sài Gòn của tàu SE7
1: Nằm khoang 4 điều hoà T2 : 1,609,000đ
2: Nằm khoang 6 điều hoà T1 : 1,444,000đ
3: Nằm khoang 6 điều hoà T3 : 1,146,000đ
4: Ngồi mềm điều hoà        : 966,000đ
5: Ngồi cứng điều hoà       : 744,000đ
6: Ghế phụ                  : 524,000đ
"""
print(ticket)

# chọn loại vé
while True:
    userChoice = int(input("Hãy nhập vào lựa chọn của bạn (1–6): ")) #py tự tạo biến userChoice nên không cần phải tạo trước biến ở ngoài
    if 1 <= userChoice <= 6:
        break
    print("Hãy nhập lại lựa chọn của bạn!")

# số lượng vé
while True:
    numberOfTicket = int(input("Hãy nhập vào số lượng vé bạn muốn mua: "))
    if numberOfTicket > 0:
        break
    print("Số vé phải lớn hơn 0!")

# giá vé theo lựa chọn (đơn vị: K VND)
match userChoice:
    case 1: ticketPrice = 1609
    case 2: ticketPrice = 1444
    case 3: ticketPrice = 1146
    case 4: ticketPrice = 966
    case 5: ticketPrice = 744
    case _: ticketPrice = 524

cost = ticketPrice * numberOfTicket
print(f"Hóa đơn của bạn: {ticketPrice} x {numberOfTicket} = {cost} K")

# thanh toán
while True:
    paid = int(input(f"Nhập số tiền thanh toán (>= {cost} K): "))
    if paid >= cost:
        break
    print("Số tiền chưa đủ, vui lòng nhập lại!")

# đổi tiền
change = paid - cost
print(f"Số tiền cần trả lại: {change} K")

denoms = [500, 200, 100, 50, 20, 10, 5, 2, 1]
breakdown = []
cnt = 0

for d in denoms:
    temp = change // d
    change %= d
    cnt += temp
    if temp > 0:
        breakdown.append(f"{temp} x {d}K")

print(f"Số tờ cần trả lại cho khách: {cnt} tờ")

if cnt != 0 : 
    print("Chi tiết:")
    for line in breakdown:
        print(" -", line)
