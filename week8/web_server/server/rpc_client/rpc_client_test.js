var client = require('./rpc_client');

// invoke 'add'
client.add(1, 2, function(response) {
  console.assert(response == 3);
});

client.getNewsSummariesForUser('test_user', 1, function(response) {
  console.assert(response != null);
  console.log("Test passed")
});

client.logNewsClickForUser('test_user','test_news');
