import pandas as pd
import random
# Sinh dữ liệu tự động
students = []
for i in range(1, 101):
    ho = random.choice(["Nguyen", "Tran", "Le", "Pham", "Hoang"])
    ten_dem = random.choice(["Van", "Thi"])
    ten = random.choice(["An", "Bich", "Cuong", "Dao", "Duc", "Hoa", "Hung", "Lan", "Long", "Mai", 
                         "Minh", "Nga", "Nam", "Oanh", "Phuc", "Quyen", "Son", "Thao", "Tien", "Trang"])
    ho_ten = f"{ho} {ten_dem} {ten}"
    mssv = f"SV{i:03d}"
    chieu_cao = random.randint(157, 182)
    students.append({"HoTen": ho_ten, "MSSV": mssv, "ChieuCao": chieu_cao})

# Tạo DataFrame
df = pd.DataFrame(students)

# Xuất ra CSV
df.to_csv("dataset_sinhvien.csv", index=False)

print(df)

import pandas as pd
import matplotlib.pyplot as plt
import random

# Sinh dữ liệu mẫu
students = []
for i in range(1, 101):
    ho = random.choice(["Nguyen", "Tran", "Le", "Pham", "Hoang"])
    ten_dem = random.choice(["Van", "Thi"])
    ten = random.choice(["An", "Bich", "Cuong", "Dao", "Duc", "Hoa", "Hung", "Lan", "Long", "Mai",
                         "Minh", "Nga", "Nam", "Oanh", "Phuc", "Quyen", "Son", "Thao", "Tien", "Trang"])
    ho_ten = f"{ho} {ten_dem} {ten}"
    mssv = f"SV{i:03d}"
    chieu_cao = random.randint(157, 182)
    students.append({"HoTen": ho_ten, "MSSV": mssv, "ChieuCao": chieu_cao})

# Tạo DataFrame
df = pd.DataFrame(students)

# Vẽ biểu đồ histogram
plt.figure(figsize=(8, 5))
plt.hist(df["ChieuCao"], bins=8, color="skyblue", edgecolor="black")
plt.title("Biểu đồ Histogram Chiều Cao Sinh Viên")
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Số lượng sinh viên")
plt.grid(axis="y", alpha=0.3)
plt.show()

