file=open("Img.png","rb")
fout=open("MyImg.png","wb")
fout.write(file.read())
file.close()
fout.close()
