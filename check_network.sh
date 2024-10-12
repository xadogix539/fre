#!/bin/bash

echo "Checking network connection..."

# Check if the network interface is up
if ip link show | grep -q "state UP"; then
    echo "Network interface is UP."
else
    echo "Network interface is DOWN. Please check your connection."
    exit 1
fi

# Check DNS resolution
echo -n "Checking DNS resolution for google.com... "
if nslookup google.com > /dev/null 2>&1; then
    echo "Success!"
else
    echo "Failed!"
    echo "Please check your DNS settings."
    exit 1
fi

# Ping a known server
echo -n "Pinging google.com... "
if ping -c 4 google.com > /dev/null 2>&1; then
    echo "Success!"
else
    echo "Failed! Please check your internet connection."
    exit 1
fi

# Check external IP address
echo "Fetching external IP address..."
external_ip=$(curl -s https://api.ipify.org)
if [ $? -eq 0 ]; then
    echo "Your external IP address is: $external_ip"
else
    echo "Failed to fetch external IP address."
    exit 1
fi

echo "Network check completed successfully!"
