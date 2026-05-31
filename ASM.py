import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# GIAI ĐOẠN 1
print("Giai đoạn 1:")

# Giới thiệu và mô tả dữ liệu, trình bày:
# nguồn dữ liệu 
df = pd.read_csv(r'D:\FPT\ITA106\learnx_user_behavior_dataset_10M.csv')

# số lượng bản ghi
print("Số lượng bản ghi:", len(df))

# các thuộc tính chính
print("Các thuộc tính chính:", df.columns)

# Làm sạch dữ liệu, dữ liệu cần được kiểm tra:
# giá trị thiếu (missing values) 
print("Giá trị thiếu:")
print(df.isnull().sum())

# giá trị bất thường (outliers)
print("Giá trị bất thường:")
print(df.describe())

# giá trị trùng lặp (duplicates)
print("Giá trị trùng lặp:", df.duplicated().sum())

# Sử dụng các biểu đồ phù hợp để phân tích
# phân phối thời gian học
plt.figure(figsize=(10, 6))
sns.histplot(df['avg_session_minutes'], bins=30, kde=True)
plt.title('Phân phối thời gian học trung bình mỗi phiên')
plt.xlabel('Thời gian học trung bình mỗi phiên (phút)')
plt.ylabel('Tần suất')
plt.show()

# số lần truy cập mỗi tuần
plt.figure(figsize=(10, 6))
sns.histplot(df['sessions_per_week'], bins=30, kde=True)
plt.title('Phân phối số lần truy cập mỗi tuần')
plt.xlabel('Số lần truy cập mỗi tuần')
plt.ylabel('Tần suất')
plt.show()

# mức độ hoàn thành khóa học
plt.figure(figsize=(10, 6))
sns.histplot(df['completion_rate'], bins=30, kde=True)
plt.title('Phân phối mức độ hoàn thành khóa học')
plt.xlabel('Mức độ hoàn thành (%)')
plt.ylabel('Tần suất')
plt.show()

# xu hướng học tập theo thời gian
df['week'] = df['signup_days_ago'] // 7
plt.figure(figsize=(10, 6))
sns.lineplot(x='week', y='avg_session_minutes', data=df)
plt.title('Xu hướng thời gian học trung bình mỗi phiên theo tuần')
plt.xlabel('Tuần')
plt.ylabel('Thời gian học trung bình mỗi phiên (phút)')
plt.show()

# Phát hiện các hành vi bất thường: 
# người dùng học cực kì nhiều
extreme_users = df[df['avg_session_minutes'] > 300]
print("Người dùng học cực kì nhiều:")
print(extreme_users)

# người dùng đăng ký nhiều khóa nhưng không học 
inactive_users = df[(df['sessions_per_week'] == 0) & (df['completion_rate'] == 0)]
print("Người dùng đăng ký nhiều khóa nhưng không học:")
print(inactive_users)

# người dùng chi tiêu bất thường
high_spenders = df[df['total_spent_usd'] > 1000]
print("Người dùng chi tiêu bất thường:")
print(high_spenders)
