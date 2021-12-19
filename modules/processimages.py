import cv2
import imutils
import time


def detect_persons_in_image(img_path: str) -> None:
    img = cv2.imread(img_path)
    img = imutils.resize(img, width=min(500, img.shape[1]))
    cv2.imshow(img_path, img)
    cv2.waitKey(0)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (persons, _) = hog.detectMultiScale(img, winStride=(4, 4), padding=(4, 4), scale=1.05)
    for (x, y, w, h) in persons:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow(img_path, img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_persons_in_image_with_time(img_path: str) -> None:
    start_time = time.time()
    img = cv2.imread(img_path)
    img = imutils.resize(img, width=min(500, img.shape[1]))
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (persons, _) = hog.detectMultiScale(img, winStride=(4, 4), padding=(4, 4), scale=1.05)
    for (x, y, w, h) in persons:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    end_time = time.time()
    print(f"[img] {img_path} - czas przetwarzania: {(end_time - start_time)} sekund")