import React, { Component } from 'react';
import { View, StyleSheet, Text } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import * as TaskManager from 'expo-task-manager';

export default class App extends Component {
  state = {
    location: null,
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
        notificationBody: 'Ensuring your safety'
      }
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
      <View style={styles.container}>
        <Text style={styles.caption}>Home</Text>
        <Text style={styles.content}>
          Rotate Element
        </Text>
      </View>
    );
  }
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
    backgroundColor: '#000',
  },
  caption: {
    fontSize: 30,
    color: '#fff',
  },
  content: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    color: '#fff',
  },
});