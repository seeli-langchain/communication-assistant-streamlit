# Communication-Assistant Streamlit

[
    ![Open in Remote - Containers](
        https://xebia.com/wp-content/uploads/2023/11/v1.svg    )
](
    https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/seeli-langchain/communication-assistant-streamlit.git
)

This is a Streamlit app that uses the provides a Communication Assistant for the user. 

## How to run the app
1. create a .env file in the root directory and add the OPENAI_API_KEY to it. 
See also .env.example
2. Run the following command to create the sqlite database
```bash
python ./src/create_tables.py
```
3. Run the following command to start the streamlit app
```bash	
streamlit run ./src/app.py
```

