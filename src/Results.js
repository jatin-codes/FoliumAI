import React, {Component} from 'react';
import {
    Image,
    PixelRatio,
    StyleSheet,
    Text,
    List,
    FlatList,
    TouchableOpacity,
    View,
  } from 'react-native';

class Results extends Component {

    constructor(props){
        super(props);

        this.state = {
            renderDetail: null,
        }
    }

    componentDidUpdate(prevResponse){
        if (this.state.prevResponse !== this.state.renderDetail) {
          // let imagesUri=[];
          // for (var i = 0; i < this.state.images.length; i++) {
          //   let source = { uri: ‘data:image/jpeg;base64,’ + this.state.images[i].data };
          //   imagesUri.push(source);
          // }
          // this.props.navigation.navigate(‘Upload’,{Image: this.state.imageSource, Images: imagesUri})
        //   console.log("COmponent did update")
        //   this.props.navigation.navigate('Results', {
        //     img: this.state.avatarSource,
        //   });
        }
      }

    handlePress = () => {
        alert("works")
        this.setState({
            renderDetail: "",
        })
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
            <TouchableOpacity onPress={() => this.props.navigation.navigate('DetailResult')}>
                <Text>Leaf Detail</Text>
            </TouchableOpacity>
        </View>
        )
    }
}

export default Results;

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#fff',
    },
  });