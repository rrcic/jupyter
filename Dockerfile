FROM jupyter/scipy-notebook
COPY jupyter_server_config.py /etc/jupyter/
ENV RANDOM_PATH='/jupyter/'
ENV JUPYTERHUB_SERVICE_PREFIX=${RANDOM_PATH}
RUN pip3 --no-cache-dir install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
