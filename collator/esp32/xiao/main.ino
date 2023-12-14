/*
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-12-11 18:36:12
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-12-14 17:58:57
 * @FilePath: \plant_image_collator\collator\esp32\xiao\main.ino
 * @Description: This is a file for ESP32S3 xiao board.
 */
// -- lib --
#include <WiFi.h> // packge: esp32
#include <WiFiClient.h> // packge: esp32
#include <WebServer.h> // packge: esp32
#include <ESPmDNS.h> // packge: esp32
#include "esp_camera.h" // packge: esp32
#include <iostream>
#include <map>

// -- namespace --
using std::copy;
using std::map;
using std::string;

// -- config --
const char* ssid = "R15-D3A4"; // change this to your WiFi SSID
const char* password = "0978526075"; // change this to your WiFi password
const char* serverName = "http://YOUR_SERVER_IP:5000/photo"; // replace with your server URL
const char* TestServerName = "https://api.binance.com/api/v3/time"; // replace with your server URL
const char* contentType = "application/json";

// -- variables --
unsigned long lastTime = 0;
unsigned long timerDelay = 5000;

// -- functions --
void network_setup(){
  WiFi.mode(WIFI_AP_STA);
  WiFi.begin(ssid, password);
  WiFi.setTxPower(WIFI_POWER_11dBm);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

void camera_setup(){
  // Initialize the camera module
}

int http_get(string get_server_name){
  // Send an HTTP GET request
  // Return the status code of the request
  int httpResponseCode = 0;

  if (WiFi.status() == WL_CONNECTED){
    
    HTTPClient http;
    http.begin(get_server_name.c_str());
    int httpResponseCode = http.GET();

    if (httpResponseCode>0){
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
      String payload = http.getString();
      Serial.println(payload);
    }
    else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  }
  else {
    Serial.println("WiFi Disconnected");
  }
  return httpResponseCode;
}

int http_post(map<string, string> data){
  // Send an HTTP POST request
  // Return the status code of the request
}

int test_network(){
  // Send an HTTP GET request to test the network, using TestServerName
  // Return the status code of the request
  int httpResponseCode = http_get(TestServerName);
  return httpResponseCode;
}

string take_photo(){
  // Take a photo using the camera module
  // Return the photo as a base64 string
}

int send_photo(string photo){
  // Send the photo to the server
  // Return the status code of the request
}

// -- main --
void setup(){
  Serial.begin(115200);
  network_setup();
  camera_setup();
  int network_test = test_network();
  if (network_test == 200){
    Serial.println("Network test passed");
  }
  else {
    Serial.println("Network test failed");
  }

}

void loop(){

}