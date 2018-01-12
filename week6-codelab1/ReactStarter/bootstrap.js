var opn = require('opn');
const SERVER_PORT = process.env.SERVER_PORT || 8080;

require('./node_modules/webpack-dev-server/bin/webpack-dev-server.js');

opn(`http://localhost:${SERVER_PORT}`, {app: 'chrome'}); //webpack-dev-server default port