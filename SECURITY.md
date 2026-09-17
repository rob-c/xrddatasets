# Security

## Reporting a vulnerability

Mail <robert.andrew.currie@gmail.com> with a description and, if you have one,
a reproducer. Please do not open a public issue for anything that lets one
party read or write another party's data. Expect an acknowledgement within a
few working days.

## What this package is trusted with

It downloads archives from strangers and unpacks them. Every dataset is
somebody else's zip, tarball, HDF5 file or pickle, fetched over the network
and read on the machine doing the converting, so the threat model here is
"the publisher's bytes are hostile" — whether because the publisher was
compromised, a mirror was, or the network in between was.

Credentials, TLS and the transport belong to
[PyXRootDClient](https://github.com/rob-c/xrd), whose
[SECURITY.md](https://github.com/rob-c/xrd/blob/main/SECURITY.md) is the
document for those; parsing the ROOT files this writes belongs to
[xrdroot](https://github.com/rob-c/xrdroot).

## What the implementation guarantees

**A pickle never names an arbitrary callable.** The publishers who ship NumPy
pickles are read through an unpickler that permits array reconstruction and
nothing else; anything else in the stream is refused by name, so a dataset
cannot execute code by being converted.

**An archive cannot write outside the directory it is unpacked into.** Member
names are checked before extraction, so neither an absolute path nor one that
climbs out with `..` can place a file elsewhere.

**A source is bounded before it is fetched, not after.** Every registered
dataset records the size of what it publishes, a build refuses a source that
arrives materially larger than that, and anything over the ceiling has to be
admitted explicitly with `--allow-oversize`. A partial download is written to
a `.part` and only renamed into place once it is complete.

**What is published is what was converted.** `xrd-datasets verify` reopens
every file in a built directory and compares it with the `index.json` beside
it; the index is refused if it does not match the bytes it describes, so a
catalogue cannot quietly point at something other than what was checked.

**Licences are data, not decoration.** A dataset whose licence does not allow
redistribution is left out of a build unless `--all` says otherwise, and the
licence statement is written into the converted file itself.
