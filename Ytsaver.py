import webbrowser
#ENTER YOUR YOUTUBE URL HERE :
url = "https://www.youtube.com/watch?v=_Zxo950vB3s"
download = url[:12] + "ss" + url[12:]

webbrowser.open(download) 
