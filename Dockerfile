FROM jupyter/scipy-notebook
RUN pip3 --no-cache-dir install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
COPY jupyter_server_config.py /etc/jupyter/
COPY .gainmanual.sh /home/jovyan/work/
COPY manual /home/jovyan/work/
WORKDIR /home/jovyan/work
