from PIL import Image
from os import walk

filelist = {}
def filenum() :
    for root, dirs, files in walk("./Root"):
        for filename in files:
            if filename.__contains__('.jpg') :
                filelist[filename] = root


filenum()
print(filelist)


for filename, root in filelist.items():
    img = Image.open(root + '/' + filename)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("Root/" + filename.replace('jpg', 'png'), "PNG")