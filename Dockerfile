FROM jupyter/scipy-notebook
COPY jupyter_server_config.py /etc/jupyter/
RUN pip3 --no-cache-dir install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
COPY manual /home/jovyan/work/
