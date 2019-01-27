
import React from 'react';
import {
  Image,
  PixelRatio,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import ImagePicker from 'react-native-image-picker';

const options = {
  title: "camera comp",
  takePhotoButtonTitle: "take a photo with your camera",
  chooseFromLibraryButtonTitle: "choose photo"
}

export default class ReactCamera extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      avatarSource: null,
    }
  }

  selectPhotoTapped() {

    ImagePicker.showImagePicker(options, (response) => {
      console.log('Response = ', response);

      if (response.didCancel) {
        console.log('User cancelled photo picker');
      } else if (response.error) {
        console.log('ImagePicker Error: ', response.error);
      } else if (response.customButton) {
        console.log('User tapped custom button: ', response.customButton);
      } else {
        let source = { uri: response.uri };
            console.log(source);
        // You can also display the image using data:
        // let source = { uri: 'data:image/jpeg;base64,' + response.data };

        this.setState({
          avatarSource: source,
        });
      }
    });
}

  render() {
    return (
      <View >
        <TouchableOpacity onPress={this.selectPhotoTapped.bind(this)}>
            <Text>Select Image</Text>
            <Image source={this.state.avatarSource} style={{height:200, margin:10}}></Image>
          </TouchableOpacity>
      </View>
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
  avatarContainer: {
    borderColor: '#9B9B9B',
    borderWidth: 1 / PixelRatio.get(),
    justifyContent: 'center',
    alignItems: 'center',
  },
  avatar: {
    borderRadius: 75,
    width: 150,
    height: 150,
  },
});