import React, { VFC } from "react";

import AvailableSources from "../AvailableSources/AvailableSources";
import GeneralSoundToggle from "../GeneralSoundToggle/GeneralSoundToggle";


const App: VFC = () => {
  return (
    <>
      <GeneralSoundToggle />
      <AvailableSources />
    </>
  );
}

export default App;