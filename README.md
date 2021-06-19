# IOT Utils

**An ESP32 Toolbox for making IOT devices**
___
While working a lot with Micropython on ESP32 to make smart devices, I noticed that I rewrote many times a lot of code that is common among those devices. 

In this code are basic IOT functions such as : 
- Wifi Station/HotSpot, configurable without flashing the board
- Config files / reboot-resilient variables
- Threaded Web Server
- OTA Updates 
- Alexa Support
- (more)

___

**Current features :**
- #### Persistent memory
	 PersistentData class allows creating a persistent variable that will keep its value through rebooting.
	 The data is retrieved by name, and can have a specific folder, that will be created automatically. As the data probably doesn't exists on first boot, it can also have a default value
	 
	 PersistantData exists in different extended classes that allows choosing a data `type`. The value will **always** be truncated/formatted to match the data type. If the data fails to be truncated, a `ValueError` is raised.
 Supported types are : `boolean`, `integer`, `float`, `string`. 
 
 - #### Wifi AP/STA Interface
      The WifiStation condenses the basic features of Station and Access Point interfaces to make it easier
      Access point and stations can be activated/deactivated in one line.
      
 - #### WebServer
      The HTTP Webserver makes it easy to create receive requests over IP.
      The HTTP requests can be handled by multiple workers, that can be threaded. 
      Concurrent code can then be ran, while serving multiple clients. 
      Multiple workers also allows hang-free browsing, as it's compatible with speculative sockets opening.
      `Note: WebServer currently only supports headers and closes before processing the body.`
      
 - ..That's all, folks. For now!
___
**Roadmap:**
- #### Wifi Access point and Station
  IOT Devices often need access to a Wifi network to communicate with other devices. 
  Wifi is also often used to configure the access point, provide an administration and basic configuration page.

- #### Threaded Webserver
   A Threaded web server would allows running concurrent code while serving web pages, running server backend, or create an API

- #### More PersistentData types : 
  Depending on the needs and suggestions, more PersistentData types will be added. Right now, `JSON`, `set`, `list`, `range`, `RGB` and `Hex` are under consideration.
- #### Over-The-Air Updates via GitHub
  Updating a board with a simple button push on the admin page is a huge quality of life improvement. OTA could be set to either use the lastest commit, a specific branch or a release. 
  It could also be set to occur automaticaly during IDLE times 
- #### Alexa Support
  Could be useful. More documentation required
