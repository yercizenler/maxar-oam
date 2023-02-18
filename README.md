```
WARNING: The repo tries to automatize MAXAR image processing
before uploading to OAM on a local machine. The design and dependencies
are far away from a production-ready code.

contact: batuhankavlak4@gmail.com
```

# Install Dependency

- Only supports OS systems.
- Install GDAL to your local machine
- Install `requirements.txt` on python

# Set AWS Credentials

- Set the following environment keys as `.env` on vscode or to your bash
```
MAXAR_AWS_KEY_ID=...
MAXAR_AWS_SECRET=...
```

# Run the script

```
python3 main.py -scene_id 2312938 -merge_path "SCENES/.."
```

# Uploading to OAM

- The image will be in `https://cdn.hotosm.org/OAMimagery/<name of file>`