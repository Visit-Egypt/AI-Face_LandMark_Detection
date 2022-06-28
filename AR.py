
import dlib, cv2
import numpy as np
from facePoints import facePoints


def writeFaceLandmarksToLocalFile(faceLandmarks, fileName):
    with open(fileName, 'w') as f:
        for p in faceLandmarks.parts():
            f.write("%s %s\n" % (int(p.x), int(p.y)))

    f.close()


Model_PATH = "shape_predictor_68_face_landmarks.dat"

frontalFaceDetector = dlib.get_frontal_face_detector()

faceLandmarkDetector = dlib.shape_predictor(Model_PATH)

image = "image_16.jpg"

img = cv2.imread(image)
imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faceLandmarksOuput = "output/image"

allFaces = frontalFaceDetector(imageRGB, 0)

print("List of all faces detected: ", len(allFaces))

allFacesLandmark = []


for k in range(0, len(allFaces)):
    faceRectangleDlib = dlib.rectangle(int(allFaces[k].left()), int(allFaces[k].top()),
                                       int(allFaces[k].right()), int(allFaces[k].bottom()))

    detectedLandmarks = faceLandmarkDetector(imageRGB, faceRectangleDlib)

    if k == 0:
        print("Total number of face landmarks detected ", len(detectedLandmarks.parts()))

    allFacesLandmark.append(detectedLandmarks)

    facePoints(img, detectedLandmarks)

    fileName = faceLandmarksOuput + "_16"  + ".pts"
    print("Lanmdark is save into ", fileName)

    writeFaceLandmarksToLocalFile(detectedLandmarks, fileName)

outputNameofImage = "output/image.jpg"
print("Saving output image to", outputNameofImage)
cv2.imwrite(outputNameofImage, img)

cv2.imshow("Face landmark result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

