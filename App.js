import React, {Component} from 'react';
import {StyleSheet, Text, View} from 'react-native';
// import WelcomePage from './src/WelcomePage';
import CameraComponent from './src/CameraComponent';
import AppNavigator from './src/AppNavigator';

class App extends Component{
  constructor(props){
    super(props);

    this.state = {
      leaf_image: [],
    }
  }

  render() {
    return (
        <AppNavigator
          screenProps={
            {
              leaf_image: this.state.leaf_image,
            }
          }
        />
    );
  }
}

export default App;

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
