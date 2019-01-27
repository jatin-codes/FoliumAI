import React, { Component } from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import AppNavigator from './src/AppNavigator';
import CameraComponent from './src/CameraComponent';

class App extends Component{
  constructor(props){
    super(props);

    this.state = {
      leaf_image: [],
    }
  }

  render(){
    return (
      // <View>
        // <AppNavigator
        //   screenProps={
        //     {
        //       leaf_image: this.state.leaf_image,
        //     }
        //   }
        // />
          // <CameraComponent/>
         <AppNavigator
          screenProps={
            {
              leaf_image: this.state.leaf_image,
            }
          }
          />
        
    )
  }
}

export default App;

