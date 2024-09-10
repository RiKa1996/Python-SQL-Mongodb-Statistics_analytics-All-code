import pytube
                                  #pytube.YouTube("url")
con=pytube.YouTube("https://youtu.be/tNp-9FrKN60")        #YouTube is class
print(con)
fmts=con.streams
print(fmts)
print("------------------------------------------")
con=pytube.YouTube("https://youtu.be/tNp-9FrKN60")        #YouTube is class

fmts=con.streams
fmts[0].download("e:/")
fmts[2].download("e:/")
print("Downloaded..")
