# Set the path to the download folder
path = '/home/satyajeet/Desktop/YouTube Videos/'
# !pip install pytubex
from pytube import YouTube

yt_url = input('Enter YouTube URL : ')
yt = YouTube(yt_url)

def download(yt, path):
	print('\n', '-'*80, '\n', '\t\t', yt.title, '-'*80, '\n')
	print('Mime Type\tRes/Abr\t\tFPS\tItag\n')
	for stm in yt.streams.filter(progressive=True).all():
	    if stm.type=='video':
	        print(stm.mime_type,'\t', stm.resolution,'\t\t', stm.fps,'\t', stm.itag)
	    else:
	        print(stm.mime_type,'\t', stm.abr,'\t\t', stm.itag)
	vid_itag = input('Enter ITag of the video you want : ')
	
	yt.streams.get_by_itag(vid_itag).download(path)
	print(f'Done! File saved in {path} folder.')
	return None

download(yt,path)

