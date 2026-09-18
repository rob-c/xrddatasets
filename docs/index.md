# xrddatasets

Open datasets converted into streamable ROOT files, and the site that serves
them.

```console
$ xrd-datasets build /srv/datasets --only 'mnist*'
$ xrd-datasets verify /srv/datasets
$ xrd-datasets site /srv/datasets --base-url https://ai.example.org
```

Each dataset is fetched from whoever publishes it, converted on the machine
doing the building, and written with its licence inside it. Nothing is
redistributed here — only the converter.

Start with [the datasets](datasets.md) for what is in the catalogue and how
each one is laid out, [running a site](datasets-site.md) for putting a
directory of them on the web, and the [API](api.md) for converting one
yourself.

## The stack

| Package | What it is |
| --- | --- |
| [`xrdclient`](https://github.com/rob-c/xrdclient) | the XRootD protocol, files, copies, authentication |
| [`xrdroot`](https://github.com/rob-c/xrdroot) | the ROOT file format |
| [`xrdml`](https://github.com/rob-c/xrdml) | trees to tensors, a URL to a training loop |
| `xrddatasets` | this package: open data converted to ROOT, and its site |
