#!/bin/bash

for i in {01..20}
do
	cd /home/hitalo/Programas/python/mc102/lab$i
	curl -k https://susy.ic.unicamp.br:9999/mc102qrst/$i/enunciado.html > enunciado.html
done
