# Documentation opencv

```
# This is how we import OpenCV, we can't use OpenCV's functions without first doing this
import cv2

# Load an image using 'imread' specifying the path to image
image = cv2.imread('./images/flowers.jpeg')

def imshow(title = "", image = None):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output.jpg', image)

# Import numpy
import numpy as np

print(image.shape)

# To access a dimension, simply index it by using 0, 1 or 2.
image.shape[0]
```

`arr.argmin`   
`arr.mean`   
`arr.reshape`   
`np.arange(0,10)`   
`np.random.seed(101)`   
`arr = np.random.randint(0,100,10)`   
`mat[:,1]` gets the entire row of the array ':'   

