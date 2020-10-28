# -*- coding: utf-8 -*-
import cv2
import imutils

def scan_document(image_name:str):
    image = cv2.imread(image_name)
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        edged = cv2.Canny(gray, 75, 200)

        # show the original and the edge detected image
        print("STEP 1: Edge Detection")
        cv2.imshow("window", image)
        cv2.imshow("window", edged)
        cv2.waitKey()
        cv2. destroyAllWindows()

        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:5]

        #loop over the contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
            print(f"find approx with len {len(approx)}")
            # if out approximated contour has four points, then we
            # can assume that we have found out screen
            if len(approx) == 4:
                screenCnt = approx
                break

        # show the contour (outline) of the piece of paper
        print("STEP 2: Find the contours of paper")
        # cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
        cv2.imshow("window", image)
        cv2.waitKey()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    print("CV2 Version ", cv2.__version__)
    print("CV2 Build", cv2.getBuildInformation())

    cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    scan_document(r"C:\development\python\mydms\data\steuer.png")