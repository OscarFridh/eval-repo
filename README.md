# Eval-repo

This repository is intended to be used to evaluate models for our thesis. Code and Docs will be added, modified and deleted in future commits. Changes that introduce inconsistencies between code and docs will be manually [labeled](misses.json) so that they can be identified during evaluation.

To evaluate a model we will go through all commits from start to end, comparing the model prediction with the labels to obtain accuracy and recall. The commits can be obtained in order using the following script:
```shell
git log --reverse --format=format:%H
```