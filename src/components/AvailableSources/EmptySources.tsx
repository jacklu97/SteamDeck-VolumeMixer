import { PanelSectionRow, staticClasses } from "decky-frontend-lib";

const EmptySources = () => {
  return ( 
    <PanelSectionRow>
      <h4 className={staticClasses.Label}>
        There are no programs using sound right now
      </h4>
    </PanelSectionRow>
   );
}
 
export default EmptySources;