import os
from PIL import Image
from glob import glob
from tkinter import filedialog

def get_logo(img, logo, k):
    x = logo.copy()
    imw, imh = img.width, img.height
    lw, lh = logo.width, logo.height
    nw = int(imw / (k*1.5))
    nh = int(lh * nw / lw)
    return x.resize((nw, nh))


def draw_logo(img, logo, k=4, position='center'):

    imw, imh = img.width, img.height
    if position == 'center':
        xp = int(imw/(k*2)) - int(logo.width/2)
    else:
        xp = 0
    yp = int(imh / 2) - int(logo.height/2)          
    
    if position == 'dung':
        xp = imw - int(logo.width * 1.2)
        yp = imh - int(logo.height * 1.2)
    
    for i in range(k):
        img.paste(logo, (xp, yp), logo)
        xp += int(imw/k)
    return img

def draw_image(img_path, number_xmlogo=4):
    img = Image.open(img_path).convert("RGBA")
    
    # Add xuong moc logo
    path = os.path.join(os.getcwd(), "xm_logo.png")
    xmlogo = Image.open(path)
    xmlogo = get_logo(img, xmlogo, k=number_xmlogo)
    img = draw_logo(img, xmlogo, k=number_xmlogo)

    # Add Dungpv logo
    path = os.path.join(os.getcwd(), "dung_logo.png")
    dunglogo = Image.open('dung_logo.png')
    dunglogo = get_logo(img, dunglogo, k=4)
    img =draw_logo(img, dunglogo, k=1, position='dung')
    return img


folder = filedialog.askdirectory(initialdir="/home/quang/temp/logo/insert_logo")
img_paths = glob(folder + "/*.jpg")
new_folder = os.path.join(folder, "folder_logo")
os.makedirs(new_folder, exist_ok=True)

for img_path in img_paths:
    img = draw_image(img_path)
    img_name = os.path.basename(img_path).split(".")[0]
    img_name = img_name + "_logo.jpg"
    p = os.path.join(new_folder, img_name)
    print(p)
    img.convert("RGB").save(p, quality=95)

