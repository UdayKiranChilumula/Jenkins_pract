#!/bin/bash

echo "SYSTEM METRICS REPORT"
echo ""
echo "CPU Usage:"
top -b -n1 | grep "Cpu(s)"
echo ""

echo "Memory Usage:"
free -h
echo ""

echo "Disk Usage:"
df -h
echo ""
