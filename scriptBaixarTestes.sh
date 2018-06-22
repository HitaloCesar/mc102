#!/bin/bash

for i in {01..20}
do
	mkdir /home/hitalo/Programas/python/mc102/lab$i
	cd /home/hitalo/Programas/python/mc102/lab$i
	mkdir inputs
	cd /home/hitalo/Programas/python/mc102/lab$i
	mkdir outputs
done


for j in {01..20}
do
	
	cd /home/hitalo/Programas/python/mc102/lab$j/inputs
	for i in {01..15}
	do
		curl -k  https://susy.ic.unicamp.br:9999/mc102qrst/$j/dados/arq$i.in > arq$i.in

	done

	cd /home/hitalo/Programas/python/mc102/lab$j/outputs
	for i in {01..15}
	do
		curl -k  https://susy.ic.unicamp.br:9999/mc102qrst/$j/dados/arq$i.out > arq$i.out

	done
done
	
