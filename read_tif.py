from skimage import io
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)


def multi_slice_viewer(volume):
    remove_keymap_conflicts({'j', 'k'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index])
    fig.canvas.mpl_connect('key_press_event', process_key)

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'j':
        previous_slice(ax)
    elif event.key == 'k':
        next_slice(ax)
    fig.canvas.draw()

def previous_slice(ax):
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])

def next_slice(ax):
    volume = ax.volume
    ax.index = (ax.index + 1) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])


#struct_arr = io.imread("FKO X10 0.5_sox2, pax6, map2-OME TIFF-Export-01.ome.tiff")
fl = "wt X10 0.5_sox2, pax6, map2.tif"
struct_arr = io.imread(fl)  #FKO X10 0.5_sox2, pax6, map2.tif, wt X10 0.5_sox2, pax6, map2.tif
struct_arr2 = struct_arr.T
print(struct_arr2.shape)

key_press = True
z_slice = struct_arr2.shape[3]
i = 0

while key_press is True and i<z_slice:
    plt.close()
    plt.figure(figsize=(7,7))
    ch1 = struct_arr2[0,:,:,i]
    ch2 = struct_arr2[1,:,:,i]
    ch3 = struct_arr2[2,:,:,i]
    ch4 = struct_arr2[3,:,:,i]
    img_ch1 = MinMaxScaler(feature_range=(0,255)).fit_transform(ch1).astype(int)
    img_ch2 = MinMaxScaler(feature_range=(0,255)).fit_transform(ch2).astype(int)
    img_ch3 = MinMaxScaler(feature_range=(0,255)).fit_transform(ch3).astype(int)
    img_ch4 = MinMaxScaler(feature_range=(0,255)).fit_transform(ch4).astype(int)

    plt.subplot(2,2,1), plt.imshow(img_ch1), plt.axis('off'),plt.title(('Data: %s, Cur: %d, Tot: %d') % (fl,i,z_slice), loc='left')
    plt.subplot(2,2,2), plt.imshow(img_ch2), plt.axis('off')
    plt.subplot(2,2,3), plt.imshow(img_ch3), plt.axis('off')
    plt.subplot(2,2,4), plt.imshow(img_ch4), plt.axis('off')

    i += 1

    key_press = plt.waitforbuttonpress()


'''
i1 = struct_arr2[:,:,20,3]
print(np.max(i1))
print(np.min(i1))
i1_max = np.max(i1)
i1_min = np.min(i1)
I = (i1/(i1_max-i1_min))*255
I = I.astype(int)
print(I[200,200])


i1 = struct_arr2[:,:,20,3]
X = MinMaxScaler(feature_range=(0,255)).fit_transform(i1).astype(int)
print(X.shape)
print(np.max(X))
print(np.min(X))


fig, ax = plt.subplots()
ax.imshow(I)
plt.show()
#multi_slice_viewer(struct_arr2) '''
