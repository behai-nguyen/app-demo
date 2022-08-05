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
    """	
    base_dir = getcwd()
	
    drive, root_path = path.splitdrive( base_dir )
    return path.join( base_dir, source_dir, root_path[1:], 'templates' )