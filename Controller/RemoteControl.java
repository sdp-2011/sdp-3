import java.awt.*;
import java.awt.event.*;

import lejos.nxt.*;
import lejos.nxt.remote.*;
import lejos.pc.comm.*;
import java.io.*;

public class RemoteControl extends Frame {

  Button button;
  NXTComm communicator;
  DataOutputStream outStream;
  DataInputStream inStream;

  public static void main(String[] args) {
    RemoteControl rc = new RemoteControl();
  }

  public RemoteControl() {
  
    super("Robot Driving Control Panel");

    // Set up connection.
    try {
      communicator = NXTCommFactory.createNXTComm(NXTCommFactory.BLUETOOTH);
      NXTInfo nxtInfo = new NXTInfo(NXTCommFactory.BLUETOOTH, "BotTheThird", "00:16:53:07:75:31");
      communicator.open(nxtInfo);
    } catch (NXTCommException e) {
      System.out.println("Comm error caught!");
      e.printStackTrace();
      System.exit(-1);
    }
    System.out.println("Connected!");
    outStream = new DataOutputStream(communicator.getOutputStream());
    inStream = new DataInputStream(communicator.getInputStream());
    
    // Set up GUI
    button = new Button("Ignore me!");
    button.addKeyListener(new MyKeyListener());
    add(button, BorderLayout.CENTER);
    addWindowListener(new WindowAdapter(){
      public void windowClosing(WindowEvent we) {
        sendCommand(Command.EXIT);
        System.exit(0);
      }
    });
    setSize(100,100);
    setVisible(true);
  }

  public void sendCommand(Command command) {

    int intToWrite = 0;
    float distToWrite = 0;
    switch(command) {
      case FORWARD:   intToWrite = 1; break;
      case BACKWARD:  intToWrite = 2; break;
      case STOP:      intToWrite = 3; break;
      case LEFT:      intToWrite = 4; break;
      case RIGHT:     intToWrite = 5; break;
      case SHOOT:     intToWrite = 6; break;
      case EXIT:      intToWrite = -1; break;
      case NEWFORWARD: intToWrite = 7; distToWrite = 20; break;
      case NEWBACKWARD: intToWrite = 8; distToWrite = 20; break;
      case NEWLEFT: intToWrite = 9; distToWrite = 180; break;
      case NEWRIGHT: intToWrite = 10; distToWrite = 180; break;
      default: break;
    }
    try {
      outStream.writeInt(intToWrite);
      outStream.flush();
      if (distToWrite > 0) {
        outStream.writeFloat(distToWrite);
        outStream.flush();
      }
      //System.out.println("Waiting for int...");
      //System.out.println(inStream.readInt());
      //System.out.println("lol.");
    } catch (IOException e) {
      System.out.println("IOException caught");
      e.printStackTrace();
    }
  }

  public class MyKeyListener extends KeyAdapter {
    public void keyPressed(KeyEvent ke) {
      System.out.println("Pressed");
      switch(ke.getKeyCode()) {
        case KeyEvent.VK_UP: sendCommand(Command.FORWARD); break;
        case KeyEvent.VK_DOWN: sendCommand(Command.BACKWARD); break;
        case KeyEvent.VK_LEFT: sendCommand(Command.LEFT); break;
        case KeyEvent.VK_RIGHT: sendCommand(Command.RIGHT); break;
        case KeyEvent.VK_SPACE: sendCommand(Command.SHOOT); break;
        case KeyEvent.VK_W: sendCommand(Command.NEWFORWARD); break;
        case KeyEvent.VK_S: sendCommand(Command.NEWBACKWARD); break;
        case KeyEvent.VK_A: sendCommand(Command.NEWLEFT); break;
        case KeyEvent.VK_D: sendCommand(Command.NEWRIGHT); break;
        default: break;
      }
    }

    public void keyReleased(KeyEvent ke) {
      System.out.println("Released");
      switch(ke.getKeyCode()) {
        case KeyEvent.VK_UP: // Cascade
        case KeyEvent.VK_DOWN: // Cascade
        case KeyEvent.VK_LEFT: // Cascade
        case KeyEvent.VK_RIGHT: sendCommand(Command.STOP); break;
        default: break; // Also captures shoot command.
      }
    }
  }
}
