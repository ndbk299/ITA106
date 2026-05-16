# Bài 1: Khám phá dữ liệu ban đầu

print("Bài 1: Khám phá dữ liệu ban đầu")

import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv(r'D:\FPT\ITA106\Finance_data.csv')

# - Hiển thị 10 dòng dữ liệu đầu tiên
print(df.head(10))

# - Kiểm tra số lượng bản ghi và số lượng thuộc tính
print(df.shape)

# - Kiểm tra kiểu dữ liệu của từng cột
print(df.dtypes)

# - Tính toán các thống kê cơ bản:
# - Giá trị trung bình
print(df.mean())

# - Giá trị lớn nhất và nhỏ nhất
print(df.max())
print(df.min())

# - Độ lệch chuẩn
print(df.std())

# - Trực quan hóa dữ liệu bằng các biểu đồ:
import matplotlib.pyplot as plt

# - Histogram cho các thuộc tính số
df.hist(figsize=(10, 8))
plt.show()

# - Bar chart cho các thuộc tính phân loại
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Bar chart of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()

# Bài 2: Làm sạch dữ liệu

print("Bài 2: Làm sạch dữ liệu")

# - Kiểm tra dữ liệu bị thiếu (Missing Values)
print(df.isnull().sum())

# - Thực hiện xử lý dữ liệu thiếu bằng một trong các phương pháp:
# - Xóa bản ghi
df_dropped = df.dropna()

# - Điền giá trị trung bình hoặc trung vị
df_filled_mean = df.fillna(df.mean())
df_filled_median = df.fillna(df.median())

# - Kiểm tra và loại bỏ các bản ghi trùng lặp
df_no_duplicates = df.drop_duplicates()

# - Chuẩn hóa dữ liệu số (Normalization hoặc Standardization)
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df_scaled = pd.DataFrame(scaler.fit_transform(df[numeric_cols]), columns=numeric_cols)

# - Vẽ boxplot trước và sau khi làm sạch dữ liệu để so sánh
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
df[numeric_cols].boxplot()
plt.title('Boxplot trước khi làm sạch dữ liệu')
plt.subplot(1, 2, 2)
df_scaled.boxplot()
plt.title('Boxplot sau khi làm sạch dữ liệu')
plt.show()  

# Bài 3: Phát hiện Outliers trong dữ liệu

print("Bài 3: Phát hiện Outliers trong dữ liệu")

# - Áp dụng phương pháp IQR (Interquartile Range) để xác định outliers
numeric_df = df[numeric_cols]
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).sum()
print("Số lượng outliers theo phương pháp IQR:")
print(outliers)

# - Vẽ các biểu đồ sau:
# - Boxplot
numeric_df.boxplot()
plt.title('Boxplot để phát hiện outliers')
plt.show()

# - Scatter plot
if len(numeric_cols) >= 2:
    plt.scatter(numeric_df[numeric_cols[0]], numeric_df[numeric_cols[1]])
    plt.title('Scatter plot để phát hiện outliers')
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.show()
else:
    print("Không đủ cột số để vẽ scatter plot.")

# - Phân tích ảnh hưởng của outliers đối với mô hình học máy
print("Phân tích ảnh hưởng của outliers đối với mô hình học máy:")
# Outliers có thể làm mô hình học máy bị lệch (ví dụ hồi quy tuyến tính sẽ bị ảnh hưởng mạnh).
# Có thể cân nhắc loại bỏ hoặc biến đổi dữ liệu (log-transform).

# Bài 4: Thiết kế sơ đồ thể hiện các bước sau:
# - Thu thập dữ liệu
# - Làm sạch dữ liệu
# - Khám phá dữ liệu (EDA)
# - Trích xuất đặc trưng (Feature Engineering)
# - Huấn luyện mô hình
# - Đánh giá mô hình

print("Bài 4: Thiết kế sơ đồ:")
fig, ax = plt.subplots(figsize=(10, 6))
steps = ['Thu thập dữ liệu', 'Làm sạch dữ liệu', 'Khám phá dữ liệu (EDA)', 'Trích xuất đặc trưng (Feature Engineering)', 'Huấn luyện mô hình', 'Đánh giá mô hình']
for i, step in enumerate(steps):    
    ax.text(0.5, 1 - i * 0.15, step, ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', edgecolor='black'))
    if i < len(steps) - 1:
        ax.arrow(0.5, 1 - i * 0.15 - 0.05, 0, -0.05, head_width=0.02, head_length=0.02, fc='black', ec='black')
ax.axis('off')
plt.title('Sơ đồ quy trình xử lý dữ liệu và xây dựng mô hình học máy')
plt.show()

