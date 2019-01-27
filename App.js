import React, { Component } from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import WelcomePage from './src/WelcomePage';
import CameraComponent from './src/CameraComponent';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tab: 2
    };
  }

  render() {
    const { tab } = this.state;
    return (
      <TouchableOpacity style={styles.container}>
        {tab == 1 &&
          <WelcomePage onPress={() => this.setState({ tab: 2 })} />
        }
        {tab == 2 &&
          <CameraComponent />
        }
      </TouchableOpacity>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});
