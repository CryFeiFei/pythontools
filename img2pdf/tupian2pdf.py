import os
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#需要预告安装支持中文的字体，如simfang从win拷贝过来安装
def createPdf(dstpath,fileList):
    img = Image.open( fileList[0].encode('UTF-8') )
    c = canvas.Canvas(dstpath, img.size)#第一张图片的尺寸新建pdf

    pdfmetrics.registerFont(TTFont('simfang','simfang.ttf')) #注册字体
    fontheight=15
    c.setFont('simfang',fontheight)
    #c.drawString(100, 300, u'宋体宋体')
    height=fontheight
    num=1
    for i in fileList:#标明本pdf的文件列表
        c.drawString(fontheight,height,str(num)+"/"+str(len(fileList)))
        c.drawString(fontheight+50, height, os.path.split(i)[1])
        num+=1
        height+=fontheight
    c.showPage()


    for i in fileList:
        c.drawImage(i.encode('UTF-8'), 0, 0)#转换为中文路径名称打开
        c.showPage()
    c.save()
def transferPdf(filePath,dstpath):
#将一个目录下所有图片生成一个pdf
    fileList=[]
    #result=os.popen(" ls -l "+filePath+"| awk \'{print $9}\' | sort -t _ -k1,1 -k2n,2 ").read()
    result=os.popen(" ls  "+filePath+"|  sort -t _ -k1,1 -k2n,2 ").read()
    currentIndex=0
    pdfIndex=0
    for i in result.split("\n"):
        if i.strip()!='':
            print (i)
            fileList.append(os.path.join(filePath, i))
            currentIndex+=1
            if currentIndex == 100:#每几页一创建
                currentIndex=0
                pdfIndex+=1
                createPdf( os.path.join(dstpath, str(pdfIndex)+".pdf") ,fileList)
                fileList=[]


filePath = "/home/zhangpf/11"#源图片文件夹
dstpath="/home/zhangpf/22"#转换出的pdf文件夹存放地址
transferPdf(filePath,dstpath)
