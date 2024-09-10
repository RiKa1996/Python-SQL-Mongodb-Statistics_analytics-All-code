import qrcode
img=qrcode.make("My name is rishav")
img.save("E:\\New folder (2)\\10. 3rd party library\\myqr.png")
print("qr genrated")

print("----------------------------------------------------")
img=qrcode.make("this is my mobile no.:7210673579 and insta id:kumar_2041996")
img.save("E:\\New folder (2)\\10. 3rd party library\\myqr2.png")
print("qr genrated")
