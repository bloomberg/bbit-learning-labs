# Redis Basics

Redis (Remote Dictionary Server) is an open-source, in-memory key-value store widely used for caching, real-time analytics, message brokering, and more. It is designed for high performance and flexibility with support for various data structures.

## Key Features
1. **In-Memory Storage**: All data resides in memory for fast read/write operations.
2. **Data Persistence**: Supports saving data to disk using snapshots or append-only files.
3. **Rich Data Structures**: Offers multiple data types like strings, hashes, lists, sets, and sorted sets.
4. **Pub/Sub Messaging**: Enables message broadcasting and subscribing for real-time applications.
5. **Replication and Clustering**: Supports master-slave replication and horizontal scaling with clustering.

## Core Concepts

### 1. Key-Value Store
Redis stores all data as key-value pairs.

Example:
```bash
SET mykey "Hello, Redis!"
GET mykey
```

### 2. Data Types
*Strings*: Basic key-value storage.
```
SET name "Redis"
GET name
```

*Lists*: Ordered collections of strings.
```
LPUSH mylist "item1"
LPUSH mylist "item2"
LRANGE mylist 0 -1
```

*Hashes*: Key-value pairs within a key.
```
HSET user name "Alice"
HSET user age 25
HGETALL user
```

*Sets*: Unordered collections of unique items.
```
SADD myset "item1"
SADD myset "item2"
SMEMBERS myset
```

*Sorted* *Sets*: Items ordered by scores.
```
ZADD leaderboard 100 "Alice"
ZADD leaderboard 200 "Bob"
ZRANGE leaderboard 0 -1 WITHSCORES
```

### 3. Persistence

Redis provides two persistence mechanisms:
* RDB Snapshots: Periodic snapshots of the dataset.
* AOF (Append-Only File): Logs every write operation for durability.

### 4. Pub/Sub

Allows message broadcasting to subscribers.
```
SUBSCRIBE channel
PUBLISH channel "Hello, Subscribers!"
```

#### Advantages
* Extremely fast with low latency.
* Simple and flexible API.
* Rich ecosystem with many client libraries.
* Built-in support for high availability.

### Basic Commands

Run the Redis CLI:
```
redis-cli
```

Try basic operations:
```
SET key "value"
GET key
```

## Use Cases
1. Caching: Store frequently accessed data for performance optimization.
2. Session Management: Manage user sessions in web applications.
3. Leaderboards: Use sorted sets to track scores.
4. Real-Time Analytics: Process and analyze data streams in real-time.
5. Message Queues: Use lists or pub/sub for task queues and messaging.
