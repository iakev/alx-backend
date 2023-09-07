# 0x03. Queuing System in JS

In this project, we explore the world of queuing systems using RabbitMQ and JavaScript. We'll learn about RabbitMQ, a powerful and flexible open-source message broker, and how to use it for various messaging patterns.

## Program Descriptions

Please select a program from the list below:

- **[0-redis_client.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/0-redis_client.js):** Basic Redis client script for connecting to a Redis server.

- **[1-redis_op.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/1-redis_op.js):** Redis operations script for performing basic Redis operations.

- **[2-redis_op_async.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/2-redis_op_async.js):** Asynchronous Redis operations script using callbacks.

- **[4-redis_advanced_op.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/4-redis_advanced_op.js):** Advanced Redis operations script for more complex Redis interactions.

- **[5-publisher.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/5-publisher.js):** Redis publisher script for publishing messages to a Redis channel.

- **[5-subscriber.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/5-subscriber.js):** Redis subscriber script for subscribing to a Redis channel and receiving messages.

- **[6-job_creator.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/6-job_creator.js):** Job creator script for creating and enqueueing jobs in a Redis queue.

- **[6-job_processor.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/6-job_processor.js):** Job processor script for processing jobs from a Redis queue.

- **[7-job_creator.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/7-job_creator.js):** Job creator script with job priority support.

- **[7-job_processor.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/7-job_processor.js):** Job processor script with job priority support.

- **[8-job.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/8-job.js):** Job class for representing jobs in a queuing system.

- **[8-job.test.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/8-job.test.js):** Test script for testing the Job class.

- **[9-stock.js](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/9-stock.js):** Stock market simulation script using Redis pub/sub.

- **[dump.rdb](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/dump.rdb):** Redis database snapshot file.

- **[package.json](https://github.com/iakev/alx-backend/blob/main/0x03-queuing_system_in_js/package.json):** Node.js project configuration file.


## Compilation and Execution

For the compilation and execution of the JavaScript scripts, follow these steps:

To compile and execute the JavaScript scripts in this directory, you'll need Node.js installed on your system. If you don't have Node.js installed, you can download and install it from the [official Node.js website](https://nodejs.org/).

Once you have Node.js installed, follow these steps:

1. Open your terminal.

2. Navigate to the directory containing the JavaScript script you want to run.

3. Use the `node` command to execute the script. Replace `script.js` with the name of the JavaScript script you want to run:

   ```bash
   node iscript.js
   ```
   For example, to run 0-redis_client.js, you would use:

   ```bash
   node 0-redis_client.js
   ```

**Note**: If you want to install the required dependencies specified in the package.json file for this project, you can do so with the following commands:

1. Navigate to the directory containing package.json.

2. Run the following command to install the dependencies:

```bash
npm install
```

This will install all the necessary packages specified in package.json. After that, you can run the JavaScript scripts as described above.

## Resources

Read or watch:

- [Redis quick start](https://redis.io/docs/getting-started/): Get started quickly with Redis, an in-memory data store.

- [Redis client interface](https://redis.io/docs/ui/cli/): Explore various Redis client libraries and interfaces.

- [Redis client for Node JS](https://github.com/redis/node-redis): Find the official Redis client for Node.js on npm.

- [Kue deprecated but still used in the industry](https://github.com/Automattic/kue): Learn about Kue, a task queue for Node.js, which is deprecated but still in use in the industry.


   
   
