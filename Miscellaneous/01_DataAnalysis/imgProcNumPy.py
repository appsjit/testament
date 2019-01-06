import numpy
import cv2


def imgProc():
    n = numpy.arange(27)
    n.reshape(3,3,3)
    ##print(n)

    nArr = [[123,12,123,12,33],[],[]]
    m=numpy.asarray(nArr)
    ##print(m)

    im_g=cv2.imread("smallgray.png",1)
    ##im_g = im_g[0:2, 2:4]
    ##print(im_g)

    # for i in im_g.T:
    #     print(i)
    #
    # for i in im_g.flat:
    #     print(i)

    ##cv2.imwrite("newsmallgray.png",im_g)

    ims = numpy.vstack((im_g,im_g,im_g))

    lst = numpy.vsplit(ims,3)
    print(lst[0])

    #return m

if __name__ == '__main__':
    print(imgProc())