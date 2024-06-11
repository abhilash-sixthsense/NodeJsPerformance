const express = require("express");
const app = express();
url = "http://localhost:5000/hello";
app.get("/hello", async (req, res) => {
  data = await fetchData();
  res.send("Hello World! " + data);
});

app.listen(3000, async () => {
  console.log("Server started on port 3000 \n" + "http://localhost:3000/hello");
});

const axios = require("axios");

async function fetchData() {
  data = "";

  const response = await axios.get(url);
  console.log(`Status: ${response.status}`);
  console.log(`Headers: ${JSON.stringify(response.headers)}`);
  console.log(`Body: ${response.data}`);
  data = response.data;

  return data;
}
