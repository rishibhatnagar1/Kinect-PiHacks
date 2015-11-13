import processing.net.*;
Server myServer;
Client myClient;
int val = 0;
 
void setup() {
  size(200, 200);
  // Starts a myServer on port 5204
  myServer = new Server(this, 5204); 
  //myClient = new Client(this,"127.0.0.1",5204);
}
 
void draw() {
  //myClient.write("Bullshit");
}

