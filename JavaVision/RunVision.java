import Ice.Object;
import au.edu.jcu.v4l4j.V4L4JConstants;
import au.edu.jcu.v4l4j.exceptions.V4L4JException;

/** 
 * The main class used to run the vision system. Creates the control
 * GUI, initialises the image processing and runs the ICE server.
 * 
 * @author s0840449
 */
public class RunVision {

	private static WorldStateI wsI;
	private static ControlGUI thresholdsGUI;
	
	private static final String ADAPTER_TOPIC_NAME = "WorldStateAdapter";
	private static final String ADAPTER_PORT_NUM = "10012";

	/**
	 * The main method for the class. Creates the control
	 * GUI, initialises the image processing and runs the 
	 * ICE server.
	 * 
	 * @param args		Program arguments. Not used.
	 */
	public static void main(String[] args) {

		WorldState worldState = new WorldState();
		ThresholdsState thresholdsState = new ThresholdsState();

		/* Default to main pitch. */
		PitchConstants pitchConstants = new PitchConstants(0);
		
		/* Default values for the main vision window. */
		String videoDevice = "/dev/video0";
		int width = 640;
		int height = 480;
		int videoStandard = V4L4JConstants.STANDARD_PAL;
		int channel = 2;
		int compressionQuality = 60;

		try {
			
			Ice.Communicator ic = Ice.Util.initialize(args);
			System.out.println("Creating Ice adapter on port "+ADAPTER_PORT_NUM+" and adapter name "+ADAPTER_TOPIC_NAME);
			Ice.ObjectAdapter adapter
			= ic.createObjectAdapterWithEndpoints(
					ADAPTER_TOPIC_NAME, "default -p "+ADAPTER_PORT_NUM);

			wsI = new WorldStateI(worldState);
			
			/* Create a new Vision object to serve the main vision window. */
			new Vision(videoDevice, width, height, videoStandard, channel,
					compressionQuality, worldState, thresholdsState, pitchConstants);
			
			/* Create the Control GUI for threshold setting/etc. */
			thresholdsGUI = new ControlGUI(thresholdsState, worldState, pitchConstants);
			thresholdsGUI.initGUI();
			
			/* Run the ICE server. */
			adapter.add((Object) wsI, ic.stringToIdentity("WorldState"));
			adapter.activate();
			
			ic.waitForShutdown();

		} catch (V4L4JException e) {
			e.printStackTrace();
		} catch (Ice.LocalException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
