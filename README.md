# Documentation opencv

## Section 2: NumPy and Image Basics


### This is how we import OpenCV, we can't use OpenCV's functions without first doing this
```
import cv2
```

### Load an image using 'imread' specifying the path to image
```
image = cv2.imread('./images/flowers.jpeg')

def imshow(title = "", image = None):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
```

### Simply use 'imwrite' specificing the file name and the image to be saved
```
cv2.imwrite('output.jpg', image)
```
### Import numpy
```
import numpy as np

print(image.shape)
```
### To access a dimension, simply index it by using 0, 1 or 2.
```
image.shape[0]
```

### To access the pixel at a specific location, simply index the image array
`arr = np.ones((5,5))*10`
`arr.argmin`   
`arr.mean`   
`arr.reshape`   
`np.arange(0,10)`   
`np.random.seed(101)`   
`arr = np.random.randint(0,100,10)` 
`mat[:,1]` gets the entire row of the array ':'   

### Images and numpy
An image has 3 dimensions
(width, height, 3 color channels)

```
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from PIL import Image

pic = Image.open('/dog.webp')

# transformando picture to array
pic_arr = np.asarray(pic)
type(pic_arr)
pic_arr.shape
plt.imshow(pic_arr)


pic_copy = pic_arr.copy()

plt.imshow(pic_copy[:,:,2])
```

## Section 3: Image basics with Opencv

```
import cv2
```

**changing opencv bgr to rgb**
```
img = cv2.imread('/dog.webp')
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
```
**changing read to grayscale**
```
img_gray = cv2.imread('/dog.webp', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray, cmap='gray')
```

**halving scale of image**
```
new_img = cv2.resize(fix_img, (0,0), fix_img, 0.5,0.5)
```

**fliping images**
```
plt.imshow(cv2.flip(fix_img,1))
```

**saving files with cv2**
```
cv2.imwrite('new_image.jpg', fix_img)
```

**to resize the image for visualization**
```
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.imshow(fix_img)
```
**to print outside jupyterlab**
```
cv2.imshow('nose', img)
cv2.waitKey()
```

### Drawing on images
**Creating black image**
```
blank_img = np.zeros(shape=(512,512,3), dtype=np = int16)
```

**Creating green rectangle inside**
```
cv2.rectangle(blank_img, pt1=(384,0), pt2=(510,150), color=(0,255,0)thickness=10)
```


**Creating circle**
```
cv2.circle(img=blank_img,center(100,100), radius=50, color(255,0,0)thickness=-1)
```

**Creating line**

```
cv2.line(blanck_img, pt1=(0,0), pt2=(512,512), color=(102,255,255), thickness= 5)
```
**Adding Fonts**

```
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text = 'Hello', org=(10,500),fontFace=font, fontScale=4, color(255,255,255) thickness =3, lineType=cv2.LINE_AA)
```

**Custom poligons**

```
vertices = np.array([[100,300], [200,200], [400,300], [200,400]], dbtype=np.int32)
pts = vertices.reshape((-1,1,2))
cv2.polylines(blank_img, [pts], isClosed=true, color=(255,0,0)thickness=5)
```



# Important unix commands

- `touch abc.txt` to create a file
- `cat > abcFile.txt` to enter a file
- `> abcFile.txt` creates new file
- `zip -j zipContent d1/file.txt d2/2.txt d2/3.txt` zipping files
- `unzip zipContent.zip` unzipping files
- `ls -l` list files
- `ls -a` list all files
- `ls -la` list all files with details
- `ls -lh` list all files with details and human readable
- `rm -f file` remove file
- `rm -rf folder` remove folder
- `cp file1 file2` copy file1 to file2
- `cp -r folder1 folder2` copy folder1 to folder2
- `mv file1 file2` move file1 to file2
- `mv folder1 folder2` move folder1 to folder2
- `mkdir folder` create folder
- `rmdir folder` remove folder
- `pwd` print working directory

- `markdown README.me | lynx -stdin` to visualize markdown file

# Homrebrew commands
- `brew list`
- `brew deps --tree --installed`


# Important vim

### 1. Modes
There are different modes
**Insert mode** 
**Editing mode** i or a
**Command mode** press "esc"

### 2. To quit Vim editor

- `:q` quit the editor
- `:q!` Quit without saving changes i.e discard changes
- `:wq` Save the changes and quit the editor

### 3. Save the changes
- `:w` Write to file called [file_name] (save as)
- `w!` Overwrite to fie called [file_name] (save s forcefully)

### 4. Navigation in Vim editor
- `k` up
- `j` down
- `h` left
- `l` right

- `w` move to the beginning of the next word
- `b` move to the beginning of the previous word
- `e` move to the end of the word
- `0` move to the beginning of the line

- `$` move to the end of the line
- `gg` move to the beginning of the file
- `G` move to the end of the file
- `:n` move to the line number n


### 5. File Editing
- `dd` for deleting line
- `yy` for copying line
- `p` for pasting line
- `u` for undo
- `ctrl + r` for redo
- `r` for replacing character
- `x` for deleting character
- `o` for adding line below
- `O` for adding line above
- `t` for moving to the next character
- `T` for moving to the previous character

- `dw` for deleting word
- `d$` for deleting from cursor to end of line
- `d^` for deleting from cursor to beginning of line
- `dG` for deleting from cursor to end of file

### 6. Search and Replace
- :[range]s/{pattern}/{string}/[flags] [count]
Example:
`s/int/string 1`
- `:%s/int/string 1` replace all occurences in the file
- `:s/int/string 1` replace the first occurence in the file
- `:'<,'>s/^/# /` add # at the beginning of the line
- `:10,20s/^/# /` add # at the beginning of the line from line 10 to 20

### 7. Display Line Number
- `set number` or `set nu`

### 8. Syntax Highlighting
`syntax on`
