# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from collections import OrderedDict

from polyaxon_lib.estimators.estimator_spec import EstimatorSpec
from polyaxon_lib.estimators.run_config import RunConfig
from polyaxon_lib.estimators.estimator import Estimator
from polyaxon_lib.estimators.agents import BaseAgent, Agent, PGAgent, TRPOAgent
from polyaxon_lib.estimators.hooks import HOOKS


ESTIMATORS = OrderedDict([
    ('Estimator', Estimator),
])

AGENTS = OrderedDict([
    ('Agent', Agent),
    ('PGAgent', PGAgent),
    ('TRPOAgent', TRPOAgent)
])
