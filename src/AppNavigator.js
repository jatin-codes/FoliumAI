import {createStackNavigator,
    createAppContainer} from 'react-navigation';
import ReactCamera from './ReactCamera';
import Results from './Results';
import DetailResult from './DetailResult';

const routeNavigator = createStackNavigator({
  ReactCamera: { screen: ReactCamera },
  Results: { screen: Results },
  DetailResult: {screen: DetailResult},
});

const AppNavigator = createAppContainer(routeNavigator)

export default AppNavigator;