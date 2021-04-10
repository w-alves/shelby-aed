mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"was4@cin.ufpe.br\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml