echo You are changing your locale to $1

changelocale(){
	echo Changing proxy into $1

}

proxy = http\:\/\/172.30.0.7\:3128
if [[ $1 = college ]]; then
	echo Changing proxy to $proxy
else
	proxy=""
	echo Outside college....No proxy needed 
fi

changelocale $proxy