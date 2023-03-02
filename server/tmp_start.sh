docker rm -f bing_chat_srv

docker run  \
	-it \
	--name bing_chat_srv \
	-p 5000:5000 \
	-e "BING_U=value of _U in your bing cookie" \
	-e "OPENAI_API_KEY=your_open_ai_api_key" \
	-v $(realpath ./app.py):/src/app.py \
	bing_chat_gpt_srv
