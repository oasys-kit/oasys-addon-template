# oasys-addon-template

This project is a template for creating add-ons in oasys. 

OASYS (OrAnge SYnchrotron Suite) is an open-source Graphical Environment
for optic simulation softwares used in synchrotron facilities, based on
Orange (http://orange.biolab.si/)

Before installing this package you should install Oasys: 

https://github.com/srio/oasys-installation-scripts/wiki


Then activate the Oasys virtual environment: 

source /users/me/OASYS\_VE/bin/activate

cd /users/me/OASYS\_VE

and then unpack this project, e.g., 

git clone  https://github.com/srio/oasys-addon-template oasysaddontemplate

cd oasysaddontemplate
python develop

and start Oasys: 
/users/me/start\_oasys.sh

you should get the new package. 

Then start replacing <oasysaddontemplate> by your Oasys project nane and
populate it with your applications. 


