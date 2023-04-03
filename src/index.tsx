import {
  definePlugin,
  DialogButton,
  Router,
  ServerAPI,
} from "decky-frontend-lib";
import { VFC } from "react";
import { RxMixerVertical } from "react-icons/rx";

import App from "./components/App/App";
import Title from "./components/UI/Title";

import PythonServer from "./services/pythonServer";


const DeckyPluginRouterTest: VFC = () => {
  return (
    <div style={{ marginTop: "50px", color: "white" }}>
      Hello World!
      <DialogButton onClick={() => Router.NavigateToLibraryTab()}>
        Go to Library
      </DialogButton>
    </div>
  );
};

export default definePlugin((serverApi: ServerAPI) => {
  PythonServer.getInstance().setServer(serverApi)
  
  serverApi.routerHook.addRoute("/decky-plugin-test", DeckyPluginRouterTest, {
    exact: true,
  });

  return {
    title: <Title />,
    content: <App />,
    icon: <RxMixerVertical />,
    onDismount() {
      serverApi.routerHook.removeRoute("/decky-plugin-test");
    },
  };
});
