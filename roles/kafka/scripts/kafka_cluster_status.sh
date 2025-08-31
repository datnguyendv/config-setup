#!/bin/bash

# Kafka Cluster Status Check Script
set -e

KAFKA_HOME=${KAFKA_HOME:-/opt/kafka}
BOOTSTRAP_SERVERS=${BOOTSTRAP_SERVERS:-localhost:9092}

echo "=== Kafka Cluster Status ==="
echo "Bootstrap Servers: $BOOTSTRAP_SERVERS"
echo

# Check broker connectivity
echo "1. Checking broker connectivity..."
$KAFKA_HOME/bin/kafka-broker-api-versions.sh --bootstrap-server $BOOTSTRAP_SERVERS --timeout 5000

# List topics
echo -e "\n2. Listing topics..."
$KAFKA_HOME/bin/kafka-topics.sh --list --bootstrap-server $BOOTSTRAP_SERVERS

# Show consumer groups
echo -e "\n3. Listing consumer groups..."
$KAFKA_HOME/bin/kafka-consumer-groups.sh --list --bootstrap-server $BOOTSTRAP_SERVERS

# Cluster metadata
echo -e "\n4. Cluster metadata..."
$KAFKA_HOME/bin/kafka-metadata-shell.sh --help >/dev/null 2>&1 && {
  echo "KRaft mode detected"
} || {
  echo "ZooKeeper mode detected"
}

echo -e "\n=== Status Check Complete ==="
