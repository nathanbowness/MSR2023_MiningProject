# Indonesian GPT-2 Demo

Part of the [Huggingface JAX/Flax event](https://discuss.huggingface.co/t/open-to-the-community-community-week-using-jax-flax-for-nlp-cv/).

To build the Docker and activate the Docker compose, run:

```
make build
```

If you only need to refresh the Docker compose:

```
make up
```

Check the logs:

```
make logs
```

If you're in a debugging mode, change the `DEBUG` variable in `.env` to enable hot reload.

- FastAPI documentation: http://localhost:8000  
- Streamlit UI: http://localhost:8501

## Credits
Base template from [here](https://github.com/davidefiocco/streamlit-fastapi-model-serving).