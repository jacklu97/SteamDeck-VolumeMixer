import { VFC } from "react";
import { PanelSection, staticClasses } from "decky-frontend-lib";

import AvailableSources from "../AvailableSources/AvailableSources";
import { QueryClient, QueryClientProvider } from "react-query";

const queryClient = new QueryClient()

const App: VFC = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <PanelSection>
        <div className={staticClasses.PanelSectionTitle}>
          Music Mixer {"Output source"}
        </div>
        <AvailableSources />
      </PanelSection>
    </QueryClientProvider>
  );
}

export default App;