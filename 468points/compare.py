import matplotlib.pyplot as plt
import numpy as np

def read_coordinates_from_file(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.split()
            points.append((int(data[1]), int(data[2])))
    return points

def compare_coordinate_sets(file_path1, file_path2, threshold=10):
    points1 = read_coordinates_from_file(file_path1)
    points2 = read_coordinates_from_file(file_path2)

    if len(points1) != len(points2):
        return 0
    
    match_count = sum(np.linalg.norm(np.array(p1) - np.array(p2)) <= threshold for p1, p2 in zip(points1, points2))
    return match_count / len(points1) * 100

# Đường dẫn đến file point.txt và point2.txt
file_path1 = "point.txt"
file_path2 = "point2.txt"

# So sánh tập tin và lấy tỷ lệ trùng khớp với sai số cộng trừ là 10
match_percentage = compare_coordinate_sets(file_path1, file_path2, threshold=10)
print(f"Matching percentage with threshold 10: {match_percentage:.2f}%")

# Vẽ biểu đồ
categories = ['Matching', 'Not Matching']
values = [match_percentage, 100 - match_percentage]

plt.bar(categories, values, color=['green', 'red'])
plt.title('Matching Percentage with Threshold 10 between point.txt and point2.txt')
plt.ylabel('Percentage')
plt.ylim(0, 100)
plt.show()
