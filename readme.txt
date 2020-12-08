QoE for Video Streaming Services

Command to run the program:
Give path to chrome driver python command line argument

python measurements.py "D:\SBU\Fall20\CSE 534 FCN\chromedriver"

Run pip install requirements.txt to install all dependencies

Code Overview:
yt_ids : list of videos to run the script for measurements

Configuration: 
	EXPCONFIG = {
		"ytId": id,  #video ids
		"duration": 60,  #duration for which the video is to be played
		"bitrates": "144p:110.139,240p:246.425,360p:262.750,480p:529.500,720p:1036.744,1080p:2793.167"
	}

videoid_buffer.txt : saves buffer values
videoid_events.txt : saves log of all video events
videoid_outStream.txt : statistics calculated

download_throughputs : array of max available throughputs - network conditioning parameter

Part II
Visualizations.py -> jupyter notebook

References:
[1] Chrome Extension tested as part of literature review
https://github.com/inria-muse/video_collection

[2] Scripts referred for Measurement study
https://github.com/lsinfo3/yomo-docker


