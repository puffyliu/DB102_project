# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=Qn3jB-vfr-Y")
# (yt.streams
#    .filter(progressive=True, file_extension='mp4')
#    .order_by('resolution')
#    .desc()
#    .first()
#    .download()
#  )

#
# from pytube import *
# import os
# pl = Playlist("https://www.youtube.com/watch?v=Jl7keidAvpU&list=PLtwas03AOcPEoHtz0IJItqCbI2ULU14bU")
# dirname = "yt/" + "歌曲清單"
# if not os.path.exists(dirname):
#     os.makedirs(dirname)
# pl.download_all(dirname)