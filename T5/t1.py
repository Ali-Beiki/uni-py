import numpy as np

# 1. تولید ۲۰ عدد صحیح تصادفی بین ۰ تا ۱۰۰
data = np.random.randint(0, 101, 20)
print("Randomly generated numbers:")
print(data)

# 2. محاسبه میانگین
mean = sum(data) / len(data)

# 3. محاسبه واریانس به صورت دستی
variance_manual = sum((x - mean) ** 2 for x in data) / len(data)

# 4. محاسبه انحراف معیار به صورت دستی
std_dev_manual = variance_manual ** 0.5

# 5. مقایسه با NumPy
variance_numpy = np.var(data)
std_dev_numpy = np.std(data)

# 6. نمایش نتایج
print(f"\naverage: {mean:.2f}")
print(f"Variance (manual): {variance_manual:.2f}")
print(f"Quality deviation (manual): {std_dev_manual:.2f}")
print(f"\nVariance (NumPy): {variance_numpy:.2f}")
print(f" standard deviation (NumPy): {std_dev_numpy:.2f}")

