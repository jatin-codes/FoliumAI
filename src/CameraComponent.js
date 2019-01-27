import React, {Component} from 'react';
import ReactCamera from './ReactCamera';
import {StyleSheet, View} from 'react-native'

class CameraComponent extends Component {
    render (){
        return (
            <View style={styles.container}>
                <ReactCamera />
            </View>
        );
    }
}

export default CameraComponent;

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#F5FCFF',
    },
  });
  