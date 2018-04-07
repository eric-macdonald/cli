import sys 
import cli_cracker 
import cv2 

fileinput =  sys.argv[1]

layers, layer_directions = cli_cracker.cli_reader(fileinput)

numlayers = len(layers)
print "number of layer = " + str(numlayers)

#filelist = open("file.list", 'w')

for i in range(0,numlayers,1):
    print "loop layer = " + str(i)
    print "loop layers length = " + str(len(layers))
    print "loop layer_directions length = " + str(len(layer_directions))
    print "loop entering draw_layers"
    frame = cli_cracker.draw_layer(i, layers, layer_directions)
    height, width, bob = frame.shape
#    print "frame1 " + str(height) + " " + str(width)
#    width = int(width*1.09)
#    height = int(width*1.69)
    print "frame2 " + str(height) + " " + str(width)
   # cv2.imshow('layer picture', frame )
   # cv2.waitKey(0)
    revlayer = numlayers - i - 1
    print "loop rev layer = " + str(revlayer)
    jpeg_name = "layer_" + format(revlayer,'05') + ".jpg"
    jpeg_line = "layer_" + format(revlayer,'05') + ".jpg\n"
#    frame = cv2.flip(frame, 1)
    frame[:5, :] = [0, 255, 0] 
    frame[height - 5:, :] = [0, 255, 0] 
    frame[:, :5] =  [0, 255, 0] 
    frame[:, width - 5:] = [0, 255, 0] 
    text_string1 = "YSU / Humtown"
    text_string2 = "Z Height=" + str(float(zheight))
    cv2.putText(frame, text_string1, (230, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    cv2.putText(frame, text_string2, (400, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.imwrite(jpeg_name, frame)
    with open("file.list", 'r') as original: data = original.read()
    with open("file.list", 'w') as modified: modified.write(jpeg_line + data)
    print jpeg_line

print "Done!"

