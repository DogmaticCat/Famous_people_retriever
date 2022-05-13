#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")


name = "famous-people-retriever"
default_task = "publish"


@init
def set_properties(project):
    project.set_property('coverage_break_build', False)
