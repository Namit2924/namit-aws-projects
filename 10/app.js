const express = require("express");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send("🚀 Node.js App Running in Docker + AWS ECS");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});