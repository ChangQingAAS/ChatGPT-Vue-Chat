docker rm -f bing_chat_cli

docker run  \
	-it \
	--name bing_chat_cli \
	-p 8585:8080 \
	--link bing_chat_srv \
	bing_chat_gpt_cli
