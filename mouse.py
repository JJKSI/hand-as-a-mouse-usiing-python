import cv2
import mediapipe as mp# it also gives us drawing utils
import pyautogui

cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screenwidth,screenheight=pyautogui.size()
index_y=0

# video camera
while True:
    _, frame= cap.read()#for the frame of the video read
    frame=cv2.flip(frame,1)# to flip the frame or screen when the camera starts beacuse in default we get inverse image
    frame_height,frame_width,_=frame.shape
    
    
    
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#converting the color in rgb form using this method
    
    output=hand_detector.process(rgb_frame)
    hands= output.multi_hand_landmarks#land mark is nothing but they are given points on your hand(we total have 20 landmaeks in our hands)
    # print(hands)
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)# this will give use the point/landmark on our hand
            landmarks=hand.landmark 
            for id, landmarks in enumerate(landmarks):
               x=int(landmarks.x*frame_width)#x axis
               y=int(landmarks.y*frame_height)#y axis
            #    print(x, y)
               
               if  id==8:#(this is finger tip)
                 cv2.circle(img=frame, center=(x,y), radius=10,color=(0,255,255))  # it will mark your index finger    
                 # now using this finger as a mouse
                 
                 index_x=screenwidth/frame_width*x#computerscreen width/frame width
                 index_y=screenheight/frame_height*y
                 # thus this will increase your finger tips reach in the windows screen
                 pyautogui.moveTo(index_x, index_y)  # this will move your mouse on nyour own but for small area only so we will incrase tthe screen size
                 # now when we touch our thumb with first finger it will perform cloick
               if  id==4:#(this is thumb tip)
                  cv2.circle(img=frame, center=(x,y), radius=10,color=(0,255,255))     
                 
                 
                  thumb_x=screenwidth/frame_width*x
                  thumb_y=screenheight/frame_height*y
                  
                  print('outside',abs(index_y-thumb_y))
                  
                  if abs(index_y-thumb_y)< 20:#if abs is the absolute difference
                      print('click')# so if the condition staisfies it clicks
                      pyautogui.click()
                      pyautogui.sleep(1)#sleep with oone sceoond
    cv2.imshow('virtual mouse',frame)# showing that is dispaklying the image
    cv2.waitKey(1)
    
    
#detecting the hands 



    