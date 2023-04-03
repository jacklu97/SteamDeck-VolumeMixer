import {
  definePlugin,
  ServerAPI,
} from "decky-frontend-lib";
import { RxMixerVertical } from "react-icons/rx";

import App from "./components/App/App";
import Title from "./components/UI/Title";

import PythonServer from "./services/pythonServer";

export default definePlugin((serverApi: ServerAPI) => {
  PythonServer.getInstance().setServer(serverApi)
  
  return {
    title: <Title />,
    content: <App />,
    icon: <RxMixerVertical />,
    onDismount() {
    },
  };
});
