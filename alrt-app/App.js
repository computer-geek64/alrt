import React, { Component } from 'react';
import { View, StyleSheet, Text, } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import * as TaskManager from 'expo-task-manager';;
import * as WebBrowser from 'expo-web-browser';
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';

export default class App extends Component {
  state = {
    result: null,
    errorMessage: null,
  };

  constructor() {
    super();
    this.ensurePermissionGranted();
    this.startLocationUpdates();
  }
  
  startLocationUpdates = () => {
    Location.startLocationUpdatesAsync('watch', {
      foregroundService: {
        notificationTitle: 'ALRT Tracker',
        notificationBody: 'ALRT Guardian 💪',
      },
      timeInterval: 30000,
      accuracy: Location.Accuracy.BestForNavigation,
    });
  }

  ensurePermissionGranted = async () => {
    let { status } = await Permissions.askAsync(Permissions.LOCATION);
    if (status !== 'granted') {
      this.setState({
        errorMessage: 'Please go to your settings and alter the permissions granted to this application',
      });
    }
  }

  render() {
    return (
      <>
        <View style={styles.container}>
          <Ionicons name="md-checkmark-circle" size={130} color="white" />
          <Text style={styles.caption}>Your guardian ALRT's is Active 👼</Text>
        </View>
        <View style={styles.footer}>
          <Text style={styles.footerText}>
            A project by Team Biryani Bandits &nbsp;
            <MaterialCommunityIcons name="pirate" size={19} color="#05ff00" /></Text>
        </View>
      </>
    );
  }

  _handlePressButtonAsync = async () => {
    let result = await WebBrowser.openBrowserAsync('http://github.com/computer-geek64/alrt');
    this.setState({ result });
  };

}

async function sendToBack(data) {
  try {
    let response = await fetch(
      "http://10.192.142.58/api/alrt/v1/update_location",
      {
        method: "POST",
        body: JSON.stringify(data),
      }
    )
  } catch(errorMessage) {
    console.log(errorMessage);
  }
}

TaskManager.defineTask('watch', ({ data: { locations = [] }, error }) => {
  if(error) {
    return console.error(error)
  } else {
    sendToBack(locations[0]);
  }
})

const styles = StyleSheet.create({
  container: {
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ade2ff',
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  caption: {
    fontSize: 22,
    color: '#fff',
  },
  footer: {
    backgroundColor: '#000',
    alignItems: "center",
    justifyContent: "center",
    padding: 10,
  },
  footerText: {
    color: '#fff',
    fontSize: 17,
  },
});