import pafy

file = open('musicas.txt','r')

for line in file:

	url = line

	try:
		video = pafy.new(url)

		bestaudio = video.getbestaudio(preftype="m4a")

		print(video.title)

		bestaudio.download(filepath="C:/Users/Will/Music/SerFunk")
	except Exception as e:
		print(video.title)
		print(50*'#')
		print(url)

file.close()