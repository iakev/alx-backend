import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error(`Jobs is not an array`);
  }
  for (const job of jobs) {
    const newJob = queue.create('push_notification_code_3', job).save(
      (error) => {
        if ( !error ) {
        console.log(`Notification job created: ${newJob.id}`);
        }
      }
    );
    newJob.on('complete', (result) => {
      console.log(`Notification job ${newJob.id} completed`);
    });
    newJob.on('failed', (error) => {
  
      console.log(`Notification job ${newJob.id} failed:`, error);
    });
    newJob.on('progress', (progress, data) => {
      console.log(`Notification job ${newJob.id} ${progress}% complete`);
    });
  }
}
