import {createStackNavigator,
    createAppContainer} from 'react-navigation';
import ReactCamera from './ReactCamera';
import Results from './Results';

const routeNavigator = createStackNavigator({
  ReactCamera: { screen: ReactCamera },
  Results: { screen: Results },
});

const AppNavigator = createAppContainer(routeNavigator)

export default AppNavigator;