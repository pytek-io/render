const HtmlWebpackPlugin = require("html-webpack-plugin");
const path = require("path");

module.exports = function (env, argv) {
  const production = argv.mode === "production";
  const output = production ? "../dist" : "../render";
  return {
    watch: !production,
    entry: { index: path.resolve(__dirname, "src", "index.tsx") },
    output: {
      path: path.resolve(output), 
      publicPath: '/',
      filename: './js/[contenthash].[name].js',
    },
    plugins: [new HtmlWebpackPlugin({
      template: "src/index.html"
    })],
    resolve: {
      extensions: [".tsx", ".ts", ".js", "scss", "css"],
    },
    module: {
      rules: [
        {
          test: /\.less$/i,
          use: [
            {
              loader: "style-loader",
            },
            {
              loader: "css-loader",
            },
            {
              loader: "less-loader",
              options: {
                lessOptions: {
                  javascriptEnabled: true,
                },
              },
            },
          ],
        },
        {
          test: /\.tsx?$/,
          use: "babel-loader",
          exclude: /node_modules/,
        },
        {
          test: /\.ts?$/,
          use: "babel-loader",
          exclude: /node_modules/,
        },
        {
          test: /\.css$/,
          use: ["style-loader", "css-loader"],
        },
        {
          test: /\.scss$/,
          use: ["style-loader", "css-loader", "sass-loader"],
        },
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: ["babel-loader"],
        },
      ],
    },
  };
};
