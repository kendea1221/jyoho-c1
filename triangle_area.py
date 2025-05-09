def calculate_triangle_area(bottom, high):
    """
    三角形の面積を計算する関数
    
    Parameters:
    bottom (float): 底辺の長さ
    high (float): 高さ
    
    Returns:
    float: 三角形の面積
    """
    return bottom * high / 2

# 使用例
if __name__ == "__main__":
    # テストケース
    bottom = 5
    high = 3
    area = calculate_triangle_area(bottom, high)
    print(f"面積は {area} です") 