import redis from 'redis';

const subscriber = redis.createClient();
const channel = 'holberton school channel';
subscriber.on('ready', () => {
  console.log('Redis client connected to the server');
});
subscriber.on('error',  (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});
subscriber.on("message", (channel = channel, message) => {
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  } else {
    console.log(`${message}`);
  }
});
subscriber.subscribe(channel);
