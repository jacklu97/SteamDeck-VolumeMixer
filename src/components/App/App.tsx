import { Fragment, VFC } from "react";

import AvailableSources from "../AvailableSources/AvailableSources";
import GeneralSoundToggle from "../GeneralSoundToggle/GeneralSoundToggle";


const App: VFC = () => {
  return (
    <Fragment>
      <GeneralSoundToggle />
      <AvailableSources />
    </Fragment>
  );
}

export default App;