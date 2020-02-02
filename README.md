# ALRT: When Danger Arises, Stay Connected :exclamation: :fire_engine::dash:

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
    
* **React Native**:iphone:
  * This allows our interface to be compatible with both Android and iOS devices, which is fundamental for allowing our app to passively collect location data wherever the user goes.
* **ReactJS**
  * Used ReactJS to develop our front-end website for first responders to use to track missing persons in a natural disaster.
* **Flask API**:outbox_tray:
  * We used a custom-built Flask API to handle location updates from the mobile app and manage the MongoDB database cluster.
* **Selenium Webdriver**:mag:
  * To gather live-feed statistics of the severe weather conditions around the world, we implemented a sophisticated Selenium Python script to automatically check if a new weather threat recently formed.
* **MongoDB**:page_facing_up:
  * After aggregating and parsing the user location and natural disaster data, our MongoDB database cluster stores all the live data that is used for the final map render.
* **TensorFlow**:chart_with_upwards_trend:
  * Using Tensorflow, we were able to implement a regression model using the user's recent location coordinates to give first-responders a prediction on where the user may be based on their previous environment and the type of weather danger.
* **Google Firebase**:fire::lock:
  * Allows us to authenticate users and make sure their data is secured due to the nature of the data we collect (high-accuracy location data).

## How it Works ##

When the user downloads the app and verifies their credentials with our database, the app begins collecting the coordinates of the person every minute and creates a short path which the user travelled. During major natural disasters, the cell towers and any forms of connectivity are either taken out by the disaster or are intentionally taken down to prevent collateral damage. This means that if the user is within the vicinity of the disaster, their phone will likely lose connection and stop sending location data. When this occurs, the app takes the 3 most recent datapoints and create a predicted range of where the user could be based on calculated velocity. Additionally, we implemented a supervised machine learning algorithm that predicts a certain point where the user would be to help first-responders quickly and effectively find people in danger.

## Team: 
* *Yash Patel ([@yashp121](https://github.com/yashp121))*
* *Ashish D'Souza ([@computer-geek64](https://github.com/computer-geek64))*
* *Sharath Palathingal ([@therealsharath](https://github.com/therealsharath))*
* *Pranav Pusarla([@PranavPusarla](https://github.com/PranavPusarla))*
