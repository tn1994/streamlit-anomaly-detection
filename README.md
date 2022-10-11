---
title: streamlit-anomaly-detection-demo
python_version: 3.10.7
sdk: streamlit
sdk_version: 1.10.0
app_file: src/app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

---

# streamlit-anomaly-detection

## Usage

1. Run build.sh

```shell
sh build.sh
```

2. Run compose_up.sh

```shell
sh compose_up.sh
```

3. Access to localhost:8501

[Access](http://localhost:8501/)

## About requirements.txt

```shell
# Basic
streamlit
pandas
numpy
matplotlib
scipy
scikit-learn

# For Anomaly Detection
changefinder
```