import { createClient } from 'redis';

const client = createClient ({
	url: 'redis://localhost:6379',
});
client.on('connect', () => {
	console.log('Redis client connected to the server');
});
client.on('error', (err) => {
	console.log('Redis client not connected to the server: ERROR_MESSAGE', err);
});
(async () => {
	    await client.connect();
})();
function setNewSchool(schoolName, value) 
