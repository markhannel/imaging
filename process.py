from h5video import h5video
import numpy as np

def vmedian(h5vid, skip=10):
    """Returns the median image of an h5video."""
    return np.median(h5vid.frames[::skip], axis=0)

def normalize(image, bg, dc=0, theory='simple'):
    """Normalizes a hologram by it's background and optionally by the dark
    count."""

    if type(dc) == int or type(dc) == float:
        dc = dc*np.ones(image.shape)

    if theory == 'simple':
        return (image - dc)/(bg - dc)

def vmedian_example():
    import matplotlib.pyplot as plt
    
    fn = 'example.h5'
    with h5video(fn) as vid:
        bg = vmedian(vid)

    plt.imshow(bg)
    plt.gray()
    plt.show()

def normalize_example():
    import matplotlib.pyplot as plt
    
    fn = 'example.h5'
    bgn = 'example_bg.npy'
    bg = np.load(bgn)

    with h5video(fn) as vid:
        norm = normalize(vid.frames[0], bg, dc=16)
        plt.imshow(norm)
        plt.gray()
        plt.show()

if __name__ == '__main__':
    normalize_example()

