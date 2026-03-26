import cv2

# Image path
input_path = "pp.jpeg"
output_path = "new_image.jpeg"

# Read image
img = cv2.imread(input_path)

if img is None:
    print("Image not found")
else:
    # Resize logic
    scale = 50
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)

    resized = cv2.resize(img, (width, height))

    # Save image
    cv2.imwrite(output_path, resized)

    # Show image
    cv2.imshow("Resized Image", resized)
    cv2.waitKey(0)

    #compare size and print
    #     img=cv2.imread("pp.jpeg")
#     print(img.shape)
#     img2=cv2.imread("new_img.jpeg")
#     print(img2.shape)
    print(cv2.imread("pp.jpeg").shape)
    print( cv2.imread("new_image.jpeg").shape)
 
