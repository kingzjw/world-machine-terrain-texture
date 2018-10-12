#coding:utf-8

from PIL import Image

'''输入的彩色图片的名字，输出的是这个彩色图片的灰度图，以及RGB分离之后的三个RGB灰度图'''
def TransFromImageToGrey(imageName,type):
    # 彩色图转化成灰度图
    name_input = imageName + type
    name_Grey_output = imageName + "_grey" + type

    im = Image.open(name_input)
    im1 = im.convert('L')
    im1.save(name_Grey_output)

    # 分离彩色图,变成灰度图
    name_R_output = imageName + "_R" + type
    name_G_output = imageName + "_G" + type
    name_B_output = imageName + "_B" + type
    r, g, b = im.split()
    r.save(name_R_output);
    g.save(name_G_output);
    b.save(name_B_output);
    return


'''输入的彩色图片的名字(这个图本质是灰度图，印为RGB的三通道的值是一模一样的)，首先得到这个彩色图片的灰度图，然后对这个灰度图进行特殊处理'''
def biomeMapImage(imageName, type, minValue, maxValue):
    if minValue < 0 or minValue>255 or maxValue < minValue or maxValue<0 or maxValue>255:
        print 'input parm error'
        return

    name_input = imageName + type
    name_output = imageName + '_'+str(minValue) + '_' + str(maxValue) + type

    im = Image.open(name_input)
    img_grey = im.convert('L')
    img_grey_pxData = img_grey.load()

    #遍历所有的像素，然后修改这个值
    for pos_x in range(img_grey.height):
        for pos_y in range(img_grey.width):
            #不符合条件的像素颜色变成黑色
            #print str(pos_x)+' '+str(pos_y)+' : '+str(img_grey_pxData[pos_x,pos_y])
            if img_grey_pxData[pos_x,pos_y] < minValue :
                img_grey_pxData[pos_x,pos_y] = 0
            elif img_grey_pxData[pos_x,pos_y] > maxValue:
                img_grey_pxData[pos_x, pos_y] = 0
            else:
                # 符合条件的，颜色像素maxValue 变成 255，也就是白色，范围内的颜色依次平移
                img_grey_pxData[pos_x, pos_y] += (255-maxValue)
                #print str(pos_x) + ' ' + str(pos_y) + ' : ' + str(img_grey_pxData[pos_x, pos_y])
    #save image
    img_grey.save(name_output)
    print  'image is ok '+ name_output
    print 'select range ( '+str(minValue) + ' , ' + str(maxValue)+')'
    return img_grey