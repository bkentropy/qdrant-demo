# Server
## Local
To start the qdrant server locally, run:
```
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```
To get the browser UI, go to http://localhost:6333/dashboard.

## Remote
I never got the remote running. But if you set
```
export QDRANT_API_KEY=<KEY>
export QDRANT_URL=<your-server-url>
```
And change the lines in `main.py` you can try it out.


# Client
See `main.py` to init, and `query.py` to make queries.

# Package.md
I kind of gave up using the in browser UI console, because it would have taken a large amount of work to:
- create a new collection, and add the embedding. I guess they want you to do that first...?
- after ad hoc creating embedding I would have also had to format everything, consumable by the browser console.

# Data
## Source data
All data was sourced from [here](https://repo.anaconda.com/pkgs/main/channeldata.json)
I just pulled the names, summaries, and descriptions from the json file.

## Model data
The embeddings are small enough to include in the repo.