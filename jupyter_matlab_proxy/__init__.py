# Copyright 2020-2021 The MathWorks, Inc.

import inspect
from pathlib import Path
from jupyter_matlab_proxy.jupyter_config import config


def _get_env(port, base_url):
    """Returns a dict containing environment settings to launch the MATLAB Desktop

    Args:
        port (int): Port number on which the MATLAB Desktop will be started. Ex: 8888
        base_url (str): Controls the prefix in the url on which MATLAB Desktop will be available.
                        Ex: localhost:8888/base_url/index.html

    Returns:
        [Dict]: Containing environment settings to launch the MATLAB Desktop.
    """
    from matlab_desktop_proxy import mwi_environment_variables as mwi_env

    return {
        mwi_env.get_env_name_app_port(): str(port),
        mwi_env.get_env_name_base_url(): f"{base_url}matlab",
        mwi_env.get_env_name_app_host(): "127.0.0.1",
    }


def setup_matlab():
    """This method is run by jupyter-server-proxy package with instruction to launch the MATLAB Desktop

    Returns:
        [Dict]: Containing information to launch the MATLAB Desktop.
    """

    import matlab_desktop_proxy

    # Get MATLAB icon from matlab_desktop_proxy
    package_path = Path(inspect.getfile(matlab_desktop_proxy)).parent
    icon_path = package_path / "icons" / "matlab.svg"
    return {
        "command": [
            matlab_desktop_proxy.get_executable_name(),
            "--config",
            config["extension_name"],
        ],
        "timeout": 100,
        "environment": _get_env,
        "absolute_url": True,
        "launcher_entry": {"title": "MATLAB", "icon_path": icon_path},
    }
