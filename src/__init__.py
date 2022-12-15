# read version from installed package
from importlib.metadata import version
__version__ = version("yi_package")

from yi_package import yi_package