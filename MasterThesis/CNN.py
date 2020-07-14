from matplotlib import pyplot
from keras.datasets import cifar10
from keras.utils import to_categorical


if __name__ == "__main__":
    # example of loading the cifar10 datase

# load dataset
    (trainX, trainY), (testX, testY) = cifar10.load_data()

# summarize loaded dataset
    print('Train: X=%s, y=%s' % (trainX.shape, trainY.shape))
    print('Test: X=%s, y=%s' % (testX.shape, testY.shape))

# plot first few images (train images)
    for i in range(9):
	# define subplot
	    pyplot.subplot(330 + 1 + i)
	# plot raw pixel data
	    pyplot.imshow(trainX[i])

# show the figure
    pyplot.show()