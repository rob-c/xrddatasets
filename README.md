# xrddatasets

Open datasets converted into streamable ROOT files, and the site that serves
them.

```console
$ xrd-datasets build /srv/datasets --only 'mnist*'
$ xrd-datasets verify /srv/datasets
$ xrd-datasets site /srv/datasets --base-url https://ai.example.org
```

```python
import xrdml

data = xrdml.load("mnist")          # found by name in that site's index.json
```

More than fourteen hundred datasets and teaching tables, each fetched from
whoever publishes it and written as ROOT laid out the way a training loop
wants it: one tree per class, a fixed-size array per entry, the label beside
it, and the row's place in the original file so any number can be traced back
to where it came from. Where what is predicted is a number rather than a
class, one tree of every row.

**Nothing is redistributed here — only the converter.** Each dataset is pulled
from its publisher on the machine doing the converting, and the entry records
what it is and what its licence says. The converted file carries that same
statement in an `about` key, so a file that outlives this program still says
where it came from. `--all` is what it takes to include a dataset whose
licence does not allow redistribution, so that decision is always somebody's.

## Install

    pip install "git+https://github.com/rob-c/xrddatasets#egg=xrddatasets[datasets]"

The `datasets` extra is the publishers' own formats — HDF5, Parquet, TIFF,
Igor, PIL-readable images. None of it is imported until a dataset that arrives
in one of those formats is built, so a catalogue read and most of a site build
need none of it.

That brings [`xrdml`](https://github.com/rob-c/xrdml) — the loader these files
are written for — and, under it,
[`xrdroot`](https://github.com/rob-c/xrdroot) for the format and
[`pyxrootdclient`](https://github.com/rob-c/xrd) for the transport.

## What is in the catalogue

The MNIST family and EMNIST, CIFAR-10 and CIFAR-100, Semeion, the spoken
digits of FSDD, the SMS Spam Collection, MiniBooNE, the MAGIC telescope, the
HTRU2 pulsar survey, Human Activity Recognition, Iris, the Palmer penguins,
Covertype, Adult, Mushroom and the rest of the UCI teaching shelf; more than
220 disk-backed sources from UCI, NIST, Toronto, Zenodo and Salesforce
including SUSY, JetNet, OmniFold Big, TinySOL, Speech Commands, AudioMNIST,
WikiText-103, ReefSet, BirdSet and Year Prediction MSD; the 17 CC BY MedMNIST
image and volume problems, Galaxy10 SDSS morphology, Curiosity rover surface
images and SWEFil solar-filament masks; 100 crystal-image regression tasks
over the 675,204 inorganic structures of Alex-MP-20; 100 visual field-learning
tasks from sixteen CC BY archives in The Well, spanning acoustics, active
matter, nonlinear waves, planetary atmospheres, convection, hydrodynamic
instabilities, soft matter, plasma and stellar astrophysics; three hundred and
thirty-two teaching tables of the R world; sixty-eight country-year tables
charted by Our World in Data; and 499 explicitly licensed public Hugging Face
Hub repositories.

Images, audio, text, dates, timestamps, spreadsheets and plain blocks of
numbers all fit. See [the datasets](docs/datasets.md) for what each one is.

## The site

`xrd-datasets site` writes the directory a catalogue is served from: the
converted files, the `index.json` that lets `xrdml.load("mnist")` find one by
name, a page describing them, and the nginx and XRootD configuration that put
it on the web. Deployment is deliberately "unpack the directory where the
server looks" — the directory *is* the deploy.

`xrd-datasets verify` reopens every file and compares it, byte for byte, with
the index beside it. A rebuild keeps a file that has not changed rather than
reconverting it.

See [running a site](docs/datasets-site.md), and
`.github/workflows/site.yml` for the whole thing as one job.

## Where this sits

    xrd          the XRootD protocol, files, copies, auth       (pyxrootdclient)
      └─ xrdroot        the ROOT file format
           └─ xrdml     trees to tensors, a URL to a training loop
                └─ xrddatasets   this package: open data converted to ROOT, and its site

## Tests

    pip install -e ".[dev,datasets]"
    pytest -q

Without the `datasets` extra the tests that need a publisher's format skip and
the rest run.

## Licence

LGPL-3.0-or-later for the code here. See [COPYING](COPYING) and
[LICENSE](LICENSE). Each dataset keeps its own licence, which is recorded in
its catalogue entry and written into every file converted from it.
