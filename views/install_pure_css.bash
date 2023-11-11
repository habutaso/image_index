if ! [ -d ./pure ];
then
    git clone https://github.com/pure-css/pure/
    cd pure
    npm i
fi

if ! command -v grunt >/dev/null 2>&1;
then
    npm i -g grunt
fi