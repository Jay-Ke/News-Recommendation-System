var jayson = require('jayson');

// create a client
var client = jayson.client.http({
  hostname: 'localhost',
  port: 4040
});

// Test Rpc method
function add(a, b, callback) {
  client.request('add', [a, b], function(err, response) {
    if(err) throw err;
    console.log(response);
    callback(response.result);
  });
};

function getNewsSummariesForUser(user_id, page_num, callback) {
  client.request('getNewsSummariesForUser', [user_id, page_num], function(err, response) {
    if(err) throw err;
    console.log(response);
    callback(response.result);
  });
};

function logNewsClickForUser(user_id,newsId){
  client.request('logNewsClickForUser', [user_id, newsId], function(err, response) {
    if(err) throw err;
    console.log(response);
  });
}

module.exports = {
  add : add,
  getNewsSummariesForUser : getNewsSummariesForUser,
  logNewsClickForUser : logNewsClickForUser
};
