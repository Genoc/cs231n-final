import torch.utils.data as data
from PIL import Image

Image.MAX_IMAGE_PIXELS = 1000000000   # avoid warnings for having really large images
IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def find_classes(df):
    classes = list(df['artist'].str.upper().unique())
    classes.sort()
    class_to_idx = {val: idx for (idx, val) in enumerate(classes)}
    idx_to_class = {idx: val for (idx, val) in enumerate(classes)}
    return classes, class_to_idx, idx_to_class

def make_dataset(img_folder, class_to_idx, df):
    images = []
    
    # artist = index 1
    # filename = index -1
    for row in df.itertuples():
        path = img_folder + row[-1]
        item = (path, class_to_idx[row[1].upper()])
        images.append(item)
    
    return images


def pil_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')

class PaintingFolder(data.Dataset):

    def __init__(self, img_folder, transform=None, df=None):
        
        classes, class_to_idx, idx_to_class = find_classes(df)
    
        imgs = []
        imgs = make_dataset(img_folder, class_to_idx, df)
        if len(imgs) == 0:
            raise(RuntimeError("Found 0 images"))

        self.img_folder = img_folder
        self.imgs = imgs
        self.classes = classes
        self.class_to_idx = class_to_idx
        self.idx_to_class = idx_to_class
        self.transform = transform
        self.loader = pil_loader

    def __getitem__(self, index):    
        path, target = self.imgs[index]
        img = self.loader(path)
        if self.transform is not None:
            img = self.transform(img)
        return img, target

    def __len__(self):
        return len(self.imgs)