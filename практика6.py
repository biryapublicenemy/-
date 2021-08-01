import cv2
import numpy as np
import math
import matplotlib as plt
 
def mean_white_balance(img):
    """
    Первый простой метод среднего баланса белого
         : param img: данные изображения читаются cv2.imread
         : return: Возвращенные данные изображения результата баланса белого
    """
         # Читать изображение
    img = cv2.imread('boris.jpg')
    b, g, r = cv2.split(img)
    r_avg = cv2.mean(r)[0]
    g_avg = cv2.mean(g)[0]
    b_avg = cv2.mean(b)[0]
         # Найдите коэффициент усиления, занимаемый каждым каналом
    k = (r_avg + g_avg + b_avg) / 3
    kr = k / r_avg
    kg = k / g_avg
    kb = k / b_avg
    r = cv2.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
    g = cv2.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
    b = cv2.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
    balance_img = cv2.merge([b, g, r])
    return balance_img
 
def perfect_reflective_white_balance(img_input):
    """
         Идеальный баланс белого с отражением
         ШАГ 1. Рассчитайте сумму R \ G \ B для каждого пикселя
         ШАГ 2: В соответствии со значением R + G + B рассчитайте значение предыдущего соотношения% как пороговое значение T контрольной точки.
         ШАГ 3: Для каждой точки изображения вычислите среднее значение совокупной суммы компонентов R \ G \ B всех точек, где значение R + G + B больше, чем T.
         ШАГ 4. Определите количество пикселей до [0,255] для каждой точки.
         В зависимости от выбора значения коэффициента изображение не является белым в самой яркой области.
         : param img: данные изображения читаются cv2.imread
         : return: Возвращенные данные изображения результата баланса белого
    """
    img = img_input.copy()
    b, g, r = cv2.split(img)
    m, n, t = img.shape
    sum_ = np.zeros(b.shape)
    # for i in range(m):
    #     for j in range(n):
    #         sum_[i][j] = int(b[i][j]) + int(g[i][j]) + int(r[i][j])
    sum_ = b.astype(np.int32) + g.astype(np.int32) + r.astype(np.int32)
 
    hists, bins = np.histogram(sum_.flatten(), 766, [0, 766])
    Y = 765
    num, key = 0, 0
    ratio = 0.01
    while Y >= 0:
        num += hists[Y]
        if num > m * n * ratio / 100:
            key = Y
            break
        Y = Y - 1
 
    # sum_b, sum_g, sum_r = 0, 0, 0
    # for i in range(m):
    #     for j in range(n):
    #         if sum_[i][j] >= key:
    #             sum_b += b[i][j]
    #             sum_g += g[i][j]
    #             sum_r += r[i][j]
    #             time = time + 1
    sum_b = b[sum_ >= key].sum()
    sum_g = g[sum_ >= key].sum()
    sum_r = r[sum_ >= key].sum()
    time = (sum_ >= key).sum()
 
    avg_b = sum_b / time
    avg_g = sum_g / time
    avg_r = sum_r / time
 
    maxvalue = float(np.max(img))
    # maxvalue = 255
    # for i in range(m):
    #     for j in range(n):
    #         b = int(img[i][j][0]) * maxvalue / int(avg_b)
    #         g = int(img[i][j][1]) * maxvalue / int(avg_g)
    #         r = int(img[i][j][2]) * maxvalue / int(avg_r)
    #         if b > 255:
    #             b = 255
    #         if b < 0:
    #             b = 0
    #         if g > 255:
    #             g = 255
    #         if g < 0:
    #             g = 0
    #         if r > 255:
    #             r = 255
    #         if r < 0:
    #             r = 0
    #         img[i][j][0] = b
    #         img[i][j][1] = g
    #         img[i][j][2] = r
 
    b = img[:, :, 0].astype(np.int32) * maxvalue / int(avg_b)
    g = img[:, :, 1].astype(np.int32) * maxvalue / int(avg_g)
    r = img[:, :, 2].astype(np.int32) * maxvalue / int(avg_r)
    b[b > 255] = 255
    b[b < 0] = 0
    g[g > 255] = 255
    g[g < 0] = 0
    r[r > 255] = 255
    r[r < 0] = 0
    img[:, :, 0] = b
    img[:, :, 1] = g
    img[:, :, 2] = r
 
    return img
plt.imshow(img)
plt.show()
