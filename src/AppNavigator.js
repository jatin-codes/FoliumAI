import {createStackNavigator,
    createAppContainer} from 'react-navigation';
import CameraComponent from './CameraComponent';

const routeNavigator = createStackNavigator({
  CameraComponent: { screen: CameraComponent },
});

const AppNavigator = createAppContainer(routeNavigator)

export default AppNavigator;