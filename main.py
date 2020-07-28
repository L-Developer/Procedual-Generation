import perlinmaking
from PIL import Image
im = Image.open("noiseframe000.png")


perlinmaking.perlinmakin(50,15,1,100) 
pixelrgb = []
x,y = 1,1
rgb_im =  im.convert("RGB")

for i in range(50*50):
  if not y > 49 and not x  > 49:
    pixelrgb.append(rgb_im.getpixel((x,y)))
    if x == 49:
      y+=1
      x=0
    else:
      x+=1
  else:
    break

pixelrgb.append(rgb_im.getpixel((49,49)))

w = 50
finalproduct = [0 for x in range(w*w)] 
num = 0 
x,y = 0,0
for i in finalproduct:
  if pixelrgb[num] > (125,125,125):
      finalproduct[num] = 1

  elif pixelrgb[num] >  (120,120,120) and pixelrgb[num] < (125,125,125):
    finalproduct[num] = 2
  num+=1
  if num == 2449:
    break






im= Image.new("RGB", (50, 50), "#0000FF")
pixels = im.load()
num,x,y = 0,0,0
for i in finalproduct:
  if not y > 49 and not x  > 49:
    if i == 1:
      pixels[x,y] = (34,139,34)
    elif i == 2:
      pixels[x,y] = (76,70,50)
    num+=1
    if x == 49:
      y+=1
      x=0
    else:
      x+=1
  else:
    break

  





im.save("output.jpg".format(0))
