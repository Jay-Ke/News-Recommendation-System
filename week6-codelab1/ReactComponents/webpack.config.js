const path = require('path');
const SERVER_PORT = process.env.SERVER_PORT || 8080;

module.exports = {

    entry: "./src/index.jsx",

    output: {
        path: path.join(__dirname, 'public'),
        filename: 'bundle.js',
        publicPath: '/'
    },

    module: {

        rules: [

            { test: /\.css$/, loader: 'style-loader!css-loader' },

            { test: /\.jsx?$/, exclude: path.join(__dirname, 'node_module'), loader: "babel-loader" }

        ]

    },

    resolve: {
        extensions: [".js", ".jsx", ".css"]
    },

    devServer: {
        contentBase: path.join(__dirname, 'public'),
        historyApiFallback: true,
        port: SERVER_PORT,
        host: '0.0.0.0',
        inline: true,
    }
};