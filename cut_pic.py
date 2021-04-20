# pip install opencv-python
import cv2


def crop_img(img):
    img = cv2.imread(img)
    # cv2.imshow('imit', img)
    # 裁切區域的 x 與 y 座標（左上角）
    x = 935
    y = 467

    # 裁切區域的長度與寬度
    w = 30
    h = 30

    # 裁切圖片
    crop_img = img[y:y+h, x:x+w]
    # 顯示圖片
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    # 寫入圖檔
    cv2.imwrite('crop.jpg', crop_img)

def get_RGBColorCode(img, x=0 ,y=0):
    img = cv2.imread(img)
    # method 2
    b, g, r = img[y, x]
    # print("RGB = ({}, {}, {})".format(r, g, b))

    # 轉成我們常見的 Hex 色碼
    rgb_hex = hex(r)[-2:] + hex(g)[-2:] + hex(b)[-2:]
    # print("RGB Hex = #{}".format(rgb_hex))
    return r, g, b
