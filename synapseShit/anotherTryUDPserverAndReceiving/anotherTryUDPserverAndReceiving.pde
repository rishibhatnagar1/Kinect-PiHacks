import hypermedia.net.*;
int PORT_RX=9000; //port
String HOST_IP="127.0.0.1"; //ip address
UDP udp;
String receivedFromUDP = "";

void setup() {
  size(400,400);
  udp= new UDP(this,PORT_RX,HOST_IP);
  udp.log(true);
  udp.listen(true);
  super.start(); 
}

void draw() {
  background(0);
  text(decode(receivedFromUDP), 50, 50);
}


void receive(byte[] data, String HOST_IP, int PORT_RX) {
//String value = new String(data);
//receivedFromUDP =value;
  println(data);

}

String decode(String s)
{
  String eu = s.substring(10);
  byte[] ba = javax.xml.bind.DatatypeConverter.parseBase64Binary(eu);
  try
  { 
    return new String(ba, "UTF-8");
  }
  catch (Exception e)
  {
    println(e);
  }
  return null; // Only if we had the exception, which shouldn't happen if you don't change the encoding...
}

