import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen5870020Navigator from '../features/BlankScreen5870020/navigator';
import BlankScreen5970019Navigator from '../features/BlankScreen5970019/navigator';
import Maps69994Navigator from '../features/Maps69994/navigator';
import Add-Item69993Navigator from '../features/Add-Item69993/navigator';
import Maps69989Navigator from '../features/Maps69989/navigator';
import UserProfile69985Navigator from '../features/UserProfile69985/navigator';
import MessengerNavigator from '../features/Messenger/navigator';
import TutorialNavigator from '../features/Tutorial/navigator';
import MapsNavigator from '../features/Maps/navigator';
import CalendarNavigator from '../features/Calendar/navigator';
import CameraNavigator from '../features/Camera/navigator';
import EmailAuthNavigator from '../features/EmailAuth/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {
    SplashScreen: {
      screen: SplashScreen
    },
    //@BlueprintNavigationInsertion
BlankScreen5870020: { screen: BlankScreen5870020Navigator },
BlankScreen5970019: { screen: BlankScreen5970019Navigator },
Maps69994: { screen: Maps69994Navigator },
Add-Item69993: { screen: Add-Item69993Navigator },
Maps69989: { screen: Maps69989Navigator },
UserProfile69985: { screen: UserProfile69985Navigator },
Messenger: { screen: MessengerNavigator },
Tutorial: { screen: TutorialNavigator },
Maps: { screen: MapsNavigator },
Calendar: { screen: CalendarNavigator },
Camera: { screen: CameraNavigator },
EmailAuth: { screen: EmailAuthNavigator },

    /** new navigators can be added here */
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu,
    initialRouteName: 'SplashScreen',
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
