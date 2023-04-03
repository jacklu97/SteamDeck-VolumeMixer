import { Fragment, VFC } from "react";
import { PanelSection } from "decky-frontend-lib";

import AvailableSources from "../AvailableSources/AvailableSources";
import GeneralSoundToggle from "../GeneralSoundToggle/GeneralSoundToggle";


const App: VFC = () => {
  return (
    <Fragment>
      <GeneralSoundToggle />
      <PanelSection>
        <AvailableSources />
      </PanelSection>
    </Fragment>
  );
}

export default App;