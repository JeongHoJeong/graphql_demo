const path = require('path')

module.exports = {
  entry: path.resolve(__dirname, 'app/static/js/main.js'),
  output: {
    path: path.resolve(__dirname, 'app/static/dist'),
    filename: 'main.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
      },
      {
        test: /\.css$/,
        loader: ['style-loader', 'css-loader'],
      },
    ],
  },
}
