import hashlib
from PIL import Image
import numpy as np

#Функция не нужна! Не трогать, расшифровывает hash md5
def decryptMD5(testHash):
	for i in range(601):
		result = hashlib.md5(str(i).encode())
		if result.hexdigest() == testHash:
			return i
	return "error: Not found hash"

#Начало
def encodeMD5(i):
	result = hashlib.md5(str(i).encode())
	return result.hexdigest()


img = Image.new('RGB', (600,267))
for i in range(600):
	img1 = Image.open(encodeMD5(i)+".png")
	img.paste(img1, (i,0))

img.show()
img.save("out.png")
