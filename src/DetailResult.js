import React, {Component} from 'react';
import {
    Image,
    PixelRatio,
    StyleSheet,
    Text,
    TouchableOpacity,
    View,
  } from 'react-native';

class DetailResult extends Component {

    handlePress = () => {
        alert("works")
    }

    render(){
        const {navigation} = this.props;
        const image_name = navigation.getParam('img');
        // need to show a spinner
        // need to show the image being uploaded + text

        return (
        <View style={styles.container}>
            <Image style={{height: 300, marginBottom:10, width: 300}} source = {image_name}/>
            <View
                style={{
                    borderBottomColor: 'black',
                    borderBottomWidth: 1,
                }}
            />
            <View onPress={this.handlePress.bind(this)}>
                <Text>Test Dummy data</Text>
            </View>
        </View>
        )
    }
}

export default DetailResult;

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#fff',
    },
  });