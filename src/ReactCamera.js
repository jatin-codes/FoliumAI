import axios from 'axios';
import React from 'react';
import {
  Image,
  PixelRatio,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  Button
} from 'react-native';
import ImagePicker from 'react-native-image-picker';

const options = {
  title: "camera comp",
  takePhotoButtonTitle: "take a photo with your camera",
  chooseFromLibraryButtonTitle: "choose photo"
}

export default class ReactCamera extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      avatarSource: null,
      response: null,
      isLoading: false,
    }
  }

  componentDidUpdate(prevResponse){
    if (this.state.prevResponse !== this.state.response) {
      // let imagesUri=[];
      // for (var i = 0; i < this.state.images.length; i++) {
      //   let source = { uri: ‘data:image/jpeg;base64,’ + this.state.images[i].data };
      //   imagesUri.push(source);
      // }
      // this.props.navigation.navigate(‘Upload’,{Image: this.state.imageSource, Images: imagesUri})
      console.log("COmponent did update")
      this.props.navigation.navigate('Results', {
        img: this.state.avatarSource,
      });
    }
  }

  selectPhotoTapped() {
    console.log('test')

    ImagePicker.showImagePicker(options, (response) => {
      console.log('Response = ', response);

      if (response.didCancel) {
        console.log('User cancelled photo picker');
      } else if (response.error) {
        console.log('ImagePicker Error: ', response.error);
      } else if (response.customButton) {
        console.log('User tapped custom button: ', response.customButton);
      } else {
        const imageData = new FormData();
        imageData.append('leaf_image',response.data);
        console.log(imageData);


        // Set Prediction-Key Header to : b045217654b04a34989a440b4ceb8b0b</image>
// Set Content-Type Header to : application/octet-stream
// Set Body to : <image file>

        axios({
          // url: 'https://westus2.api.cognitive.microsoft.com/customvision/v2.0/Prediction/42e1e328-0208-4214-ba53-71cb87320f4d/image?iterationId=ab1b2cc0-b5c7-442b-b8d4-778aa949b9b9',
          url: 'http://127.0.0.1:5000/api/ml',
          method: 'post',
          data: imageData,
          headers: {
            "Prediction-Key" : "b045217654b04a34989a440b4ceb8b0b",
            "Content-Type" : "application/octet-stream",
            },
          body : imageData,
        }).then(function (response){
          console.log(response);
        }).catch((error) => {
          console.warn(error,'Promise error');
          // done();
        });

        // create an endpoint here.. 
        // if the process is successful pass the image to processing

        let source = { uri: response.uri };
        console.log(source);
        // You can also display the image using data:
        // let source = { uri: 'data:image/jpeg;base64,' + response.data };

        this.setState({
          avatarSource: source,
          response: source,
          isLoading: true
        });

        // need to process this in order to start move to another page
        // this.handleNextPage.bind(this);
      }
    });
  }
  handleNextPage(){
    // e.preventDefault();
    console.log('triggeres');
   // this.props.navigation.navigate('Processing'); 
  }

  render() {
    const {isLoading} = this.state;
    return (
      <View style={styles.container}>
        {
            !isLoading &&
            <View >
              <View style={styles.homeContainer}>
                <Image resizeMode="contain" style={styles.logo} source={require('./images/logo.png')} />
              </View>
              <TouchableOpacity style={styles.homeContainer}
                onPress={this.selectPhotoTapped.bind(this)}>
                <Image resizeMode="contain" style={styles.logo} source={require('./images/start.png')} />
              </TouchableOpacity>
            </View>
        }

        {
          isLoading &&
          
          <View style={styles.container}>
            <Image style={{height: 300, marginBottom:10, width: 300}} source = {this.state.avatarSource}/>
            <Text>Processing file</Text>
          </View>
        }
        </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  homeContainer: {
    alignItems: 'center',
    flexGrow: 1,
    justifyContent: 'center',
    backgroundColor: '#5FA717'
  },
  logo: {
    marginTop: 100,
    position: 'absolute',
    width: 250,
    height: 250
  },
  button: {
    backgroundColor: 'green',
    borderColor: '#a4db82',
    borderWidth: 200,
    borderRadius: 5,
    width: 600,
    color: 'white',
    fontSize: 24,
    fontWeight: 'bold',
    overflow: 'hidden',
    padding: 10,
    textAlign:'center',
  },
  avatarContainer: {
    borderColor: '#9B9B9B',
    borderWidth: 1 / PixelRatio.get(),
    justifyContent: 'center',
    alignItems: 'center',
  },
});