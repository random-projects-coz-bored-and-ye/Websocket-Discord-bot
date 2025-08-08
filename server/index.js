    const { WebSocketServer } = require("ws");
    const server = new WebSocketServer({ port: 3000 });
    server.on("connection", (socket) => {
    console.log("!~ Client Connected ~!");
    socket.on("message", (data) => {
        console.log("MESSAGE RECEIVED: ", data.toString());
        server.clients.forEach(client => {
        if (client.readyState === client.OPEN) { 
            client.send(data.toString());
        }
        });
    });
    socket.on("close", () => {
        console.log("Client disconnected");
    });
    socket.on("error", (error) => {
        console.error("Socket error:", error);
    });
    });
    console.log("WebSocket server running on ws://localhost:3000");
