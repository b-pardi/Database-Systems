#!/bin/bash

#java
echo "JAVA"
javac Final.java
java -classpath ".:sqlite-jdbc-3.32.3.2.jar" Final

#python
echo ""
echo ""
echo "PYTHON"
python3 Final.py

