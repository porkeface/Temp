import pandas as pd

# 创建一个简单的 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', "Marry", "Tony"],
    'Age': [24, 27, 22, 23, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', "New York", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
print("_______________________+")
# 查看前几行数据
print(df.head())
print("______________________________-")
# 选择特定的列
print(df[['Name', 'Age']])
print("______________________2")
#提取特定行
print(df.iloc[2])
print("______________________5")
#提取多行
print(df.iloc[0:4])
print("_________________________3")
#提取特定行列
print(df.iloc[0]["Name"])
print("_______________________________--")
# 添加新列
df['AgeCategory'] = df['Age'] > 25
print(df)

print("______________________________zidian")
# 从字典创建
data = {
    'Column1': [1, 2, 3],
    'Column2': ['a', 'b', 'c']
}
df = pd.DataFrame(data)
print(df)
print("______________________________")
# 从列表的列表创建
data = [[1, 'a'], [2, 'b'], [3, 'c']]
df = pd.DataFrame(data, columns=['Column1', 'Column2'])
print(df)
print("______________________________")
df = pd.DataFrame(data)
print(df)

print("_______________________")
# 从 NumPy 数组创建
import numpy as np

array = np.array([[1, 'a'], [2, 'b'], [3, 'c']])
df = pd.DataFrame(array, columns=['Column1', 'Column2'])
print(df)
