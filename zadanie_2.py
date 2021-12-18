import cv2


def show_photo(img) -> None:
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('img/img-2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

c_img_1 = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
show_photo(c_img_1)
c_img_2 = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
show_photo(c_img_2)
c_img_3 = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
show_photo(c_img_3)
c_img_4 = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
show_photo(c_img_4)
c_img_5 = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
show_photo(c_img_5)
c_img_6 = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
show_photo(c_img_6)