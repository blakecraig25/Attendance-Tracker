import cv2, time, msvcrt
from time import localtime, strftime

video = cv2.VideoCapture(0)
first_frame = None

xlist = []
timelist = []

class_size = 12


def attendance(x_list, time_list, today_date):
    
    count = 0
    #takes away all the excess rectangle x values and compute only one x value per time
    xlist_condensed = []
    i = 0
    #print(x_list, time_list)

    while(i < len(time_list)-1):
        time_temp = time_list[i+1]
        if time_list[i] == time_temp:
            i = i + 1
            continue
        else:
            xlist_condensed.append(x_list[i])
        
        i = i + 1
    
    xlist_condensed.append(x_list[len(xlist)-1])
    
    xlist_initial = []
    xlist_next = []

    for k in range(len(xlist_condensed)):
        if k % 2 == 0:
            xlist_initial.append(xlist_condensed[k])
        else:
            xlist_next.append(xlist_condensed[k])

    #there should be two x values to consider in each segment now. We will compare every two values in the list
    j = 0
    error_count = 0
    #print(xlist_condensed,xlist_initial, xlist_next)

    for j in range(len(xlist_initial)):
        if (len(xlist_condensed)) % 2 != 0:
            if (len(xlist_initial) % 2 != 0 and (len(xlist_initial) > 2 or len(xlist_initial) < 1)):
                error_count = error_count + 1
                xlist_initial.remove(xlist_initial[len(xlist_initial)-1])
                print("Someone walked in too quickly or slowly. The error is now +/- ", error_count, "people.")
            if (len(xlist_next) % 2 != 0 and (len(xlist_next) > 2 or len(xlist_next) < 1)):
                error_count = error_count + 1
                xlist_next.remove(xlist.next[len(xlist_next)-1])
                print("Someone walked in too quickly or slowly. The error is now +/- ", error_count, "people.")
        else:
            if xlist_initial[j] < xlist_next[j]:
                count = count + 1
            if xlist_initial[j] > xlist_next[j]:
                count = count - 1
    
    class_missing = class_size - count

    attendance_text1 = "Today's Attendance\n\nThere are a total of %d people present today.\n" % count
    attendance_text2 = ("This class is missing %d people today.\n\n" % class_missing)
    attendance_text3 = ("There is an error margin of %d student(s)." % error_count)
    
    file_name = ("Attendance_"+str(today_date)+".txt")
    print("created ", file_name, " files")

    file_write = open(file_name, 'w+')
    file_write.write(attendance_text1)
    file_write.write(attendance_text2)
    file_write.write(attendance_text3)

    file_write.close()

    #print(count)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    threshold_frame = cv2.threshold(delta_frame, 80, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    (cntr,_) = cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   
    for contour in cntr:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        local_time = time.localtime()
        timelist.append(int(time.strftime("%H%M%S", local_time)))

        xlist.append(x)

    local_time = time.localtime()
    today = str(time.strftime("%m.%d.%Y", local_time))
    cv2.imshow(("Attendance for " + today), frame) 
    key = cv2.waitKey(500)
    if key==ord('q'):
        video.release()
        cv2.destroyAllWindows()
        attendance(xlist, timelist, today)
        break