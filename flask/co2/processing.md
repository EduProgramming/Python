# Processing Code

```java
import processing.net.*;

Server server;
Client client;

int startX = 10;
int startY = 30;
int xInterval = 200;
int yInterval = 50;

void setup() {
  size(800, 600);
  textSize(24);
  background(255);
  PFont fontSetting = createFont("굴림체", 32); // 한글 사용하고 싶을시
  textFont(fontSetting); // 폰트 설정
  fill(0, 0, 0); // 폰트 색상 -> 검정, (r, g, b)
  server = new Server(this, 12345);
  text("교통수단", startX, startY);
  text("km", startX + xInterval, startY);
  text("co2", startX + 2 * xInterval, startY);
  startY += yInterval;
}

void draw() {
  client = server.available();
  if (client != null) {
    try {
      String data = client.readString();
      String paramsString = split(data, '?')[1];
      String[] params = split(paramsString, '&');
      
      for (String param : params) {
        String[] paramData = split(param, '=');
        // String paramKey = paramData[0];
        String paramValue = paramData[1];
        
        println(paramValue);
        text(paramValue, startX, startY);
        startX += xInterval;
      }
    } catch(Exception e) {
      text(e.toString(), startX, startY);
    }
    startX = 10;
    startY += yInterval;
    
    client.write("HTTP/1.1 200 OK\r\n");
    client.stop();
  }
}
```

프로세싱에서 작업하는 불편함이 있어서 Flask로 작업