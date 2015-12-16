#!/bin/bash

cat drop_tables.sql setup.sql | mysql -uroot -p 
