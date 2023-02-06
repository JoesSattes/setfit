__version__ = "0.6.0.dev0"

import warnings

from .data import add_templated_examples, sample_dataset
from .modeling import SetFitHead, SetFitModel
from .trainer import SetFitTrainer, Trainer
from .trainer_distillation import DistillationSetFitTrainer, DistillationTrainer


# Ensure that DeprecationWarnings are shown by default, as recommended by
# https://docs.python.org/3/library/warnings.html#overriding-the-default-filter
warnings.filterwarnings("default", category=DeprecationWarning)
