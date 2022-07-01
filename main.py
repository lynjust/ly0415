import pipeline
import cv2

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('img', img)
        cv2.waitKey(1)
        img = cv2.flip(img, 0)



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
