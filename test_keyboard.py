import matplotlib.pyplot as plt

key_press = False
while key_press is False:
    print('no key is pressed')
    img = plt.imread("Channel1-01-A-01.tif")
    plt.imshow(img)

    key_press = plt.waitforbuttonpress()
    print('key press: ', key_press)
    #plt.show()