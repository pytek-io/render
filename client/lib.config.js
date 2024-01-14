const HtmlWebpackPlugin = require("html-webpack-plugin");
const path = require("path");

module.exports = {
  watch: false,
  entry: { index: path.resolve(__dirname, "src", "app.tsx") },
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "render.js",
    library: "render",
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "babel-loader",
        exclude: /node_modules/,
      },
    ],
  },
};
