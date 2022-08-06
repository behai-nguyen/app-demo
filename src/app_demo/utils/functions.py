"""
Application scope utility functions.
"""
from os import (
    getcwd,
    path,
)

def template_root_path( source_dir='src' ):
    """This method assumes the project has the following layout:

        f:\project_name\
        |
        |-- ...
        |
        |-- src\
        |   |
        |   |-- project_name\
        |       |
        |       |-- ...
        |       |
        |       |-- templates\
        |       |   |
        |       |   |-- base_template.html
        |       |   |
        |       |   |-- auth\
        |       |   |-- report\
        |       |
        |       |-- static\

    Return:

	    f:\project_name\{source_dir}\project_name\templates
		/volume1/web/project_name/src/project_name/templates
    """
    base_dir = getcwd()

    drive, root_path = path.splitdrive( base_dir )

    paths = root_path.split( '/' )
    project_path = paths[len(paths)-1][1:] if len(drive) > 0 else paths[len(paths)-1]

    return path.join( base_dir, source_dir, project_path, 'templates' )