"""
Script that trains Tensorflow models on PDBbind dataset.
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

__author__ = "Bharath Ramsundar"
__copyright__ = "Copyright 2016, Stanford University"
__license__ = "MIT"

import os
import numpy as np
import tensorflow as tf
# For stable runs
np.random.seed(123)
tf.set_random_seed(123)

import deepchem as dc
from deepchem.molnet import load_pdbbind_grid

from deepchem.molnet import load_pdbbind

split = "random"
subset = "full"
#pdbbind_tasks, pdbbind_datasets, transformers = load_pdbbind_grid(
#    split=split, subset=subset)

pdbbind_tasks, pdbbind_datasets, transformers = load_pdbbind(featurizer="grid", split="random", subset="refined")
train_dataset, valid_dataset, test_dataset = pdbbind_datasets

metric = dc.metrics.Metric(dc.metrics.pearson_r2_score)

current_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.join(current_dir, "%s_%s_DNN" % (split, subset))

n_features = train_dataset.X.shape[1]
model = dc.models.MultitaskRegressor(
    len(pdbbind_tasks),
    n_features,
    logdir=model_dir,
    dropouts=[.75],
    learning_rate=0.0003,
    weight_init_stddevs=[.1],
    batch_size=64)

# Fit trained model
model.fit(train_dataset, nb_epoch=100)

print("Evaluating model")
train_scores = model.evaluate(train_dataset, [metric], transformers)
valid_scores = model.evaluate(valid_dataset, [metric], transformers)

print("Train scores")
print(train_scores)

print("Validation scores")
print(valid_scores)


my_tasks,my_dataset,my_transformers = load_pdbbind(
    data_dir="/root/mydir/testdata",
    split=None

)


print(my_dataset[0])

result = model.predict(my_dataset[0],transformers=my_transformers);
#result = model.evaluate(my_dataset[0], [metric], transformers)

print("Result of prediction...")

for z in range(0,len(result)):
  print(result[z])





print (result)


