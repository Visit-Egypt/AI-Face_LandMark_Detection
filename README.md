# AI-Face_LandMark_Detection

The computer engineer researching how they identify the face of a human in an image. For this, we need to identify first where the human face is located in the whole image. The face detector is the method which locates the face of a human in an image and returns as a bounding box or rectangle box values.

After getting the face position in an image and next we have to find out small features of the face like eyebrows, lips, etc. The facial landmark detection tells all the required features of a human face which we want.

The below image is an example of a Model's 68 points model. There we can see that points from 1 to 68

![image](https://s3.ap-south-1.amazonaws.com/s3.studytonight.com/curious/uploads/pictures/1592469192-74364.png)

There are mostly two steps to detect face landmarks in an image which are given below:

## Face detection:

Face detection is the first methods which locate a human face and return a value in x,y,w,h which is a rectangle.

## Face landmark:

After getting the location of a face in an image, then we have to through points inside of that rectangle.

There are many methods of face detector but we focus on Dlib's method.  Like, Opencv uses methods LBP cascades and HAAR and Dlib's use methods HOG (Histogram of Oriented Gradients) and SVM (Support Vector Machine).



## Result

The 68 point stored in pts file and pic with detection on main points on face


[Pts file](https://github.com/Visit-Egypt/AI-Face_LandMark_Detection/blob/main/shape_predictor_68_face_landmarks.dat)

![image2](https://raw.githubusercontent.com/Visit-Egypt/AI-Face_LandMark_Detection/main/image.jpg?token=GHSAT0AAAAAABRI6JN3UPURY4QY5BUDH4P6YTMMUWA)

