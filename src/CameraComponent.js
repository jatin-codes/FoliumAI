import React, {Component} from 'react';
import {StyleSheet, Text, View} from 'react-native';
import ReactCamera from './ReactCamera';

class CameraComponent extends Component {
    render (){
        return (
            <View>
                <View>
                    <ReactCamera/>
                </View>
            </View>
        )
    }
}

export default CameraComponent;


const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#42f4a1',
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