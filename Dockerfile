FROM jupyter/scipy-notebook
# COPY jupyter_server_config.py /etc/jupyter/
#RUN pip3 --no-cache-dir install \
#	torch==1.8.2 \
#	torchvision==0.9.2 \
#	torchaudio==0.8.2 \
#	--extra-index-url https://download.pytorch.org/whl/lts/1.8/cpu
RUN pip3 --no-cache-dir install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
