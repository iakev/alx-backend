import { createClient } from 'redis';

async function redisConnect() {
  const client = createClient();
  client.on('error', (error) => {
    console.log('Redis client not connected to the server: ', error.message);
  });
  client.on('ready', () => {
    console.log('Redis client connected to the server');
  });
}
redisConnect();
