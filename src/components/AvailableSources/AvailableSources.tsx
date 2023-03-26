import VolumeControl from "../UI/VolumeControl";

const AvailableSources = () => {
  return ( 
    <div>
      <VolumeControl sourceName="Firefox"/>
      <VolumeControl sourceName="Steam"/>
      <VolumeControl sourceName="Spotify"/>
    </div>
   );
}
 
export default AvailableSources;