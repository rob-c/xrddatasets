"""The datasets machine learning is taught with, written as ROOT files.

    >>> import xrddatasets                                   # doctest: +SKIP
    >>> datasets.convert("cifar10", "cifar10.root")          # doctest: +SKIP
    {'train_airplane': 5000, 'train_automobile': 5000, ...}

Physics keeps its data in ROOT and reads it over XRootD; everyone else keeps
theirs in whatever the framework of the year unpacks. That is a shame in one
direction only - the format is perfectly good at images and tables - so this
module converts the sets people actually teach and benchmark with into ROOT
files, laid out the way a training loop wants them: one tree per class, a
fixed-size array per entry, the label beside it, and the row's place in the
original file so any number can be traced back to where it came from.

Nothing is redistributed here. Each dataset is fetched from the people who
publish it, on the machine doing the converting, and :attr:`DATASETS` records
what each one is and what its licence says. The converted file carries that
same statement in an ``about`` key, so a file that outlives this program still
says where it came from.

Almost every archive is read with the standard library: IDX, tar, zip, a zip
inside a zip, gzip, WAV, ARFF, CSV and the XML a spreadsheet keeps inside its
own zip. The few large scientific formats use narrowly scoped optional readers
for HDF5 and JPEG. What comes out is pictures, sound, sentences, tables and
plain blocks of numbers, because a training loop should not have to care which
of those it is reading. Some sets have a class to sort a row into and some have
a number to predict from it; both are here. The CIFAR sets are taken in their
binary distribution rather than the Python one on purpose: that one is a
pickle, and unpickling a download is a way to run somebody else's code.
"""

from .catalogue import (
    CIFAR,
    DATASETS,
    IDX_FILES,
    IDX_TYPES,
    IMAGE_BASKET,
    MISSING,
    MNIST_MIRROR,
    REQUIRED,
    TABLE_BASKET,
    Audio,
    Dataset,
    Images,
    Large,
    Matrix,
    Table,
    convert,
    describe,
    fetch,
    licence_url,
    read_arff,
    read_idx,
    read_table,
    read_xlsx,
    redistributable,
)

__all__ = [
    "CIFAR",
    "DATASETS",
    "IDX_FILES",
    "MNIST_MIRROR",
    "IDX_TYPES",
    "IMAGE_BASKET",
    "MISSING",
    "REQUIRED",
    "TABLE_BASKET",
    "Audio",
    "Dataset",
    "Images",
    "Large",
    "Matrix",
    "Table",
    "convert",
    "describe",
    "fetch",
    "licence_url",
    "read_arff",
    "read_idx",
    "read_table",
    "read_xlsx",
    "redistributable",
]
