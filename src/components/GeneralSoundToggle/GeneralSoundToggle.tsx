import { PanelSection, PanelSectionRow, ToggleField } from "decky-frontend-lib";

const GeneralSoundToggle = () => {
  return (
    <PanelSection title="System Volume">
      <PanelSectionRow>
        <ToggleField
          label="Mute System"
          checked={false}
        />
      </PanelSectionRow>
    </PanelSection>
  );
}

export default GeneralSoundToggle;