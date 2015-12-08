echo You are changing your locale to $1

changelocale(){
	export http_proxy=$1
	git config --global http.proxy $1
	git config --global https.proxy $1
}

proxy="http://172.30.0.7:3128"
if [[ $1 = college ]]; then
	echo Changing proxy to $proxy
	changelocale $proxy
else
	proxy=""
	echo Outside college....No proxy needed
	unset http_proxy
	git config --global --unset http.proxy
	git config --global --unset https.proxy
fi