from perlin import PerlinNoiseFactory
import PIL.Image

def perlinmakin(size,res,frames,frameres):

  space_range = size//res
  frame_range = frames//frameres

  pnf = PerlinNoiseFactory(3, octaves=4, tile=(space_range, space_range, frame_range))

  for t in range(frames):
      img = PIL.Image.new('L', (size, size))
      for x in range(size):
          for y in range(size):
              n = pnf(x/res, y/res, t/frameres)
              img.putpixel((x, y), int((n + 1) / 2 * 255 + 0.5))

      img.save("noiseframe{:03d}.png".format(t))
      print(t)

perlinmakin(50,40,1,5)
