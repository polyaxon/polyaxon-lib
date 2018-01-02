# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from collections import OrderedDict

from polyaxon_lib.models.base import BaseModel
from polyaxon_lib.models.generators import Generator
from polyaxon_lib.models.classifiers import Classifier
from polyaxon_lib.models.regressors import Regressor
from polyaxon_lib.models.rl import (
    BaseQModel,
    BasePGModel,
    DQNModel,
    DDQNModel,
    NAFModel,
    TRPOModel,
    VPGModel
)

MODELS = OrderedDict([
    ('Classifier', Classifier),
    ('Regressor', Regressor),
    ('Generator', Generator),
    ('DQNModel', DQNModel),
    ('DDQNModel', DDQNModel),
    ('NAFModel', NAFModel),
    ('TRPOModel', TRPOModel),
    ('VPGModel', VPGModel),
])
