giSeriesDate [![Build Status](https://travis-ci.org/muflone/giseries_date.svg?branch=master)](https://travis-ci.org/muflone/giseries_date)
=====
**Descrizione:** Converte date in formato iSeries.

**Copyright:** 2016 Fabio Castelli (Muflone) <muflone(at)vbsimple.net>

**Licenza:** GPL-2+

**Codice sorgente:** https://github.com/muflone/giseries_date

**Documentazione:** http://www.muflone.com/giseries_date/

Requisiti di sistema
--------------------

* Python 2.x (sviluppato e testato per Python 2.7.5)
* Libreria GTK+ 3.0 per Python 2.x
* Libreria GObject per Python 2.x
* Libreria XDG per Python 2.x
* Libreria Distutils per Python 2.x (generalmente fornita col pacchetto Python)

Installazione
-------------

E' disponibile uno script di installazione distutils per installare da sorgenti.

Per installare nel tuo sistema utilizzare:

    cd /percorso/alla/cartella
    python2 setup.py install

Per installare i files in un altro percorso invece del prefisso /usr standard
usare:

    cd /percorso/alla/cartella
    python2 setup.py install --root NUOVO_PERCORSO

Utilizzo
--------

Se l'applicazione non è stata installata utilizzare:

    cd /path/to/folder
    python2 giseries_date.py

Se l'applicazione è stata installata utilizzare semplicemente il comando
giseries_date.
