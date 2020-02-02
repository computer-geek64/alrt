# ALRT: When Danger Arises, Stay Connected

*SwampHacks VI Hackathon*
### ALRT (Automated Life Rescue Tracker) is an application that aims to tackle the challenge of finding victims of natural disasters when weather conditions cause power and connection loss. By implementing 2 custom APIs, a sophisticated webscraping algorithm, a linear regression model, live updating weather and location databases, and a multitude of other cutting-edge technologies. ###
---
## Some of the technolgies we used include: ##
  ![React](https://img.icons8.com/ios/150/000000/react-native.png)
  ![Selenium](https://github.com/computer-geek64/alrt/blob/master/assets/img/Selenium.png)
  ![Mongo](https://github.com/computer-geek64/alrt/blob/master/assets/img/mongo2.png)
  ![Flask](https://www.olirowan.xyz/static/images/icons/flask-plain.svg)
  ![Tensorflow](https://github.com/computer-geek64/alrt/blob/master/assets/img/tensor.png)
  ![Firebase](https://github.com/computer-geek64/alrt/blob/master/assets/img/firebase2.png)
    
* **React Native**
  * This allows our interface to be compatible with both Android and iOS devices, which is fundamental for allowing our app to passively collect location data wherever the user goes.
* **Selenium Web Driver**
  * To gather live-feed statistics of the severe weather conditions around the world, we implemented a sophisticated Selenium Python script to automatically check if a new weather threat recently formed.
* **MongoDB Database**
  * After aggregating and parsing the user location and weather data, our MongoDB database stores all the live data that is used for the final graph.
* **Flask**
  * We used a custom-built flask api to handle location updates from the mobile app and manage the MongoDB database.
* **Tensorflow**
  * Using Tensorflow, we were able to implement a linear regression model using the user's recent location coordinates to give first-responders a prediction on where the user may be based on their previous environment and the type of weather danger.
* **Firebase**
  * Allows us to authenticate users and make sure their data is secured due to the nature of the data we collect (pinpoint location).
