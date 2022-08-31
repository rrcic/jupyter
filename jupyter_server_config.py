# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# mypy: ignore-errors
import os
import stat
import subprocess

from jupyter_core.paths import jupyter_data_dir

c = get_config()  # noqa: F821
c.ServerApp.ip = "0.0.0.0"
c.ServerApp.port = 8888
c.ServerApp.open_browser = False

# docker health check demands that base_url equals JUPYTERHUB_SERVICE_PREFIX
# https://github.com/jupyter/docker-stacks/issues/1709
c.ServerApp.base_url = os.getenv('JUPYTERHUB_SERVICE_PREFIX')

# iframe
c.ServerApp.tornado_settings = { 
    'headers': { 
        'Content-Security-Policy': "frame-ancestors  * 'self' "
    } 
}

# https://github.com/nteract/hydrogen/issues/922
c.ServerApp.disable_check_xsrf = True

# password:jupyter
# c.ServerApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$w9kYb4Hs9c3rrnyIf3cTIg$fR7mnOrBP8+gJA4fKAv8N7AMheAaiAWVGXNM6BVhFnM'
c.ServerApp.passwork = ''
c.ServerApp.token = ''

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False

# Generate a self-signed certificate
OPENSSL_CONFIG = """\
[req]
distinguished_name = req_distinguished_name
[req_distinguished_name]
"""
if "GEN_CERT" in os.environ:
    dir_name = jupyter_data_dir()
    pem_file = os.path.join(dir_name, "notebook.pem")
    os.makedirs(dir_name, exist_ok=True)

    # Generate an openssl.cnf file to set the distinguished name
    cnf_file = os.path.join(os.getenv("CONDA_DIR", "/usr/lib"), "ssl", "openssl.cnf")
    if not os.path.isfile(cnf_file):
        with open(cnf_file, "w") as fh:
            fh.write(OPENSSL_CONFIG)

    # Generate a certificate if one doesn't exist on disk
    subprocess.check_call(
        [
            "openssl",
            "req",
            "-new",
            "-newkey=rsa:2048",
            "-days=365",
            "-nodes",
            "-x509",
            "-subj=/C=XX/ST=XX/L=XX/O=generated/CN=generated",
            f"-keyout={pem_file}",
            f"-out={pem_file}",
        ]
    )
    # Restrict access to the file
    os.chmod(pem_file, stat.S_IRUSR | stat.S_IWUSR)
    c.ServerApp.certfile = pem_file

# Change default umask for all subprocesses of the notebook server if set in
# the environment
if "NB_UMASK" in os.environ:
    os.umask(int(os.environ["NB_UMASK"], 8))
