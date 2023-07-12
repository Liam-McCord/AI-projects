import cv2
import mediapipe as mp
import time
#import math
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands    
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
temp_data_gathering = [[1000,1000,1],[0,0,1],[0,0,1],[0,0,1]]
dot_coord_x = 10
dot_coord_y = 10
initial_scale = 15
scale = 1
scale_ref_done = False
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    
    
    
    

    #print(scaling_factor)
    if scale_ref_done == False:
        #print("H")
        Thumb_Pinky_X_Separation = (temp_data_gathering[0][0] - temp_data_gathering[2][0])
        Thumb_Pinky_Y_Separation = (temp_data_gathering[0][1] - temp_data_gathering[2][1])
        Thumb_Pinky_Separation = int(((Thumb_Pinky_X_Separation ** 2) + (Thumb_Pinky_Y_Separation ** 2) ) ** 0.5)

        if Thumb_Pinky_Separation < 100:
            ScaleX = (temp_data_gathering[1][0] - temp_data_gathering[3][0])
            ScaleY = (temp_data_gathering[1][1] - temp_data_gathering[3][1])
            
            initial_scale = ((ScaleX ** 2) + (ScaleY ** 2) ) ** 0.5
            scale_ref_done = True
            print(initial_scale)
    if scale_ref_done == True:
        
        ScaleXCurrent = (temp_data_gathering[1][0] - temp_data_gathering[3][0])
        ScaleYCurrent = (temp_data_gathering[1][1] - temp_data_gathering[3][1])
        
        scale_current = ((ScaleXCurrent ** 2) + (ScaleYCurrent ** 2) ) ** 0.5
        scaling_factor = scale_current / initial_scale
        print(scaling_factor)
    
    
    
    PXSeparation = (temp_data_gathering[0][0] - temp_data_gathering[1][0])
    PYSeparation = (temp_data_gathering[0][1] - temp_data_gathering[1][1])
    
    P_T_Separation = int(((PXSeparation ** 2) + (PYSeparation ** 2)) ** 0.5)
    #print(scaling_factor)

    if P_T_Separation < 50 * scaling_factor:
        #cv2.circle(img, (int((temp_data_gathering[0][0] + temp_data_gathering[1][0])/2), int((temp_data_gathering[0][1] + temp_data_gathering[1][1])/2)), 15, (255, 0, 255), cv2.FILLED)
        dot_coord_x = int((temp_data_gathering[0][0] + temp_data_gathering[1][0]) / 2)
        dot_coord_y = int((temp_data_gathering[0][1] + temp_data_gathering[1][1]) / 2)
        #distance_from_0 = abs(5 * (temp_data_gathering[0][2] + temp_data_gathering[1][2]) / 2)
        scale = initial_scale * scaling_factor
        #print(f"{scale:.2f}")

    #print(dot_coords) 
    cv2.circle(img, (dot_coord_x, dot_coord_y), int(scale), (255, 0, 0), cv2.FILLED)
    #print(int(XSeparation), int(YSeparation), int(ZSeparation))
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            #print(temp_data_gathering)
            for id, lm in enumerate(handLms.landmark):
                # Goes through the individual fingers?
                
                # print(id, lm)
                h, w, c = img.shape
                cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                  #print(id, cx, cy)
                if id == 4:
                    #cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                    
                    temp_data_gathering[0][0] = cx
                    temp_data_gathering[0][1] = cy
                    
                    if cz + 400 > 100:
                        temp_data_gathering[0][2] = 500 - cz
                        temp_data_gathering[1][2] = 500 - cz
                if id == 8:
                    #cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                    temp_data_gathering[1][0] = cx
                    temp_data_gathering[1][1] = cy
                    #temp_data_gathering[1][2] = cz + 300
                
                if id == 20:
                    temp_data_gathering[2][0] = cx
                    temp_data_gathering[2][1] = cy
                    
                if id == 7:
                    temp_data_gathering[3][0] = cx
                    temp_data_gathering[3][1] = cy 
                    
                                      
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)
    cv2.putText(img, f"Ball Coords (x,y,z): ({dot_coord_x}, {dot_coord_y}, {int(((temp_data_gathering[0][2] + temp_data_gathering[1][2]) / 2))}) - Scaling Factor: {scaling_factor}", (10, 450), cv2.FONT_HERSHEY_PLAIN, 1,
                (255, 0, 255), 1)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)