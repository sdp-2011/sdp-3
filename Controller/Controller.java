/**
 * The controller class reads from the Control Topic. It waits for commands
 * defined in the interface and passes them through ControllerI.
 *
 * @author Daniel Holden
 * @author Stephen McGruer
 */
public class Controller {

  private static Ice.Object montrolI;
  
  private static final String ADAPTER_TOPIC_NAME = "ControlAdapter";
  private static final String ADAPTER_PORT_NUM = "10000";
 
  /**
   * The main method for the class, which starts the ICE server and 
   * passes commands through to the ControllerI. 
   * 
   * @param args    Program arugments. Not used.
   */
  public static void main(String[] args) {

    int status = 0;
    Ice.Communicator ic = null;

    try {

      /* Instantiate ICE */
      System.out.println("Initializing Ice.");
      ic = Ice.Util.initialize(args);
      
      /* Create an adapter for the topic - uses port 10000 */
      System.out.println("Creating Ice adapter on port "+ ADAPTER_PORT_NUM + 
          " and adapter name " + ADAPTER_TOPIC_NAME);
      Ice.ObjectAdapter adapter = ic.createObjectAdapterWithEndpoints(
          ADAPTER_TOPIC_NAME, "default -p "+ADAPTER_PORT_NUM);
      
      /* Create our new class to serve the interface defined in the topic */
      montrolI = new ControllerI();
      
      /* Add this class to the adapter */
      System.out.println("Adding interface to adapter.");
      adapter.add(montrolI, ic.stringToIdentity("ControlPython"));
      
      /* Activate! */
      System.out.println("Activating!");
      adapter.activate();
      ic.waitForShutdown();

    } catch (Ice.LocalException e) {

      e.printStackTrace();

      System.err.println(e.getMessage());
      status = 1;

    } catch (Exception e) {

      System.err.println(e.getMessage());
      status = 1;

    }

    if (ic != null) {

      /* Clean up */
      try {

        ic.destroy();

      } catch (Exception e) {

        System.err.println(e.getMessage());
        status = 1;

      }
    }

    /* When done, close the connection */
    System.out.println("Done, disconnecting.");
    ((ControllerI)montrolI).disconnect();

    System.exit(status);

  }
}
