import numpy as np

def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 1. 模拟一张图片
print_separator("1. Create Image Data")
# 创建一个 5x5 的微型彩色图片用于演示 (Height=5, Width=5, Channels=3)
# 像素值在 0-255 之间
image = np.random.randint(0, 256, (5, 5, 3))

print(f"Image Shape: {image.shape}")
print("Top-left pixel (RGB):", image[0, 0]) # 打印左上角第一个像素的颜色

# 2. 裁剪 (Cropping) - 还是切片
print_separator("2. Cropping")
# 类似于在图片中心切个 3x3 的小图
# 行取 1-4，列取 1-4
crop = image[1:4, 1:4, :] 
print(f"Cropped Shape: {crop.shape}")
print("Centered Data:\n", crop[:, :, 0]) # 打印 R 通道看看

# 3. 灰度化 (Grayscale) - 降维打击
print_separator("3. Grayscale")
# 灰度原理：把 RGB 三个值求平均
# axis=2 表示沿着“颜色通道”这个轴求平均
gray_image = image.mean(axis=2)
print("Gray Shape:", gray_image.shape) # 变成 (5, 5)，没有 RGB 了
print("Gray Data (First row):\n", gray_image[0])

# 4. 亮度调节 (Brightness) - 广播
print_separator("4. Adjust Brightness")
# 给所有像素 + 50
bright_image = image + 50
# 注意！像素值不能超过 255。使用 clip 函数限制范围
bright_image = np.clip(bright_image, 0, 255)

print("Original Pixel:", image[0, 0])
print("Brighter Pixel:", bright_image[0, 0])

# 5. 简单抠图 (Masking) - 布尔索引
print_separator("5. Masking (Remove Red)")
# 假设我们要把所有红色分量 > 150 的点都变成黑色 (0,0,0)

# step 1: 找到红通道 (channel 0)
red_channel = image[:, :, 0]

# step 2: 生成掩码 (Mask)
mask = red_channel > 150
print(f"\nFound {np.sum(mask)} pixels with strong red.")

# step 3: 替换
# 注意：这里需要一点高级技巧。
# image[mask] 会选中所有符合条件的像素点 (N, 3)
image[mask] = 0 # 设为黑色

print("After masking, check a masked pixel (if any)...")
# 仅作演示，实际数据随机，不一定能打出来
if np.sum(mask) > 0:
    # 找到第一个被 mask 的点的坐标
    coords = np.argwhere(mask)[0]
    print(f"Pixel at {coords} is now: {image[coords[0], coords[1]]}")
