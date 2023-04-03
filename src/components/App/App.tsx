import { VFC } from "react";
import { PanelSection, staticClasses } from "decky-frontend-lib";

import AvailableSources from "../AvailableSources/AvailableSources";


const App: VFC = () => {
  return (
    <PanelSection>
      <div className={staticClasses.PanelSectionTitle}>
        {/* Music Mixer */}
      </div>
      <AvailableSources />
    </PanelSection>
  );
}

export default App;