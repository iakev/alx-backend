import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];
const queue = kue.createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
  // console.log(`got job phone number as ${job.data.phoneNumber} and message is ${job.data.message}`);
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
}
