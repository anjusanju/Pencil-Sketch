import cv2
image = cv2.imread("F:\MY PROJECTS FOR GITHUB UPLOAD\dulquer.jpg")
cv2.imshow("Dulquer", image)
cv2.waitKey(0)

'''conversion into grayscale image '''
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray_image)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

'''Gaussian function to convert the blur image'''
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

'''to obtain the pencile skecth image'''
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

'''comparsion of the original image with the pencil sketch image '''
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
