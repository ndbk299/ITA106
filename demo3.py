# Code demo: Tạo dữ liệu khách hàng
# Thu thập dữ liệu khách hàng 
# Tuổi, thu nhập, điểm chi tiêu
# Số lần ghé thăm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
# Cố định kết quả ngẫu nhiên sinh ra mỗi lần chạy
# Code đều cho ra 1 kết quả giống nhau
data = pd.DataFrame({
    'Age': np.random.randint(18, 70, size=100),
    # Sinh ra 100 giá trị ngẫu nhiên từ 18 đến 70
    'Income': np.random.randint(30000, 100000, size=100),
    # Sinh ra 100 giá trị ngẫu nhiên từ 30,000 đến 100,000
    'Spending Score': np.random.randint(1, 100, size=100),
    # Sinh ra 100 giá trị ngẫu nhiên từ 1 đến 100
    'Visit Count': np.random.randint(1, 20, size=100)
    # Sinh ra 100 giá trị ngẫu nhiên từ 1 đến 20
})
print(data.head())
# Ma trận đồ thị tán xạ
# Nếu 1 dataset có d biến thì ta tạo ra ma trận d x d
# Mỗi hàng là 1 biến, mỗi cột là 1 biến
# Đường chéo chính sẽ là biểu đồ histogram 
sns.pairplot(data)
plt.show()