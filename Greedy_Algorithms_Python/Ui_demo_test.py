import tkinter as tk

NAMES = ["4 giường T2 (1609K)", "6 giường T1 (1444K)", "6 giường T3 (1146K)",
         "Ngồi mềm (966K)", "Ngồi cứng (744K)", "Ghế phụ (524K)"]
PRICES = [1609, 1444, 1146, 966, 744, 524]
DENOMS = [500, 200, 100, 50, 20, 10, 5, 2, 1]   # đơn vị: K VND

def fmt(n): return f"{n:,}".replace(",", ".")  # 1.488 -> 1.488 (dấu . ngăn cách nghìn)
def get_int(e, default=0):
    try: return int(e.get())
    except: return default

def current_cost():
    i = opt.curselection()[0] if opt.curselection() else 0
    qty = max(get_int(e_qty, 1), 1)
    return PRICES[i] * qty, i, qty

def update_bill(*_):
    cost, i, qty = current_cost()
    bill_lbl.config(text=f"Số tiền tối thiểu cần thanh toán: {fmt(cost)} K\n"
                         f"({PRICES[i]} x {qty})")

def calc():
    if not opt.curselection(): opt.select_set(0)   # chọn mặc định nếu chưa chọn
    cost, i, qty = current_cost()
    paid = get_int(e_paid, 0)
    if paid < cost:
        out.config(text="❌ Lỗi: Tiền khách đưa phải ≥ hóa đơn!")
        return
    change = paid - cost
    lines, cnt = [], 0
    for d in DENOMS:
        k = change // d
        if k: lines.append(f"{k} x {d}K"); cnt += k; change %= d
    out.config(text=(f"--- HÓA ĐƠN ---\n"
                     f"Loại vé: {NAMES[i]}\nSố lượng: {qty}\n"
                     f"Tối thiểu: {fmt(cost)} K\nKhách đưa: {fmt(paid)} K\n"
                     f"Tiền thừa: {fmt(paid - cost)} K\n\n--- TRẢ LẠI ---\n"
                     + ("\n".join(lines) if lines else "0") + f"\nTổng số tờ: {cnt}"))

root = tk.Tk(); root.title("Máy bán vé SE7 (Greedy)")
root.geometry("640x380")

# Trái: danh sách vé
left = tk.Frame(root, padx=10, pady=10); left.pack(side="left", fill="y")
tk.Label(left, text="Bảng giá vé", font=("Arial", 12, "bold")).pack(anchor="w")
opt = tk.Listbox(left, height=6, exportselection=False, width=28)
[opt.insert(tk.END, s) for s in NAMES]; opt.pack(pady=5)
opt.select_set(0)  # <-- CHỌN MẶC ĐỊNH

# Phải: nhập liệu + bill + kết quả
right = tk.Frame(root, padx=10, pady=10); right.pack(side="right", fill="both", expand=True)

tk.Label(right, text="Số lượng vé:").grid(row=0, column=0, sticky="w")
e_qty = tk.Entry(right, width=10); e_qty.insert(0, "1"); e_qty.grid(row=0, column=1, sticky="w", pady=5)

tk.Label(right, text="Tiền khách đưa (K):").grid(row=1, column=0, sticky="w")
e_paid = tk.Entry(right, width=10); e_paid.grid(row=1, column=1, sticky="w", pady=5)

bill_lbl = tk.Label(right, justify="left", anchor="w", fg="#006400", font=("Consolas", 10, "bold"))
bill_lbl.grid(row=2, column=0, columnspan=2, sticky="w", pady=(6, 6))

tk.Button(right, text="Tính tiền thừa", command=calc).grid(row=3, column=0, columnspan=2, sticky="ew", pady=8)

out = tk.Label(right, justify="left", anchor="nw", font=("Consolas", 10))
out.grid(row=4, column=0, columnspan=2, sticky="nsew")

# cập nhật bill khi đổi lựa chọn/nhập số lượng
opt.bind("<<ListboxSelect>>", update_bill)
e_qty.bind("<KeyRelease>", update_bill)
update_bill()  # hiển thị bill ngay khi mở app

root.mainloop()
