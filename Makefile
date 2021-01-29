# This should probably be replaced by some python code
# it may not be smaller but there will be less manual work
# to update

IP_NAME=riscv-torture-rv32

TOP:=$(shell pwd)

IP_NAME_LC = $(shell echo $(IP_NAME) | tr '[:upper:]' '[:lower:]')
IP_NAME_UC = $(shell echo $(IP_NAME) | tr '[:lower:]' '[:upper:]')



# Virtualenv setup

SHELL := /bin/bash
mkvenv:
	. `which virtualenvwrapper.sh` && mkvirtualenv -p python3 $(IP_NAME_LC)

freeze:
	pip freeze > requirements.txt

install_env:
	pip install -r requirements.txt

export: TOP

check-syntax:
	TOP=$(TOP) iverilog -t null -o tb  -c sim/verilog/vlist_tb.txt
