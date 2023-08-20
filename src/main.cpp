/*
This example will receive multiple universes via Art-Net and control a strip of
WS2812 LEDs via the FastLED library: https://github.com/FastLED/FastLED
This example may be copied under the terms of the MIT license, see the LICENSE file for details
*/
#include <ArtnetWifi.h>
#include <Arduino.h>
#include <FastLED.h>

#include <WiFiClient.h>
#include <WebServer.h>
#include <WiFi.h>
#include <esp_wifi.h>
#include <ESPmDNS.h>

// Wifi settings
const char* ssid = "Ravescape";
const char* password = "20857150976705574946";
IPAddress local_ip(192, 168, 178, 99);
IPAddress gateway(192, 168, 178, 1);
IPAddress subnet(255, 255, 255, 0);

WebServer server(80);

// LED settings
const int numLeds = 60; 
const byte dataPin = 27;
CRGB leds[numLeds];
const int numberOfChannels = numLeds * 3; // Total number of channels you want to receive (1 led = 3 channels)

// Art-Net settings
ArtnetWifi artnet;
const int startUniverse = 0; // CHANGE FOR YOUR SETUP most software this is 1, some software send out artnet first universe as 0.

// Analog Read
int analog;

void getspannung() {
  analog=analogRead(33);
    server.send(200, "text/json", "{\"spannung\": "+String(analog)+"}");
}

// Check if we got all universes
const int maxUniverses = numberOfChannels / 512 + ((numberOfChannels % 512) ? 1 : 0);
bool universesReceived[maxUniverses];
bool sendFrame = 1;
int previousDataLength = 0;

// Define routing
void restServerRouting() {
    server.on("/", HTTP_GET, []() {
        server.send(200, F("text/html"),
            F("Welcome to the REST Web Server"));
    });
    server.on(F("/spannung"), HTTP_GET, getspannung);
}

// Manage not found URL
void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
}

// connect to wifi – returns true if successful or false if not
boolean ConnectWifi(void)
{
  boolean state = true;
  int i = 0;
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  WiFi.config(local_ip, gateway, subnet);
  Serial.println("");
  Serial.println("Connecting to WiFi");

  // Wait for connection
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    if (i > 20){
      state = false;
      break;
    }
    i++;
  }
  if (state){
    Serial.println("");
    Serial.print("Connected to ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("");
    Serial.println("Connection failed.");
  }

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  // Set server routing
  restServerRouting();
  // Set not found response
  server.onNotFound(handleNotFound);
  // Start server
  server.begin();
  Serial.println("HTTP server started");
  return state;
}

void initTest()
{
  for (int i = 0 ; i < numLeds ; i++) {
    leds[i] = CRGB(127, 0, 0);
  }
  FastLED.show();
  delay(500);
  for (int i = 0 ; i < numLeds ; i++) {
    leds[i] = CRGB(0, 127, 0);
  }
  FastLED.show();
  delay(500);
  for (int i = 0 ; i < numLeds ; i++) {
    leds[i] = CRGB(0, 0, 127);
  }
  FastLED.show();
  delay(500);
  for (int i = 0 ; i < numLeds ; i++) {
    leds[i] = CRGB(0, 0, 0);
  }
  FastLED.show();
}

void onDmxFrame(uint16_t universe, uint16_t length, uint8_t sequence, uint8_t* data)
{
  sendFrame = 1;
  // set brightness of the whole strip
  if (universe == 15)
  {
    FastLED.setBrightness(data[0]);
    FastLED.show();
  }

  // Store which universe has got in
  if ((universe - startUniverse) < maxUniverses) {
    universesReceived[universe - startUniverse] = 1;
  }

  for (int i = 0 ; i < maxUniverses ; i++)
  {
    if (universesReceived[i] == 0)
    {
      Serial.println("Broke");
      sendFrame = 0;
      break;
    }
  }

  // read universe and put into the right part of the display buffer
  for (int i = 0; i < length / 3; i++)
  {
    int led = i + (universe - startUniverse) * (previousDataLength / 3);
    if (led < numLeds)
      leds[led] = CRGB(data[i * 3], data[i * 3 + 1], data[i * 3 + 2]);
  }


  
  previousDataLength = length;

  if (sendFrame)
  {
    FastLED.show();
    // Reset universeReceived to 0
    memset(universesReceived, 0, maxUniverses);
  }
}

// Sleep timer
void sleepTimer(int artnet_status)
{
  static int count;
  static int count_sleeps;
  count++;
  if(artnet_status != 0)
  {
    // Reset counters if artnet data is recieved
    count = 0;
    count_sleeps = 0;
    return;
  }

  // After 15 seconds of no signal go to sleep
  if(count >= 15000)
  {
    // Reset counter. After wakeup: activate WiFi for 30 sec
    count = 0;

    // Turn off all LEDs 
    for(int i = 0; i < numLeds; i++)
    {
      leds[i] = CRGB(0,0,0);
    }
    FastLED.show();

    switch (count_sleeps)
    {
    case 0:
      // Sleep for 30 Seconds
      count_sleeps = 1;

      // Show red light on one LED to indicate sleeping
      leds[0] = CRGB(5, 0, 0);
      FastLED.show();

      WiFi.disconnect(true, true);
      esp_sleep_enable_timer_wakeup(30 * 1000 * 1000);
      esp_light_sleep_start();
      ConnectWifi();
      artnet.begin();

      // Show green light on one LED to indicate search
      leds[0] = CRGB(0, 5, 0);
      FastLED.show();
      break;
    
    case 1:
      // Sleep for 60 Seconds
      count_sleeps = 2;

      // Show red light on one LED to indicate sleeping
      leds[0] = CRGB(5, 0, 0);
      FastLED.show();

      WiFi.disconnect(true, true);
      esp_sleep_enable_timer_wakeup(60 * 1000 * 1000);
      esp_light_sleep_start();
      ConnectWifi();
      artnet.begin();

      // Show green light on one LED to indicate search
      leds[0] = CRGB(0, 5, 0);
      FastLED.show();
      break;

    case 2:
      // Sleep for 5 minutes
      count_sleeps = 2;

      // Show red light on one LED to indicate sleeping
      leds[0] = CRGB(5, 0, 0);
      FastLED.show();

      WiFi.disconnect(true, true);
      esp_sleep_enable_timer_wakeup(300 * 1000 * 1000);
      esp_light_sleep_start();
      ConnectWifi();
      artnet.begin();

      // Show green light on one LED to indicate search
      leds[0] = CRGB(0, 5, 0);
      FastLED.show();
      break;

    default:
      break;
    }
    
  }
}

void setup()
{
  ConnectWifi();
  artnet.begin();
  FastLED.addLeds<WS2812, dataPin, GRB>(leds, numLeds);
  initTest();

  // this will be called for each packet received
  artnet.setArtDmxCallback(onDmxFrame);
}

int artnet_retval;

void loop()
{
  // we call the read function inside the loop
  artnet_retval = artnet.read();
  sleepTimer(artnet_retval);
  server.handleClient();
}
